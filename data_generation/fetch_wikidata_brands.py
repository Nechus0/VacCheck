import requests
import json
import time

def fetch_and_update_brands():
    # 1. Load the database
    db_path = '../drug-checker-web-app/app_drugs_db.json'
    with open(db_path, 'r', encoding='utf-8') as f:
        drugs_db = json.load(f)
        
    print(f"Loaded {len(drugs_db)} drugs from database.")

    # 2. Query Wikidata for brand names
    # We query for all items that are pharmaceutical products and have an ATC code, and get their German labels.
    # We use a simple query that shouldn't time out. We fetch in chunks using OFFSET if needed, but since
    # there might be many, we will fetch ATC code -> brandName mapping.
    
    url = "https://query.wikidata.org/sparql"
    
    query = """
    SELECT ?atc ?brandLabel WHERE {
      ?med wdt:P31/wdt:P279* wd:Q12140; # instance/subclass of medication
           wdt:P267 ?atc;
           rdfs:label ?brandLabel.
      FILTER(LANG(?brandLabel) = "de")
    } LIMIT 100000
    """
    
    headers = {
        "User-Agent": "VaccineDrugCheckerBot/1.0 (joschapocha@example.com)",
        "Accept": "application/sparql-results+json"
    }
    
    print("Fetching brand names from Wikidata...")
    response = requests.get(url, params={"query": query}, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching from Wikidata: {response.status_code}")
        print(response.text)
        return
        
    data = response.json()
    bindings = data["results"]["bindings"]
    
    # Map ATC code to brand names
    atc_to_brands = {}
    for row in bindings:
        atc = row.get("atc", {}).get("value")
        brand = row.get("brandLabel", {}).get("value")
        if atc and brand:
            atc = atc.strip()
            brand = brand.strip()
            if atc not in atc_to_brands:
                atc_to_brands[atc] = set()
            atc_to_brands[atc].add(brand)
            
    print(f"Fetched {len(atc_to_brands)} distinct ATC codes with brand names from Wikidata.")
    
    # 3. Update our database
    updated_count = 0
    for drug in drugs_db:
        if 'atc_code' in drug and drug['atc_code']:
            atc = drug['atc_code']
            if atc in atc_to_brands:
                brands = atc_to_brands[atc]
                # Merge unique brands
                existing_brands = set(drug.get('brand_names', []))
                merged_brands = list(existing_brands.union(brands))
                
                if len(merged_brands) > len(existing_brands):
                    drug['brand_names'] = merged_brands
                    updated_count += 1

    # 4. Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(drugs_db, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully updated {updated_count} drugs with brand names.")

if __name__ == "__main__":
    fetch_and_update_brands()
