import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

und_count = 0
for d in db:
    sub = d['substance']
    if ' und ' in sub and not d.get('is_immunosuppressant'):
        und_count += 1
        if 'Atorvastatin' in sub or 'Statin' in sub:
            print(f"Statin combination: {sub}")

print(f"Total non-immunosuppressant combinations with ' und ': {und_count}")

# Check for "jegliche Grundlage"
for d in db:
    abstract = d.get('class_abstract', '')
    if 'jegliche Grundlage' in abstract:
        print(f"Found dramatic phrasing in class: {d.get('drug_class')}")
        break

