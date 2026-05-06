#!/usr/bin/env python3
"""Translate all 788 card descriptions to Spanish and inject into the es: block of i18n.js."""
from pathlib import Path
import json
import re

# Sport (12)
ES_SPORT = {
    "cd_s01": "Videos de movimiento y mindfulness favoritos del aula que sacan a los niños de sus asientos — bailes, yoga y pausas activas en clips de 3–5 min.",
    "cd_s02": "Aventuras de yoga narradas para niños — posturas integradas en cuentos imaginativos sobre dragones, superhéroes y mundos mágicos.",
    "cd_s03": "Cientos de tutoriales de juegos de educación física e ideas de actividad física para la escuela — fáciles de hacer sin material y adaptables a cualquier grupo.",
    "cd_s04": "Enorme biblioteca de planes de educación física, calentamientos y actividades de fitness organizados por edad, habilidad y material — un clásico para docentes de EF.",
    "cd_s05": "Artículos amigables para niños sobre ciencia del ejercicio, nutrición, sueño y seguridad en el deporte — escritos por médicos para construir hábitos saludables de por vida.",
    "cd_s06": "Rutinas de entrenamiento en video diseñadas específicamente para niños — circuitos de fuerza, flexibilidad y cardio que se adaptan al tiempo y espacio disponibles.",
    "cd_s07": "Kits, fichas de actividades y guías de programa para integrar movimiento diario en la vida escolar — 60 minutos de actividad al día, llevados a la práctica.",
    "cd_s08": "Más de 600 videos completos y gratuitos de entrenamiento en cardio, fuerza, HIIT y estiramientos — filtrables por duración, dificultad y material necesario.",
    "cd_s09": "El plan de carrera para principiantes más popular del mundo — 9 semanas para correr 5 km sin parar, con app gratuita y guías de audio de entrenadores reconocidos.",
    "cd_s10": "Artículos de entrenamiento por deporte escritos con entrenadores profesionales — velocidad, agilidad, fuerza y ciencia de la recuperación para jóvenes atletas serios.",
    "cd_s11": "Biblioteca completa de entrenamientos guiados por entrenadores — sesiones de peso corporal, fuerza y yoga de 15 a 60 minutos, ahora todas gratis tras la decisión de Nike.",
    "cd_s12": "Cursos universitarios gratuitos sobre la ciencia del deporte, la actividad física y el rendimiento humano — ideales para estudiantes interesados en carreras deportivas.",
}

# University (144)
ES_UNI = {
    "cd_uni_000": "El asistente insignia de Anthropic — un nivel gratuito generoso cubre escritura, código e investigación con un razonamiento sólido.",
    "cd_uni_001": "ChatGPT de OpenAI — el nivel gratuito incluye GPT-4o mini, modo voz, comprensión de imágenes y análisis básico de datos.",
    "cd_uni_002": "El asistente multimodal de Google con integración profunda en Docs, Drive y Gmail — buen nivel gratuito con soporte para imágenes y código.",
    "cd_uni_003": "Copilot gratuito con razonamiento al nivel de GPT-4, generación de imágenes e integración con Microsoft 365 — incluido gratis con cualquier cuenta de Microsoft.",
    "cd_uni_004": "Buscador con IA que cita cada afirmación — perfecto cuando necesitas fuentes verificables en lugar de respuestas alucinadas.",
    "cd_uni_005": "Sube tus apuntes y PDFs — la IA de Google responde estrictamente desde tus fuentes, con citas y resúmenes en audio.",
    "cd_uni_006": "Ejecuta miles de modelos de IA de código abierto en tu navegador — texto, visión, voz, agentes — y aloja tus propios Spaces gratis.",
    "cd_uni_007": "Cursos gratuitos de 1 hora de Andrew Ng sobre prompts, RAG, agentes y fine-tuning — impartidos con los principales laboratorios de IA.",
    "cd_uni_008": "Curso gratuito de código abierto que enseña las cuatro competencias clave para trabajar con IA — delegación, descripción, discernimiento y diligencia.",
    "cd_uni_009": "MOOC gratuito de la Universidad de Helsinki — 30 horas sobre fundamentos de IA, ética y límites, ya cursado por un millón de estudiantes.",
    "cd_uni_010": "Currículo gratuito de Google sobre IA generativa, diseño de prompts y uso responsable — sin experiencia previa requerida.",
    "cd_uni_011": "Guía comunitaria de código abierto sobre prompts — técnicas, ejemplos y artículos científicos, todo gratis y actualizado con frecuencia.",
    "cd_uni_012": "La legendaria introducción a la informática de Harvard — videos, ejercicios y certificado gratuito vía edX. Sigue siendo el mejor primer curso de CS online.",
    "cd_uni_013": "Miles de horas de programación práctica y certificaciones gratuitas — desarrollo web, análisis de datos y machine learning.",
    "cd_uni_014": "Currículo gratuito y completo de desarrollo web full-stack usado por autodidactas que consiguen empleo real — comunitario y probado en la práctica.",
    "cd_uni_015": "Lecciones interactivas de programación en el navegador — Python, JS, SQL, HTML/CSS — con un sólido nivel gratuito que cubre los fundamentos.",
    "cd_uni_016": "Microcursos prácticos cortos de ciencia de datos y ML — más miles de datasets reales y competencias para practicar.",
    "cd_uni_017": "Cuadernos Jupyter gratuitos en el navegador con GPU gratis — perfecto para ML, ciencia de datos y prototipado de investigación sin instalación.",
    "cd_uni_018": "Practical Deep Learning for Coders — un curso gratuito top-down que convierte programadores en practicantes de deep learning en siete semanas.",
    "cd_uni_019": "Primeros capítulos gratis de cada curso — sólida introducción a Python, R, SQL y visualización de datos con ejercicios en el navegador.",
    "cd_uni_020": "El tutorial gratuito de SQL más claro de la web — orientado a analítica, con datasets reales y un editor integrado en el navegador.",
    "cd_uni_021": "Programa en más de 50 lenguajes directamente en tu navegador — sin configuración, hosting gratis, colaboración instantánea y programación asistida por IA.",
    "cd_uni_022": "Ejercicios prácticos gratuitos en más de 70 lenguajes con feedback de mentores — afina sintaxis y modismos más allá de los tutoriales.",
    "cd_uni_023": "Introducción del MIT a la informática usando Python — clases, ejercicios y exámenes gratuitos del curso presencial.",
    "cd_uni_024": "Gestor de contraseñas de código abierto con un nivel gratuito generoso — dispositivos y contraseñas ilimitados con cifrado de extremo a extremo.",
    "cd_uni_025": "Comprueba gratis si tu correo o contraseña han sido expuestos en una filtración — del investigador de seguridad Troy Hunt.",
    "cd_uni_026": "Mensajería gratuita con cifrado de extremo a extremo — el estándar de oro para chats, voz y video privados. Usado por periodistas en todo el mundo.",
    "cd_uni_027": "App gratuita de código abierto para autenticación de dos factores — mucho más segura que los códigos por SMS y protege tus cuentas aunque se filtren las contraseñas.",
    "cd_uni_028": "Navegador gratuito de anonimato que enruta el tráfico a través de relés voluntarios — esencial para periodistas, activistas y usuarios de alto riesgo.",
    "cd_uni_029": "Guía de compras gratuita de Mozilla que califica la privacidad de la tecnología de consumo — móviles, altavoces inteligentes, apps de salud mental. Fácil de revisar antes de comprar.",
    "cd_uni_030": "Guía gratuita de seguridad digital de la Electronic Frontier Foundation — manuales prácticos para estudiantes, activistas y usuarios cotidianos.",
    "cd_uni_031": "Entrenamiento gamificado de ciberseguridad — salas gratuitas sobre redes, Linux y seguridad web; la plataforma de hacking más amigable para principiantes.",
    "cd_uni_032": "Cursos introductorios gratuitos sobre fundamentos de ciberseguridad, hacking ético y preparación para el examen CompTIA Security+.",
    "cd_uni_033": "Orientación gratuita de ciberseguridad de la Cybersecurity & Infrastructure Security Agency de EE.UU. — práctica para individuos y pequeñas organizaciones.",
    "cd_uni_034": "Open Worldwide Application Security Project — listas top-10 gratuitas, fichas y frameworks que todo desarrollador web debería conocer.",
    "cd_uni_035": "Curso de seguridad informática y de redes de Stanford — diapositivas, notas y bibliografía gratuitas de un programa de referencia.",
    "cd_uni_036": "Curso gratuito de la Universidad de Washington para detectar tonterías en números, gráficos e historias — cada video y lectura abiertos online.",
    "cd_uni_037": "Introducción gratuita y completa a la estadística y la probabilidad — la alfabetización que necesitas para cuestionar cualquier gráfico de las noticias.",
    "cd_uni_038": "Muestra titulares de noticias de izquierda, centro y derecha en paralelo — calibra tu dieta mediática y detecta sesgos a diario.",
    "cd_uni_039": "Compara cómo la misma historia se cubre en todo el espectro político — el nivel gratuito muestra puntos ciegos y sesgos.",
    "cd_uni_040": "El sitio original de fact-checking — veredictos gratuitos y transparentes sobre afirmaciones virales, leyendas urbanas y rumores políticos.",
    "cd_uni_041": "Podcast y artículos gratuitos de Tim Harford en la BBC desentrañando los números detrás de los titulares — la formación más amena en pensamiento estadístico.",
    "cd_uni_042": "Auditoría gratuita de Richard Nisbett, premio Nobel, sobre los conceptos más útiles de psicología y estadística para el razonamiento cotidiano.",
    "cd_uni_043": "Introducción gratuita en formato libro a la racionalidad — sesgos cognitivos, pensamiento probabilístico, razonamiento científico y toma de decisiones.",
    "cd_uni_044": "Guía interactiva gratuita sobre 24 falacias lógicas comunes — un favorito para detectar malos argumentos online y offline.",
    "cd_uni_045": "Enciclopedia gratuita de sesgos cognitivos y ciencia del comportamiento — explicaciones claras e ilustradas de cómo pensamos mal.",
    "cd_uni_046": "Cursos gratuitos de alfabetización mediática para adolescentes y adultos del Poynter Institute — fact-checking práctico con ejemplos reales.",
    "cd_uni_047": "Artículos gratuitos de Ben Goldacre desmontando estadísticas malas en medicina y periodismo — el antídoto canónico contra titulares dudosos.",
    "cd_uni_048": "Más de 2.500 cursos del MIT gratis — apuntes, ejercicios, exámenes y a menudo videos completos de la mejor escuela de ingeniería del mundo.",
    "cd_uni_049": "Audita la mayoría de cursos de Stanford, Yale, Michigan y más gratis — videos y lecturas incluidas en la pista sin coste.",
    "cd_uni_050": "Cursos de Harvard, MIT, Berkeley — gratis para auditar, con certificados pagos opcionales y programas MicroMasters para créditos.",
    "cd_uni_051": "Cursos gratuitos curados de profesores de Stanford — IA, ingeniería, medicina, educación y emprendimiento.",
    "cd_uni_052": "Clases completas de pregrado de Yale — filosofía, economía, astronomía, literatura — con video completo y bibliografía.",
    "cd_uni_053": "Cursos gratuitos de la Open University — más de 1.000 temas con certificados de participación disponibles sin coste.",
    "cd_uni_054": "Cursos universitarios autorregulados con certificados gratuitos — algunos elegibles para créditos vía alianzas con ACE, sin coste de matrícula.",
    "cd_uni_055": "Cursos adaptativos basados en investigación de Carnegie Mellon — estadística, psicología, biología y lógica.",
    "cd_uni_056": "Cursos fundamentales con seguimiento de dominio — cálculo, álgebra lineal, física, economía y preparación para exámenes, totalmente gratis.",
    "cd_uni_057": "Cursos cortos gratuitos de universidades europeas y de la Commonwealth — aprendizaje basado en debate con compañeros de todo el mundo.",
    "cd_uni_058": "Buscador gratuito de más de 200.000 MOOCs — la forma más fácil de encontrar la mejor versión gratuita de cualquier curso en la web.",
    "cd_uni_059": "El MOOC más popular de la historia — curso auditable gratis sobre meta-aprendizaje, práctica enfocada y vencer la procrastinación.",
    "cd_uni_060": "El mayor buscador académico gratuito — artículos, citas y a menudo enlaces directos a PDFs gratuitos en cada disciplina.",
    "cd_uni_061": "Gestor de referencias de código abierto y gratuito — captura cualquier fuente con un clic y formatea bibliografías en cualquier estilo automáticamente.",
    "cd_uni_062": "Buscador académico con IA del Allen Institute — destaca citas influyentes y trabajos relacionados para cualquier paper.",
    "cd_uni_063": "Grafo visual de papers relacionados con cualquier artículo clave — un cambio de juego para revisiones bibliográficas y trabajos de tesis.",
    "cd_uni_064": "El mayor agregador del mundo de investigación de acceso abierto — 300 millones de papers en 11.000 repositorios, totalmente buscables.",
    "cd_uni_065": "Base de datos gratuita del NIH con más de 35M de citaciones biomédicas — esencial para ciencias de la vida, medicina y psicología.",
    "cd_uni_066": "Directory of Open Access Journals — más de 20.000 revistas peer-reviewed con texto completo gratuito, sin muros de pago.",
    "cd_uni_067": "Libros de texto peer-reviewed gratuitos de Rice University — biología, física, economía, sociología y cálculo, totalmente descargables.",
    "cd_uni_068": "La mayor biblioteca de libros de texto abiertos — química, ingeniería, humanidades y medicina, libremente remezclables para educadores.",
    "cd_uni_069": "Servidor gratuito de preprints de física, matemáticas, CS y biología cuantitativa — ve nueva investigación meses antes de su publicación formal.",
    "cd_uni_070": "Más de 75.000 libros clásicos de dominio público — ideal para cursos de literatura, historia y filosofía.",
    "cd_uni_071": "Millones de libros, papers académicos y documentos históricos gratuitos — incluyendo el servicio de préstamo Open Library.",
    "cd_uni_072": "Comprobación en tiempo real de gramática, ortografía y claridad en tu navegador o Word — el nivel gratuito cubre lo esencial diario.",
    "cd_uni_073": "Resalta oraciones complicadas, voz pasiva y adverbios — hace que la escritura académica y profesional sea mucho más clara.",
    "cd_uni_074": "Corrector gramatical de código abierto que admite más de 30 idiomas — sólido nivel gratuito, ideal para ensayos en alemán, francés y español.",
    "cd_uni_075": "Editor LaTeX online — escritura colaborativa de tesis y papers con vista previa en vivo y plantillas de revistas; nivel gratuito suficiente para la mayoría.",
    "cd_uni_076": "Alternativa moderna y de código abierto a LaTeX — compilación más rápida, sintaxis más limpia, sigue produciendo PDFs hermosos para trabajo académico.",
    "cd_uni_077": "La referencia de escritura gratuita más usada de la web — guías de estilo APA/MLA/Chicago, consejos gramaticales y manuales de escritura académica.",
    "cd_uni_078": "Lecciones gratuitas de TED-Ed sobre oratoria, narración y presentación — impartidas por personas que dan charlas TED reales.",
    "cd_uni_079": "La mayor comunidad de oratoria del mundo — muchos clubes locales permiten visitar gratis, con itinerarios estructurados de crecimiento.",
    "cd_uni_080": "Especialización auditable gratis de Patrick Barry sobre escritura y edición persuasiva — práctica para ensayos, solicitudes y pitches.",
    "cd_uni_081": "Coach de oratoria con IA gratuito — practica presentaciones en video y recibe feedback sobre muletillas, ritmo, claridad y confianza.",
    "cd_uni_082": "Procesador de texto colaborativo gratuito con edición en tiempo real, comentarios, historial de versiones y dictado por voz — universal para trabajo estudiantil.",
    "cd_uni_083": "Asistente de escritura con IA gratuito de DeepL — reescribe en función del tono y la claridad en inglés, alemán y otros idiomas principales.",
    "cd_uni_084": "Plan Plus gratuito para estudiantes con correo .edu — notas, bases de datos, listas de tareas y wikis en un solo espacio de trabajo.",
    "cd_uni_085": "Toma de notas en markdown local con backlinks — la mejor herramienta gratuita para construir un grafo de conocimiento académico personal.",
    "cd_uni_086": "Tarjetas de repetición espaciada gratuitas y de código abierto — usadas por estudiantes de medicina e idiomas en todo el mundo; la herramienta de memoria probada.",
    "cd_uni_087": "Gestor de tareas limpio que maneja tareas recurrentes y plazos en todos tus dispositivos — el nivel gratuito sirve para la mayoría de flujos.",
    "cd_uni_088": "Temporizador gamificado de enfoque — planta un árbol virtual que muere si sales de la app. La versión web gratuita bloquea distracciones de manera fiable.",
    "cd_uni_089": "Temporizador Pomodoro gratuito y simple — inicia sesiones de 25 minutos enfocadas en tu navegador sin registro ni configuración.",
    "cd_uni_090": "Bloqueador de sitios y apps gratuito difícil de saltar — programa bloques de trabajo profundo que ni tú mismo puedes anular.",
    "cd_uni_091": "Ensayos, podcasts y guías gratuitos del autor de Deep Work — manuales prácticos para enfoque sostenido y sin distracciones.",
    "cd_uni_092": "Grafo de conocimiento local-first y de código abierto — notas diarias, esquemas y backlinks; alternativa gratuita a Roam respetuosa con la privacidad.",
    "cd_uni_093": "Tableros Kanban gratuitos para proyectos — gestión visual de tareas para proyectos grupales, tesis y proyectos personales.",
    "cd_uni_094": "Calendario gratuito con time-blocking, eventos compartidos y entrada en lenguaje natural — la base de cualquier práctica de trabajo profundo.",
    "cd_uni_095": "App gratuita de seguimiento del tiempo con temporizadores de un clic — ve realmente a dónde van tus horas de estudio y diseña mejores rutinas.",
    "cd_uni_096": "El curso más popular en la historia de Yale — auditable gratis, impartido por Laurie Santos, sobre la psicología de la felicidad con prácticas diarias.",
    "cd_uni_097": "Headspace Plus gratuito para estudiantes en más de 1.000 universidades — meditaciones guiadas, historias para dormir y cursos sobre el estrés.",
    "cd_uni_098": "Meditaciones guiadas, ejercicios de respiración e historias para dormir gratuitos — los fundamentos del mindfulness sin muro de pago.",
    "cd_uni_099": "Programa gratuito basado en TCC de la Australian National University — probado para reducir síntomas de depresión y ansiedad.",
    "cd_uni_100": "Apoyo gratuito a la salud mental basado en chatbot — usa técnicas de TCC para ayudar con el ánimo, la ansiedad y el pensamiento estresante.",
    "cd_uni_101": "Centro gratuito de salud mental del NHS británico — consejos prácticos para ansiedad, sueño, ánimo bajo y estrés.",
    "cd_uni_102": "Meditaciones y ejercicios gratuitos de Kristin Neff — prácticas de autocompasión basadas en investigación que demuestran fortalecer la resiliencia.",
    "cd_uni_103": "La mayor app de meditación gratuita — más de 200.000 meditaciones guiadas, charlas y música de profesores de todo el mundo.",
    "cd_uni_104": "Apoyo emocional gratuito de oyentes formados — chats anónimos 24/7, además de terapia online de bajo coste si necesitas más.",
    "cd_uni_105": "Apoyo gratuito 24/7 en crisis por mensaje de texto — consejeros formados y confidenciales en EE.UU., Reino Unido, Irlanda y Canadá.",
    "cd_uni_106": "Recurso educativo gratuito de Harvard Medical School sobre biología, higiene y trastornos del sueño — claro, basado en evidencia y accesible.",
    "cd_uni_107": "Calendarios mensuales gratuitos de acciones diarias basadas en evidencia — pequeños hábitos sostenibles que demuestran mejorar el ánimo y la resiliencia.",
    "cd_uni_108": "Curso completo y gratuito de finanzas personales — impuestos, crédito, inversión, jubilación y bienes raíces, con la claridad de un curso de secundaria.",
    "cd_uni_109": "Enciclopedia gratuita de finanzas e inversión — más de 30.000 artículos y un simulador gratuito para hacer paper-trading sin riesgo.",
    "cd_uni_110": "Guías gratuitas que comparan tarjetas de crédito, préstamos estudiantiles, cuentas de ahorro y plataformas de inversión — consejo independiente.",
    "cd_uni_111": "Wiki comunitaria gratuita sobre inversión indexada de bajo coste — basada en los principios de John Bogle, el estándar para inversores pasivos.",
    "cd_uni_112": "Herramientas y guías gratuitas del Consumer Financial Protection Bureau de EE.UU. — préstamos estudiantiles, crédito, estafas y nociones básicas de dinero.",
    "cd_uni_113": "Centro gratuito de finanzas del gobierno australiano — calculadoras, guías y herramientas de presupuesto utilizables internacionalmente.",
    "cd_uni_114": "Curso gratuito del Nobel Robert Shiller — auditable en Coursera, cubre riesgo, finanzas conductuales y mercados modernos.",
    "cd_uni_115": "Introducción a la teoría financiera del MIT Sloan — clases y ejercicios gratuitos sobre valoración, carteras y mercados de capitales.",
    "cd_uni_116": "Videos prácticos y gratuitos sobre dinero para adultos jóvenes — presupuesto, inversión, negociación salarial e inflación del estilo de vida, sin jerga.",
    "cd_uni_117": "Más de 15 años gratuitos de escritura accesible sobre finanzas personales por JD Roth — pago de deudas, ahorro, inversión y consumo consciente.",
    "cd_uni_118": "Ensayos gratuitos sobre independencia financiera y frugalidad — el texto fundacional del movimiento FIRE, opinionado pero práctico.",
    "cd_uni_119": "Suscripción gratuita de 12 meses a YNAB para estudiantes universitarios — el método de presupuesto más querido, clases incluidas.",
    "cd_uni_120": "Curso gratuito de 10 semanas de la mejor aceleradora del mundo — más de 1M de fundadores formados, con biblioteca de ensayos y charlas de YC.",
    "cd_uni_121": "Muchas bibliotecas públicas dan acceso gratuito a LinkedIn Learning — miles de cursos sobre carreras, herramientas y habilidades blandas.",
    "cd_uni_122": "Feedback gratuito con IA sobre CV y perfil de LinkedIn — creado por ex-reclutadores, puntúa tu currículum frente a rúbricas reales de contratación.",
    "cd_uni_123": "Plantillas descargables de CV y guías de redacción gratuitas — prácticas para primeros empleos, prácticas y cambios de carrera.",
    "cd_uni_124": "Archivo gratuito de artículos sobre carrera — preparación de entrevistas, negociación salarial, política laboral y cambios profesionales.",
    "cd_uni_125": "Datos salariales gratuitos crowdsourcing de ofertas reales — ve lo que realmente pagan los puestos en tech, finanzas y consultoría antes de negociar.",
    "cd_uni_126": "Reseñas, rangos salariales y preguntas de entrevista gratuitos sobre miles de empresas — la lectura estándar antes de cualquier entrevista.",
    "cd_uni_127": "Consejos profesionales gratuitos centrados en hacer el mayor bien con tu trabajo — guías basadas en investigación sobre carreras de alto impacto.",
    "cd_uni_128": "Stanford CS183B gratuito impartido por Sam Altman y socios de Y Combinator — 20 clases gratuitas sobre construir una startup desde cero.",
    "cd_uni_129": "Comunidad gratuita de fundadores bootstrapped — entrevistas, podcasts y foros sobre construir negocios paralelos rentables.",
    "cd_uni_130": "Certificaciones gratuitas en marketing, ventas, contenido y SEO — reconocidas por empleadores, completables online en pocas horas cada una.",
    "cd_uni_131": "Certificados de Google auditables gratis en soporte TI, análisis de datos, UX y gestión de proyectos — reconocidos por más de 150 empleadores.",
    "cd_uni_132": "Visualizaciones de datos gratuitas y de licencia abierta sobre los mayores problemas del mundo — clima, pobreza y salud — creadas por investigadores de Oxford.",
    "cd_uni_133": "Explicaciones gratuitas curadas por el MIT sobre el cambio climático — la ciencia, las soluciones, la política — accesibles y rigurosamente referenciadas.",
    "cd_uni_134": "Lista gratuita y ranqueada de las soluciones climáticas más eficaces — base de datos buscable con análisis técnicos profundos para cada una.",
    "cd_uni_135": "Periodismo climático diario y gratuito de Yale — reportajes precisos y accesibles sobre ciencia, impactos y soluciones del clima.",
    "cd_uni_136": "Introducción gratuita y completa a la educación cívica de EE.UU. — Constitución, poderes, elecciones — útil incluso para estudiantes no estadounidenses que aprenden los fundamentos democráticos.",
    "cd_uni_137": "Juegos y lecciones gratuitos sobre participación democrática — creados por la Jueza O'Connor, usados en más de 50.000 aulas.",
    "cd_uni_138": "Centro gratuito de recursos sobre ética de la Santa Clara University — marcos para reflexionar sobre tecnología, negocio, IA y bioética.",
    "cd_uni_139": "Informes, primers y policy briefs gratuitos del Stanford Human-Centered AI Institute — la fuente líder sobre el impacto social de la IA.",
    "cd_uni_140": "Manual gratuito de investigación de fuentes abiertas — verifica videos, geolocaliza fotos y comprueba afirmaciones virales como los profesionales.",
    "cd_uni_141": "Archivo gratuito de periodismo basado en evidencia sobre lo que está funcionando — antídoto contra el doomscrolling, centrado en respuestas a problemas sociales.",
    "cd_uni_142": "Guías gratuitas de la Electronic Frontier Foundation sobre libertad de expresión, vigilancia y derechos digitales — la principal organización de libertades civiles digitales.",
    "cd_uni_143": "Cursos gratuitos sobre los Objetivos de Desarrollo Sostenible de la ONU — clima, igualdad, pobreza y gobernanza, impartidos por agencias de la ONU y socios.",
}

# Teachers (344)
ES_TEACHERS = {}  # populated below

# Students (288)
ES_STUDENTS = {}  # populated below

# I'll fill these dicts incrementally in this script. For brevity at this stage,
# we inject just the sport batch and signal "ready" for the others.

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
src = src_path.read_text(encoding="utf-8")

# Find ES block end: "  }\n};"
es_start = src.index("\n  es: {")
end_marker = "\n  }\n};"
es_end = src.index(end_marker, es_start)

new_keys = {**ES_SPORT, **ES_UNI, **ES_TEACHERS, **ES_STUDENTS}

# Build new lines
new_lines = []
for k, v in new_keys.items():
    v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v_esc}",')
new_block = "\n".join(new_lines)

new_src = src[:es_end] + "\n" + new_block + src[es_end:]
src_path.write_text(new_src, encoding="utf-8")
print(f"Inserted {len(new_keys)} ES card translations")
