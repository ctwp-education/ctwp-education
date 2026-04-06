/* ── CTWP i18n — English / German ── */
const translations = {
  en: {
    /* Navbar */
    'nav.about': 'About', 'nav.work': 'Our Work', 'nav.resources': 'Resources',
    'nav.support': 'Support Us', 'nav.contact': 'Contact',
    /* Hero */
    'hero.badge': 'Free Education for Every Learner',
    'hero.title': 'Empowering the world through <em>Education</em>',
    'hero.subtitle': 'CTWP Educational Empowerment bridges the gap between learners and free, open-source knowledge — testing technology in real classrooms, for real impact.',
    'hero.cta.resources': 'Explore Resources', 'hero.cta.support': 'Support Us', 'hero.cta.about': 'About the Project',
    'stat.countries': 'Countries Visited', 'stat.schools': 'Schools Visited',
    'stat.students': 'Students Reached', 'stat.labs': 'Computer Lab Built',
    /* About */
    'about.label': 'About the Project', 'about.title': 'What We Do',
    'vision.title': 'Our Vision',
    'vision.text': 'Empower every child / individual on this planet through access to (free) education by using technology and thereby positively impact the world of us all.',
    'mission.title': 'Our Mission',
    'mission.text': 'Create an innovative school concept for underprivileged children that combines online and offline learning and integrates personalized education and real-life experiences.',
    'journey.title': 'Our Journey to Impact', 'journey.subtitle': 'Currently at Phase 4 out of 5',
    'journey.desc': 'From discovering real needs across 60+ countries to building and improving a pilot school — watch our journey unfold or explore each phase below.',
    /* Phase labels */
    'phase.label.1': 'Discover', 'phase.label.2': 'Design', 'phase.label.3': 'Build',
    'phase.label.4': 'Improve', 'phase.label.5': 'Scale',
    /* Phase badges */
    'badge.completed': 'Completed', 'badge.current': 'Current Phase', 'badge.upcoming': 'Upcoming',
    /* Phase content */
    'phase1.title': 'Discover', 'phase1.tagline': 'Understanding real needs before creating solutions',
    'phase1.li1': '150+ schools and universities visited across 60+ countries',
    'phase1.li2': 'Teachers and students trained in digital learning and AI tools',
    'phase1.li3': 'Global courses completed on pedagogy, learning science, and edtech',
    'phase2.title': 'Design', 'phase2.tagline': 'Turning insights into a powerful learning model',
    'phase2.li1': 'Built a future-ready school concept (Prototype / MVP)',
    'phase2.li2': 'Combined online + offline learning experiences',
    'phase2.li3': 'Focused on personalized learning and real-life skills',
    'phase3.title': 'Build', 'phase3.tagline': 'From vision to real-world impact',
    'phase3.li1': 'Pilot school launched',
    'phase3.li2': 'Safe and inspiring learning environment created',
    'phase3.li3': 'Model tested in everyday school life',
    'phase4.title': 'Improve', 'phase4.tagline': 'Improving through real experiences',
    'phase4.li1': 'Continuous testing and refinement',
    'phase4.li2': 'Feedback from students, teachers, and communities',
    'phase4.li3': 'Ongoing adaptation to increase impact',
    'phase5.title': 'Scale', 'phase5.tagline': 'Scaling what works to reach more children',
    'phase5.li1': 'Strategic partnerships with schools and organizations',
    'phase5.li2': 'Model prepared for replication globally',
    'phase5.li3': 'Expanding access to meaningful education',
    /* Gallery */
    'gallery.label': 'See the Impact', 'gallery.title': 'Our Work in Action',
    'gallery.subtitle': 'Photos and videos from our schools, training sessions, and community work.',
    'gallery.follow': 'Follow Our Journey',
    /* Resources */
    'resources.label': 'Free Learning Tools', 'resources.title': 'Educational Resources',
    'resources.subtitle': 'Curated free resources to enhance learning and teaching with technology.',
    'resources.k12.title': 'School Students (K-12)',
    'resources.k12.desc': 'Free courses, interactive coding tools, science simulations, AI tutors, and language platforms for K–12 learners.',
    'resources.k12.link': 'Explore School Resources',
    'resources.uni.title': 'University Students',
    'resources.uni.desc': 'Academic research tools, free textbooks, productivity apps, AI assistants, and open courseware for higher education.',
    'resources.uni.link': 'Explore University Resources',
    'resources.teacher.title': 'Educators & Teachers',
    'resources.teacher.desc': 'Lesson plans, AI teaching tools, classroom management, assessment resources, and professional development.',
    'resources.teacher.link': 'Explore Educator Resources',
    /* Support */
    'support.label': 'Make an Impact', 'support.title': 'Support Us',
    'support.subtitle': "Whether you're an individual or a company — there are many ways to contribute to our mission.",
    'tab.hint': 'Select your category to see how you can help',
    'tab.individuals': 'For Individuals', 'tab.companies': 'For Companies',
    'support.donate.title': 'Donate',
    'support.donate.desc': 'Every contribution directly funds technology access, teacher training, and learning materials for children in need.',
    'support.volunteer.title': 'Volunteer',
    'support.volunteer.desc': 'Share your skills in tech, education, content creation, or marketing — remotely or on-site in Zimbabwe.',
    'support.member.title': 'Become a Member',
    'support.member.desc': 'Join the Bongai Shamwari community. Your yearly membership forms the financial foundation we build on.',
    'support.spread.title': 'Spread the Word',
    'support.spread.desc': 'Share our mission on social media and in your network. Awareness is the first step to meaningful change.',
    'support.corp.title': 'Corporate Sponsorship',
    'support.corp.desc': 'Partner as a main sponsor like Trelleborg. Fund digital infrastructure, computer labs, and educational programs. Get visibility and impact reports.',
    'support.tech.title': 'Technology Donations',
    'support.tech.desc': 'Donate laptops, tablets, or other devices to equip our computer labs and classrooms with the tools students need.',
    'support.employee.title': 'Employee Volunteering',
    'support.employee.desc': 'Send skilled employees to train teachers and students in digital literacy, coding, and AI tools as part of your CSR program.',
    'support.partner.title': 'Strategic Partnership',
    'support.partner.desc': 'Co-develop educational programs, provide software licenses, or support our scaling strategy across new regions.',
    'cta.title': 'Every Contribution Counts',
    'cta.desc': '100% of donations go directly to education programs. Bank transfers have zero transaction fees.',
    'cta.donate': 'Donate Now', 'cta.sponsor': 'Become a Sponsor',
    'sponsors.label': 'Our Partners & Sponsors',
    'sponsor.main_sponsor': 'Main Sponsor', 'sponsor.main_partner': 'Main Partner', 'sponsor.partner': 'Partner',
    'sponsor.placeholder': 'Here could be your logo',
    /* Contact */
    'contact.label': 'Get Involved', 'contact.title': "Let's Build the Future of Education",
    'contact.desc': "Whether you're an investor, educator, potential partner, or simply curious about our work — we'd love to hear from you.",
    'contact.location': 'Zurich, Switzerland (HQ)',
    'contact.form.title': 'Send us a message',
    'form.name': 'Name', 'form.name.ph': 'Your full name',
    'form.email': 'Email', 'form.email.ph': 'your@email.com',
    'form.interest': "I'm interested as...", 'form.select': 'Select an option',
    'form.donor': 'A Donor', 'form.corp_sponsor': 'A Corporate Sponsor',
    'form.teacher_role': 'A Teacher', 'form.student_role': 'A Student',
    'form.volunteer': 'A Volunteer', 'form.partner_role': 'A Partner Organization', 'form.other': 'Other',
    'form.message': 'Message', 'form.message.ph': "Tell us how you'd like to get involved...",
    'form.submit': 'Send Message',
    /* Footer */
    'footer.desc': 'Empowering every child through access to free education using technology.',
    'footer.nav': 'Navigation', 'footer.connect': 'Connect',
    'footer.about': 'About', 'footer.work': 'Our Work', 'footer.resources': 'Resources',
    'footer.support': 'Support Us', 'footer.contact': 'Contact Us',
    'footer.copyright': '© 2026 CTWP Educational Empowerment. All rights reserved.',
    /* Subpages */
    'sub.students.badge': 'K–12 Learning Tools', 'sub.students.title': 'Resources for School Students (K-12)',
    'sub.students.desc': 'Curated free platforms to help you learn anything — from coding and languages to science, math, and AI. Perfect for ages 6–18.',
    'sub.students.back': 'Back to Resources',
    'sub.uni.badge': 'Higher Education Tools', 'sub.uni.title': 'Resources for University Students',
    'sub.uni.desc': 'Free platforms for research, open courseware, textbooks, productivity, and AI tools — everything you need to thrive in higher education.',
    'sub.uni.back': 'Back to Resources',
    'sub.teachers.badge': 'For Educators & Teachers', 'sub.teachers.title': 'Free Teaching Resources',
    'sub.teachers.desc': 'Curated tools and platforms to help you plan lessons, manage classrooms, assess students, and grow professionally.',
    'sub.teachers.back': 'Back to Resources',
  },
  de: {
    /* Navbar */
    'nav.about': 'Über uns', 'nav.work': 'Unsere Arbeit', 'nav.resources': 'Ressourcen',
    'nav.support': 'Unterstützen', 'nav.contact': 'Kontakt',
    /* Hero */
    'hero.badge': 'Kostenlose Bildung für alle Lernenden',
    'hero.title': 'Die Welt durch <em>Bildung</em> stärken',
    'hero.subtitle': 'CTWP Educational Empowerment überbrückt die Lücke zwischen Lernenden und freiem, offenem Wissen — Technologie wird in echten Klassenzimmern für echte Wirkung getestet.',
    'hero.cta.resources': 'Ressourcen entdecken', 'hero.cta.support': 'Unterstützen', 'hero.cta.about': 'Über das Projekt',
    'stat.countries': 'Besuchte Länder', 'stat.schools': 'Besuchte Schulen',
    'stat.students': 'Erreichte Schüler', 'stat.labs': 'Computerraum errichtet',
    /* About */
    'about.label': 'Über das Projekt', 'about.title': 'Was wir tun',
    'vision.title': 'Unsere Vision',
    'vision.text': 'Jedes Kind und jede Person auf diesem Planeten durch Zugang zu (kostenloser) Bildung mithilfe von Technologie stärken und die Welt dadurch positiv verändern.',
    'mission.title': 'Unsere Mission',
    'mission.text': 'Ein innovatives Schulkonzept für benachteiligte Kinder schaffen, das Online- und Offline-Lernen kombiniert und auf personalisierte Bildung sowie reale Erfahrungen setzt.',
    'journey.title': 'Unsere Reise zur Wirkung', 'journey.subtitle': 'Derzeit in Phase 4 von 5',
    'journey.desc': 'Von der Entdeckung realer Bedürfnisse in 60+ Ländern bis zum Aufbau einer Pilotschule — verfolge unsere Reise oder erkunde jede Phase unten.',
    /* Phase labels */
    'phase.label.1': 'Entdecken', 'phase.label.2': 'Gestalten', 'phase.label.3': 'Aufbauen',
    'phase.label.4': 'Verbessern', 'phase.label.5': 'Skalieren',
    /* Phase badges */
    'badge.completed': 'Abgeschlossen', 'badge.current': 'Aktuelle Phase', 'badge.upcoming': 'Bevorstehend',
    /* Phase content */
    'phase1.title': 'Entdecken', 'phase1.tagline': 'Echte Bedürfnisse verstehen, bevor Lösungen entwickelt werden',
    'phase1.li1': '150+ Schulen und Universitäten in 60+ Ländern besucht',
    'phase1.li2': 'Lehrende und Lernende in digitalem Lernen und KI-Tools geschult',
    'phase1.li3': 'Globale Kurse zu Pädagogik, Lernwissenschaft und Edtech absolviert',
    'phase2.title': 'Gestalten', 'phase2.tagline': 'Erkenntnisse in ein leistungsstarkes Lernmodell verwandeln',
    'phase2.li1': 'Zukunftsfähiges Schulkonzept entwickelt (Prototyp / MVP)',
    'phase2.li2': 'Online- und Offline-Lernerfahrungen kombiniert',
    'phase2.li3': 'Fokus auf personalisiertes Lernen und Lebenskompetenzen',
    'phase3.title': 'Aufbauen', 'phase3.tagline': 'Von der Vision zur realen Wirkung',
    'phase3.li1': 'Pilotschule eröffnet',
    'phase3.li2': 'Sichere und inspirierende Lernumgebung geschaffen',
    'phase3.li3': 'Modell im Schulalltag erprobt',
    'phase4.title': 'Verbessern', 'phase4.tagline': 'Lernen durch echte Erfahrungen',
    'phase4.li1': 'Kontinuierliches Testen und Verfeinern',
    'phase4.li2': 'Rückmeldungen von Schülern, Lehrenden und Gemeinschaften',
    'phase4.li3': 'Fortlaufende Anpassung zur Steigerung der Wirkung',
    'phase5.title': 'Skalieren', 'phase5.tagline': 'Was funktioniert, ausbauen und mehr Kinder erreichen',
    'phase5.li1': 'Strategische Partnerschaften mit Schulen und Organisationen',
    'phase5.li2': 'Modell zur weltweiten Replikation vorbereitet',
    'phase5.li3': 'Zugang zu sinnvoller Bildung ausbauen',
    /* Gallery */
    'gallery.label': 'Die Wirkung sehen', 'gallery.title': 'Unsere Arbeit in Aktion',
    'gallery.subtitle': 'Fotos und Videos aus unseren Schulen, Trainings und Gemeinschaftsprojekten.',
    'gallery.follow': 'Folge unserer Reise',
    /* Resources */
    'resources.label': 'Kostenlose Lernmittel', 'resources.title': 'Bildungsressourcen',
    'resources.subtitle': 'Kuratierte kostenlose Ressourcen für besseres Lernen und Lehren mit Technologie.',
    'resources.k12.title': 'Schülerinnen & Schüler (K-12)',
    'resources.k12.desc': 'Kostenlose Kurse, interaktive Programmierwerkzeuge, Wissenschaftssimulationen, KI-Tutoren und Sprachplattformen für K–12-Lernende.',
    'resources.k12.link': 'Schulressourcen entdecken',
    'resources.uni.title': 'Studierende',
    'resources.uni.desc': 'Akademische Recherche-Tools, kostenlose Lehrbücher, Produktivitäts-Apps, KI-Assistenten und offene Kurse für die Hochschulbildung.',
    'resources.uni.link': 'Hochschulressourcen entdecken',
    'resources.teacher.title': 'Lehrerinnen & Lehrer',
    'resources.teacher.desc': 'Unterrichtspläne, KI-Lehrwerkzeuge, Klassenmanagement, Bewertungsressourcen und berufliche Weiterentwicklung.',
    'resources.teacher.link': 'Lehrerressourcen entdecken',
    /* Support */
    'support.label': 'Wirkung erzielen', 'support.title': 'Unterstütze uns',
    'support.subtitle': 'Ob als Einzelperson oder Unternehmen — es gibt viele Möglichkeiten, unsere Mission zu unterstützen.',
    'tab.hint': 'Wähle deine Kategorie aus, um zu sehen, wie du helfen kannst',
    'tab.individuals': 'Für Einzelpersonen', 'tab.companies': 'Für Unternehmen',
    'support.donate.title': 'Spenden',
    'support.donate.desc': 'Jeder Beitrag finanziert direkt den Zugang zu Technologie, die Lehrerausbildung und Lernmaterialien für bedürftige Kinder.',
    'support.volunteer.title': 'Ehrenamtlich helfen',
    'support.volunteer.desc': 'Teile deine Kenntnisse in Technik, Bildung, Content-Erstellung oder Marketing — remote oder vor Ort in Simbabwe.',
    'support.member.title': 'Mitglied werden',
    'support.member.desc': 'Werde Teil der Bongai-Shamwari-Gemeinschaft. Deine jährliche Mitgliedschaft bildet das finanzielle Fundament, auf dem wir aufbauen.',
    'support.spread.title': 'Weitersagen',
    'support.spread.desc': 'Teile unsere Mission in sozialen Medien und in deinem Netzwerk. Bewusstsein ist der erste Schritt zu echtem Wandel.',
    'support.corp.title': 'Unternehmenspartnerschaft',
    'support.corp.desc': 'Werde Hauptsponsor wie Trelleborg. Finanziere digitale Infrastruktur, Computerräume und Bildungsprogramme. Erhalte Sichtbarkeit und Wirkungsberichte.',
    'support.tech.title': 'Technologiespenden',
    'support.tech.desc': 'Stifte Laptops, Tablets oder andere Geräte, um unsere Computerräume und Klassen mit den nötigen Werkzeugen auszustatten.',
    'support.employee.title': 'Mitarbeiter-Volunteering',
    'support.employee.desc': 'Entsende qualifizierte Mitarbeitende, um Lehrende und Lernende in digitaler Kompetenz, Programmieren und KI-Tools zu schulen — als Teil deines CSR-Programms.',
    'support.partner.title': 'Strategische Partnerschaft',
    'support.partner.desc': 'Entwickle gemeinsam Bildungsprogramme, stelle Software-Lizenzen bereit oder unterstütze unsere Skalierungsstrategie in neuen Regionen.',
    'cta.title': 'Jeder Beitrag zählt',
    'cta.desc': '100 % der Spenden fliessen direkt in Bildungsprogramme. Banküberweisungen haben keine Transaktionsgebühren.',
    'cta.donate': 'Jetzt spenden', 'cta.sponsor': 'Sponsor werden',
    'sponsors.label': 'Unsere Partner & Sponsoren',
    'sponsor.main_sponsor': 'Hauptsponsor', 'sponsor.main_partner': 'Hauptpartner', 'sponsor.partner': 'Partner',
    'sponsor.placeholder': 'Hier könnte Ihr Logo stehen',
    /* Contact */
    'contact.label': 'Mitmachen', 'contact.title': 'Gestalten wir gemeinsam die Zukunft der Bildung',
    'contact.desc': 'Ob Investor, Lehrperson, potenzielle Partnerorganisation oder einfach neugierig auf unsere Arbeit — wir freuen uns von dir zu hören.',
    'contact.location': 'Zürich, Schweiz (Hauptsitz)',
    'contact.form.title': 'Schreib uns eine Nachricht',
    'form.name': 'Name', 'form.name.ph': 'Vollständiger Name',
    'form.email': 'E-Mail', 'form.email.ph': 'deine@email.com',
    'form.interest': 'Ich interessiere mich als...', 'form.select': 'Option auswählen',
    'form.donor': 'Spender/in', 'form.corp_sponsor': 'Unternehmenssponsor',
    'form.teacher_role': 'Lehrkraft', 'form.student_role': 'Schüler/in oder Student/in',
    'form.volunteer': 'Freiwillige/r', 'form.partner_role': 'Partnerorganisation', 'form.other': 'Sonstiges',
    'form.message': 'Nachricht', 'form.message.ph': 'Wie möchtest du dich einbringen?',
    'form.submit': 'Nachricht senden',
    /* Footer */
    'footer.desc': 'Jedes Kind durch Zugang zu kostenloser Bildung mit Technologie stärken.',
    'footer.nav': 'Navigation', 'footer.connect': 'Verbinden',
    'footer.about': 'Über uns', 'footer.work': 'Unsere Arbeit', 'footer.resources': 'Ressourcen',
    'footer.support': 'Unterstützen', 'footer.contact': 'Kontakt',
    'footer.copyright': '© 2026 CTWP Educational Empowerment. Alle Rechte vorbehalten.',
    /* Subpages */
    'sub.students.badge': 'K–12 Lernmittel', 'sub.students.title': 'Ressourcen für Schülerinnen & Schüler (K-12)',
    'sub.students.desc': 'Kuratierte kostenlose Plattformen für alles Wissenswerte — von Programmieren und Sprachen bis zu Naturwissenschaften, Mathematik und KI. Für Altersgruppen 6–18.',
    'sub.students.back': 'Zurück zu Ressourcen',
    'sub.uni.badge': 'Hochschulbildung', 'sub.uni.title': 'Ressourcen für Studierende',
    'sub.uni.desc': 'Kostenlose Plattformen für Forschung, offene Kurse, Lehrbücher, Produktivität und KI-Tools — alles für ein erfolgreiches Studium.',
    'sub.uni.back': 'Zurück zu Ressourcen',
    'sub.teachers.badge': 'Für Lehrerinnen & Lehrer', 'sub.teachers.title': 'Kostenlose Lehrressourcen',
    'sub.teachers.desc': 'Kuratierte Tools und Plattformen für Unterrichtsplanung, Klassenmanagement, Schülerbewertung und berufliche Weiterentwicklung.',
    'sub.teachers.back': 'Zurück zu Ressourcen',
  }
};

let currentLang = localStorage.getItem('ctwp-lang') || 'en';

function t(key) {
  return translations[currentLang][key] || translations['en'][key] || key;
}

function applyTranslations() {
  /* Text content */
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.textContent = t(el.dataset.i18n);
  });
  /* HTML content (for elements with tags like <em>) */
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    el.innerHTML = t(el.dataset.i18nHtml);
  });
  /* Placeholders */
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    el.placeholder = t(el.dataset.i18nPh);
  });
  /* Update toggle button — highlight active language */
  const btn = document.getElementById('langToggle');
  if (btn) {
    btn.querySelectorAll('.lang-opt').forEach(opt => {
      opt.classList.toggle('lang-active', opt.dataset.lang === currentLang);
    });
  }
  /* Update html lang attribute */
  document.documentElement.lang = currentLang;
}

function toggleLanguage() {
  currentLang = currentLang === 'en' ? 'de' : 'en';
  localStorage.setItem('ctwp-lang', currentLang);
  applyTranslations();
}

function i18nInit() {
  applyTranslations();
  const btn = document.getElementById('langToggle');
  if (btn) btn.addEventListener('click', toggleLanguage);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', i18nInit);
} else {
  i18nInit();
}
