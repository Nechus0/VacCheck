import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

new_db = []
removed = 0
for d in db:
    sub = d['substance']
    
    # 1. Remove non-immuno combinations with " und "
    if ' und ' in sub and not d.get('is_immunosuppressant'):
        removed += 1
        continue
        
    # 2. Update Zytostatika phrasing
    if d.get('drug_class') == 'Zytostatika' and d.get('class_abstract'):
        d['class_abstract'] = d['class_abstract'].replace(
            "Dem Körper fehlt jegliche Grundlage, um Impfviren abzuwehren.",
            "Dem Körper fehlt dadurch die immunologische Grundlage, um Impfviren sicher abzuwehren."
        )
        d['class_abstract'] = d['class_abstract'].replace(
            "ausgeprägte Leukopenie",
            "Leukopenie"
        )
        
    new_db.append(d)

with open('app_drugs_db.json', 'w', encoding='utf-8') as f:
    json.dump(new_db, f, ensure_ascii=False, indent=2)

print(f"Removed {removed} ' und ' combination drugs.")
