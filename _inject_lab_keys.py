#!/usr/bin/env python3
"""Insert missing lab.* open-point keys into all 4 language blocks of i18n.js."""
from pathlib import Path

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
lines = src_path.read_text(encoding="utf-8").splitlines(keepends=True)

EN_ANCHOR = "    'lab.cta.btn1': 'Donate Now', 'lab.cta.btn2': 'Bongai Shamwari Website', 'lab.cta.btn3': '← Back to CTWP',"
DE_ANCHOR = "    'lab.cta.btn1': 'Jetzt spenden', 'lab.cta.btn2': 'Bongai Shamwari Website', 'lab.cta.btn3': '← Zurück zu CTWP',"
ES_ANCHOR = '    "lab.cta.btn3": "← Volver a CTWP",'
PT_ANCHOR = '    "lab.cta.btn3": "← Voltar para o CTWP",'

EN_INSERT = (
    "    'lab.done': 'Done', 'lab.needhelp': 'Still needed — can you help?',\n"
    "    'lab.op1.title': 'ICT Teacher Salary', 'lab.op1.desc': 'We need ongoing sponsors to fund the full-time ICT educator each year.',\n"
    "    'lab.op2.title': 'Internet Costs', 'lab.op2.desc': 'The Starlink subscription must be funded monthly to keep the lab connected to the world.',\n"
    "    'lab.op3.title': 'Printer & Projector', 'lab.op3.desc': 'A printer, projector, and classroom display are still missing from the lab.',\n"
    "    'lab.op4.title': 'Remaining Supplies', 'lab.op4.desc': 'Mouse pads, USB sticks, dust covers, shelves, and ICT schoolbooks are outstanding.',\n"
    "    'lab.op.sponsor': 'Sponsor now', 'lab.op.donate': 'Donate',\n"
)

DE_INSERT = (
    "    'lab.done': 'Erledigt', 'lab.needhelp': 'Noch ausstehend — können Sie helfen?',\n"
    "    'lab.op1.title': 'Gehalt des ICT-Lehrers', 'lab.op1.desc': 'Wir suchen laufende Sponsoren zur Finanzierung des hauptamtlichen ICT-Lehrers.',\n"
    "    'lab.op2.title': 'Internetkosten', 'lab.op2.desc': 'Das Starlink-Abonnement muss monatlich finanziert werden, damit das Lab mit der Welt verbunden bleibt.',\n"
    "    'lab.op3.title': 'Drucker & Projektor', 'lab.op3.desc': 'Drucker, Projektor und ein Klassendisplay fehlen noch im Lab.',\n"
    "    'lab.op4.title': 'Restliche Ausstattung', 'lab.op4.desc': 'Mauspads, USB-Sticks, Staubschutzhüllen, Regale und IT-Schulbücher stehen noch aus.',\n"
    "    'lab.op.sponsor': 'Jetzt sponsern', 'lab.op.donate': 'Spenden',\n"
)

ES_INSERT = (
    '    "lab.done": "Hecho",\n'
    '    "lab.needhelp": "Aún pendiente — ¿puedes ayudar?",\n'
    '    "lab.op1.title": "Salario del Profesor de TIC",\n'
    '    "lab.op1.desc": "Necesitamos patrocinadores continuos para financiar al educador de TIC a tiempo completo cada año.",\n'
    '    "lab.op2.title": "Costos de Internet",\n'
    '    "lab.op2.desc": "La suscripción de Starlink debe financiarse mensualmente para mantener el laboratorio conectado al mundo.",\n'
    '    "lab.op3.title": "Impresora y Proyector",\n'
    '    "lab.op3.desc": "Una impresora, proyector y pantalla para el aula todavía faltan en el laboratorio.",\n'
    '    "lab.op4.title": "Suministros Restantes",\n'
    '    "lab.op4.desc": "Alfombrillas, memorias USB, fundas antipolvo, estantes y libros de texto de TIC aún faltan.",\n'
    '    "lab.op.sponsor": "Patrocinar ahora",\n'
    '    "lab.op.donate": "Donar",\n'
)

PT_INSERT = (
    '    "lab.done": "Concluído",\n'
    '    "lab.needhelp": "Ainda necessário — você pode ajudar?",\n'
    '    "lab.op1.title": "Salário do Professor de TIC",\n'
    '    "lab.op1.desc": "Precisamos de patrocinadores contínuos para financiar o educador de TIC em tempo integral a cada ano.",\n'
    '    "lab.op2.title": "Custos de Internet",\n'
    '    "lab.op2.desc": "A assinatura do Starlink precisa ser financiada mensalmente para manter o laboratório conectado ao mundo.",\n'
    '    "lab.op3.title": "Impressora e Projetor",\n'
    '    "lab.op3.desc": "Uma impressora, projetor e tela para a sala de aula ainda estão faltando no laboratório.",\n'
    '    "lab.op4.title": "Suprimentos Restantes",\n'
    '    "lab.op4.desc": "Mouse pads, pen drives, capas antipoeira, prateleiras e livros didáticos de TIC ainda estão pendentes.",\n'
    '    "lab.op.sponsor": "Patrocinar agora",\n'
    '    "lab.op.donate": "Doar",\n'
)

inserts = {
    EN_ANCHOR.rstrip(): EN_INSERT,
    DE_ANCHOR.rstrip(): DE_INSERT,
    ES_ANCHOR.rstrip(): ES_INSERT,
    PT_ANCHOR.rstrip(): PT_INSERT,
}

new_lines = []
inserted = set()
for line in lines:
    stripped = line.rstrip("\n")
    new_lines.append(line)
    if stripped in inserts and stripped not in inserted:
        new_lines.append(inserts[stripped])
        inserted.add(stripped)

assert len(inserted) == 4, f"Only inserted into {len(inserted)} blocks: {inserted}"
src_path.write_text("".join(new_lines), encoding="utf-8")
print(f"Done — inserted keys into {len(inserted)} language blocks")
