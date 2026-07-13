import json
import os

db_path = '../app_drugs_db.json'

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Mapping of Substance -> List of Aliases to inject into brand_names
aliases_map = {
    "Acetylsalicylsäure": ["Aspirin", "ASS", "ASS 100", "Aspirin Protect"],
    "Levothyroxin-Natrium": ["L-Thyroxin", "Euthyrox", "Levothyroxin"],
    "Colecalciferol": ["Vitamin D3", "Cholecalciferol", "Dekristol", "Vigantol"],
    "Metamizol-Natrium": ["Novaminsulfon", "Novalgin", "Metamizol"],
    "Hydrochlorothiazid": ["HCT"],
    "Ibuprofen": ["Ibu", "Ibuflam"],
    "Pantoprazol": ["Pantozol"],
    "Paracetamol": ["Benuron"],
    "Macrogol": ["Movicol"],
    "Diclofenac": ["Voltaren"],
    "Cyanocobalamin": ["Vitamin B12"],
    "Hydroxocobalamin": ["Vitamin B12"],
    "Methotrexat": ["MTX"],
    "Phenprocoumon": ["Marcumar", "Falithrom"]
}

updated_count = 0

for drug in db:
    substance = drug['substance']
    # Check if the substance name contains any of the keys
    for key, aliases in aliases_map.items():
        if key.lower() in substance.lower():
            existing_brands = set(drug.get('brand_names', []))
            # Merge
            merged_brands = list(existing_brands.union(aliases))
            if len(merged_brands) > len(existing_brands):
                drug['brand_names'] = merged_brands
                updated_count += 1

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Injected aliases into {updated_count} substances.")
