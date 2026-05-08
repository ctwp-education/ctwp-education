#!/usr/bin/env python3
"""Insert missing lab hero + partner keys into all 5 language blocks of i18n.js."""
from pathlib import Path

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
src = src_path.read_text(encoding="utf-8")

# ── Keys to insert per language ────────────────────────────────────────────────
INSERTS = {
    # EN — single-quote style, inline after cta2 line
    "'lab.hero.cta1': 'Support This Project', 'lab.hero.cta2': 'See What We Built',": (
        "    'lab.hero.badge': 'Mutare, Zimbabwe · Bongai Shamwari',\n"
        "    'lab.hero.title': 'Our <em>Computer Lab</em> in Zimbabwe',\n"
        "    'lab.partner.tag': 'Joint Initiative',\n"
        "    'lab.partner.h4': 'Stronger together — from idea to first lesson.',\n"
        "    'lab.partner.p': 'This computer lab is the result of two organisations sharing one conviction: that every child, regardless of where they are born, deserves access to quality digital education. CTWP Educational Empowerment and Bongai Shamwari e.V. pooled their expertise, networks, and resources to make it happen — from fundraising and procurement to the very first lesson.',\n"
    ),
    # DE — single-quote style
    "'lab.hero.cta1': 'Projekt unterstützen', 'lab.hero.cta2': 'Was wir gebaut haben',": (
        "    'lab.hero.badge': 'Mutare, Simbabwe · Bongai Shamwari',\n"
        "    'lab.hero.title': 'Unser <em>Computer Lab</em> in Simbabwe',\n"
        "    'lab.partner.tag': 'Gemeinsame Initiative',\n"
        "    'lab.partner.h4': 'Gemeinsam stärker — von der Idee zur ersten Stunde.',\n"
        "    'lab.partner.p': 'Dieses Computerlabor ist das Ergebnis zweier Organisationen, die eine gemeinsame Überzeugung teilen: dass jedes Kind, unabhängig davon, wo es geboren wurde, Zugang zu qualitativ hochwertiger digitaler Bildung verdient. CTWP Educational Empowerment und Bongai Shamwari e.V. haben ihr Fachwissen, ihre Netzwerke und Ressourcen zusammengelegt, um dies zu ermöglichen — von der Mittelbeschaffung bis zur allerersten Unterrichtsstunde.',\n"
    ),
    # ES — double-quote style
    '"lab.hero.cta2": "Ver lo que Construimos",': (
        '    "lab.hero.badge": "Mutare, Zimbabue · Bongai Shamwari",\n'
        '    "lab.hero.title": "Nuestro <em>Laboratorio Informático</em> en Zimbabue",\n'
        '    "lab.partner.tag": "Iniciativa Conjunta",\n'
        '    "lab.partner.h4": "Más fuertes juntos — de la idea a la primera lección.",\n'
        '    "lab.partner.p": "Este laboratorio informático es el resultado de dos organizaciones que comparten una convicción: que cada niño, independientemente del lugar en el que haya nacido, merece acceso a una educación digital de calidad. CTWP Educational Empowerment y Bongai Shamwari e.V. unieron su experiencia, redes y recursos para lograrlo — desde la recaudación de fondos y la adquisición hasta la primera lección.",\n'
    ),
    # PT — double-quote style
    '"lab.hero.cta2": "Veja o que Construímos",': (
        '    "lab.hero.badge": "Mutare, Zimbábue · Bongai Shamwari",\n'
        '    "lab.hero.title": "Nosso <em>Laboratório de Informática</em> no Zimbábue",\n'
        '    "lab.partner.tag": "Iniciativa Conjunta",\n'
        '    "lab.partner.h4": "Mais fortes juntos — da ideia à primeira aula.",\n'
        '    "lab.partner.p": "Este laboratório de informática é o resultado de duas organizações que compartilham uma convicção: que toda criança, independentemente de onde nasceu, merece acesso a uma educação digital de qualidade. CTWP Educational Empowerment e Bongai Shamwari e.V. uniram sua experiência, redes e recursos para tornar isso possível — desde a arrecadação de fundos e aquisição até a primeira aula.",\n'
    ),
    # FR — double-quote style
    '"lab.hero.cta2": "Voir ce que Nous Avons Construit",': (
        '    "lab.hero.badge": "Mutare, Zimbabwe · Bongai Shamwari",\n'
        '    "lab.hero.title": "Notre <em>Laboratoire Informatique</em> au Zimbabwe",\n'
        '    "lab.partner.tag": "Initiative Conjointe",\n'
        '    "lab.partner.h4": "Plus forts ensemble — de l\'idée à la première leçon.",\n'
        '    "lab.partner.p": "Ce laboratoire informatique est le fruit de deux organisations partageant une conviction commune : que chaque enfant, quel que soit son lieu de naissance, mérite d\'avoir accès à une éducation numérique de qualité. CTWP Educational Empowerment et Bongai Shamwari e.V. ont mis en commun leur expertise, leurs réseaux et leurs ressources pour y parvenir — du financement et des achats jusqu\'à la toute première leçon.",\n'
    ),
}

inserted = 0
for anchor, block in INSERTS.items():
    if anchor not in src:
        print(f"WARNING: anchor not found: {anchor[:60]}")
        continue
    # Insert AFTER the anchor line (find end of that line)
    pos = src.index(anchor) + len(anchor)
    # Insert newline + block after the anchor
    src = src[:pos] + "\n" + block + src[pos:]
    inserted += 1
    print(f"Inserted after: {anchor[:60]}")

assert inserted == 5, f"Only inserted {inserted}/5 blocks"
src_path.write_text(src, encoding="utf-8")
print(f"\nDone — inserted {inserted} language blocks")
