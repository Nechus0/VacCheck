import json

db_path = '../app_drugs_db.json'

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

abstracts_map = {
    "Kortikosteroide": "Glukokortikoide hemmen die Aktivierung von T- und B-Zellen und reduzieren entzündliche Botenstoffe. Dadurch fehlt dem Körper die nötige Abwehr, um die abgeschwächten Viren eines Lebendimpfstoffs zu kontrollieren.",
    "B-Zell-depletierende Substanzen (anti-CD19/anti-CD20)": "Diese Medikamente zerstören gezielt B-Zellen, die für die Antikörperproduktion verantwortlich sind. Ohne Antikörper kann der Körper die Impfviren nicht effektiv neutralisieren.",
    "CD52-Rezeptor-Antagonist": "Führt zu einem massiven Abbau von zirkulierenden T- und B-Zellen. Dieses stark geschwächte Immunsystem ist den vermehrungsfähigen Viren eines Lebendimpfstoffs schutzlos ausgeliefert.",
    "Inhibitor des B-Zell-Aktivierungsfaktors": "Hemmt das Überleben und die Entwicklung von B-Zellen. Dies schwächt die Immunantwort und die Antikörperproduktion, sodass Lebendimpfviren ein Risiko darstellen.",
    "Anti-TNF": "Blockiert den Tumornekrosefaktor (TNF), einen zentralen Botenstoff der Entzündungsreaktion und zellulären Abwehr. Bei einer Lebendimpfung droht eine ungebremste Virusvermehrung im Gewebe.",
    "Anti-IFN-1R": "Blockiert Interferon-Rezeptoren, die essenziell für die unmittelbare antivirale Abwehr sind. Ohne dieses Alarmsystem können sich Impfviren unkontrolliert ausbreiten.",
    "Anti-IL-1": "Hemmt Interleukin-1, einen wichtigen Botenstoff der angeborenen Immunabwehr. Die verzögerte Immunreaktion kann die Kontrolle des Lebendimpfstoffs beeinträchtigen.",
    "Anti-IL-2R": "Blockiert die Aktivierung und Vermehrung von T-Zellen. Ohne eine effektive T-Zell-Antwort kann der Körper intrazelluläre Erreger (wie Viren in Lebendimpfstoffen) nicht bekämpfen.",
    "Anti-IL-4/-13": "Greift in Entzündungswege ein, die vor allem bei allergischem Asthma und Neurodermitis wichtig sind. Obwohl das Risiko geringer als bei anderen Immunsuppressiva ist, gilt bei Lebendimpfungen aus Sicherheitsgründen oft ein genereller Vorbehalt.",
    "Anti-IL-5": "Richtet sich spezifisch gegen Eosinophile (Zellen der allergischen Entzündung). Lebendimpfungen sind hier laut Zulassung teils möglich, jedoch ist aufgrund der Immunmodulation Vorsicht geboten.",
    "Anti-IL-6": "Hemmt Interleukin-6, einen zentralen Entzündungsbotenstoff. Dies dämpft die Akut-Phase-Reaktion und die T-Zell-Aktivierung, was die Abwehr gegen Impfviren schwächt.",
    "Anti-IL-6R": "Blockiert den Rezeptor für Interleukin-6, was die Entzündungsreaktion und die Aktivierung von Immunzellen stark unterdrückt, sodass Lebendimpfviren nicht sicher kontrolliert werden können.",
    "Anti-IL-12 und -23": "Hemmen Botenstoffe, die essenziell für die T-Zell-Aktivierung sind. Eine abgeschwächte zelluläre Abwehr kann zu einer unkontrollierten Vermehrung des Impfvirus führen.",
    "Anti-IL-13": "Blockiert spezifische Entzündungswege (oft bei atopischer Dermatitis). Aufgrund des Eingriffs in das Immunsystem ist bei Lebendimpfungen Vorsicht geboten.",
    "Anti-IL-17": "Hemmt Interleukin-17, was besonders die Abwehr an den Schleimhäuten und der Haut schwächt. Lebendimpfungen sind aufgrund des allgemeinen immunsuppressiven Effekts kontraindiziert.",
    "Anti-IL-23": "Unterdrückt die Aktivierung bestimmter T-Zellen. Die unzureichende zelluläre Immunantwort birgt das Risiko, dass der Körper mit dem Impfvirus nicht fertig wird.",
    "Peripher wirksame B- und T-Zell-depletierende Substanzen": "Hemmen die Vermehrung von T- und B-Zellen oder zerstören sie. Der resultierende Mangel an Abwehrzellen erhöht das Risiko einer impfinduzierten Infektion erheblich.",
    "S1P-Rezeptor-Modulator": "Sperren Lymphozyten in den Lymphknoten ein, sodass sie nicht ins periphere Blut gelangen können. Die im Gewebe fehlenden Abwehrzellen können die Impfviren nicht bekämpfen.",
    "Immunstimulanzien/-modulatoren": "Verändern tiefgreifend die Balance der Immunantwort. Je nach Wirkstoff und individueller Reaktion kann das Immunsystem die Lebendimpfviren nicht adäquat kontrollieren.",
    "Anti-IgE": "Blockiert IgE-Antikörper, um allergische Reaktionen zu verhindern. Lebendimpfungen sind hier grundsätzlich erlaubt, da die generelle antivirale Abwehr intakt bleibt.",
    "Fc-Rezeptor-Blocker": "Beschleunigen den Abbau von Antikörpern (IgG) im Blut. Dies kann die körpereigene Abwehr schwächen und die Kontrolle von Lebendimpfviren gefährden.",
    "Zytostatika": "Zerstören sich schnell teilende Zellen und verursachen eine ausgeprägte Leukopenie (Mangel an weißen Blutkörperchen). Dem Körper fehlt jegliche Grundlage, um Impfviren abzuwehren.",
    "Organabstoßung/Antiproliferativ": "Hemmen die Zellteilung und die T-Zell-Aktivierung massiv, um eine Organabstoßung zu verhindern. Dieses künstlich unterdrückte Immunsystem ist Lebendimpfviren schutzlos ausgeliefert.",
    "T-Lymphozyten-Kostimulatoren-Inhibitor": "Verhindert das notwendige 'Zweite Signal' zur Aktivierung von T-Zellen. Ohne aktivierte T-Zellen können Viren nicht eliminiert werden.",
    "Interaktionsinhibitor von VCAM-1": "Verhindert, dass Immunzellen aus den Blutgefäßen in das Gewebe (insbesondere das ZNS) einwandern. Eine lokale Immunabwehr gegen Impfviren ist dadurch gestört.",
    "Intestinaler Integrin-Antagonist": "Verhindert das Einwandern von T-Zellen in den Darm. Systemische Lebendimpfungen (z.B. Gelbfieber) sind zwar teilweise möglich, orale Impfungen (z.B. Cholera, Typhus) können jedoch unwirksam sein.",
    "Januskinase (JAK-)Inhibitoren": "Blockieren intrazelluläre Signalwege (JAK/STAT) für viele verschiedene Zytokine, was die Immunantwort sehr breit unterdrückt und die rasche Abwehr von Impfviren verhindert.",
    "Anti-PDE4": "Wirkt entzündungshemmend durch Erhöhung des intrazellulären cAMP. Lebendimpfungen sind hier meistens ausreichend sicher, aber individuelle ärztliche Rücksprache ist ratsam.",
    "Inhibitor des Komplementproteins C5": "Blockiert das Komplementsystem, das für die frühe Zerstörung von Erregern wichtig ist. Dies erhöht vor allem das Risiko für bakterielle Infektionen, beeinträchtigt aber auch die allgemeine Immunkontrolle.",
    "Inhibitor des Komplementproteins C3": "Hemmt die zentrale Komplementkaskade, wodurch Erreger nicht mehr effektiv für die Zerstörung markiert werden. Die Abwehr von Lebendimpfviren kann eingeschränkt sein.",
    "Inhibitor des Komplementproteins C1s": "Blockiert den klassischen Weg des Komplementsystems. Wie bei anderen Komplementinhibitoren kann die Immunantwort auf den Lebendimpfstoff gestört sein.",
    "Komplementinhibitor Faktor B": "Blockiert den alternativen Weg des Komplementsystems. Erreger können dadurch in der Frühphase der Infektion schlechter abgewehrt werden.",
    "Komplementinhibitor Faktor D": "Hemmt den alternativen Komplementweg. Die reduzierte Immunantwort kann zu einer verminderten Kontrolle des Impfvirus führen.",
    "Andere Immunsuppressiva/immunmod. Therapeutika": "Unterdrücken oder verändern die körpereigene Abwehr auf zellulärer Ebene. Die mangelhafte Immunkontrolle birgt das Risiko schwerer Reaktionen auf Lebendimpfstoffe."
}

updated_count = 0

for drug in db:
    if drug.get('is_immunosuppressant') and drug.get('drug_class'):
        cls = drug['drug_class']
        if cls in abstracts_map:
            drug['class_abstract'] = abstracts_map[cls]
            updated_count += 1
        else:
            print(f"Warning: No abstract found for class '{cls}' (Substance: {drug['substance']})")

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} immunosuppressants with an abstract.")
