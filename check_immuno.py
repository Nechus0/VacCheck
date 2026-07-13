import json

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print("Checking current immunosuppressant rules...")
seen_classes = {}
for d in db:
    if d.get('is_immunosuppressant'):
        cls = d.get('drug_class')
        if cls not in seen_classes:
            seen_classes[cls] = {
                'example': d['substance'],
                'live_allowed': d.get('live_vaccine_allowed'),
                'pause': d.get('therapy_pause_needed'),
                'dead_resp': d.get('immune_response_dead_vaccine')
            }

for k, v in seen_classes.items():
    print(f"\nClass: {k}")
    print(f"  Example: {v['example']}")
    print(f"  Live Allowed: {v['live_allowed']}")
    print(f"  Pause: {v['pause']}")

