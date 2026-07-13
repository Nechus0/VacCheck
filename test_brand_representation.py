import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Evaluate brand name population
total_drugs = len(db)
drugs_with_brands = sum(1 for d in db if len(d.get('brand_names', [])) > 0)
total_brands = sum(len(d.get('brand_names', [])) for d in db)

print(f"Total Drugs: {total_drugs}")
print(f"Drugs with at least one brand name: {drugs_with_brands} ({drugs_with_brands/total_drugs*100:.1f}%)")
print(f"Total individual brand names in DB: {total_brands}")

