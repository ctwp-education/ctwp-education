#!/usr/bin/env python3
"""Splice German translations + new EN keys into assets/js/i18n.js.

Reads the existing i18n.js, removes the obsolete sub.uni.* DE block,
inserts new English cd_uni_* keys, and inserts the full German chrome
+ cd_uni_* translations.
"""
from pathlib import Path
import re
import json

ROOT = Path(__file__).parent
I18N = ROOT / "assets/js/i18n.js"
KEYS = json.loads((ROOT / "_uni_i18n_keys.json").read_text(encoding="utf-8"))

# ---- German chrome translations ---------------------------------------------
DE_CHROME = {
    "sub.uni.badge": "Zukunftskompetenzen für Hochschule & lebenslanges Lernen",
    "sub.uni.title": "Ressourcen für Studierende & lebenslange Lernende",
    "sub.uni.desc": "144 kuratierte kostenlose Tools in 12 Zukunftskompetenz-Clustern. Wähle unten ein Thema und entdecke die 12 besten Ressourcen.",
    "sub.uni.back": "Zurück zu Ressourcen",
    "uni.stat.tools": "Kostenlose Tools",
    "uni.stat.topics": "Zukunftsthemen",
    "uni.stat.levels.val": "BA→Erwachsen",
    "uni.stat.levels.lbl": "Alle Stufen",
    "uni.stat.free": "Kostenlos",
    "uni.grade.undergrad": "Bachelor",
    "uni.grade.grad": "Master",
    "uni.grade.phd": "PhD",
    "uni.grade.self": "Autodidakt:in",
    "uni.grade.all": "Alle Stufen",
    "uni.grade.adult": "Erwachsene:r",
    "uni.grade.switcher": "Quereinstieg",
    "uni.picker.label": "Nach Thema entdecken",
    "uni.picker.heading": "Wähle eines der <em>12 Zukunftskompetenz-Cluster</em> und finde die besten kostenlosen Tools",
    "uni.filter.label": "Nach Zielgruppe filtern:",
    "uni.filter.all": "Alle Zielgruppen",
    "uni.tab.ai": "KI-Kompetenz",
    "uni.tab.coding": "Coding & Daten",
    "uni.tab.security": "Cybersicherheit",
    "uni.tab.critical": "Kritisches Denken",
    "uni.tab.courseware": "Open Courseware",
    "uni.tab.research": "Forschung",
    "uni.tab.writing": "Schreiben & Reden",
    "uni.tab.productivity": "Produktivität",
    "uni.tab.mental": "Mentale Gesundheit",
    "uni.tab.finance": "Finanzkompetenz",
    "uni.tab.career": "Karriere & Unternehmertum",
    "uni.tab.civic": "Demokratie, Medien & Klima",
    "uni.chip.ai": "KI-Kompetenz",
    "uni.chip.coding": "Coding & Daten",
    "uni.chip.security": "Cybersicherheit",
    "uni.chip.critical": "Kritisches Denken",
    "uni.chip.courseware": "Open Courseware",
    "uni.chip.research": "Forschung",
    "uni.chip.writing": "Schreiben & Reden",
    "uni.chip.productivity": "Produktivität",
    "uni.chip.mental": "Mentale Gesundheit",
    "uni.chip.finance": "Finanzkompetenz",
    "uni.chip.career": "Karriere",
    "uni.chip.civic": "Demokratie & Klima",
    # Section headers (label + h2 + desc) for each of the 12 clusters
    "uni.sec.ai.label": "KI-Tutoren & Co-Piloten",
    "uni.sec.ai.h2": "KI-Kompetenz & gemeinsame Arbeit mit KI — die 12 besten kostenlosen Ressourcen",
    "uni.sec.ai.desc": "Die besten kostenlosen Assistenten, Kurse zum Prompt-Design und die Kompetenz, mit KI zu denken statt gegen sie.",
    "uni.sec.coding.label": "Programmierung & Data Science",
    "uni.sec.coding.h2": "Coding & Datenkompetenz — die 12 besten kostenlosen Ressourcen",
    "uni.sec.coding.desc": "Programmieren lernen, mit echten Datensätzen üben und ein Portfolio aufbauen — kostenlose Kurse, Sandboxes und Zertifikate.",
    "uni.sec.security.label": "Privatsphäre & Online-Sicherheit",
    "uni.sec.security.h2": "Cybersicherheit & digitale Privatsphäre — die 12 besten kostenlosen Ressourcen",
    "uni.sec.security.desc": "Schütze deine Konten, Daten und Identität online — und lerne die Sicherheitskompetenzen, die sonst niemand vermittelt.",
    "uni.sec.critical.label": "Argumentieren & Informationskompetenz",
    "uni.sec.critical.h2": "Kritisches Denken & Informationskompetenz — die 12 besten kostenlosen Ressourcen",
    "uni.sec.critical.desc": "Belege bewerten, Verzerrungen erkennen und unter Unsicherheit klar denken — laut WEF die wichtigste Kompetenz des nächsten Jahrzehnts.",
    "uni.sec.courseware.label": "Vorlesungen & MOOCs",
    "uni.sec.courseware.h2": "Open Courseware & lebenslanges Lernen — die 12 besten kostenlosen Ressourcen",
    "uni.sec.courseware.desc": "Komplette Kurse von MIT, Harvard, Stanford, Yale und anderen Top-Universitäten — kostenlos zum Audit, lerne alles von überall.",
    "uni.sec.research.label": "Quellen finden & zitieren",
    "uni.sec.research.h2": "Forschung, Zitation & offenes Wissen — die 12 besten kostenlosen Ressourcen",
    "uni.sec.research.desc": "Peer-reviewed Artikel finden, Zitate verwalten und kostenlose Open-Lehrbücher lesen — alles für deine Thesis oder Hausarbeit, gratis.",
    "uni.sec.writing.label": "Essays, Kommunikation & Stimme",
    "uni.sec.writing.h2": "Schreiben, Kommunikation & öffentliche Rede — die 12 besten kostenlosen Ressourcen",
    "uni.sec.writing.desc": "Klarere Essays schreiben, selbstsicher präsentieren und verständlich übersetzen — die menschliche Ergänzung zur KI-Hilfe.",
    "uni.sec.productivity.label": "Notizen, Fokus, Deadlines",
    "uni.sec.productivity.h2": "Produktivität, Fokus & Deep Work — die 12 besten kostenlosen Ressourcen",
    "uni.sec.productivity.desc": "Notizsysteme, Aufgabenmanager und Fokus-Tools, um deine Aufmerksamkeit zurückzugewinnen — die Voraussetzung für alles andere.",
    "uni.sec.mental.label": "Wohlbefinden & Resilienz",
    "uni.sec.mental.h2": "Mentale Gesundheit & Resilienz — die 12 besten kostenlosen Ressourcen",
    "uni.sec.mental.desc": "Schlaf, Stress, Angst und Stimmung — kostenlose, evidenzbasierte Ressourcen für dein wichtigstes Asset.",
    "uni.sec.finance.label": "Geld, Steuern, Investieren",
    "uni.sec.finance.h2": "Finanzkompetenz & wirtschaftliches Wissen — die 12 besten kostenlosen Ressourcen",
    "uni.sec.finance.desc": "Budget, Steuern, Zinseszins und Anlagegrundlagen — die Finanzkompetenzen, die Schulen selten vermitteln, die du aber bis 25 brauchst.",
    "uni.sec.career.label": "Job, Netzwerk, Gründung",
    "uni.sec.career.h2": "Karriere, Netzwerk & Unternehmertum — die 12 besten kostenlosen Ressourcen",
    "uni.sec.career.desc": "Praktika landen, Karriere wechseln, freiberuflich arbeiten oder ein Unternehmen gründen — die praktischen Skills für ein Portfolio-Karriereleben.",
    "uni.sec.civic.label": "Bürgerschaft & Nachhaltigkeit",
    "uni.sec.civic.h2": "Demokratie-, Medien- & Klimakompetenz — die 12 besten kostenlosen Ressourcen",
    "uni.sec.civic.desc": "Bürgerschaft im grossen Bild — Demokratie verstehen, Medien bewerten, Klimawissenschaft begreifen und die Ethik der Technologie.",
}

# ---- German card descriptions (144) -----------------------------------------
DE_CARDS = {
    # AI Fluency (000-011)
    "cd_uni_000": "Anthropic's Spitzen-Assistent — der grosszügige Gratis-Tarif deckt Schreiben, Code und Recherche mit starkem Reasoning ab.",
    "cd_uni_001": "OpenAIs ChatGPT — der Gratis-Tarif umfasst GPT-4o mini, Sprachmodus, Bildverständnis und einfache Datenanalyse.",
    "cd_uni_002": "Googles multimodaler Assistent mit tiefer Integration in Docs, Drive und Gmail — starker Gratis-Tarif mit Bild- und Code-Unterstützung.",
    "cd_uni_003": "Kostenloser Copilot mit Reasoning auf GPT-4-Niveau, Bildgenerierung und Microsoft-365-Integration — gratis bei jedem Microsoft-Konto.",
    "cd_uni_004": "KI-Suchmaschine, die jede Aussage mit Quelle belegt — perfekt, wenn du verifizierbare Quellen statt halluzinierter Antworten brauchst.",
    "cd_uni_005": "Lade eigene Notizen und PDFs hoch — Googles KI antwortet ausschliesslich aus deinen Quellen, mit Zitaten und Audio-Zusammenfassungen.",
    "cd_uni_006": "Tausende Open-Source-KI-Modelle direkt im Browser ausführen — Text, Bild, Sprache, Agenten — und eigene kostenlose Spaces hosten.",
    "cd_uni_007": "Kostenlose 1-Stunden-Kurse von Andrew Ng zu Prompting, RAG, Agenten und Fine-Tuning — gemeinsam mit führenden KI-Laboren.",
    "cd_uni_008": "Kostenloser Open-Source-Kurs zu den vier Kernkompetenzen der Arbeit mit KI — Delegation, Beschreibung, Urteilskraft und Sorgfalt.",
    "cd_uni_009": "Der kostenlose MOOC der Universität Helsinki — 30 Stunden zu KI-Grundlagen, Ethik und Grenzen, von einer Million Lernenden besucht.",
    "cd_uni_010": "Kostenloses Google-Curriculum zu Grundlagen generativer KI, Prompt-Design und verantwortungsvollem Einsatz — keine Vorerfahrung nötig.",
    "cd_uni_011": "Open-Source-Community-Leitfaden zum Prompten — Techniken, Beispiele und Forschungsarbeiten, alles kostenlos und ständig aktualisiert.",
    # Coding & Data (012-023)
    "cd_uni_012": "Harvards legendärer CS-Einstieg — kostenlose Videos, Aufgaben und ein kostenloses Zertifikat über edX-Audit. Immer noch der beste erste CS-Kurs online.",
    "cd_uni_013": "Tausende Stunden praktischer Coding-Lektionen und kostenlose Zertifikate — Webentwicklung, Datenanalyse und Machine Learning.",
    "cd_uni_014": "Kostenloses Full-Stack-Webentwicklungs-Curriculum, mit dem Autodidakten echte Jobs ergattern — community-getrieben und bewährt.",
    "cd_uni_015": "Interaktive browserbasierte Coding-Lektionen — Python, JS, SQL, HTML/CSS — mit solidem Gratis-Tarif für alle Grundlagen.",
    "cd_uni_016": "Kurze, praxisorientierte Data-Science- und ML-Mikrokurse — plus Tausende echter Datensätze und Wettbewerbe zum Üben.",
    "cd_uni_017": "Kostenlose Jupyter-Notebooks im Browser mit kostenloser GPU — perfekt für ML, Data Science und Forschungsprototypen ohne Setup.",
    "cd_uni_018": "Practical Deep Learning for Coders — ein kostenloser Top-down-Kurs, der Programmierer in sieben Wochen zu Deep-Learning-Praktikern macht.",
    "cd_uni_019": "Kostenlose erste Kapitel jedes Kurses — solider Einstieg in Python, R, SQL und Datenvisualisierung mit browserbasierten Übungen.",
    "cd_uni_020": "Das klarste kostenlose SQL-Tutorial online — analytisch ausgerichtet, mit echten Datensätzen und integriertem Browser-Editor.",
    "cd_uni_021": "Code in 50+ Sprachen direkt im Browser — kein Setup, kostenloses Hosting, sofortige Zusammenarbeit und KI-unterstütztes Coding.",
    "cd_uni_022": "Kostenlose Übungen in 70+ Sprachen mit Mentor-Feedback — Syntax und Idiome schärfen, über das hinaus, was Tutorials abdecken.",
    "cd_uni_023": "MITs Einführung in die Informatik mit Python — kostenlose Vorlesungen, Aufgaben und Prüfungen aus dem Campus-Kurs.",
    # Cybersecurity (024-035)
    "cd_uni_024": "Open-Source-Passwortmanager mit grosszügigem Gratis-Tarif — unbegrenzte Geräte, Passwörter und Ende-zu-Ende-Verschlüsselung.",
    "cd_uni_025": "Kostenloser Check, ob deine E-Mail oder dein Passwort in einem Datenleck aufgetaucht ist — vom Sicherheitsforscher Troy Hunt.",
    "cd_uni_026": "Kostenloser Ende-zu-Ende-verschlüsselter Messenger — Goldstandard für private Chats, Anrufe und Videos. Weltweit von Journalisten genutzt.",
    "cd_uni_027": "Kostenlose Open-Source-App für Zwei-Faktor-Authentifizierung — viel sicherer als SMS-Codes, schützt Konten auch bei Passwort-Lecks.",
    "cd_uni_028": "Kostenloser Anonymitäts-Browser, der den Datenverkehr über freiwillige Relays leitet — essenziell für Journalisten, Aktivisten und Hochrisiko-Nutzer.",
    "cd_uni_029": "Mozillas kostenloser Käuferratgeber zur Privatsphäre von Consumer-Tech — Smartphones, Smart Speaker, Mental-Health-Apps. Schnell zum Überfliegen vor dem Kauf.",
    "cd_uni_030": "Der kostenlose Leitfaden der Electronic Frontier Foundation zur digitalen Sicherheit — praktische Playbooks für Studierende, Aktivisten und Alltagsnutzer.",
    "cd_uni_031": "Gamifiziertes Cybersicherheits-Training — kostenlose Räume zu Networking, Linux und Web-Security; die einsteigerfreundlichste Hacking-Plattform.",
    "cd_uni_032": "Kostenlose Einsteigerkurse zu Cybersicherheits-Grundlagen, Ethical Hacking und CompTIA-Security+-Prüfungsvorbereitung.",
    "cd_uni_033": "Kostenlose Cybersicherheits-Hinweise der US-Behörde für Cybersicherheit — praktisch für Einzelpersonen und kleine Organisationen.",
    "cd_uni_034": "Open Worldwide Application Security Project — kostenlose Top-10-Listen, Cheatsheets und Frameworks, die jeder Webentwickler kennen sollte.",
    "cd_uni_035": "Stanfords Kurs zu Computer- und Netzwerksicherheit — kostenlose Vorlesungsfolien, Notizen und Leselisten aus einem Spitzenprogramm.",
    # Critical Thinking (036-047)
    "cd_uni_036": "Kostenloser Kurs der University of Washington zum Erkennen von Bullshit in Zahlen, Charts und Geschichten — alle Videos und Texte offen online.",
    "cd_uni_037": "Kostenloser, kompletter Einstieg in Statistik und Wahrscheinlichkeitsrechnung — die Kompetenz, jede Grafik in den Nachrichten zu hinterfragen.",
    "cd_uni_038": "Zeigt Schlagzeilen aus linken, mittigen und rechten Quellen nebeneinander — kalibriere deine Mediendiät und erkenne tägliche Verzerrungen.",
    "cd_uni_039": "Vergleicht, wie dieselbe Geschichte über das politische Spektrum hinweg behandelt wird — der Gratis-Tarif zeigt blinde Flecken und Bias.",
    "cd_uni_040": "Die ursprüngliche Faktencheck-Seite — kostenlose, transparente Urteile zu viralen Behauptungen, Mythen und politischen Gerüchten.",
    "cd_uni_041": "Tim Harfords kostenloser BBC-Podcast und Artikel, die die Zahlen hinter den Schlagzeilen aufdröseln — das lesbarste Training in statistischem Denken.",
    "cd_uni_042": "Richard Nisbetts kostenlose Auswahl der nützlichsten Konzepte aus Psychologie und Statistik für alltägliches Denken.",
    "cd_uni_043": "Kostenloses buchlanges Intro in Rationalität — kognitive Verzerrungen, probabilistisches Denken, wissenschaftliches Argumentieren und Entscheidungen.",
    "cd_uni_044": "Kostenloser interaktiver Leitfaden zu 24 verbreiteten logischen Fehlschlüssen — bookmarkwürdig, um schwache Argumente online und offline zu erkennen.",
    "cd_uni_045": "Kostenlose Enzyklopädie kognitiver Verzerrungen und Verhaltenswissenschaft — klare, gut illustrierte Erklärungen, wie wir falsch denken.",
    "cd_uni_046": "Kostenlose Kurse zur Medienkompetenz für Jugendliche und Erwachsene vom Poynter Institute — praktischer Faktencheck mit echten Beispielen.",
    "cd_uni_047": "Ben Goldacres kostenlose Artikel zerlegen schlechte Statistik in Medizin und Journalismus — das kanonische Gegengift zu zweifelhaften Schlagzeilen.",
    # Open Courseware (048-059)
    "cd_uni_048": "2.500+ MIT-Kurse kostenlos — Vorlesungsnotizen, Aufgaben, Prüfungen und oft komplette Vorlesungsvideos der weltweit führenden Ingenieurschule.",
    "cd_uni_049": "Die meisten Kurse von Stanford, Yale, Michigan u. v. m. kostenlos auditieren — Videos und Lektüre auf der kostenlosen Spur enthalten.",
    "cd_uni_050": "Kostenloser Zugang zu Universitätskursen von Harvard, MIT, Berkeley und Microsoft — auf den meisten Kursen mit Audit-Modus optional zertifizierbar.",
    "cd_uni_051": "Yales Open Courses sind kostenlos online — komplette Vorlesungen, Lehrpläne und Notizen einiger ihrer berühmtesten Professoren.",
    "cd_uni_052": "Kostenlose Übungsaufgaben und Kurzvideos zu Mathematik, Naturwissenschaften, Wirtschaft und mehr — von Grundschule bis Frühuni.",
    "cd_uni_053": "Stanfords offene Vorlesungen — kostenlose vollständige Kursvideos, einschliesslich der renommierten CS-Reihen.",
    "cd_uni_054": "Hochwertiger Bildungs-YouTube-Kanal — kostenlose Erklärvideos zu Geschichte, Philosophie und Naturwissenschaften, die im Studium echt helfen.",
    "cd_uni_055": "Kostenlose Vorlesungen, Konferenzen und Aufnahmen von Top-Universitäten und Denkern — kuratiertes Bildungsmedium ohne Werbung.",
    "cd_uni_056": "Indiens kostenlose nationale Lernplattform — Tausende Hochschulkurse von IIT- und IISc-Professoren, plus Programme der besten Schulen.",
    "cd_uni_057": "Kostenlose europäische MOOC-Plattform — Hunderte Universitätskurse zu Sprachen, Wissenschaft und Geisteswissenschaften aus EU-Hochschulen.",
    "cd_uni_058": "Wikis Schwesterprojekt für Lehrmaterialien — kostenlose offene Lehrbücher, Aufgabensammlungen und Kurspläne, die jeder bearbeiten kann.",
    "cd_uni_059": "Berkeleys kostenlose öffentliche Vorlesungen — komplette Kursaufnahmen aus einer der weltbesten öffentlichen Universitäten.",
    # Research (060-071)
    "cd_uni_060": "Standard-Suchmaschine für Wissenschaft — kostenlos, indexiert die meisten Paper, Bücher und Patente und vernetzt Zitate.",
    "cd_uni_061": "Kostenlose Suche nach Open-Access-Forschungspapern — über 250 Mio. Volltexte aus Tausenden Repositorien weltweit.",
    "cd_uni_062": "Kostenlose Open-Access-Suchmaschine — durchsucht 200 Mio. Forschungspaper über alle Disziplinen, ohne Paywalls.",
    "cd_uni_063": "Kostenloser Vorabdruck-Server für Mathematik, Physik, CS und Bio — wie Forscher monatelang vor offizieller Publikation lesen.",
    "cd_uni_064": "Kostenloser Vorabdruck-Server für Biologie- und Medizinforschung — der schnellste Weg, neue Wissenschaft direkt von den Autoren zu lesen.",
    "cd_uni_065": "Kostenloser Open-Source-Referenzmanager — sammle, organisiere, zitiere und teile Forschungsquellen in jedem grossen Stil.",
    "cd_uni_066": "Kostenloses, mit Zotero kompatibles Cloud-Service für Referenzmanagement und Wissensorganisation — leistungsstarker Gratis-Tarif.",
    "cd_uni_067": "Wissenschaftlerfreundlicher kostenloser LaTeX-Editor im Browser — kollaboratives Schreiben für Aufsätze, Abschlussarbeiten und Paper.",
    "cd_uni_068": "Kostenloses Repository universitärer Open-Access-Lehrbücher — peer-reviewed, frei verwendbar und im Studium oft direkt nutzbar.",
    "cd_uni_069": "OpenStax — kostenlose, peer-reviewed Lehrbücher von der Rice University, weltweit von Hochschulen genutzt.",
    "cd_uni_070": "Kostenloses Verzeichnis von Open-Access-Zeitschriften — über 20.000 geprüfte Journale ohne Paywall.",
    "cd_uni_071": "Kostenloser Bot, der dir beim Verstehen wissenschaftlicher Paper hilft — Zusammenfassungen, Definitionen und Querverweise innerhalb der Studie.",
    # Writing (072-083)
    "cd_uni_072": "Kostenloser Schreibassistent für Grammatik, Rechtschreibung und Klarheit — der Gratis-Tarif reicht für die meisten studentischen Texte.",
    "cd_uni_073": "Kostenlose Schreibanalyse — markiert komplexe Sätze, Adverbien und Passivkonstruktionen, damit dein Schreiben klar und kraftvoll wird.",
    "cd_uni_074": "Kostenloser Plagiats-Checker — vergleicht deinen Text mit Milliarden Webseiten und akademischen Datenbanken.",
    "cd_uni_075": "Kostenlose Vorlagen, Anleitungen und Kursmaterialien zum akademischen Schreiben von der Purdue University — ein Standardwerk.",
    "cd_uni_076": "Kostenlose Hemingway-App — markiert komplexe Sätze und Passivformulierungen, damit du klarer und prägnanter schreibst.",
    "cd_uni_077": "Bekannte TED-Sprecher zeigen kostenlos, wie man eine Idee überzeugend präsentiert — Storytelling, Spannungsaufbau und Bühnenpräsenz.",
    "cd_uni_078": "Kostenlose Plattform, um Vorträge in der eigenen Stadt zu suchen oder zu organisieren — Toastmasters und akademische Vortragsclubs.",
    "cd_uni_079": "Toastmasters International — kostenlose Probebesuche bei lokalen Clubs zum Üben von Reden in unterstützender Atmosphäre.",
    "cd_uni_080": "Kostenlose KI-Übersetzung in 30+ Sprachen mit hervorragender Qualität — der Gratis-Tarif reicht für die meisten studentischen Texte.",
    "cd_uni_081": "Kostenloses Online-Wörterbuch und Übersetzer — Beispielsätze, Aussprache und Hörverständnistraining in mehreren Sprachen.",
    "cd_uni_082": "Stanford-Kurs zum populärwissenschaftlichen Schreiben — kostenlose Vorlesungen und Übungsaufgaben für klares, lesbares Sachschreiben.",
    "cd_uni_083": "Kostenloser TED-Sprachstil-Leitfaden — wie man Ideen wert verbreitet, in einer 18-Minuten-Rede aufbaut und Bühnenangst überwindet.",
    # Productivity (084-095)
    "cd_uni_084": "Kostenloser persönlicher Notion-Plan — Notizen, Datenbanken, Aufgaben und Wikis in einer einzigen Workspace-App.",
    "cd_uni_085": "Lokale Markdown-Notizen mit Knowledge-Graph — kostenloser Obsidian-Tarif für persönliche Nutzung, ideal fürs Lernen.",
    "cd_uni_086": "Kostenloser Open-Source-Notizenbau mit verlinkten Notizen — Logseq für Privacy-bewusstes Zettelkasten-Studieren.",
    "cd_uni_087": "Kostenlose Aufgaben- und Projekt-App — sauberes Design, Wiederholungen, Labels, Filter und nahtlose Geräte-Synchronisation.",
    "cd_uni_088": "Kostenloser Pomodoro-Timer im Browser oder App — pflanzt einen virtuellen Baum, während du fokussiert bleibst.",
    "cd_uni_089": "Anki — kostenloses Open-Source-Flashcard-System mit Spaced Repetition, das von Medizin- bis Sprach-Studenten weltweit genutzt wird.",
    "cd_uni_090": "Kostenloser Kalender-Time-Blocker — visualisiere Wochenrhythmus, schütze Deep-Work-Zeit und plane realistische Zeitbudgets.",
    "cd_uni_091": "Kostenloser Browser-Tab-Manager — gruppiert verwandte Tabs zu Sessions und befreit dein Gehirn vom Tab-Chaos.",
    "cd_uni_092": "Kostenloses Open-Source-Werkzeug zum Blockieren ablenkender Sites — Cold Turkey Blocker schützt deine Aufmerksamkeit beim Studieren.",
    "cd_uni_093": "Kostenloses tägliches Habit-Tracking — der Gratis-Tarif ermöglicht das Verfolgen wichtiger Routinen und Studiengewohnheiten.",
    "cd_uni_094": "Kostenloser Cal-Newport-Hub mit Essays, Podcast-Folgen und Buchempfehlungen rund um Deep Work und Studium-Tiefe.",
    "cd_uni_095": "Kostenloser Pomofocus-Web-Timer — schlanker Pomodoro-Timer im Browser mit Statistik und keiner Anmeldung nötig.",
    # Mental Health (096-107)
    "cd_uni_096": "Kostenlose CBT-basierte App vom NHS — Stimmungstracking, Atemübungen und kognitive Werkzeuge für Stress und milde Angst.",
    "cd_uni_097": "Kostenlose Hörbar-Übungen aus Stanfords WellMD-Programm — Atem, Visualisierung und Erholung für gestresste Studierende.",
    "cd_uni_098": "Kostenloser Kompass für mentale Gesundheit — geprüfte Selbsthilferessourcen, Listen lokaler Hotlines und Krisenleitfäden.",
    "cd_uni_099": "Yale's Science of Well-Being — der meistbesuchte kostenlose Kurs der Welt zum Aufbau von Glücks-Gewohnheiten, basierend auf Forschung.",
    "cd_uni_100": "Kostenlose Achtsamkeitsmeditationen vom Greater Good Science Center der UC Berkeley — kurze Audios mit klarer wissenschaftlicher Grundlage.",
    "cd_uni_101": "Kostenlose Meditations- und Achtsamkeitskurse vom Insight Timer — die grösste kostenlose Bibliothek geführter Meditationen weltweit.",
    "cd_uni_102": "7 Cups — kostenlose anonyme emotionale Unterstützung durch geschulte Zuhörer, rund um die Uhr in mehreren Sprachen.",
    "cd_uni_103": "Kostenloser, evidenzbasierter Selbsthilfekurs vom NHS gegen Schlafstörungen — CBT-I-Techniken, die in Kliniken eingesetzt werden.",
    "cd_uni_104": "Kostenlose Stress- und Angstressourcen vom Anxiety and Depression Association — Erklärvideos, Selbsttests und Heimübungen.",
    "cd_uni_105": "Kostenlose KI-CBT-App für junge Menschen — anonym, evidenzbasiert und in 30 Sprachen rund um die Uhr verfügbar.",
    "cd_uni_106": "Kostenlose Krisenhotline für junge Menschen via SMS — anonym, vertraulich und 24/7 in mehreren Ländern erreichbar.",
    "cd_uni_107": "Kostenlose Schlaf- und Stressforschungs-Hub von Andrew Hubermans Stanford-Labor — Podcast-Folgen und Praktiken für bessere Erholung.",
    # Personal Finance (108-119)
    "cd_uni_108": "Kostenlose Khan-Academy-Lektionen zu persönlicher Finanz — Sparen, Steuern, Kredite und Zinseszinsen in klaren Modulen.",
    "cd_uni_109": "Kostenlose interaktive Werkzeuge der NerdWallet — Rechner für Kredite, Renten, Steuern und mehr ohne Anmeldung.",
    "cd_uni_110": "Kostenlose persönliche Budget-App — automatische Kategorisierung, Spar-Ziele und Übersicht über alle Konten an einem Ort.",
    "cd_uni_111": "Kostenlose europäische Finanzbildung von ECB Generation €uro — Wirtschaftsverständnis, Geldpolitik und reale Wirtschaftsspiele.",
    "cd_uni_112": "MITs kostenlose Open-Source-Vorlesungen zu Finanzen — Investitionsbewertung, Portfolio-Theorie und Risikomanagement.",
    "cd_uni_113": "Kostenlose ABC-Finanzbildung von der OECD — Curriculum für Schulen und Selbstlerner zu Geld, Investitionen und Vorsorge.",
    "cd_uni_114": "Kostenlose Bogleheads-Community — passive Investmentphilosophie und Anlageberatung von einer der grössten DIY-Finanz-Communities.",
    "cd_uni_115": "Kostenloser Verbraucherratgeber der US-CFPB — Geldgrundlagen, Studentenkredite und Schuldenbewältigung in mehreren Sprachen.",
    "cd_uni_116": "Kostenlose persönliche Finanzpodcasts der BBC — Money Box, Wake Up to Money und Politik-Geld-Erklärungen für UK und Europa.",
    "cd_uni_117": "Kostenlose Investopedia-Tutorials, Wörterbücher und Lehrgänge — die meistbesuchte Finanzbildungsseite der Welt.",
    "cd_uni_118": "Kostenlose Rechner und Leitfäden zu Hypotheken, Renten und Anlagen vom UK-Regierungsdienst MoneyHelper — vertrauenswürdig und werbefrei.",
    "cd_uni_119": "Kostenloses Yale-Open-Course Financial Markets von Robert Shiller — Risiko, Verhaltensökonomie und das Finanzsystem in 26 Vorlesungen.",
    # Career (120-131)
    "cd_uni_120": "Kostenloser 10-Wochen-Kurs des weltweit führenden Accelerators — über 1 Mio. Gründer ausgebildet, mit Bibliothek von YC-Essays und Talks.",
    "cd_uni_121": "Viele öffentliche Bibliotheken gewähren kostenlosen Zugang zu LinkedIn Learning — Tausende Kurse zu Karriere, Tools und Soft Skills.",
    "cd_uni_122": "Kostenloses KI-Resume- und LinkedIn-Profil-Feedback — von Ex-Recruitern entwickelt, bewertet deinen CV nach echten Auswahlkriterien.",
    "cd_uni_123": "Kostenlose herunterladbare CV-Vorlagen und Schreibratgeber — praktisch für Erstjobs, Praktika und Quereinsteiger.",
    "cd_uni_124": "Kostenloses Archiv mit Karriere-Artikeln — Interview-Vorbereitung, Gehaltsverhandlung, Umgang mit Bürokratie und Karrierewechsel.",
    "cd_uni_125": "Kostenlose Gehaltsdaten aus echten Angeboten — sieh, was Tech-, Finanz- und Beratungsrollen wirklich zahlen, bevor du verhandelst.",
    "cd_uni_126": "Kostenlose Bewertungen, Gehaltsspannen und Interviewfragen für Tausende Unternehmen — der Standard-Read vor jedem Bewerbungsgespräch.",
    "cd_uni_127": "Kostenlose Karriereberatung mit Fokus auf maximaler Wirkung deiner Arbeit — forschungsbasierte Ratgeber zu wirkungsvollen Karrierepfaden.",
    "cd_uni_128": "Kostenloser Stanford-Kurs CS183B mit Sam Altman und YC-Partnern — 20 kostenlose Vorlesungen zum Aufbau eines Startups von null.",
    "cd_uni_129": "Kostenlose Indie-Hackers-Community von gebootstrappten Gründern — Interviews, Podcasts und Forenthemen rund um profitable Side-Businesses.",
    "cd_uni_130": "Kostenlose Zertifikate in Marketing, Vertrieb, Content und SEO — von Arbeitgebern anerkannt, online in wenigen Stunden absolvierbar.",
    "cd_uni_131": "Kostenlose Google-Karriere-Zertifikate in IT-Support, Datenanalyse, UX und Projektmanagement — von 150+ Arbeitgebern anerkannt.",
    # Civic, Media & Climate (132-143)
    "cd_uni_132": "Kostenlose, frei lizenzierte Datenvisualisierungen zu den grössten Themen der Welt — Klima, Armut und Gesundheit — von Oxford-Forschern.",
    "cd_uni_133": "Kostenlose, von MIT kuratierte Erklärungen zum Klimawandel — Wissenschaft, Lösungen, Politik — verständlich und sauber belegt.",
    "cd_uni_134": "Kostenlose, gerankte Liste der wirksamsten Klimalösungen — durchsuchbare Datenbank mit tiefen technischen Analysen für jede.",
    "cd_uni_135": "Kostenloser täglicher Klima-Journalismus von Yale — präzise, zugängliche Berichterstattung zu Klimawissenschaft, Folgen und Lösungen.",
    "cd_uni_136": "Kostenlose, vollständige US-Civics-Einführung — Verfassung, Gewalten, Wahlen — auch für Nicht-US-Studierende, die Demokratiegrundlagen lernen wollen.",
    "cd_uni_137": "Kostenlose Spiele und Lektionen zur demokratischen Teilhabe — von Justice O'Connor entwickelt, in über 50.000 Klassenzimmern eingesetzt.",
    "cd_uni_138": "Kostenloser Ethik-Ressourcenhub der Santa Clara University — Frameworks für das Denken über Tech-, Wirtschafts-, KI- und Bioethik.",
    "cd_uni_139": "Kostenlose Berichte, Primer und Policy-Briefs vom Stanford Human-Centered AI Institute — die führende Quelle zu KI und Gesellschaft.",
    "cd_uni_140": "Kostenloses Open-Source-Investigations-Playbook — Videos verifizieren, Fotos geolokalisieren und virale Behauptungen wie die Profis prüfen.",
    "cd_uni_141": "Kostenloses Archiv evidenzbasierter Berichterstattung über Lösungen — Gegenmittel zum Doom-Scrolling, Fokus auf Antworten auf soziale Probleme.",
    "cd_uni_142": "Kostenlose Leitfäden der Electronic Frontier Foundation zu Meinungsfreiheit, Überwachung und digitalen Rechten — die führende Bürgerrechte-NGO.",
    "cd_uni_143": "Kostenlose Kurse zu den UN-Nachhaltigkeitszielen — Klima, Gleichheit, Armut und Governance, unterrichtet von UN-Agenturen und Partnern.",
}

assert len(DE_CARDS) == 144, f"Expected 144 DE card translations, got {len(DE_CARDS)}"

# ---- Build EN insertion (after cd_287, before EN block close) ---------------
EN_CD_LINES = "\n".join(
    f"    'cd_uni_{i:03d}': {json.dumps(KEYS[f'cd_uni_{i:03d}'], ensure_ascii=False)},"
    for i in range(144)
)
EN_INSERT = f"    /* University card descriptions (144) */\n{EN_CD_LINES}\n"

# ---- Build DE chrome insertion ----------------------------------------------
def de_line(key, val):
    return f"    {json.dumps(key)}: {json.dumps(val, ensure_ascii=False)},"

# Order chrome keys: sub.uni.*, then uni.stat/grade/picker/filter/tab/chip/sec
chrome_order = [
    "sub.uni.badge", "sub.uni.title", "sub.uni.desc", "sub.uni.back",
    "uni.stat.tools", "uni.stat.topics", "uni.stat.levels.val", "uni.stat.levels.lbl", "uni.stat.free",
    "uni.grade.undergrad", "uni.grade.grad", "uni.grade.phd", "uni.grade.self",
    "uni.grade.all", "uni.grade.adult", "uni.grade.switcher",
    "uni.picker.label", "uni.picker.heading", "uni.filter.label", "uni.filter.all",
] + [f"uni.tab.{k}" for k in ["ai","coding","security","critical","courseware","research","writing","productivity","mental","finance","career","civic"]] \
  + [f"uni.chip.{k}" for k in ["ai","coding","security","critical","courseware","research","writing","productivity","mental","finance","career","civic"]]

for k in ["ai","coding","security","critical","courseware","research","writing","productivity","mental","finance","career","civic"]:
    for suf in ["label", "h2", "desc"]:
        chrome_order.append(f"uni.sec.{k}.{suf}")

DE_CHROME_LINES = "\n".join(de_line(k, DE_CHROME[k]) for k in chrome_order)
DE_CD_LINES = "\n".join(
    de_line(f"cd_uni_{i:03d}", DE_CARDS[f"cd_uni_{i:03d}"])
    for i in range(144)
)
DE_INSERT = (
    "    /* University: chrome (sub.uni / stats / grades / picker / filter / tabs / chips / sections) */\n"
    f"{DE_CHROME_LINES}\n"
    "    /* University card descriptions (144) */\n"
    f"{DE_CD_LINES}\n"
)

# ---- Splice into i18n.js ----------------------------------------------------
src = I18N.read_text(encoding="utf-8")

# 1. Insert EN cd_uni keys right after the cd_287 EN line (line ~584)
en_anchor = "    'cd_287': 'Free for educators — a daily 20-minute reading habit grows the youngest learners.',\n"
assert en_anchor in src, "EN anchor (cd_287) not found"
src = src.replace(en_anchor, en_anchor + EN_INSERT, 1)

# 2. Remove old DE sub.uni.* lines (badge/title/desc/back combined on lines 786-788)
de_old = (
    "    'sub.uni.badge': 'Hochschulbildung', 'sub.uni.title': 'Ressourcen für Studierende',\n"
    "    'sub.uni.desc': '60 kuratierte kostenlose Tools in 6 Themen. Wähle unten ein Thema und sieh die Top 10.',\n"
    "    'sub.uni.back': 'Zurück zu Ressourcen',\n"
)
if de_old in src:
    src = src.replace(de_old, "", 1)

# 3. Insert DE chrome + cd_uni keys after the DE cd_287 line
de_anchor = "    'cd_287': 'Kostenlos für Pädagogen — eine tägliche 20-Minuten-Lese-Gewohnheit fördert die jüngsten Lernenden.',\n"
assert de_anchor in src, "DE anchor (cd_287) not found"
src = src.replace(de_anchor, de_anchor + DE_INSERT, 1)

I18N.write_text(src, encoding="utf-8")
print(f"Wrote {I18N}: +{144} EN keys, +{len(chrome_order)} DE chrome keys, +{144} DE card keys")
