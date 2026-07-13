import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

def is_phytopharmaka(sub):
    s = sub.lower()
    keywords = ['pflanzlich', 'extrakt', 'blätter', 'kraut', 'wurzel', 'blüten', 'organextrakte', 'öl', 'rinde', 'samen', 'früchte', 'zapfen', 'balsam']
    for k in keywords:
        if k in s:
            return True
    return False

new_db = []
for d in db:
    sub = d['substance']
    
    # 1. Check Phytopharmaka
    if is_phytopharmaka(sub) and not d.get('is_immunosuppressant'):
        continue
        
    # 2. Check Kombinationen
    if ', Kombinationen' in sub and not d.get('is_immunosuppressant'):
        continue
        
    # 3. Dedup brand_names
    # Convert all brands to lower to dedup case variations, but keep original case
    b_dict = {}
    for b in d['brand_names']:
        if b.lower() not in b_dict:
            b_dict[b.lower()] = b
    d['brand_names'] = list(b_dict.values())
    
    new_db.append(d)

with open('app_drugs_db.json', 'w', encoding='utf-8') as f:
    json.dump(new_db, f, ensure_ascii=False, indent=2)

print(f"Cleaned DB! Reduced from {len(db)} to {len(new_db)} drugs.")
