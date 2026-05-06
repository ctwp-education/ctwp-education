#!/usr/bin/env python3
"""Add missing ES keys to the existing es: block in i18n.js."""
from pathlib import Path
import re

ES_MORE = {
    # Resources hub on index
    "resources.label": "Recursos Educativos Gratuitos",
    "resources.title": "Recursos Educativos",
    "resources.subtitle": "Recursos gratuitos curados para aprender y enseñar mejor — explora por audiencia.",
    "resources.k12.title": "Estudiantes (K–12)",
    "resources.k12.desc": "Cursos gratuitos, herramientas interactivas de programación, ciencias, idiomas, salud mental y mucho más para edades de 3 a 18.",
    "resources.k12.link": "Descubrir recursos escolares",
    "resources.teacher.title": "Docentes",
    "resources.teacher.desc": "Planes de lección, herramientas de IA para enseñar, gestión del aula, evaluación y desarrollo profesional.",
    "resources.teacher.link": "Descubrir recursos para docentes",
    "resources.uni.title": "Estudiantes Universitarios",
    "resources.uni.desc": "Herramientas de investigación académica, libros de texto gratuitos, productividad y carrera para estudiantes y aprendices permanentes.",
    "resources.uni.link": "Descubrir recursos universitarios",
    # Sponsors
    "sponsors.label": "Nuestros Socios y Patrocinadores",
    "sponsor.main_partner": "Socio Principal",
    "sponsor.main_sponsor": "Patrocinador Principal",
    "sponsor.partner": "Socio",
    "sponsor.placeholder": "Tu logo podría estar aquí",
    # Support tabs and cards
    "tab.individuals": "Para Individuos",
    "tab.companies": "Para Empresas",
    "support.member.title": "Hazte Miembro",
    "support.member.desc": "Únete a la comunidad de Bongai Shamwari. Tu cuota anual apoya nuestros programas y construye comunidad.",
    "support.tech.title": "Donaciones de Tecnología",
    "support.tech.desc": "Dona portátiles, tabletas u otros dispositivos para apoyar nuestros laboratorios informáticos en África.",
    "support.spread.title": "Difunde la Voz",
    "support.spread.desc": "Comparte nuestra misión en redes sociales y en tu red. Cada nueva mirada amplía nuestro impacto.",
    "support.corp.title": "Asociación Corporativa",
    "support.corp.desc": "Conviértete en patrocinador principal como Trelleborg. Financia infraestructura digital y construyamos un programa juntos.",
    # CTA
    "cta.title": "Cada Aporte Cuenta",
    "cta.desc": "El 100% de las donaciones va directamente a programas educativos. Detalles bancarios y opciones de patrocinio disponibles bajo petición.",
    "cta.donate": "Donar Ahora",
    "cta.sponsor": "Convertirse en Patrocinador",
    # Contact
    "contact.desc": "Seas inversor, docente, organización potencialmente socia o simplemente curioso — escríbenos.",
    "contact.form.title": "Envíanos un Mensaje",
    "contact.location": "Zúrich, Suiza (Sede)",
    # Form fields
    "form.name": "Nombre",
    "form.name.ph": "Nombre completo",
    "form.email": "Correo Electrónico",
    "form.email.ph": "tu@correo.com",
    "form.interest": "Me interesa como...",
    "form.select": "Selecciona una opción",
    "form.student_role": "Estudiante",
    "form.teacher_role": "Docente",
    "form.partner_role": "Organización Socia",
    "form.donor": "Donante",
    "form.corp_sponsor": "Patrocinador Corporativo",
    "form.volunteer": "Voluntario/a",
    "form.other": "Otro",
    "form.message": "Mensaje",
    "form.message.ph": "¿Cómo te gustaría involucrarte?",
    "form.submit": "Enviar Mensaje",
    # Gallery follow
    "gallery.follow": "Sigue nuestro recorrido",
    # Footer
    "footer.about": "Acerca de",
    "footer.work": "Nuestro Trabajo",
    "footer.resources": "Recursos",
    "footer.support": "Apóyanos",
    "footer.contact": "Contacto",
    "footer.connect": "Conectar",
    "footer.nav": "Navegación",
    "footer.desc": "Empoderar a cada niño y persona del planeta mediante el acceso a educación gratuita usando tecnología.",
    "footer.copyright": "© 2026 CTWP Educational Empowerment. Todos los derechos reservados.",
    # Students subpage extras
    "students.stat.freestart": "Inicio Gratuito",
    "sub.students.back": "Volver a Recursos",
    "sub.students.badge": "Habilidades K–12 para el Futuro",
    "sub.students.title": "Recursos para Estudiantes (K–12)",
    "sub.students.desc": "300 herramientas gratuitas curadas para 14 habilidades para la vida — desde alfabetización y matemáticas hasta salud mental, finanzas y deporte.",
    # University extras
    "uni.stat.topics": "Temas del Futuro",
    "uni.chip.ai": "Fluidez en IA",
    "uni.chip.coding": "Programación y Datos",
    "uni.chip.security": "Ciberseguridad",
    "uni.chip.critical": "Pensamiento Crítico",
    "uni.chip.research": "Investigación",
    "uni.chip.writing": "Escritura y Oratoria",
    "uni.chip.productivity": "Productividad",
    "uni.chip.courseware": "Cursos Abiertos",
    "uni.chip.career": "Carrera",
    "uni.chip.finance": "Finanzas",
    "uni.chip.mental": "Salud Mental",
    "uni.chip.civic": "Democracia y Clima",
}

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
src = src_path.read_text(encoding="utf-8")

# Find the closing of es block: "  }\n};" at the very end
# Find: last occurrence of structural ES key before "  }\n};"
# Simpler: look for "  es: {" then find its matching "  }"
es_start = src.index("\n  es: {")
end_marker = "\n  }\n};"
es_end = src.index(end_marker, es_start)

# Build new keys block
new_lines = []
for k, v in ES_MORE.items():
    v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v_esc}",')
new_block = "\n".join(new_lines) + "\n"

# Insert before the closing "  }\n};"
new_src = src[:es_end] + "\n" + new_block.rstrip() + src[es_end:]

src_path.write_text(new_src, encoding="utf-8")
print(f"Added {len(ES_MORE)} more ES keys")
