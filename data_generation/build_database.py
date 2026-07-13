import pandas as pd
import json

def build_database():
    # Load the base immunosuppressant and brand name JSON
    with open('drugs_germany.json', 'r', encoding='utf-8') as f:
        base_drugs = json.load(f)

    # Track substances we already have to avoid duplicates
    existing_substances = {d['substance'].lower() for d in base_drugs}

    # Load ATC Excel file
    # The sheet 'WIdO-Index 2026 alphabetisch' has 'ATC-Code' and 'ATC-Bedeutung'
    print("Loading Excel file...")
    df = pd.read_excel('ATC_GKV_AI_2026.xlsx', sheet_name='WIdO-Index 2026 alphabetisch')
    
    # Clean up column names and drop NaNs
    df = df.rename(columns={'ATC-Code': 'atc_code', 'ATC-Bedeutung': 'atc_bedeutung'})
    df = df.dropna(subset=['atc_code', 'atc_bedeutung'])

    # Filter to specific active ingredients (ATC codes with 7 characters usually)
    df = df[df['atc_code'].str.len() == 7]

    print(f"Extracted {len(df)} specific ATC codes.")

    new_drugs = []
    for _, row in df.iterrows():
        substance = str(row['atc_bedeutung']).strip()
        substance_lower = substance.lower()
        if substance_lower not in existing_substances:
            new_drugs.append({
                "substance": substance,
                "brand_names": [],
                "is_immunosuppressant": False,
                "live_vaccine_allowed": "Ja (Standard)",
                "therapy_pause_needed": "Keine",
                "immune_response_dead_vaccine": "Ausreichend",
                "atc_code": str(row['atc_code']).strip()
            })
            existing_substances.add(substance_lower)

    # Combine
    final_db = base_drugs + new_drugs

    with open('app_drugs_db.json', 'w', encoding='utf-8') as f:
        json.dump(final_db, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated app_drugs_db.json with {len(final_db)} drugs.")

if __name__ == "__main__":
    build_database()
