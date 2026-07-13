import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

for d in db:
    sub = d['substance'].lower()
    brands = [b.lower() for b in d['brand_names']]
    if 'metamizol' in sub or 'metamizol' in brands:
        print(f"Found Metamizol: {d['substance']} - Brands: {d['brand_names']}")

