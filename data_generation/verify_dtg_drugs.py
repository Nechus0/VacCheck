import json

db_path = '../app_drugs_db.json'
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# from add_substanzklasse.py
substanz_map = {
    "Prednison": "Kortikosteroide",
    "Prednisolon": "Kortikosteroide",
    "Inebilizumab": "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)",
    "Obinutuzumab": "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)",
    "Ocrelizumab": "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)",
    "Ofatumumab": "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)",
    "Rituximab": "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)",
    "Alemtuzumab": "CD52-Rezeptor-Antagonist",
    "Belimumab": "Inhibitor des B-Zell-Aktivierungsfaktors",
    "Adalimumab": "Anti-TNF",
    "Certolizumab": "Anti-TNF",
    "Etanercept": "Anti-TNF",
    "Golimumab": "Anti-TNF",
    "Infliximab": "Anti-TNF",
    "Anifrolumab": "Anti-IFN-1R",
    "Anakinra": "Anti-IL-1",
    "Canakinumab": "Anti-IL-1",
    "Basiliximab": "Anti-IL-2R",
    "Dupilumab": "Anti-IL-4/-13",
    "Mepolizumab": "Anti-IL-5",
    "Benralizumab": "Anti-IL-5",
    "Siltuximab": "Anti-IL-6",
    "Tocilizumab": "Anti-IL-6R",
    "Sarilumab": "Anti-IL-6R",
    "Satralizumab": "Anti-IL-6R",
    "Ustekinumab": "Anti-IL-12 und -23",
    "Lebrikizumab": "Anti-IL-13",
    "Tralokinumab": "Anti-IL-13",
    "Bimekizumab": "Anti-IL-17",
    "Brodalumab": "Anti-IL-17",
    "Ixekizumab": "Anti-IL-17",
    "Secukinumab": "Anti-IL-17",
    "Guselkumab": "Anti-IL-23",
    "Mirikizumab": "Anti-IL-23",
    "Risankizumab": "Anti-IL-23",
    "Tildrakizumab": "Anti-IL-23",
    "Dimethylfumarat": "Peripher wirksame B- und T-Zell-depletierende Substanzen",
    "Diroximelfumarat": "Peripher wirksame B- und T-Zell-depletierende Substanzen",
    "Leflunomid": "Peripher wirksame B- und T-Zell-depletierende Substanzen",
    "Teriflunomid": "Peripher wirksame B- und T-Zell-depletierende Substanzen",
    "Etrasimod": "S1P-Rezeptor-Modulator",
    "Fingolimod": "S1P-Rezeptor-Modulator",
    "Ozanimod": "S1P-Rezeptor-Modulator",
    "Siponimod": "S1P-Rezeptor-Modulator",
    "Glatirameracetat": "Immunstimulanzien/-modulatoren",
    "Interferon beta": "Immunstimulanzien/-modulatoren",
    "Peginterferon alfa-2a": "Immunstimulanzien/-modulatoren",
    "Sulfasalazin": "Immunstimulanzien/-modulatoren",
    "Mesalazin": "Immunstimulanzien/-modulatoren",
    "Mifamurtid": "Immunstimulanzien/-modulatoren",
    "Omalizumab": "Anti-IgE",
    "Nipocalimab": "Fc-Rezeptor-Blocker",
    "Rozanolixizumab": "Fc-Rezeptor-Blocker",
    "Cyclophosphamid": "Zytostatika",
    "Dacarbazin": "Zytostatika",
    "Ifosfamid": "Zytostatika",
    "Trofosfamid": "Zytostatika",
    "Mitoxantron": "Zytostatika",
    "Cladribin": "Zytostatika",
    "Irinotecan": "Zytostatika",
    "Azathioprin": "Organabstoßung/Antiproliferativ",
    "Belatacept": "Organabstoßung/Antiproliferativ",
    "Ciclosporin": "Organabstoßung/Antiproliferativ",
    "Voclosporin": "Organabstoßung/Antiproliferativ",
    "6-Mercaptopurin": "Organabstoßung/Antiproliferativ",
    "Tacrolimus": "Organabstoßung/Antiproliferativ",
    "Everolimus": "Organabstoßung/Antiproliferativ",
    "Mycophenolat-Mofetil": "Organabstoßung/Antiproliferativ",
    "Mycophenolsäure": "Organabstoßung/Antiproliferativ",
    "Methotrexat": "Organabstoßung/Antiproliferativ",
    "Abatacept": "T-Lymphozyten-Kostimulatoren-Inhibitor",
    "Natalizumab": "Interaktionsinhibitor von VCAM-1",
    "Vedolizumab": "Intestinaler Integrin-Antagonist",
    "Baricitinib": "Januskinase (JAK-)Inhibitoren",
    "Filgotinib": "Januskinase (JAK-)Inhibitoren",
    "Ritlecitinib": "Januskinase (JAK-)Inhibitoren",
    "Tofacitinib": "Januskinase (JAK-)Inhibitoren",
    "Upadacitinib": "Januskinase (JAK-)Inhibitoren",
    "Deucravacitinib": "Januskinase (JAK-)Inhibitoren",
    "Apremilast": "Anti-PDE4",
    "Eculizumab": "Inhibitor des Komplementproteins C5",
    "Crovalimab": "Inhibitor des Komplementproteins C5",
    "Ravulizumab": "Inhibitor des Komplementproteins C5",
    "Zilucoplan": "Inhibitor des Komplementproteins C5",
    "Avacopan": "Inhibitor des Komplementproteins C5",
    "Pegcetacoplan": "Inhibitor des Komplementproteins C3",
    "Sutimlimab": "Inhibitor des Komplementproteins C1s",
    "Iptacopan": "Komplementinhibitor Faktor B",
    "Danicopan": "Komplementinhibitor Faktor D",
    "Pirfenidon": "Andere Immunsuppressiva/immunmod. Therapeutika",
    "Efgartigimod alfa": "Andere Immunsuppressiva/immunmod. Therapeutika"
}

db_immunos = [d for d in db if d.get('is_immunosuppressant')]
db_immuno_substances = [d['substance'].lower() for d in db_immunos]

missing = []
for key in substanz_map.keys():
    # Check if exact or fuzzy match exists in the db_immuno_substances
    found = False
    for sub in db_immuno_substances:
        if key.lower() in sub:
            found = True
            break
    if not found:
        missing.append(key)

print("Missing immunosuppressants in database:")
for m in missing:
    print("- " + m)
