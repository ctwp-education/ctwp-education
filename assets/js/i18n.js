/* ── CTWP i18n — English / German ── */
const translations = {
  en: {
    /* Navbar */
    'nav.about': 'About', 'nav.work': 'Our Work', 'nav.resources': 'Resources',
    'nav.support': 'Support Us', 'nav.contact': 'Contact', 'nav.lab': 'Our Lab',
    /* Hero */
    'hero.badge': 'Free Education for Every Learner',
    'hero.title': 'Empowering the world through <em>Education</em>',
    'hero.subtitle': 'CTWP Educational Empowerment bridges the gap between learners and free, open-source knowledge — testing technology in real classrooms, for real impact.',
    'hero.cta.resources': 'Explore Resources', 'hero.cta.support': 'Support Us', 'hero.cta.about': 'About the Project',
    'stat.countries': 'Countries Visited', 'stat.schools': 'Schools Visited',
    'stat.students': 'Students Reached', 'stat.labs': 'Computer Lab Built', 'stat.labs.cta': 'See the Lab →',
    'lab.btn': 'See the Computer Lab →', 'lab.banner': 'Explore our Computer Lab in Zimbabwe →',
    /* Lab subpage */
    'lab.hero.subtitle': 'A fully equipped digital learning lab for disadvantaged and disabled children — powered by solar energy, Starlink internet, and the belief that every child deserves access to technology.',
    'lab.hero.cta1': 'Support This Project', 'lab.hero.cta2': 'See What We Built',
    'lab.intro.label': 'Status Report 2025', 'lab.intro.title': 'Thank You for Your Support!',
    'lab.intro.quote': '"For disadvantaged and disabled children in Zimbabwe, Bongai Shamwari is far more than a place of learning — it is a source of hope, opportunity, and community."',
    'lab.intro.p1': 'Your generous contribution in 2025 has been instrumental in advancing the digitalization project at the Bongai Shamwari kindergarten and school. Thanks to your support, we have built sustainable digital infrastructure that opens the door to knowledge and new learning opportunities for the children, their teachers, and the wider community.',
    'lab.intro.p2': 'Your commitment is helping to shape a future in which every child can explore their potential and participate fully in the digital world. Each step brings us closer to our goal: making education accessible to all, regardless of external challenges.',
    'lab.milestones.label': 'Completed in 2025', 'lab.milestones.title': 'What We Built Together',
    'lab.milestones.subtitle': 'From laying the foundations to the first ICT lessons — every milestone reached thanks to your support.',
    'lab.m1.title': 'Solar Energy Installation', 'lab.m1.desc': 'Full solar power system installed, ensuring reliable and sustainable electricity for the computer lab.',
    'lab.m2.title': 'Room Preparation', 'lab.m2.desc': 'Computer lab interior fully prepared, including tables and chairs purchased locally to support the community.',
    'lab.m3.title': 'Security Enhancements', 'lab.m3.desc': 'Burglar bars and additional security cameras installed to protect all equipment.',
    'lab.m4.title': 'Starlink Internet', 'lab.m4.desc': 'Starlink internet system installed, providing reliable high-speed connectivity to support digital learning.',
    'lab.m5.title': 'Computers Delivered', 'lab.m5.desc': 'All computers including peripherals shipped to the school; monitors purchased locally.',
    'lab.m6.title': 'Technical Setup', 'lab.m6.desc': 'All hardware and software installed for classroom use, including educational tools and child-friendly access controls.',
    'lab.m7.title': 'ICT Teacher Hired', 'lab.m7.desc': 'A qualified ICT teacher hired after thorough interviews to ensure the best fit for the program.',
    'lab.m8.title': 'First ICT Lessons', 'lab.m8.desc': 'Introductory sessions for students and teachers successfully started, introducing foundational digital literacy skills.',
    'lab.gallery.label': 'Impressions', 'lab.gallery.title': 'Inside the Computer Lab',
    'lab.gallery.subtitle': 'Real moments from the first lessons at Bongai Shamwari School, Zimbabwe.',
    'lab.nextsteps.label': 'Looking Ahead', 'lab.nextsteps.title': 'Next Steps — 2026 & Beyond',
    'lab.nextsteps.subtitle': 'The lab is running — now we need to sustain and grow it. Here\'s what comes next.',
    'lab.ns1.title': 'Secure Sponsorship for the ICT Teacher\'s Salary', 'lab.ns1.desc': 'Identify donors, partners, or CSR programs to fund the full-time ICT educator — ensuring long-term sustainability of the digital learning program.',
    'lab.ns2.title': 'Ship Remaining Equipment & Classroom Enhancements', 'lab.ns2.desc': 'Ship printer, projector, mouse pads, and USB sticks; purchase locally a shelf for storing equipment, dust-proof computer covers, and ICT schoolbooks.',
    'lab.ns3.title': 'Launch Full ICT Curriculum', 'lab.ns3.desc': 'Begin the first official teaching term of ICT as a structured subject at Bongai Shamwari — turning the pilot lessons into a complete digital education program.',
    'lab.contact.label': 'Get in Touch', 'lab.contact.title': 'Contact the Project Team',
    'lab.contact.subtitle': 'Questions about the lab, partnership opportunities, or how to contribute? Reach out directly.',
    'lab.contact.lars.role': 'CDO of Bongai', 'lab.contact.christa.role': 'Chairman',
    'lab.cta.title': 'Help Us Keep the Lab Running', 'lab.cta.subtitle': 'Your donation directly funds the ICT teacher\'s salary, new equipment, and the continued education of children who have never had access to a computer before.',
    'lab.cta.btn1': 'Donate Now', 'lab.cta.btn2': 'Bongai Shamwari Website', 'lab.cta.btn3': '← Back to CTWP',
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
    'phase1.li1': 'Visited 150+ schools and universities across 60+ countries',
    'phase1.li2': 'Trained teachers and students in digital learning and AI tools',
    'phase1.li3': 'Completed education and training in pedagogy, learning science, and edtech',
    'phase2.title': 'Design', 'phase2.tagline': 'Turning insights into a powerful learning model',
    'phase2.li1': 'Built a future-ready school concept',
    'phase2.li2': 'Combined online and offline learning experiences',
    'phase2.li3': 'Focused on personalized learning and real-life skills',
    'phase3.title': 'Build', 'phase3.tagline': 'From vision to real-world impact',
    'phase3.li1': 'Launched our pilot school',
    'phase3.li2': 'Created a safe and inspiring learning environment',
    'phase3.li3': 'Tested the model in everyday school life',
    'phase4.title': 'Improve', 'phase4.tagline': 'Improving through real experiences',
    'phase4.li1': 'Continuously testing and refining the model',
    'phase4.li2': 'Gathering feedback from students, teachers, and communities',
    'phase4.li3': 'Adapting the model to increase impact',
    'phase5.title': 'Scale', 'phase5.tagline': 'Scaling what works to reach more children',
    'phase5.li1': 'Build strategic partnerships with schools and organizations',
    'phase5.li2': 'Prepare the model for global replication',
    'phase5.li3': 'Expand access to meaningful education worldwide',
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
    /* GDPR */
    'gdpr.title': 'Cookie & Storage Notice',
    'gdpr.text': 'We use browser local storage solely to remember your language preference. No tracking cookies or personal data are collected or shared.',
    'gdpr.accept': 'Accept',
    'gdpr.decline': 'Decline',
  },
  de: {
    /* Navbar */
    'nav.about': 'Über uns', 'nav.work': 'Unsere Arbeit', 'nav.resources': 'Ressourcen',
    'nav.support': 'Unterstützen', 'nav.contact': 'Kontakt', 'nav.lab': 'Unser Lab',
    /* Hero */
    'hero.badge': 'Kostenlose Bildung für alle Lernenden',
    'hero.title': 'Die Welt durch <em>Bildung</em> stärken',
    'hero.subtitle': 'CTWP Educational Empowerment überbrückt die Lücke zwischen Lernenden und freiem, offenem Wissen — Technologie wird in echten Klassenzimmern für echte Wirkung getestet.',
    'hero.cta.resources': 'Ressourcen entdecken', 'hero.cta.support': 'Unterstützen', 'hero.cta.about': 'Über das Projekt',
    'stat.countries': 'Besuchte Länder', 'stat.schools': 'Besuchte Schulen',
    'stat.students': 'Erreichte Schüler', 'stat.labs': 'Computerraum errichtet', 'stat.labs.cta': 'Zum Computer Lab →',
    'lab.btn': 'Zum Computer Lab →', 'lab.banner': 'Unser Computer Lab in Simbabwe entdecken →',
    /* Lab subpage DE */
    'lab.hero.subtitle': 'Ein voll ausgestattetes digitales Lernlabor für benachteiligte und behinderte Kinder — betrieben mit Solarenergie, Starlink-Internet und der Überzeugung, dass jedes Kind Zugang zu Technologie verdient.',
    'lab.hero.cta1': 'Projekt unterstützen', 'lab.hero.cta2': 'Was wir gebaut haben',
    'lab.intro.label': 'Statusbericht 2025', 'lab.intro.title': 'Danke für Ihre Unterstützung!',
    'lab.intro.quote': '„Für benachteiligte und behinderte Kinder in Simbabwe ist Bongai Shamwari weit mehr als ein Lernort — es ist eine Quelle der Hoffnung, der Möglichkeiten und der Gemeinschaft."',
    'lab.intro.p1': 'Ihr großzügiger Beitrag im Jahr 2025 war entscheidend für den Fortschritt des Digitalisierungsprojekts an der Bongai Shamwari Kita und Schule. Dank Ihrer Unterstützung haben wir eine nachhaltige digitale Infrastruktur aufgebaut, die den Kindern, ihren Lehrern und der gesamten Gemeinschaft Zugang zu Wissen und neuen Lernmöglichkeiten eröffnet.',
    'lab.intro.p2': 'Ihr Engagement trägt dazu bei, eine Zukunft zu gestalten, in der jedes Kind sein Potenzial entfalten und vollständig an der digitalen Welt teilhaben kann. Jeder Schritt bringt uns unserem Ziel näher: Bildung für alle zugänglich zu machen.',
    'lab.milestones.label': 'Erreicht in 2025', 'lab.milestones.title': 'Was wir gemeinsam aufgebaut haben',
    'lab.milestones.subtitle': 'Von den Grundlagen bis zu den ersten IT-Stunden — jeder Meilenstein dank Ihrer Unterstützung erreicht.',
    'lab.m1.title': 'Solaranlage', 'lab.m1.desc': 'Vollständige Solaranlage installiert — zuverlässige und nachhaltige Stromversorgung für den Computerraum.',
    'lab.m2.title': 'Raumvorbereitung', 'lab.m2.desc': 'Innenausstattung des Computerraums komplett fertiggestellt, inkl. lokal gekaufter Tische und Stühle.',
    'lab.m3.title': 'Sicherheitsmassnahmen', 'lab.m3.desc': 'Sicherheitsgitter und zusätzliche Überwachungskameras installiert.',
    'lab.m4.title': 'Starlink-Internet', 'lab.m4.desc': 'Starlink-Internetsystem installiert — zuverlässige Hochgeschwindigkeitsverbindung für das digitale Lernen.',
    'lab.m5.title': 'Computer geliefert', 'lab.m5.desc': 'Alle Computer inkl. Peripheriegeräte geliefert; Monitore lokal gekauft.',
    'lab.m6.title': 'Technisches Setup', 'lab.m6.desc': 'Alle Hard- und Software für den Unterrichtsbetrieb installiert, inkl. Lerntools und kindergerechter Zugangskontrolle.',
    'lab.m7.title': 'ICT-Lehrkraft eingestellt', 'lab.m7.desc': 'Qualifizierte ICT-Lehrkraft nach sorgfältiger Auswahl eingestellt.',
    'lab.m8.title': 'Erste IT-Stunden', 'lab.m8.desc': 'Einführungseinheiten für Schüler und Lehrkräfte erfolgreich gestartet — Grundlagen der digitalen Kompetenz.',
    'lab.gallery.label': 'Eindrücke', 'lab.gallery.title': 'Im Computer Lab',
    'lab.gallery.subtitle': 'Echte Momente aus den ersten Stunden an der Bongai Shamwari Schule, Simbabwe.',
    'lab.nextsteps.label': 'Blick nach vorne', 'lab.nextsteps.title': 'Nächste Schritte — 2026 und darüber hinaus',
    'lab.nextsteps.subtitle': 'Das Lab läuft — jetzt geht es darum, es zu erhalten und auszubauen.',
    'lab.ns1.title': 'Finanzierung des ICT-Lehrers sichern', 'lab.ns1.desc': 'Spender, Partner oder CSR-Programme finden, um das Gehalt des ICT-Lehrers langfristig zu finanzieren.',
    'lab.ns2.title': 'Restliche Ausstattung liefern & Raum ausstatten', 'lab.ns2.desc': 'Drucker, Projektor, Mauspads und USB-Sticks liefern; lokal Regal, staubdichte Abdeckungen und IT-Schulbücher kaufen.',
    'lab.ns3.title': 'Vollständigen ICT-Lehrplan starten', 'lab.ns3.desc': 'Das erste offizielle Unterrichtshalbjahr mit IT als strukturiertem Schulfach an der Bongai Shamwari Schule beginnen.',
    'lab.contact.label': 'Kontakt', 'lab.contact.title': 'Das Projektteam kontaktieren',
    'lab.contact.subtitle': 'Fragen zum Lab, Partnerschaftsmöglichkeiten oder wie Sie beitragen können? Wenden Sie sich direkt an uns.',
    'lab.contact.lars.role': 'CDO von Bongai', 'lab.contact.christa.role': 'Vorsitzende',
    'lab.cta.title': 'Helfen Sie uns, das Lab am Laufen zu halten', 'lab.cta.subtitle': 'Ihre Spende finanziert direkt das Gehalt der ICT-Lehrkraft, neue Ausstattung und die Bildung von Kindern, die noch nie Zugang zu einem Computer hatten.',
    'lab.cta.btn1': 'Jetzt spenden', 'lab.cta.btn2': 'Bongai Shamwari Website', 'lab.cta.btn3': '← Zurück zu CTWP',
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
    'phase1.li3': 'Aus- und Weiterbildung in Pädagogik, Lernwissenschaft und Edtech abgeschlossen',
    'phase2.title': 'Gestalten', 'phase2.tagline': 'Erkenntnisse in ein leistungsstarkes Lernmodell verwandeln',
    'phase2.li1': 'Zukunftsfähiges Schulkonzept entwickelt',
    'phase2.li2': 'Online- und Offline-Lernerfahrungen kombiniert',
    'phase2.li3': 'Fokus auf personalisiertes Lernen und Lebenskompetenzen',
    'phase3.title': 'Aufbauen', 'phase3.tagline': 'Von der Vision zur realen Wirkung',
    'phase3.li1': 'Pilotschule eröffnet',
    'phase3.li2': 'Sichere und inspirierende Lernumgebung geschaffen',
    'phase3.li3': 'Modell im Schulalltag erprobt',
    'phase4.title': 'Verbessern', 'phase4.tagline': 'Lernen durch echte Erfahrungen',
    'phase4.li1': 'Modell kontinuierlich testen und verfeinern',
    'phase4.li2': 'Rückmeldungen von Schülern, Lehrenden und Gemeinschaften einholen',
    'phase4.li3': 'Modell anpassen, um die Wirkung zu steigern',
    'phase5.title': 'Skalieren', 'phase5.tagline': 'Was funktioniert, ausbauen und mehr Kinder erreichen',
    'phase5.li1': 'Strategische Partnerschaften mit Schulen und Organisationen aufbauen',
    'phase5.li2': 'Modell zur weltweiten Replikation vorbereiten',
    'phase5.li3': 'Zugang zu sinnvoller Bildung weltweit ausbauen',
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
    /* GDPR */
    'gdpr.title': 'Cookie- & Speicherhinweis',
    'gdpr.text': 'Wir verwenden den lokalen Browser-Speicher ausschliesslich, um deine Spracheinstellung zu speichern. Es werden keine Tracking-Cookies oder persönliche Daten erfasst oder weitergegeben.',
    'gdpr.accept': 'Akzeptieren',
    'gdpr.decline': 'Ablehnen',
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
