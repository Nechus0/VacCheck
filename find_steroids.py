import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

steroids = [
    'Cortison', 'Hydrocortison', 'Prednison', 'Prednisolon', 'Methylprednisolon',
    'Triamcinolon', 'Dexamethason', 'Betamethason', 'Deflazacort', 'Cloprednol',
    'Fludrocortison', 'Budesonid', 'Fluticason', 'Beclometason', 'Mometason',
    'Ciclesonid', 'Fluocortolon', 'Paramethason'
]

found_steroids = []
for d in db:
    sub = d['substance']
    for s in steroids:
        # Check if the substance exactly matches or starts with the steroid name
        if sub == s or sub.startswith(s + ' ') or sub.startswith(s + '-'):
            found_steroids.append((sub, d.get('is_immunosuppressant', False)))

for fs in found_steroids:
    print(f"{fs[0]} - is_immuno: {fs[1]}")

