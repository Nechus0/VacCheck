import json

with open('app_drugs_db.json', 'r') as f:
    db = json.load(f)

print(f"Original DB size: {len(db)}")

def is_phytopharmaka(sub):
    s = sub.lower()
    keywords = ['pflanzlich', 'extrakt', 'blätter', 'kraut', 'wurzel', 'blüten', 'organextrakte', 'öl', 'rinde', 'samen', 'früchte', 'zapfen', 'balsam']
    for k in keywords:
        # Check if it's a separate word or part of a compound word
        if k in s:
            return True
    return False

new_db = []
removed_kombinationen = 0
removed_phyto = 0

for d in db:
    sub = d['substance']
    
    # 1. Check Phytopharmaka
    if is_phytopharmaka(sub) and not d.get('is_immunosuppressant'):
        removed_phyto += 1
        continue
        
    # 2. Check Kombinationen
    if ', Kombinationen' in sub and not d.get('is_immunosuppressant'):
        removed_kombinationen += 1
        continue
        
    # 3. Check for exact duplicate aliases inside a drug
    # e.g., if brand_names has duplicates
    d['brand_names'] = list(set(d['brand_names']))
    
    new_db.append(d)

print(f"Removed {removed_phyto} Phytopharmaka")
print(f"Removed {removed_kombinationen} Kombinationen")
print(f"New DB size: {len(new_db)}")

# Check ASS aliases
for d in new_db:
    if d['substance'] == 'Acetylsalicylsäure':
        print("Acetylsalicylsäure aliases:", d['brand_names'])

