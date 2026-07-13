import json

# A robust dictionary of Top ~50 German active ingredients and their most common brand names
brand_map = {
    "Levothyroxin": ["L-Thyroxin", "Euthyrox"],
    "Pantoprazol": ["Pantozol", "Rifun"],
    "Ramipril": ["Delix", "Vesdil"],
    "Metoprolol": ["Beloc", "Metohexal"],
    "Omeprazol": ["Antra", "Gastroloc"],
    "Ibuprofen": ["Ibu", "Ibuflam", "Dolormin", "Nurofen"],
    "Amlodipin": ["Norvasc"],
    "Simvastatin": ["Zocor", "Denan"],
    "Metamizol": ["Novaminsulfon", "Novalgin", "Berlosin"],
    "Metformin": ["Glucophage", "Siofor", "Mescorit"],
    "Atorvastatin": ["Sortis"],
    "Bisoprolol": ["Concor", "Bisohexal"],
    "Candesartan": ["Blopress", "Atacand"],
    "Diclofenac": ["Voltaren", "Diclac"],
    "Salbutamol": ["Sultanol", "Bronchospray"],
    "Torasemid": ["Torem", "Unat"],
    "Hydrochlorothiazid": ["Esidrix", "HCT"],
    "Valsartan": ["Diovan", "Provas"],
    "Allopurinol": ["Zyloric", "Urikoliz"],
    "Mirtazapin": ["Remergil"],
    "Citalopram": ["Cipramil"],
    "Cholecalciferol": ["Vigantol", "Dekristol"],
    "Acetylsalicylsäure": ["Aspirin", "ASS", "Godamed", "HerzASS"],
    "Lisinopril": ["Acerbon", "Zestril"],
    "Sertralin": ["Zoloft", "Gladem"],
    "Furosemid": ["Lasix"],
    "Prednisolon": ["Decortin H"],
    "Escitalopram": ["Cipralex"],
    "Cefuroxim": ["Elobact"],
    "Amoxicillin": ["Amoxypen", "Infectomox"],
    "Doxycyclin": ["Vibramycin", "Supracyclin"],
    "Ciprofloxacin": ["Ciprobay"],
    "Clindamycin": ["Sobelin"],
    "Azithromycin": ["Zithromax", "Ultreon"],
    "Clarithromycin": ["Klacid"],
    "Loratadin": ["Lisino", "Lorano"],
    "Cetirizin": ["Zyrtec", "Cetadolor"],
    "Desloratadin": ["Aerius"],
    "Fexofenadin": ["Telfast"],
    "Levocetirizin": ["Xyzall"],
    "Pregabalin": ["Lyrica"],
    "Gabapentin": ["Neurontin"],
    "Duloxetin": ["Cymbalta", "Yentreve"],
    "Venlafaxin": ["Trevalor", "Efectin"],
    "Quetiapin": ["Seroquel"],
    "Risperidon": ["Risperdal"],
    "Apixaban": ["Eliquis"],
    "Rivaroxaban": ["Xarelto"],
    "Edoxaban": ["Lixiana"],
    "Dabigatran": ["Pradaxa"],
    "Marcumar": ["Phenprocoumon"], # Inverse mapping
    "Phenprocoumon": ["Marcumar", "Falithrom"]
}

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

updated_count = 0
for d in db:
    sub = d['substance']
    # Check if the exact substance or a partial match (if safe) is in our map
    for base_sub, brands in brand_map.items():
        if base_sub.lower() in sub.lower():
            # Inject brands
            existing = set(d.get('brand_names', []))
            for b in brands:
                existing.add(b)
            if len(existing) > len(d.get('brand_names', [])):
                d['brand_names'] = list(existing)
                updated_count += 1

with open('app_drugs_db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {updated_count} database entries with top German brand names!")
