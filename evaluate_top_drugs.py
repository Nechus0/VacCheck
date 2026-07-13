import json

# Known top ~30 active ingredients in Germany (by prescriptions / DDD)
top_drugs = [
    "Levothyroxin", "Ramipril", "Pantoprazol", "Metoprolol", "Omeprazol", 
    "Ibuprofen", "Amlodipin", "Simvastatin", "Metamizol", "Metformin", 
    "Atorvastatin", "Bisoprolol", "Candesartan", "Diclofenac", "Salbutamol",
    "Torasemid", "Hydrochlorothiazid", "Valsartan", "Allopurinol", "Mirtazapin",
    "Citalopram", "L-Thyroxin", "Ginkgo", "Macrogol", "Cholecalciferol",
    "Acetylsalicylsäure", "ASS", "Lisinopril", "Sertralin", "Furosemid",
    "Prednisolon", "Escitalopram", "Novaminsulfon", "Cefuroxim", "Amoxicillin",
    "Doxycyclin", "Ciprofloxacin", "Clindamycin", "Azithromycin", "Clarithromycin",
    "Loratadin", "Cetirizin", "Desloratadin", "Fexofenadin", "Levocetirizin"
]

with open('app_drugs_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print("--- Testing Representation in App ---")

missing = []
for test_drug in top_drugs:
    found = False
    for d in db:
        # Search substance or brand
        sub = d['substance'].lower()
        brands = [b.lower() for b in d['brand_names']]
        if test_drug.lower() in sub or test_drug.lower() in brands:
            found = True
            break
    if not found:
        missing.append(test_drug)

print(f"Missing Top Drugs: {missing}")
