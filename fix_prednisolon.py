import json

db_path = 'app_drugs_db.json'
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

for drug in db:
    if drug['substance'] == 'Prednisolon':
        drug['is_immunosuppressant'] = True
        drug['live_vaccine_allowed'] = "Nein (> 20mg/d)"
        drug['therapy_pause_needed'] = "> 2 Monate"
        drug['immune_response_dead_vaccine'] = "Vermindert"
        drug['drug_class'] = "Kortikosteroide"
        drug['class_abstract'] = "Glukokortikoide hemmen die Aktivierung von T- und B-Zellen und reduzieren entzündliche Botenstoffe. Dadurch fehlt dem Körper die nötige Abwehr, um die abgeschwächten Viren eines Lebendimpfstoffs zu kontrollieren."
        print("Updated Prednisolon!")
        break

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
