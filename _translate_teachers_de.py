#!/usr/bin/env python3
"""
Splice GERMAN teacher translations into assets/js/i18n.js.

DE chrome keys (sub.teachers.*, teachers.stat.*, teachers.grade.*,
teachers.picker.*, teachers.filter.*, teachers.tab.*, teachers.chip.*,
teachers.sec.*) and 192 card descriptions (cd_t_NNN).

Splice anchor in DE block: after the last cd_uni_143 line.
Idempotent: replaces existing teacher DE block if already inserted.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent
I18N = ROOT / "assets" / "js" / "i18n.js"

# ---------------- DE chrome translations ----------------
DE_CHROME = {
    "sub.teachers.back": "Zurück zu den Ressourcen",
    "sub.teachers.badge": "Kostenlose Tools für Lehrkräfte & Pädagog:innen",
    "sub.teachers.title": "Ressourcen für Lehrkräfte",
    "sub.teachers.desc": "192 kuratierte kostenlose Tools in 16 Lehrclustern. Wähle unten ein Thema und entdecke die 12 besten Ressourcen.",
    "teachers.stat.tools": "Kostenlose Tools",
    "teachers.stat.topics": "Lehrcluster",
    "teachers.stat.levels.val": "Vorschule→Hochschule",
    "teachers.stat.levels.lbl": "Alle Stufen",
    "teachers.stat.free": "Kostenlos",
    "teachers.grade.prek": "Vorschule",
    "teachers.grade.primary": "Grundschule",
    "teachers.grade.secondary": "Sekundarstufe",
    "teachers.grade.higher": "Hochschule",
    "teachers.grade.sen": "Sonderpädagogik",
    "teachers.grade.all": "Alle Stufen",
    "teachers.picker.label": "Nach Thema entdecken",
    "teachers.picker.heading": "Wähle einen der <em>16 Lehrcluster</em>, um die besten kostenlosen Tools zu entdecken",
    "teachers.filter.label": "Nach Stufe filtern:",
    "teachers.filter.all": "Alle Stufen",

    # tab + chip labels (kept identical for consistency with EN labels)
    "teachers.tab.planning": "Unterrichtsplanung", "teachers.chip.planning": "Unterrichtsplanung",
    "teachers.tab.ai": "KI-Co-Piloten", "teachers.chip.ai": "KI-Co-Piloten",
    "teachers.tab.interactive": "Interaktive Stunden", "teachers.chip.interactive": "Interaktive Stunden",
    "teachers.tab.assessment": "Lernkontrolle", "teachers.chip.assessment": "Lernkontrolle",
    "teachers.tab.management": "Klassenführung", "teachers.chip.management": "Klassenführung",
    "teachers.tab.admin": "Noten & Admin", "teachers.chip.admin": "Noten & Admin",
    "teachers.tab.comms": "Eltern-Kommunikation", "teachers.chip.comms": "Eltern-Kommunikation",
    "teachers.tab.visual": "Visuelles Denken", "teachers.chip.visual": "Visuelles Denken",
    "teachers.tab.content": "Material erstellen", "teachers.chip.content": "Material erstellen",
    "teachers.tab.inclusion": "Differenzierung", "teachers.chip.inclusion": "Differenzierung",
    "teachers.tab.language": "Sprache & Schreiben", "teachers.chip.language": "Sprache & Schreiben",
    "teachers.tab.wellbeing": "Lehrer-Wohlbefinden", "teachers.chip.wellbeing": "Lehrer-Wohlbefinden",
    "teachers.tab.stem": "MINT-Labore", "teachers.chip.stem": "MINT-Labore",
    "teachers.tab.creative": "Kunst & Musik", "teachers.chip.creative": "Kunst & Musik",
    "teachers.tab.homework": "Hausaufgaben & Familie", "teachers.chip.homework": "Hausaufgaben & Familie",
    "teachers.tab.pd": "Weiterbildung", "teachers.chip.pd": "Weiterbildung",

    # section label / h2 / desc
    "teachers.sec.planning.label": "Lehrplan & Unterrichtsdesign",
    "teachers.sec.planning.h2": "Unterrichtsplanung & Curriculum — die 12 besten kostenlosen Tools",
    "teachers.sec.planning.desc": "Erstelle in Minuten standardgerechte Einheiten, Wochenpläne und unterrichtsfertige Stunden — kostenlose Vorlagen und vollständige offene Lehrpläne.",
    "teachers.sec.ai.label": "KI-Assistenten für Lehrkräfte",
    "teachers.sec.ai.h2": "KI-Co-Piloten für Lehrkräfte — die 12 besten kostenlosen Tools",
    "teachers.sec.ai.desc": "Erstelle Stundenpläne, Bewertungsraster, differenzierte Arbeitsblätter und Rückmeldungen in Sekunden — kostenlose KI-Tools für Pädagog:innen.",
    "teachers.sec.interactive.label": "Folien, Videos & Interaktives",
    "teachers.sec.interactive.h2": "Interaktive Stunden & Folien — die 12 besten kostenlosen Tools",
    "teachers.sec.interactive.desc": "Verwandle jede Stunde in ein interaktives Erlebnis — Quizze, Umfragen, Zeichnungen und Diskussionen live im Klassenzimmer einbinden.",
    "teachers.sec.assessment.label": "Quizze, Bewertungsraster & Feedback",
    "teachers.sec.assessment.h2": "Lernkontrolle, Quizze & Feedback — die 12 besten kostenlosen Tools",
    "teachers.sec.assessment.desc": "Verstehen schnell überprüfen, Bewertungsraster bauen und sinnvolles Feedback geben — formative Tools, Exit-Tickets und benotete Quizze.",
    "teachers.sec.management.label": "Verhalten & Routinen",
    "teachers.sec.management.h2": "Klassenführung & Engagement — die 12 besten kostenlosen Tools",
    "teachers.sec.management.desc": "Positive Routinen aufbauen, gutes Verhalten anerkennen und Klassenrituale reibungslos gestalten — kostenlose Tools, die Schüler:innen respektieren.",
    "teachers.sec.admin.label": "Anwesenheit, Noten & Dateien",
    "teachers.sec.admin.h2": "Anwesenheit, Noten & Verwaltung — die 12 besten kostenlosen Tools",
    "teachers.sec.admin.desc": "Weniger Papierkram — kostenlose LMS, Notenbücher, Anwesenheits-Tracker und Dateifreigabe-Tools, die einfach funktionieren.",
    "teachers.sec.comms.label": "Familie & Schulgemeinschaft",
    "teachers.sec.comms.h2": "Eltern- & Gemeinschaftskommunikation — die 12 besten kostenlosen Tools",
    "teachers.sec.comms.desc": "Erreiche jede Familie in ihrer Sprache und auf ihre Art — sichere Nachrichten, Newsletter und Übersetzungstools.",
    "teachers.sec.visual.label": "Whiteboards & Mind-Maps",
    "teachers.sec.visual.h2": "Visuelles Denken & Brainstorming — die 12 besten kostenlosen Tools",
    "teachers.sec.visual.desc": "Mache Schüler-Denken sichtbar — kollaborative Whiteboards, Mind-Maps, Sticky-Note-Boards und Concept-Mapping-Tools.",
    "teachers.sec.content.label": "Arbeitsblätter, Video & Visuelles",
    "teachers.sec.content.h2": "Material erstellen: Arbeitsblätter, Video & Visuelles — die 12 besten kostenlosen Tools",
    "teachers.sec.content.desc": "Erstelle ansprechende Arbeitsblätter, Infografiken, Podcasts und Videos — keine Designkenntnisse nötig, alles kostenlos für Lehrkräfte.",
    "teachers.sec.inclusion.label": "Inklusion & Sonderpädagogik",
    "teachers.sec.inclusion.h2": "Differenzierung, Inklusion & SEN — die 12 besten kostenlosen Tools",
    "teachers.sec.inclusion.desc": "Erreiche jede:n Lernende:n — adaptive Lese-Apps, Barrierefreiheit, dyslexie-freundliche Schriften und SEN-Ressourcen.",
    "teachers.sec.language.label": "DaZ, ELL & Schreibförderung",
    "teachers.sec.language.h2": "Sprachförderung & Schreibhilfe — die 12 besten kostenlosen Tools",
    "teachers.sec.language.desc": "Unterstütze EAL/ESL-Lernende und stärke das Schreiben aller — Übersetzung, Grammatik, Wortschatz und Lesehilfen.",
    "teachers.sec.wellbeing.label": "Mentale Gesundheit & Selbstfürsorge",
    "teachers.sec.wellbeing.h2": "Lehrer-Wohlbefinden & Selbstfürsorge — die 12 besten kostenlosen Tools",
    "teachers.sec.wellbeing.desc": "Sorge zuerst für dich selbst — kostenlose Ressourcen für mentale Gesundheit, Achtsamkeit und Burnout-Prävention für Pädagog:innen.",
    "teachers.sec.stem.label": "Simulationen & virtuelle Labore",
    "teachers.sec.stem.h2": "MINT-Labore & Simulationen — die 12 besten kostenlosen Tools",
    "teachers.sec.stem.desc": "Führe Physik-, Chemie-, Biologie- und Mathe-Experimente in jeder Klasse durch — kostenlose interaktive Simulationen und virtuelle Labore.",
    "teachers.sec.creative.label": "Kreativstudios",
    "teachers.sec.creative.h2": "Kunst, Musik & Kreativstudios — die 12 besten kostenlosen Tools",
    "teachers.sec.creative.desc": "Kostenlose Studios für Musik, Zeichnen, Animation und Audio — perfekt für Kunststunden, fächerübergreifende Projekte und AGs.",
    "teachers.sec.homework.label": "Lernen zu Hause für Eltern",
    "teachers.sec.homework.h2": "Hausaufgaben & Familienlernen — die 12 besten kostenlosen Tools",
    "teachers.sec.homework.desc": "Empfehle Familien sichere, wirksame Ressourcen — Hausaufgabenhilfe, Wiederholung und Lernen zu Hause für Eltern.",
    "teachers.sec.pd.label": "Berufliche Weiterbildung",
    "teachers.sec.pd.h2": "Weiterbildung für Lehrkräfte — die 12 besten kostenlosen Tools",
    "teachers.sec.pd.desc": "Kostenlose CPD, Mikro-Zertifikate und Zertifikate von Coursera, edX, Microsoft, Google, Apple und der Open University.",
}

# ---------------- DE card descriptions (192 cards: cd_t_000 through cd_t_191) ----------------
DE_CARDS = {
    # ── Cluster 1: Lesson Planning (cd_t_000 - cd_t_011) ──
    "cd_t_000": "Kostenlose, standardgerechte Lese-Stunden für Klassen 3–12 — Texte, Fragen, Tests und vollständige ELA-Einheiten an einem Ort.",
    "cd_t_001": "Kostenloses ELA- und Mathe-Curriculum vom Bundesstaat New York für Vorschule bis 12. Klasse — vollständige Jahresmodule, Lehrer-Guides und Schülermappen.",
    "cd_t_002": "Kostenlose K–12 MINT-Lehrplan-Bibliothek — ingenieursorientierte Stunden und Hands-on-Aktivitäten passend zu NGSS und Common Core.",
    "cd_t_003": "Kostenlose Common-Core-Aufgaben, Stunden und Planungstools vom Team, das die Standards verfasst hat — ELA und Mathe.",
    "cd_t_004": "Über 420.000 kostenlose Stundenpläne, Aktivitäten und Einheiten von AFT-Lehrkräften — durchsuchbar nach Fach, Klasse und Standard.",
    "cd_t_005": "Der kostenlose Bereich von TPT — Millionen lehrer-erstellter Arbeitsblätter, Einheiten und Druckvorlagen, gefiltert auf den No-Cost-Track.",
    "cd_t_006": "Kostenlose, am UK-Lehrplan orientierte Ressourcen aus der weltgrößten Lehr-Community — komplette Stoffverteilungen und Stundenpakete.",
    "cd_t_007": "Kostenlose lehrplanrelevante Videoclips und fertige Stunden der BBC — besonders stark in Geschichte, Naturwissenschaften und englischer Literatur.",
    "cd_t_008": "Kostenlose, top-bewertete offene Mathe- und ELA-Lehrpläne (6.–8. Klasse Mathe von Illustrative Math, EL Education ELA) — vollständige Jahreskurse.",
    "cd_t_009": "Kostenlose wiederverwendbare Stundengerüste für jeden Inhalt — Cyber Sandwich, Iron Chef, Worst Preso Ever und mehr.",
    "cd_t_010": "Kostenlose UbD-Planungsvorlagen und Starter-Kits — Backward Design von Lernzielen über Belege bis zur Instruktion.",
    "cd_t_011": "Schlanker digitaler Stundenplaner — kostenlose 30-Tage-Testphase, dann günstige Bezahlversion; Wochenraster-Ansicht von Klassenlehrkräften geliebt.",

    # ── Cluster 2: AI Co-pilots (cd_t_012 - cd_t_023) ──
    "cd_t_012": "Über 60 von Lehrkräften gebaute KI-Tools — Stundenpläne, IEP-Ziele, Bewertungsraster, Differenzierung und Feedback. Großzügige kostenlose Stufe für Pädagog:innen.",
    "cd_t_013": "KI-generierte interaktive Stunden in 30 Sekunden — Folien, Umfragen, Zeichnungen und Exit-Tickets, mit starkem Gratisplan für Lehrkräfte.",
    "cd_t_014": "Passe jeden Text sofort jeder Lesestufe an — gestufte Passagen, Wortschatz und Fragen; die KI-Goldreferenz für Differenzierung.",
    "cd_t_015": "Über 100 Generatoren für Stundenpläne, Tests und Anpassungen — die kostenlose Stufe deckt die meisten Alltagsbedürfnisse im Klassenzimmer.",
    "cd_t_016": "Anthropics KI-Vorzeige-Assistent — herausragend für Stundenplanung, Bewertungsraster, Eltern-Mails und Feedback-Entwürfe.",
    "cd_t_017": "OpenAIs kostenlose Stufe umfasst GPT-4o mini — stark für Fragenerstellung, Zusammenfassungen und Arbeitsblatt-Generierung.",
    "cd_t_018": "Googles KI tief integriert mit Docs, Slides und Drive — ideal für Lehrkräfte, die bereits in Google Workspace arbeiten.",
    "cd_t_019": "Kostenlose KI in Word, OneNote und PowerPoint — generiere Stunden-Outlines, Foliensätze und Schüler-Handouts direkt im Dokument.",
    "cd_t_020": "Kostenlose Chrome-Erweiterung mit KI-Sidebar in Google Docs und Slides — sofortiges Feedback, Niveau-Anpassung und Bewertungsraster.",
    "cd_t_021": "Sichere, überwachte KI-Chat-„Räume“ für Schüler:innen plus KI-Assistent für Lehrkräfte — großzügige kostenlose Stufe für K–12.",
    "cd_t_022": "Lade Lehrbuchkapitel und Notizen hoch — Googles KI antwortet ausschließlich aus deinen Quellen, mit Audio-Zusammenfassungen für die Wiederholung.",
    "cd_t_023": "Anthropics kostenloser Kurs zu den vier Kern-KI-Kompetenzen — Delegation, Beschreibung, Beurteilung, Sorgfalt. Für Pädagog:innen entwickelt.",

    # ── Cluster 3: Interactive Lessons & Slides (cd_t_024 - cd_t_035) ──
    "cd_t_024": "Interaktive Folien-Stunden mit Umfragen, Quizzen, Zeichnungen und VR — die kostenlose Silver-Stufe deckt die meisten Klassenraumbedürfnisse.",
    "cd_t_025": "Füge interaktive Fragen zu Google Slides oder PowerPoint hinzu — die Gratis-Stufe unterstützt die beliebtesten formativen Bewertungsformate.",
    "cd_t_026": "Bette Fragen und Notizen direkt in jedes Video ein — kostenlos für Lehrkräfte (bis zu 20 gespeicherte Videos) mit voller Auswertung.",
    "cd_t_027": "Drag-and-Drop-Digitalstunden mit Videos, Folien, Artikeln und Quizzen auf einer Seite — kostenlos für Lehrkräfte.",
    "cd_t_028": "Erstelle interaktive Stunden mit Umfragen, Sofort-Feedback und Schülergeräten — kostenlos für einzelne Lehrkräfte.",
    "cd_t_029": "Canvas voller Pro-Suite ist kostenlos für verifizierte K–12-Lehrkräfte — Folien, Infografiken, Videos und Schüler-Klassen.",
    "cd_t_030": "Erstelle interaktive Präsentationen, Escape Rooms und Infografiken — Gratis-Stufe mit hunderten Pädagogik-Vorlagen.",
    "cd_t_031": "Füge Hotspots zu Bildern und Videos mit Text, Audio und Links hinzu — die kostenlose Basic-Stufe deckt kleine Klassen ab.",
    "cd_t_032": "Kostenlose unbegrenzte Bildschirmaufnahmen für verifizierte Lehrkräfte — Flipped-Classroom-Videos mit eingebauter Engagement-Anzeige aufnehmen.",
    "cd_t_033": "Kostenloses Screencast-Tool mit klassenfreundlichen Untertiteln und einfachem Hosting — von Millionen Pädagog:innen genutzt.",
    "cd_t_034": "Kostenlose All-in-One-Klassenraumanzeige — Timer, Zufallsgenerator, Ampel, Arbeitssymbole und Lärmpegel auf einem Bildschirm.",
    "cd_t_035": "Kostenloses Kurations-Tool — organisiere Videos, Artikel, Tweets und Schülerarbeiten in teilbaren Sammlungen für jede Stunde.",

    # ── Cluster 4: Assessment (cd_t_036 - cd_t_047) ──
    "cd_t_036": "Das klassische Game-Show-Quizformat — die kostenlose Basic-Stufe unterstützt bis zu 40 Spielende für formative Live-Bewertung.",
    "cd_t_037": "Selbstgesteuerte KI-gestützte Quizze und Stunden — kostenlos für Lehrkräfte mit umfangreichen Fragenbanken und Live-Modus.",
    "cd_t_038": "Live-Umfragen, Wortwolken und Q&A vom Publikum — die kostenlose Stufe deckt formative Bewertung in kleinen Klassen perfekt ab.",
    "cd_t_039": "Live-Umfragen, Erhebungen und Q&A-Overlay für jedes Meeting oder jede Klasse — die Gratis-Stufe unterstützt bis zu 100 Teilnehmende.",
    "cd_t_040": "Kostenlose automatisch ausgewertete Quizze mit Sofort-Feedback und Auswertung — das Arbeitstier für Bewertung in Google Classroom.",
    "cd_t_041": "Kostenlose Quizze und Umfragen mit Auto-Bewertung und Verzweigungslogik — in jedem Microsoft-Konto enthalten.",
    "cd_t_042": "Schnelle Quizze, Exit-Tickets und Space-Race-Spiel — kostenlos für bis zu 50 Schüler:innen pro Raum.",
    "cd_t_043": "Papier-QR-Karten plus Telefon-Scan — formative Bewertung ohne Schülergeräte, kostenlos für bis zu 60 Karten.",
    "cd_t_044": "Vorlagenbasierte Quiz-Spiele — Match-up, Anagramm, Gameshow — generiere jede Aktivität aus einer Wortliste; kostenlos bis zu 5 gespeicherte.",
    "cd_t_045": "Sieh Schülerantworten live während des Tippens — Zeichnungen, Gleichungen, Absätze. Die kostenlose Bronze-Stufe deckt die formative Kernnutzung ab.",
    "cd_t_046": "Kostenloses Google-Sheets-Add-on für Selbst-, Peer- und Lehrer-Bewertung — generiert personalisiertes Feedback pro Schüler:in.",
    "cd_t_047": "AP- und SAT/ACT-Prüfungsfragen mit detaillierten Erklärungen — kostenloser Probezugang und laufende Gratis-Übung zu vielen Themen.",

    # ── Cluster 5: Classroom Management (cd_t_048 - cd_t_059) ──
    "cd_t_048": "Baue eine positive Klassenraumkultur auf — Punkte, Eltern-Nachrichten und Schülerportfolios. Kostenlos für alle Lehrkräfte und Eltern.",
    "cd_t_049": "Gamifizierte Klassenführungs-Plattform — Schüler:innen verdienen XP und Kräfte für gutes Verhalten. Großzügige kostenlose Stufe.",
    "cd_t_050": "Visueller Klassenraum-Lärmmesser, der mit Schallpegeln animiert — die kostenlose Lite-Version wird von Grundschullehrkräften geliebt.",
    "cd_t_051": "Kostenloser, lustiger visueller Lärmmesser — hüpfende Bälle reagieren auf die Klassenraumlautstärke. Perfektes Hintergrund-Tool bei Gruppenarbeit.",
    "cd_t_052": "Kostenloser Zufallsgenerator für Namen — drehe das Rad, um Schüler:innen fair auszuwählen. Gespeicherte Listen, Farben, werbefrei.",
    "cd_t_053": "Kostenlose, lustige Klassenraum-Timer — Bomben, Kerzen, Rennautos — halte Aktivitäten mit ansprechenden Visuals im Zeitplan.",
    "cd_t_054": "All-in-One-Klassenraumanzeige — Timer, Arbeitssymbole, Ampel, Zufallsgenerator und Lärmmesser zusammen.",
    "cd_t_055": "Schulweite Plattform für positive Verhaltensverstärkung — kostenloser Probezugang; viele kostenlose PBIS-Ressourcen auf der Seite.",
    "cd_t_056": "Kostenlose Bewegungs- und Achtsamkeitsvideos — kurze Pausen, die K–5-Schüler:innen mitten in der Stunde refokussieren.",
    "cd_t_057": "Kostenlose Morgenkreis-Begrüßungen, Aktivitäten und Botschafts-Ideen — forschungsbasierte sozial-emotionale Klassenraum-Gemeinschaft.",
    "cd_t_058": "Kostenlose SEL-Ressourcen und wöchentliche Webinare von der Goldreferenz für sozial-emotionale Lernforschung.",
    "cd_t_059": "Der meistgefolgte Lehr-Blog Großbritanniens — kostenlose praktische Strategien für Verhalten, Engagement und Routinen.",

    # ── Cluster 6: Admin & Grading (cd_t_060 - cd_t_071) ──
    "cd_t_060": "Das kostenlose Standard-LMS für Millionen Lehrkräfte — Aufgaben, Bewertung, Kommunikation und Dateifreigabe an einem Ort.",
    "cd_t_061": "Kostenloser Bildungsplan mit Klassen, Aufgaben, OneNote-Klassennotizbüchern und 1 TB OneDrive-Speicher pro Schüler:in.",
    "cd_t_062": "Kostenlose Version des führenden Hochschul-LMS — vollständige Aufgaben, Bewertung und Bewertungsraster für einzelne Lehrkräfte.",
    "cd_t_063": "Kostenloses Open-Source-LMS, weltweit von Universitäten genutzt — selbst hosten oder die kostenlose MoodleCloud-Stufe für kleine Klassen.",
    "cd_t_064": "Kuratierte Liste kostenloser Edmodo-Nachfolger — Schoology Free, ManageBac-Trials und moderne Lehrer-Schüler-LMS-Optionen.",
    "cd_t_065": "Standardbasiertes Notenbuch, dem über 5 Mio. Schüler:innen vertrauen — kostenlos für Solo-Lehrkräfte; Bezahlpläne für Schulen und Bezirke.",
    "cd_t_066": "Webbasiertes Notenbuch und Reporting-Tool — die Gratis-Stufe deckt Klassenbedürfnisse ab; integriert sich mit allen großen LMS.",
    "cd_t_067": "Kostenloser 15-GB-Cloudspeicher mit Docs, Sheets und Slides — Lehrmaterialien teilen und Aufgaben nahtlos einsammeln.",
    "cd_t_068": "Kostenlose 2-GB-Stufe mit Klassenraumfreigabe und kollaborativen Ordnern — vergünstigte Bildungs-Pläne verfügbar.",
    "cd_t_069": "Kostenloser Plus-Plan für verifizierte Pädagog:innen — Wikis, Stunden-Notizen, Schüler-Tracker und kollaborative Klassenraum-Hubs.",
    "cd_t_070": "Kostenlose flexible Datenbank — ideal für Schülerdaten, IEP-Ziele, Projektportfolios und Lehrplan-Karten.",
    "cd_t_071": "Kostenlose Kanban-Boards — verfolge Stundenplanung, Schülerprojekte, Schulkomitees und persönliche Lehrer-To-dos.",

    # ── Cluster 7: Parent Comms (cd_t_072 - cd_t_083) ──
    "cd_t_072": "Sende sichere Einweg-Nachrichten an Schüler:innen und Eltern — die Gratis-Stufe deckt tägliche Klassenraum-Ankündigungen mit Auto-Übersetzung ab.",
    "cd_t_073": "Kostenloser Familien-Engagement-Messenger, der Nachrichten zwischen Lehrkräften und Eltern in über 100 Sprachen automatisch übersetzt.",
    "cd_t_074": "Kostenlose sichere Eltern-Nachrichten mit Foto- und Videofreigabe — übersetzt Nachrichten automatisch in über 35 Sprachen.",
    "cd_t_075": "Kostenlose Eltern-Kommunikation und Konferenz-Planer — Vorschul- und Grundschul-Favorit mit Foto-Sharing.",
    "cd_t_076": "Wunderschöne Drag-and-Drop-Klassen-Newsletter — die Gratis-Stufe unterstützt 5 Newsletter mit vollen Design-Tools.",
    "cd_t_077": "Schulweite Kommunikationsplattform mit Auto-Übersetzung — viele Bezirke bieten kostenlose Lehrerkonten über Schulpläne an.",
    "cd_t_078": "Kostenlose Sofort-Übersetzung in über 130 Sprachen — Text, Fotos, Gespräche und Dokumente für die Eltern-Kommunikation.",
    "cd_t_079": "Höhere Übersetzungsqualität als Google für europäische Sprachen — die Gratis-Stufe deckt die meisten Lehrer-Kommunikationsbedürfnisse ab.",
    "cd_t_080": "Kostenlose Echtzeit-Gesprächsübersetzung für Elterngespräche — Smartphones sprechen jeweils eine Sprache, die App untertitelt live.",
    "cd_t_081": "Kostenlose geteilte Dokumente für Elterngespräche, IEP-Entwürfe und Klassen-Newsletter-Zusammenarbeit mit Kommentaren.",
    "cd_t_082": "Kostenlose Konferenz-Planung, Klassenparty-Anmeldungen und Freiwilligen-Listen — das Arbeitstier für Eltern-Koordination.",
    "cd_t_083": "Kostenlose Microsoft-Video-Diskussionsplattform — Schülerarbeit sicher mit Familien teilen und Video-Antworten einsammeln.",

    # ── Cluster 8: Visual Thinking (cd_t_084 - cd_t_095) ──
    "cd_t_084": "Kostenloses geteiltes Whiteboard von Google — Sticky Notes, Zeichnungen, Bilder und Live-Zusammenarbeit für bis zu 50 Schüler:innen.",
    "cd_t_085": "Kostenloser Education-Plan mit unbegrenzten Boards und Vorlagen für verifizierte Lehrkräfte — das beliebteste Tool für visuelle Zusammenarbeit.",
    "cd_t_086": "Kostenloses FigJam für Pädagog:innen und Lernende — kollaboratives Whiteboarding mit charmanten Vorlagen und Engagement-Funktionen.",
    "cd_t_087": "Kostenlose Bildungsstufe von Lucids Whiteboard — Sticky Notes, Abstimmungen und unendliche Leinwand für Klassen-Brainstorming.",
    "cd_t_088": "Kostenlos für verifizierte Hochschul-Studierende und Dozent:innen — kollaborativer visueller Arbeitsraum für Design Thinking und Gruppenarbeit.",
    "cd_t_089": "Kostenlose „Sticky-Note-Wand“ für Ideen, Fotos, Links und Audio — drei kostenlose Padlets und von Lehrkräften geliebt.",
    "cd_t_090": "Kostenlose unbegrenzte öffentliche Mind-Maps — klare visuelle Hierarchie, Echtzeit-Zusammenarbeit und Bild-Einbettung.",
    "cd_t_091": "Kostenlos 3 Mind-Maps mit Kollaboration — ideal für Klassen-Concept-Mapping und Schüler-Gruppenprojekte.",
    "cd_t_092": "Kostenloses Open-Source-Diagramming — Flowcharts, ER-Diagramme, UML, Mind-Maps. Speichert direkt in Drive oder OneDrive.",
    "cd_t_093": "Kostenloses Browser-Whiteboard von Google — schnelle Skizzen, Anmerkungen und Schüler-Visualnotizen ohne Installation.",
    "cd_t_094": "Kostenloses Sofort-Lehrer-Dashboard — jede:r Schüler:in hat ein eigenes Board, die Lehrkraft sieht alle live.",
    "cd_t_095": "Kostenloses Open-Source-Whiteboard für Schulen — funktioniert mit jedem Beamer oder interaktiven Bildschirm, kein Abo.",

    # ── Cluster 9: Content Creation (cd_t_096 - cd_t_107) ──
    "cd_t_096": "Vollständiges Canva Pro kostenlos für verifizierte K–12-Lehrkräfte — Arbeitsblätter, Poster, Videos, Folien, Animationen und Infografiken.",
    "cd_t_097": "Kostenloses Adobe Express für K–12-Lehrkräfte und Schüler:innen — Flyer, Social-Posts, Videos und KI-Bildgenerierung.",
    "cd_t_098": "Millionen kostenloser Icons für Arbeitsblätter und Folien — vollständige Quellenangabe nötig, aber hervorragende Qualität und Vielfalt.",
    "cd_t_099": "Kostenlose hochwertige Fotos für jedes Klassenraummaterial — keine Quellenangabe nötig, voll nutzbar in Lehrressourcen.",
    "cd_t_100": "Kostenlose Fotos, Videos, Illustrationen und Musik — voll nutzbar in Klassenraummaterial ohne Quellenangabe.",
    "cd_t_101": "Public-Domain-Clipart-Bibliothek — über 160.000 kostenlose Bilder für Arbeitsblätter, Klassenraumposter und Schülerprojekte.",
    "cd_t_102": "Kostenloser Wortwolken-Generator — verwandle Vokabel-Listen in ansprechende Visuals für Aushänge und Stundeneinstiege.",
    "cd_t_103": "Kostenlose konfigurierbare Mathe- und Lese-Arbeitsblätter — generieren, drucken, neu generieren. Kein Login erforderlich.",
    "cd_t_104": "Erzeuge bis zu 7 verschiedene Spielstile aus einer Wortliste — kostenlos für Lehrkräfte, perfekt für Vokabeln und Wiederholung.",
    "cd_t_105": "Animierter Video-Ersteller für Erklärvideos — die Gratis-Stufe unterstützt 5-Min-Videos mit umfangreicher Charakterbibliothek.",
    "cd_t_106": "Kostenloser Open-Source-Audio-Editor — Podcasts aufnehmen, Audio für Stunden bearbeiten, mit jedem Audioformat arbeiten.",
    "cd_t_107": "Kostenloser Open-Source-Desktop-Videoeditor — einfach genug für Schülerprojekte, leistungsstark für Lehrer-Tutorials.",

    # ── Cluster 10: Differentiation / SEN (cd_t_108 - cd_t_119) ──
    "cd_t_108": "Umfassende kostenlose Ressourcen für Lehrkräfte und Eltern zu Dyslexie, ADHS und Lernunterschieden — forschungsbasiert.",
    "cd_t_109": "Das definitive Universal-Design-for-Learning-Framework — kostenlose Richtlinien, Beispiele und Implementierungs-Tools.",
    "cd_t_110": "Kostenlos für US-Schüler:innen mit Lese-Beeinträchtigung — über 1,4 Mio. barrierefreie Hörbücher und E-Books mit Text-zu-Sprache.",
    "cd_t_111": "Kostenloses Text-zu-Sprache mit natürlichen Stimmen — liest PDFs, Webseiten und Word-Dokumente vor, um den Lesezugang zu unterstützen.",
    "cd_t_112": "Kostenlose Open-Source-dyslexiefreundliche Schriftart — bewiesen reduziert sie Buchstabenrotation, inklusive Browser-Erweiterungen.",
    "cd_t_113": "Kostenloser 30-Tage-Probezugang zum führenden Lese-Förder-Tool — Text-zu-Sprache, prädiktives Tippen, Bildwörterbuch.",
    "cd_t_114": "Passe jeden Text sofort jeder Lesestufe an — gestufte Passagen, Wortschatz und Fragen; KI-Goldreferenz für Differenzierung.",
    "cd_t_115": "Kostenlose gestufte Nachrichtenartikel — jeder Artikel auf 5 Lesestufen für differenzierten Inhaltszugang.",
    "cd_t_116": "Kostenlose Ressourcen zu sozialen Fertigkeiten, Autismus und Verhalten — Bildkarten, Lieder, Spiele und druckbare visuelle Pläne.",
    "cd_t_117": "Kostenlose kuratierte Sensorik- und Feinmotorik-Aktivitäten für SEN-Klassen — Ruheecken, Sensorik-Boxen und OT-empfohlene Ideen.",
    "cd_t_118": "Kostenloses Microsoft-Tool — liest jeden Text vor mit Zeilenfokus, Silbentrennung, Bildwörterbuch und über 60 Sprachen.",
    "cd_t_119": "Kostenlose downloadbare Leitfäden der British Dyslexia Association für Lehrkräfte — Best-Practice-Anpassungen im Klassenraum.",

    # ── Cluster 11: Language & Writing (cd_t_120 - cd_t_131) ──
    "cd_t_120": "Kostenlose Sofort-Übersetzung in über 130 Sprachen — Text, Gespräche, Fotos und Dokumente. Unverzichtbar für DaZ-Klassen.",
    "cd_t_121": "Höhere Übersetzungsqualität als Google für europäische Sprachen — natürlich klingender Output für akademisches Schreiben.",
    "cd_t_122": "Kostenlose Sprachlern-Plattform mit Lehrer-Dashboards — verfolge den Fortschritt der Schüler:innen in über 40 Zielsprachen.",
    "cd_t_123": "Kostenlose zweisprachige forschungsbasierte Ressourcen für ELL-Lehrkräfte — Strategien, Stunden, Familien-Handouts und Buchlisten.",
    "cd_t_124": "Kostenlose Grammarly-Stufe — Vorschläge zu Grammatik, Klarheit und Ton für Schüler-Schreiben in Browser, Word und Docs.",
    "cd_t_125": "Kostenlose Web-App, die komplexe Sätze, Passivkonstruktionen und Adverbien hervorhebt — klareres Schüler-Schreiben in Sekunden.",
    "cd_t_126": "Füge schwierigen Text ein — Rewordify ersetzt schwere Wörter durch einfachere mit Definitionen beim Hover.",
    "cd_t_127": "Kostenloser Karteikarten-Ersteller und Lernmodi — Wortschatz, Grammatik-Drills und Sprachübung für jede Klasse.",
    "cd_t_128": "Adaptive Wortschatzübung mit Verwendungshinweisen — kostenlos für einzelne Lehrkräfte, Bestenlisten machen Übung spannend.",
    "cd_t_129": "Kostenlose vertrauenswürdige zweisprachige Wörterbücher mit Beispielsätzen und Forendiskussionen — ideal für MFL-Klassen.",
    "cd_t_130": "Kostenlose von der Community geteilte ESL-Arbeitsblätter — über eine Million Druckvorlagen nach Stufe und Grammatikfokus getaggt.",
    "cd_t_131": "Kostenlose Ressourcen des British Council für Teen-ESL-Lernende — Videos, Magazinartikel und Prüfungsvorbereitung auf allen Stufen.",

    # ── Cluster 12: Wellbeing (cd_t_132 - cd_t_143) ──
    "cd_t_132": "Calm-Apps kostenlose K–12-Lehrer-Initiative — voller App-Zugang inkl. Sleep-Stories, Meditationen und Musik.",
    "cd_t_133": "Kostenloses Headspace Plus für verifizierte K–12-Lehrkräfte in den USA, UK, Kanada und Australien — Achtsamkeit und Meditation.",
    "cd_t_134": "Kostenlose Meditations-App mit der größten kostenlosen Bibliothek — über 200.000 geführte Meditationen und lehrer-spezifische Tracks.",
    "cd_t_135": "Kostenlose Artikel, geführte Praktiken und Forschung zu Achtsamkeit — zugängliche Einführung für gestresste Lehrkräfte.",
    "cd_t_136": "Berkeleys kostenlose wissenschaftsbasierte SEL-Ressourcen für Lehrkräfte — Praktiken für Dankbarkeit, Freundlichkeit und Resilienz im Klassenraum.",
    "cd_t_137": "Kostenloser Podcast und Artikel von Daniela Falecki — praktische Wohlbefinden-Strategien und Burnout-Prävention für Lehrkräfte.",
    "cd_t_138": "Britische Wohltätigkeitsorganisation — kostenloses 24/7-Helpline, Counselling und mentale Gesundheit für jede Lehrkraft, unabhängig vom Land.",
    "cd_t_139": "Kostenlose globale Bewegung für Lehrer-Mental-Health-Treffen — über 100 Chapter weltweit, online und persönlich.",
    "cd_t_140": "Jennifer Gonzalez' kostenlose Artikel und Podcast-Folgen zu Lehrer-Selbstfürsorge — praktisch, ehrlich, ohne toxische Positivität.",
    "cd_t_141": "Kostenloser Blog mit realistischen Strategien zum Umgang mit Stress, Eltern und Verwaltung — von Klassenlehrkräften geschrieben.",
    "cd_t_142": "Kostenlose MHA-Toolkit für Lehrkräfte — Burnout-Selbstscreening, evidenzbasierte Bewältigungsstrategien und Krisenhilfe-Verzeichnisse.",
    "cd_t_143": "Kostenloses interaktives kognitiv-verhaltenstherapeutisches Programm — bewiesene Selbsthilfe gegen Stress und niedrige Stimmung, weltweit genutzt.",

    # ── Cluster 13: STEM Labs & Simulations (cd_t_144 - cd_t_155) ──
    "cd_t_144": "Über 160 kostenlose interaktive Physik-, Chemie-, Biologie- und Mathe-Simulationen der University of Colorado — in über 90 Sprachen.",
    "cd_t_145": "Kostenlose 3D-Design-, Elektronik-Simulations- und Code-Block-Plattform von Autodesk — speziell für Klassenzimmer entwickelt.",
    "cd_t_146": "Kostenlose dynamische Mathematik — Geometrie, Algebra, Analysis, 3D und Statistik in einem Tool. Von 100 Mio. Schüler:innen genutzt.",
    "cd_t_147": "Kostenloser Grafikrechner und Klassenraum-Aktivitäten — der Goldstandard für die Visualisierung von Funktionen im Mathematikunterricht.",
    "cd_t_148": "MITs kostenlose Block-Programmier-Plattform — über 100 Mio. Projekte weltweit, der Einstieg in die Programmierung für Kinder ab 8.",
    "cd_t_149": "Kostenlose agentenbasierte Modellierung für Biologie, Sozialwissenschaft und komplexe Systeme — läuft im Browser, keine Installation.",
    "cd_t_150": "Kostenloses Planetarium im Browser — zeige Schüler:innen den Nachthimmel von überall, jederzeit, perfekt für Astronomie.",
    "cd_t_151": "Kostenlose computergestützte Wissensmaschine — löst und erklärt Mathe, plottet Funktionen und beantwortet Wissenschaftsfragen Schritt für Schritt.",
    "cd_t_152": "Kostenloser 2D-Physik-Sandkasten — baue Maschinen, lasse Objekte fallen, sieh Newtons Gesetze live. Von Physiklehrkräften geliebt.",
    "cd_t_153": "Kostenloses Daten-Wissenschafts-Tool für Klassen 6–12 — Drag-and-Drop-Diagramme und Analysen mit Beispieldatensätzen über alle Fächer.",
    "cd_t_154": "Kostenlose Biologie-Ressourcen vom Howard Hughes Medical Institute — interaktive Videos, virtuelle Labore und Click-and-Learns.",
    "cd_t_155": "Kostenlose American-Chemical-Society-Stunden, Lab-Kits und Adventures-in-Chemistry-Portal — von der Vorschule bis darüber hinaus.",

    # ── Cluster 14: Art, Music & Creative Studios (cd_t_156 - cd_t_167) ──
    "cd_t_156": "Kostenlose verspielte Musik-Experimente von Google — Song Maker, Rhythm, Spectrogram, Kandinsky. Kein Login, läuft im Browser.",
    "cd_t_157": "Browserbasierte kollaborative DAW — nimm Podcasts und Musik mit Schüler:innen in Echtzeit auf. Großzügige Gratis-Stufe.",
    "cd_t_158": "Kostenloser Retro-Chiptune-Musik-Maker — Schüler:innen komponieren 8-Bit-Melodien und Beats in Minuten, kein Konto nötig.",
    "cd_t_159": "Kostenlose Demo der wild-spaßigen Beatbox-Musik-App — ziehe Kostüme auf Charaktere, um Beats und Melodien zu schichten.",
    "cd_t_160": "Kostenlose Open-Source-Software für professionelles digitales Malen und Animation — umfangreiche Pinsel-Engine, in Kunsthochschulen genutzt.",
    "cd_t_161": "Kostenlose professionelle Zeichen-App von Autodesk — übersichtliche Oberfläche, vollständiger Pinselsatz, im Web, Desktop und Mobile verfügbar.",
    "cd_t_162": "Kostenlose Open-Source-Notensatzsoftware — Notenblätter für jedes Instrument oder Ensemble schreiben, abspielen und drucken.",
    "cd_t_163": "Browserbasierter kollaborativer Notensatz — Schüler:innen komponieren live in Gruppen, kostenlose Education-Stufe mit Klassen-Dashboard.",
    "cd_t_164": "Kostenlose cloudbasierte DAW mit Klassen-Steuerung — Schüler:innen kollaborieren an Musikprojekten mit Echtzeit-Mixing.",
    "cd_t_165": "Kostenloses Pixel-Art-Studio mit Community-Galerie — erstelle Sprite-Art, Animationen und Spielgrafiken im Browser.",
    "cd_t_166": "Kostenloser Open-Source-Mehrspur-Audio-Editor — Podcasts aufnehmen, Musik bearbeiten, Klassenraum-Aufnahmen säubern.",
    "cd_t_167": "Kostenlose virtuelle Museumstouren, zoombare Meisterwerke und AR-Experimente von über 2.000 Institutionen weltweit.",

    # ── Cluster 15: Homework & Family Learning (cd_t_168 - cd_t_179) ──
    "cd_t_168": "Kostenlose Eltern-Dashboards in allen Fächern K–12 — Fortschritt verfolgen, Stärken und Schwächen sehen, mit Lehrkräften teilen.",
    "cd_t_169": "Kostenlose UK-lehrplangerechte Wiederholung nach Klassenstufen — Leitfäden für Eltern zur Hausaufgaben- und Prüfungsvorbereitung.",
    "cd_t_170": "Kostenlos 10 Fragen/Tag in 8.500 Skills — umfassende K–12-Übung mit elternfreundlichen Fortschrittsberichten.",
    "cd_t_171": "Kostenlose Bewertungen jeder Kinder-App, jedes Spiels und Films — hilf Familien, kluge Medienentscheidungen zu treffen, forschungsbasiert.",
    "cd_t_172": "Kostenlose 30-Tage-Testphase des umfassenden Frühförder-Lehrplans — Phonetik, Mathe, Kunst und Musik für Kinder von 2–8.",
    "cd_t_173": "Kostenloser Probezugang zum führenden Frühlese-Programm — Phonetik, Sichtwörter und dekodierbare Bücher für Alter 3–13.",
    "cd_t_174": "Adaptive Mathe-Übung für K–12 mit weltweiten Turnieren — kostenlose Familien-Tests und Eltern-Fortschritts-Tracking.",
    "cd_t_175": "Kostenloses spielbasiertes Mathe für Klassen 1–8 — Kinder bekämpfen Monster durch Antworten, Eltern sehen Wochenberichte.",
    "cd_t_176": "Kostenlose GCSE/A-level-Wiederholungs-Plattform für UK-Familien — interaktive Kurse basierend auf kognitionswissenschaftlicher Forschung.",
    "cd_t_177": "Kostenlose Karteikarten und Lernmodi — über eine halbe Milliarde Lernsets zu jedem Fach und Prüfungsplan.",
    "cd_t_178": "Kostenlose lehrplangerechte Druckvorlagen, Arbeitsblätter und Aktivitätspakete — UK-basiert, aber in über 200 Ländern genutzt.",
    "cd_t_179": "Über 40.000 Kinder-E-Books, Hörbücher und Videos — kostenlos für verifizierte Pädagog:innen, günstig für Familien.",

    # ── Cluster 16: PD & Certificates (cd_t_180 - cd_t_191) ──
    "cd_t_180": "Stanford-, Penn- und Johns-Hopkins-Lehrkurse kostenlos auditieren — Bezahl-Zertifikate verfügbar, voller Inhalt immer kostenlos.",
    "cd_t_181": "Harvard-, MIT- und HarvardX-Bildungskurse — kostenlos zum Auditieren, mit optionalen kostenpflichtigen MicroMasters für Schulleitung.",
    "cd_t_182": "Kostenlose kurze Lehrkurse von UK-Universitäten — praktische Pädagogik, EdTech und fachspezifische Weiterbildung.",
    "cd_t_183": "Kostenlose Open-University-Kurse mit Teilnahmebescheinigungen — vollständige Weiterbildung in inklusiver Lehre, Mentoring, Führung.",
    "cd_t_184": "MITs kostenloses Pädagogen-Portal — Videos von MIT-Klassen mit Lehr-Einsichten, Aufgabensätzen und Prüfungsfragen.",
    "cd_t_185": "Kostenlose Microsoft-Innovative-Educator-Badges — Kurse zu Teams, OneNote, Minecraft Edu, Flip und globaler Zusammenarbeit.",
    "cd_t_186": "Kostenloses Apple-Teacher-Selbstlernprogramm — verdiene Badges und Anerkennung für Skills mit iPad, Mac und Apple-Apps.",
    "cd_t_187": "Kostenlose Schulung zu Google Workspace für Lehrkräfte, mit Level-1- und 2-Certified-Educator-Bezahlprüfungen.",
    "cd_t_188": "International Society for Tech in Education — kostenlose Webinare, Artikel und viele kostenlose PD-Ressourcen der führenden EdTech-Organisation.",
    "cd_t_189": "Kostenlose Khan-Academy-Schulung für Lehrkräfte — Onboarding, Klassenraum-Integration und Schüler-Fortschrittsberichte.",
    "cd_t_190": "Hunderte kostenlose Artikel zu innovativer Pädagogik, projektbasiertem Lernen und Klassenraum-Design.",
    "cd_t_191": "Kostenlose Live- und On-Demand-Webinare von Education Week — modernste Forschung, Politik und Klassenraumpraxis.",
}

assert len(DE_CARDS) == 192, f"Expected 192 card translations, got {len(DE_CARDS)}"

# ---------------- Splice into i18n.js ----------------
src = I18N.read_text(encoding="utf-8")

# Build the DE block string
def fmt(k, v):
    return f"    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},\n"

de_block_parts = ["\n    /* ─────────────── Teachers page (DE) ─────────────── */\n"]
for k in DE_CHROME:
    de_block_parts.append(fmt(k, DE_CHROME[k]))
de_block_parts.append("    /* Teacher card descriptions DE (192 cards) */\n")
for k in sorted(DE_CARDS.keys()):
    de_block_parts.append(fmt(k, DE_CARDS[k]))
de_block = "".join(de_block_parts)

# Splice anchor: after the last cd_uni_143 line in DE block
# The DE block ends with cd_uni_143 and then `  }` and then `};`
DE_ANCHOR = "    \"cd_uni_143\": \"Kostenlose Kurse zu den UN-Nachhaltigkeitszielen — Klima, Gleichheit, Armut und Governance, unterrichtet von UN-Agenturen und Partnern.\",\n"
if DE_ANCHOR not in src:
    raise SystemExit("DE anchor not found — has DE cd_uni_143 line changed?")

START_MARK = "    /* ─────────────── Teachers page (DE) ─────────────── */"
if START_MARK in src:
    # Idempotent replace: from START_MARK up to the closing `  }\n};`
    pre, _, rest = src.partition(START_MARK)
    end_marker = "  }\n};"
    _, _, after = rest.partition(end_marker)
    src = pre + de_block.lstrip() + end_marker + after
    print("Refreshed existing teacher DE block.")
else:
    src = src.replace(DE_ANCHOR, DE_ANCHOR + de_block, 1)
    print(f"Inserted teacher DE block ({len(DE_CHROME) + len(DE_CARDS)} keys).")

# ---------------- Remove the obsolete legacy DE sub.teachers entries ----------------
# These predate the redesign: 'sub.teachers.badge': 'Für Lehrerinnen & Lehrer', 'sub.teachers.title': 'Kostenlose Lehrressourcen',
# We removed the EN counterparts implicitly because the new ones are inserted later in the same object;
# but for readability, also strip the old DE lines so they don't confuse future maintainers.
LEGACY_DE_BLOCK_PATTERN = re.compile(
    r"\n    'sub\.teachers\.badge': 'Für Lehrerinnen & Lehrer', 'sub\.teachers\.title': 'Kostenlose Lehrressourcen',\n"
    r"    'sub\.teachers\.desc': '60 kuratierte kostenlose Tools in 6 Themen\. Wähle unten ein Thema und sieh die Top 10\.',\n"
    r"    'sub\.teachers\.back': 'Zurück zu Ressourcen',\n"
)
new_src, n_removed = LEGACY_DE_BLOCK_PATTERN.subn("\n", src)
if n_removed:
    src = new_src
    print(f"Removed {n_removed} legacy DE sub.teachers block(s).")

# Same for legacy EN counterpart
LEGACY_EN_BLOCK_PATTERN = re.compile(
    r"\n    'sub\.teachers\.badge': 'For Educators & Teachers', 'sub\.teachers\.title': 'Free Teaching Resources',\n"
    r"    'sub\.teachers\.desc': '60 curated free tools across 6 topics\. Pick a topic below to see the top 10\.',\n"
    r"    'sub\.teachers\.back': 'Back to Resources',\n"
)
new_src, n_removed = LEGACY_EN_BLOCK_PATTERN.subn("\n", src)
if n_removed:
    src = new_src
    print(f"Removed {n_removed} legacy EN sub.teachers block(s).")

I18N.write_text(src, encoding="utf-8")
print(f"Wrote {I18N} ({len(src):,} bytes)")
