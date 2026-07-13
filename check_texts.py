import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

abstracts = {}
for d in db:
    cls = d.get('drug_class')
    abs_text = d.get('class_abstract')
    if cls and abs_text:
        abstracts[cls] = abs_text

for cls, text in abstracts.items():
    print(f"[{cls}]: {text}")

