import json

with open('app_drugs_db.json', 'r') as f:
    db = json.load(f)

# Look for duplicates
seen_substances = {}
for d in db:
    sub = d['substance']
    if sub in seen_substances:
        print(f"Duplicate exact substance found: {sub}")
    seen_substances[sub] = True

# Group by base substance (e.g. before ', Kombinationen')
bases = {}
for d in db:
    sub = d['substance']
    base = sub.split(',')[0].strip()
    if base not in bases:
        bases[base] = []
    bases[base].append(sub)

duplicates_count = 0
for b, subs in bases.items():
    if len(subs) > 1:
        duplicates_count += 1
        if b == "Acetylsalicylsäure":
            print(f"Acetylsalicylsäure variants: {subs}")

print(f"Total base substances with variants: {duplicates_count}")

# Find Phytopharmaka
phytos = []
for d in db:
    sub = d['substance'].lower()
    if 'extrakt' in sub or 'blätter' in sub or 'wurzel' in sub or 'kraut' in sub or 'blüten' in sub or 'pflanz' in sub:
        phytos.append(d['substance'])

print(f"Potential Phytopharmaka count: {len(phytos)}")
print("Sample phytos:", phytos[:10])
