import json

db_path = '../app_drugs_db.json'

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

garbage_substances = ["Lieferengpass", "Meerwasser"]
garbage_brands = ["Lieferengpass", "Meerwasser"]

filtered_db = []
removed_count = 0

for drug in db:
    substance = drug['substance']
    sub_lower = substance.lower()
    
    if substance in garbage_substances or "ohne pzn" in sub_lower or "ohne pharmazentralnummer" in sub_lower or "abrechnung von" in sub_lower or "hilfsmittel" in sub_lower or "blutprodukte" in sub_lower or substance == "Öl" or substance == "Wasser" or "sonstige" in sub_lower:
        removed_count += 1
        continue
    
    # Also clean up brand names
    new_brands = [b for b in drug.get('brand_names', []) if b not in garbage_brands]
    if len(new_brands) != len(drug.get('brand_names', [])):
        drug['brand_names'] = new_brands
        
    filtered_db.append(drug)

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_db, f, ensure_ascii=False, indent=2)

print(f"Removed {removed_count} garbage substances.")
