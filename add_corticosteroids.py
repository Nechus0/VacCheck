import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Find the exact template from Prednison
template = {}
for d in db:
    if d['substance'] == 'Prednison':
        template = {
            'is_immunosuppressant': True,
            'live_vaccine_allowed': d['live_vaccine_allowed'],
            'therapy_pause_needed': d['therapy_pause_needed'],
            'immune_response_dead_vaccine': d['immune_response_dead_vaccine'],
            'drug_class': d['drug_class'],
            'class_abstract': d.get('class_abstract', '')
        }
        break

steroids = [
    'Cortison', 'Hydrocortison', 'Methylprednisolon',
    'Triamcinolon', 'Dexamethason', 'Betamethason', 'Deflazacort', 'Cloprednol',
    'Fludrocortison', 'Budesonid', 'Fluticason', 'Beclometason', 'Mometason',
    'Ciclesonid', 'Fluocortolon', 'Paramethason'
]

updated_count = 0
for d in db:
    sub = d['substance']
    for s in steroids:
        # Match exact substance or "-Depot" (e.g. Triamcinolon-Depot). 
        # Don't match " und Antibiotika" because those are mostly topical drops.
        if sub == s or sub == f"{s}-Depot":
            if not d.get('is_immunosuppressant'):
                d.update(template)
                updated_count += 1
                print(f"Updated {sub}")

with open('app_drugs_db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Total updated: {updated_count}")
