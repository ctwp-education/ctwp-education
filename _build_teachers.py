#!/usr/bin/env python3
"""
Generate teachers.html organised by the teaching workflow:
  4 PHASES (Before/During/After/Supporting) -> 18 sub-clusters -> 12 cards each = 216 cards.
Two-level navigation (Option B):
  - Top: 4 big phase tabs
  - Below: row of sub-chips for the active phase
  - Each sub-chip toggles its own panel of 12 cards
  - Audience filter (Pre-K / Primary / Secondary / Higher Ed / Special Ed) on top of all
"""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "teachers.html"

AUD_LABELS = {
    "prek": "Pre-K", "primary": "Primary", "secondary": "Secondary",
    "higher": "Higher Ed", "sen": "Special Ed", "all": "All Stages",
}
AUD_CLASS = {k: f"gb-{k}" for k in AUD_LABELS}
PILL_LABELS = {"free": "Free", "free-signup": "Free (sign-up)", "freemium": "Freemium"}
PILL_CLASS = {"free": "pill-free", "free-signup": "pill-free-signup", "freemium": "pill-freemium"}

# ---------------- PHASES (6) -> sub-clusters -> cards ----------------
PHASES = [
    # ═══════════════════════════════════════════════════════════════════════
    # 📘 TEACHER'S FUNDAMENTALS — Didactics & Pedagogy
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "fundamentals", "color": "#0ea5e9", "color_bg": "#f0f9ff",
        "icon": "fas fa-graduation-cap",
        "tab_label": "Teacher's Fundamentals", "tag": "Didactics & Pedagogy",
        "subclusters": [
            # ── F1. Didactics ──
            {
                "key": "didactics", "color": "#0ea5e9", "color_bg": "#f0f9ff",
                "icon": "fas fa-chalkboard",
                "chip_label": "Didactics",
                "label": "How to Teach",
                "title": "Didactics — How You Teach",
                "desc": "Master the craft of teaching: instructional models, lesson structure, content delivery and evidence-based techniques to make any lesson land.",
                "cards": [
                    {"href":"https://www.coursera.org/learn/learning-how-to-learn", "title":"Learning How to Learn", "icon":"fas fa-brain", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"The world's most popular learning-science MOOC (4M+ students) — chunking, memory, diffuse thinking. Free to audit."},
                    {"href":"https://www.cultofpedagogy.com", "title":"Cult of Pedagogy", "icon":"fas fa-podcast", "pill":"free", "audiences":["all"],
                     "desc":"Jennifer Gonzalez's podcast and blog — hundreds of free deep-dives on instructional strategies, engagement and classroom technique."},
                    {"href":"https://www.learningscientists.org", "title":"The Learning Scientists", "icon":"fas fa-flask", "pill":"free", "audiences":["all"],
                     "desc":"Six evidence-based study strategies (spaced practice, retrieval, elaboration etc.) explained clearly for teachers and students."},
                    {"href":"https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/", "title":"Bloom's Taxonomy Guide", "icon":"fas fa-layer-group", "pill":"free", "audiences":["all"],
                     "desc":"Vanderbilt's definitive free guide to Bloom's revised taxonomy — verb lists, question stems and lesson-planning templates."},
                    {"href":"https://www.cast.org/impact/universal-design-for-learning-udl", "title":"CAST UDL Framework", "icon":"fas fa-universal-access", "pill":"free", "audiences":["all","sen"],
                     "desc":"Free Universal Design for Learning guidelines — plan lessons that work for every learner from the start, not as an afterthought."},
                    {"href":"https://www.teachlikeachampion.com/resources/", "title":"Teach Like a Champion", "icon":"fas fa-star", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Doug Lemov's 63 classroom techniques — free video clips, read-alongs and field guides on cold calling, pacing and more."},
                    {"href":"https://www.edutopia.org/teaching-strategies", "title":"Edutopia Strategies", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Research-to-practice articles on differentiation, project-based learning, social-emotional integration and assessment design."},
                    {"href":"https://www.teachthought.com", "title":"TeachThought", "icon":"fas fa-atom", "pill":"free", "audiences":["all"],
                     "desc":"Free articles on modern pedagogical models — learning taxonomies, innovative frameworks and classroom-ready thinking tools."},
                    {"href":"https://www.instructionalcoaching.com/resources/", "title":"Instructional Coaching Group", "icon":"fas fa-user-tie", "pill":"free", "audiences":["all"],
                     "desc":"Jim Knight's free resources on the impact cycle — a practical framework any teacher can use for self-directed improvement."},
                    {"href":"https://tsl.mit.edu/", "title":"MIT Teaching Systems Lab", "icon":"fas fa-university", "pill":"free", "audiences":["higher"],
                     "desc":"Free MIT research and tools on teacher learning — simulations, case studies and courses on instructional design."},
                    {"href":"https://www.ascd.org/articles", "title":"ASCD Free Articles", "icon":"fas fa-book-open", "pill":"free", "audiences":["all"],
                     "desc":"Hundreds of free peer-reviewed articles on curriculum, instruction and assessment from the world's leading educator association."},
                    {"href":"https://www.deansforimpact.org/resources", "title":"Deans for Impact", "icon":"fas fa-chart-line", "pill":"free", "audiences":["all"],
                     "desc":"Free reports translating cognitive science into teacher-prep principles — The Science of Learning made accessible."},
                ],
            },
            # ── F2. Pedagogy ──
            {
                "key": "pedagogy", "color": "#8b5cf6", "color_bg": "#f5f3ff",
                "icon": "fas fa-brain",
                "chip_label": "Pedagogy",
                "label": "Why You Teach the Way You Do",
                "title": "Pedagogy — Why You Teach the Way You Do",
                "desc": "Explore the theory and philosophy behind great teaching: learning psychology, motivation, constructivism and the learner's experience.",
                "cards": [
                    {"href":"https://www.danielwillingham.com/articles", "title":"Daniel Willingham", "icon":"fas fa-brain", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"Cognitive scientist's free articles on memory, attention and motivation — translated from research lab to classroom practice."},
                    {"href":"https://www.mindsetworks.com/science/", "title":"Growth Mindset (Dweck)", "icon":"fas fa-seedling", "pill":"free", "audiences":["all"],
                     "desc":"Carol Dweck's Mindset Works — free research summaries and classroom-ready strategies for building a growth mindset culture."},
                    {"href":"https://selfdeterminationtheory.org/theory/", "title":"Self-Determination Theory", "icon":"fas fa-compass", "pill":"free", "audiences":["all"],
                     "desc":"Deci & Ryan's SDT explained — why autonomy, competence and relatedness are the three keys to student motivation."},
                    {"href":"https://pz.harvard.edu/thinking-routines", "title":"Harvard Thinking Routines", "icon":"fas fa-route", "pill":"free", "audiences":["all"],
                     "desc":"Project Zero's free thinking-routine toolkit — See-Think-Wonder, Claim-Support-Question and 20+ classroom-ready protocols."},
                    {"href":"https://characterlab.org/playbooks/", "title":"Character Lab Playbooks", "icon":"fas fa-heart", "pill":"free", "audiences":["all"],
                     "desc":"Angela Duckworth's free teacher playbooks on grit, curiosity, gratitude and self-control — research-backed, ready to use."},
                    {"href":"https://greatergood.berkeley.edu/education", "title":"Greater Good in Education", "icon":"fas fa-hand-holding-heart", "pill":"free", "audiences":["all"],
                     "desc":"Berkeley Science Center's free SEL practices grounded in positive psychology — kindness, mindfulness and resilience."},
                    {"href":"https://www.kqed.org/mindshift", "title":"MindShift (KQED)", "icon":"fas fa-wave-square", "pill":"free", "audiences":["all"],
                     "desc":"Free podcast and articles on how learning works — neuroscience, motivation, equity and the future of education."},
                    {"href":"https://www.gse.harvard.edu/ideas", "title":"Harvard Ed Ideas", "icon":"fas fa-graduation-cap", "pill":"free", "audiences":["higher"],
                     "desc":"Free Harvard Graduate School of Education research articles — equity, learning science, school leadership and policy."},
                    {"href":"https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/cognitive-load-theory", "title":"Cognitive Load Theory (EEF)", "icon":"fas fa-memory", "pill":"free", "audiences":["all"],
                     "desc":"EEF's free plain-English summary of cognitive load theory — what it means for lesson design, worked examples and practice."},
                    {"href":"https://www.simplypsychology.org/vygotsky.html", "title":"Vygotsky & the ZPD", "icon":"fas fa-people-arrows", "pill":"free", "audiences":["all"],
                     "desc":"Clear free guide to Vygotsky's Zone of Proximal Development — how scaffolding and social learning shape the classroom."},
                    {"href":"https://www.edutopia.org/article/what-makes-great-teaching/", "title":"What Makes Great Teaching", "icon":"fas fa-award", "pill":"free", "audiences":["all"],
                     "desc":"Edutopia's evidence-based synthesis of what the research says makes teaching effective — accessible and practical."},
                    {"href":"https://pz.harvard.edu/projects/visible-thinking", "title":"Visible Thinking (Harvard)", "icon":"fas fa-eye", "pill":"free", "audiences":["all"],
                     "desc":"Harvard PZ's free Visible Thinking project — routines that make student thinking visible, discussable and transferable."},
                ],
            },
            # ── F3. Both Together ──
            {
                "key": "together", "color": "#10b981", "color_bg": "#ecfdf5",
                "icon": "fas fa-circle-nodes",
                "chip_label": "Both Together",
                "label": "Theory Meets Practice",
                "title": "Both Together — Theory Meets Practice",
                "desc": "Resources that bridge research and classroom reality — frameworks, videos of real teaching and toolkits that work because they're grounded in both.",
                "cards": [
                    {"href":"https://www.teachingchannel.com", "title":"Teaching Channel", "icon":"fas fa-video", "pill":"freemium", "audiences":["all"], "top":True,
                     "desc":"Video library of real classroom teaching — watch expert teachers in action across subjects and age groups, with reflection guides."},
                    {"href":"https://www.pblworks.org/what-is-pbl", "title":"PBL Works (Buck Institute)", "icon":"fas fa-project-diagram", "pill":"free", "audiences":["all"],
                     "desc":"The gold-standard Project-Based Learning resource — free starter kits, rubrics and project ideas grounded in research."},
                    {"href":"https://www.designthinkingforeducators.com/", "title":"Design Thinking for Edu", "icon":"fas fa-pencil-ruler", "pill":"free", "audiences":["all"],
                     "desc":"IDEO's free design-thinking toolkit for educators — a human-centred process for solving classroom and school challenges."},
                    {"href":"https://eleducation.org/resources", "title":"EL Education Resources", "icon":"fas fa-mountain-sun", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free Expeditionary Learning resources — character, crew and mastery-based assessment grounded in decades of school evidence."},
                    {"href":"https://www.edutopia.org/research-based-learning", "title":"Edutopia Research Hub", "icon":"fas fa-microscope", "pill":"free", "audiences":["all"],
                     "desc":"Free research-to-practice articles with classroom video — each strategy explained, evidenced and shown in action."},
                    {"href":"https://www.visiblelearningplus.com/resources", "title":"Visible Learning Resources", "icon":"fas fa-chart-bar", "pill":"freemium", "audiences":["all"],
                     "desc":"Hattie's 250+ effect sizes with free downloads — understand which teaching practices have the highest impact and why."},
                    {"href":"https://pz.harvard.edu/projects/visible-thinking", "title":"Making Learning Visible", "icon":"fas fa-magnifying-glass", "pill":"free", "audiences":["all"],
                     "desc":"Harvard PZ's free protocols for making student understanding visible — thinking routines with classroom application guides."},
                    {"href":"https://www.responsiveteaching.org", "title":"Responsive Teaching", "icon":"fas fa-arrows-left-right-to-line", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free framework for adapting instruction in real time — bridging formative assessment theory with moment-to-moment practice."},
                    {"href":"https://www.edx.org/learn/learning-design", "title":"Learning Design (edX)", "icon":"fas fa-school", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free-audit courses on designing for learning — environment design, engagement theory and instructional systems thinking."},
                    {"href":"https://www.teachervision.com", "title":"TeacherVision", "icon":"fas fa-glasses", "pill":"freemium", "audiences":["all"],
                     "desc":"Research-backed lesson plans, strategies and classroom management tools — all connected to learning standards."},
                    {"href":"https://www.edweek.org/teaching-learning", "title":"Education Week Teaching", "icon":"fas fa-newspaper", "pill":"freemium", "audiences":["all"],
                     "desc":"Research-informed teaching articles, webinars and guides from the US's leading education journalism outlet."},
                    {"href":"https://www.scienceoflearningcenter.org", "title":"Science of Learning Center", "icon":"fas fa-atom", "pill":"free", "audiences":["all"],
                     "desc":"Free practical resources from NSF-funded learning-science research — translating neuroscience into classroom action."},
                ],
            },
            # ── F4. Where to Start ──
            {
                "key": "fund_start", "color": "#f59e0b", "color_bg": "#fffbeb",
                "icon": "fas fa-map-signs",
                "chip_label": "Where to Start",
                "label": "Your Starting Point",
                "title": "Where to Start",
                "desc": "New to exploring your practice? Start here — a curated path through the most important free resources for developing teachers.",
                "cards": [
                    {"href":"https://edu.google.com/teacher-center/", "title":"Google for Education", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Free Teacher Center with training, certification paths and classroom integration guides — the most-used free teacher platform."},
                    {"href":"https://learn.microsoft.com/en-us/training/educator-center/", "title":"Microsoft Educator Center", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free badge-earning learning paths on Teams, OneNote, Minecraft Edu and AI tools for classrooms."},
                    {"href":"https://www.edutopia.org/professional-development", "title":"Edutopia PD Hub", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Curated free PD articles, videos and guides on every aspect of teaching — the best single free starting point for teachers."},
                    {"href":"https://www.teachthought.com/professional-development/", "title":"TeachThought PD", "icon":"fas fa-road", "pill":"free", "audiences":["all"],
                     "desc":"Free structured paths into modern pedagogy — where to go first, what to read and how to grow your teaching practice."},
                    {"href":"https://tntp.org/resources/", "title":"TNTP Free Resources", "icon":"fas fa-toolbox", "pill":"free", "audiences":["all"],
                     "desc":"The New Teacher Project's free guides — what great teaching looks like and how to build toward it systematically."},
                    {"href":"https://www.nea.org/professional-excellence", "title":"NEA Professional Excellence", "icon":"fas fa-medal", "pill":"free-signup", "audiences":["all"],
                     "desc":"National Education Association's free PD portal — courses, webinars and resources for every career stage."},
                    {"href":"https://www.ascd.org/topics/new-teachers", "title":"ASCD New Teachers", "icon":"fas fa-door-open", "pill":"free", "audiences":["all"],
                     "desc":"Free curated ASCD resources specifically for early-career teachers — classroom setup, mindset, and first-year survival."},
                    {"href":"https://www.tes.com/en/for-teachers/new-teachers", "title":"TES New Teacher Hub", "icon":"fas fa-star-of-life", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free lesson resources, advice articles and community forums tailored to teachers in their first years of teaching."},
                    {"href":"https://teachertoolkit.co.uk/for-new-teachers/", "title":"TeacherToolkit New Teachers", "icon":"fas fa-wrench", "pill":"free", "audiences":["all"],
                     "desc":"Free practical starters for new teachers — workload management, marking strategies and dealing with your first class."},
                    {"href":"https://www.khanacademy.org/teacher-essentials", "title":"Khan Academy Essentials", "icon":"fas fa-leaf", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Khan Academy teacher onboarding — set up your classroom, assign work and track student progress from day one."},
                    {"href":"https://education.apple.com", "title":"Apple Teacher Program", "icon":"fab fa-apple", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free self-paced Apple Teacher recognition program — earn badges for iPad, Mac and creative learning skills."},
                    {"href":"https://chartered.college/membership/", "title":"Chartered College (Free Tier)", "icon":"fas fa-certificate", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free associate membership gives access to the Impact journal, research digests and community forum for UK teachers."},
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # 🟢 BEFORE CLASS — Design & Preparation
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "before", "color": "#22c55e", "color_bg": "#f0fdf4",
        "icon": "fas fa-pen-ruler",
        "tab_label": "Before Class", "tag": "Design & Preparation",
        "subclusters": [
            # ── 1. Lesson planning & curriculum ──
            {
                "key": "planning", "color": "#2563eb", "color_bg": "#eff6ff",
                "icon": "fas fa-chalkboard",
                "chip_label": "Lesson Planning & Curriculum",
                "label": "Curriculum & Lesson Design",
                "title": "Lesson Planning & Curriculum",
                "desc": "Build standards-aligned units, weekly plans and ready-to-teach lessons in minutes — free templates and full open curricula.",
                "cards": [
                    {"href":"https://www.commonlit.org", "title":"CommonLit", "icon":"fas fa-book-open", "pill":"free-signup", "audiences":["primary","secondary"], "top":True,
                     "desc":"Free standards-aligned reading lessons grades 3-12 — texts, questions, assessments and full ELA units, all in one place."},
                    {"href":"https://www.engageny.org", "title":"EngageNY (NY State)", "icon":"fas fa-school-flag", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free PK-12 ELA and math curriculum from New York State — full year-long modules, teacher guides and student workbooks."},
                    {"href":"https://www.openupresources.org", "title":"Open Up Resources", "icon":"fas fa-book", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free top-rated open math and ELA curricula (Illustrative Math, EL Education ELA) — full year-long courses written by leading teams."},
                    {"href":"https://www.share-my-lesson.com", "title":"Share My Lesson", "icon":"fas fa-share-nodes", "pill":"free-signup", "audiences":["all"],
                     "desc":"Over 420,000 free lesson plans, activities and units shared by AFT teachers — searchable by subject, grade and standard."},
                    {"href":"https://www.teacherspayteachers.com/Browse/Price-Range/Free", "title":"TPT Free Resources", "icon":"fas fa-folder-open", "pill":"free-signup", "audiences":["all"],
                     "desc":"The free section of Teachers Pay Teachers — millions of teacher-made worksheets, units and printables filtered to the no-cost track."},
                    {"href":"https://www.tes.com/teaching-resources/hub/free", "title":"Tes Free Lessons", "icon":"fas fa-folder-tree", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free UK-curriculum-aligned resources from the world's largest teaching community — full schemes of work and lesson packs."},
                    {"href":"https://www.bbc.co.uk/teach", "title":"BBC Teach", "icon":"fas fa-tv", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free curriculum-mapped video clips and ready-made lessons from the BBC — strong on history, science and English literature."},
                    {"href":"https://www.commoncurriculum.com", "title":"Common Curriculum", "icon":"fas fa-calendar-week", "pill":"freemium", "audiences":["all"],
                     "desc":"Free digital lesson planner with weekly grid view, standards alignment and unit views — solid free tier for individual teachers."},
                    {"href":"https://planbook.com", "title":"Planbook", "icon":"fas fa-calendar-days", "pill":"freemium", "audiences":["all"],
                     "desc":"Lightweight digital lesson planner — free 30-day trial then a low-cost paid tier; weekly grid view loved by classroom teachers."},
                    {"href":"https://betterlesson.com", "title":"BetterLesson", "icon":"fas fa-lightbulb", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free library of master-teacher lesson plans across K-12 subjects — vetted, classroom-tested and aligned to Common Core."},
                    {"href":"https://www.pbslearningmedia.org", "title":"PBS LearningMedia", "icon":"fas fa-tower-broadcast", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free PBS K-12 digital media library — 100,000+ standards-aligned videos, lessons and interactives across every subject."},
                    {"href":"https://www.ck12.org", "title":"CK-12 Foundation", "icon":"fas fa-book-bookmark", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free customisable digital textbooks (FlexBooks) for every K-12 subject — adapt content, add notes, share with students."},
                    {"href":"https://www.gynzy.com/en/", "title":"Gynzy", "icon":"fas fa-chalkboard-user", "pill":"freemium", "audiences":["primary"],
                     "desc":"Interactive whiteboard lessons and ready-made activities for primary teachers — large free library of drag-and-drop lesson tools."},
                    {"href":"https://www.lessonup.com/en", "title":"LessonUp", "icon":"fas fa-presentation-screen", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Build interactive lessons combining slides, quizzes, video and polls — free tier with thousands of teacher-shared lessons."},
                ],
            },
            # ── 2. Creating materials ──
            {
                "key": "materials", "color": "#dc2626", "color_bg": "#fef2f2",
                "icon": "fas fa-pen-ruler",
                "chip_label": "Creating Materials",
                "label": "Worksheets, Slides, Video & Visuals",
                "title": "Creating Materials — Slides, Worksheets, Video & Visuals",
                "desc": "Make polished worksheets, slides, infographics and videos in minutes — no design skills required, all free for teachers.",
                "cards": [
                    {"href":"https://www.canva.com/education/", "title":"Canva for Education", "icon":"fas fa-palette", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Full Canva Pro free for verified K-12 teachers — worksheets, posters, videos, slides, animations and infographics in one studio."},
                    {"href":"https://www.adobe.com/express/education", "title":"Adobe Express Edu", "icon":"fab fa-adobe", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free Adobe Express for K-12 teachers and students — flyers, social posts, videos and AI image generation for any lesson."},
                    {"href":"https://www.flaticon.com/teachers", "title":"Flaticon for Teachers", "icon":"fas fa-icons", "pill":"freemium", "audiences":["all"],
                     "desc":"Millions of free icons for worksheets and slides — full attribution required, but excellent quality and variety."},
                    {"href":"https://unsplash.com", "title":"Unsplash", "icon":"fas fa-camera", "pill":"free", "audiences":["all"],
                     "desc":"Free high-quality photos for any classroom material — no attribution required, fully usable in lesson resources."},
                    {"href":"https://pixabay.com", "title":"Pixabay", "icon":"fas fa-image", "pill":"free", "audiences":["all"],
                     "desc":"Free photos, videos, illustrations and music — fully usable in classroom materials with no attribution required."},
                    {"href":"https://www.pexels.com", "title":"Pexels", "icon":"fas fa-camera-retro", "pill":"free", "audiences":["all"],
                     "desc":"Free stock photos and videos curated by a community of photographers — high quality, fully free for educational use."},
                    {"href":"https://wordart.com", "title":"WordArt", "icon":"fas fa-font", "pill":"freemium", "audiences":["all"],
                     "desc":"Free word-cloud generator — turn vocabulary lists into engaging visuals for displays, starters and quick formative checks."},
                    {"href":"https://worksheetworks.com", "title":"WorksheetWorks", "icon":"fas fa-file-pdf", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free configurable maths and reading worksheets — generate, print, regenerate. No login required, decades-old teacher classic."},
                    {"href":"https://www.educandy.com", "title":"Educandy", "icon":"fas fa-candy-cane", "pill":"free-signup", "audiences":["primary"],
                     "desc":"Generate up to 7 different game styles from one wordlist — free for teachers, perfect for vocab and revision activities."},
                    {"href":"https://www.animaker.com/education", "title":"Animaker for Edu", "icon":"fas fa-film", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Animated video creator for explainer videos — free tier supports 5-minute videos with extensive character library."},
                    {"href":"https://www.audacityteam.org", "title":"Audacity", "icon":"fas fa-microphone", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source audio editor — record podcasts, edit audio for lessons, work with any sound file format."},
                    {"href":"https://www.openshot.org", "title":"OpenShot Video Editor", "icon":"fas fa-video", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free open-source desktop video editor — straightforward enough for student projects, powerful for teacher tutorials."},
                    {"href":"https://h5p.org", "title":"H5P", "icon":"fas fa-cubes", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source authoring tool — 50+ interactive content types (quizzes, branching scenarios, drag-the-words) embeddable anywhere."},
                ],
            },
            # ── 3. Selecting & adapting resources ──
            {
                "key": "adapting", "color": "#f59e0b", "color_bg": "#fffbeb",
                "icon": "fas fa-arrows-split-up-and-left",
                "chip_label": "Selecting & Adapting",
                "label": "Levelling, Accessibility & SEN",
                "title": "Selecting & Adapting Resources",
                "desc": "Pick existing resources and adapt them for every learner — text levellers, leveled libraries, accessibility readers and dyslexia-friendly tools.",
                "cards": [
                    {"href":"https://diffit.me", "title":"Diffit for Teachers", "icon":"fas fa-arrows-split-up-and-left", "pill":"freemium", "audiences":["primary","secondary","sen"], "top":True,
                     "desc":"Adapt any text to any reading level instantly — leveled passages, vocabulary and questions; the gold-standard differentiation AI."},
                    {"href":"https://newsela.com", "title":"Newsela", "icon":"fas fa-newspaper", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free leveled news articles — every article available at 5 reading levels for differentiated content access across subjects."},
                    {"href":"https://www.readworks.org", "title":"ReadWorks", "icon":"fas fa-book-reader", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free comprehensive K-12 reading library — thousands of leveled passages and paired texts with comprehension questions."},
                    {"href":"https://rewordify.com", "title":"Rewordify", "icon":"fas fa-book-bookmark", "pill":"free", "audiences":["primary","secondary","sen"],
                     "desc":"Paste any difficult text — Rewordify replaces hard words with simpler ones inline, with definitions on hover."},
                    {"href":"https://www.twinkl.com", "title":"Twinkl Resources", "icon":"fas fa-star", "pill":"freemium", "audiences":["prek","primary","secondary"],
                     "desc":"Free curriculum-aligned printables across age ranges and abilities — adapt any worksheet up or down a level in seconds."},
                    {"href":"https://education.microsoft.com/en-us/resource/35d33d56", "title":"Immersive Reader", "icon":"fab fa-microsoft", "pill":"free", "audiences":["all"],
                     "desc":"Free Microsoft tool — read any text aloud with line focus, syllable splitting, picture dictionary and 60+ languages."},
                    {"href":"https://www.naturalreaders.com", "title":"Natural Reader", "icon":"fas fa-volume-high", "pill":"freemium", "audiences":["all"],
                     "desc":"Free text-to-speech with natural voices — read PDFs, web pages and Word docs aloud to support reading access."},
                    {"href":"https://www.opendyslexic.org", "title":"OpenDyslexic Font", "icon":"fas fa-font", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source dyslexia-friendly typeface — designed to reduce letter rotation, includes browser extensions."},
                    {"href":"https://www.texthelp.com/products/read-and-write-education/", "title":"Read&Write (Texthelp)", "icon":"fas fa-book", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free 30-day trial of the leading literacy support tool — text-to-speech, predictive typing, picture dictionary."},
                    {"href":"https://www.bookshare.org", "title":"Bookshare", "icon":"fas fa-book-open-reader", "pill":"free-signup", "audiences":["primary","secondary","sen"],
                     "desc":"Free for US students with reading disabilities — over 1.4M accessible audiobooks and ebooks with text-to-speech."},
                    {"href":"https://www.cast.org/our-work/about-udl.html", "title":"CAST UDL Guidelines", "icon":"fas fa-universal-access", "pill":"free", "audiences":["all"],
                     "desc":"The definitive Universal Design for Learning framework — free guidelines, examples and implementation tools for every classroom."},
                    {"href":"https://www.understood.org", "title":"Understood.org", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Comprehensive free resources for teachers and parents on dyslexia, ADHD and learning differences — research-backed and practical."},
                ],
            },
            # ── 4. Setting objectives & standards alignment ──
            {
                "key": "objectives", "color": "#6366f1", "color_bg": "#eef2ff",
                "icon": "fas fa-bullseye",
                "chip_label": "Objectives & Standards Alignment",
                "label": "Standards, Frameworks & Lesson Frames",
                "title": "Setting Objectives & Standards Alignment",
                "desc": "Anchor every lesson to clear standards and learning goals — official frameworks, taxonomies and OER alignment libraries.",
                "cards": [
                    {"href":"https://achievethecore.org", "title":"Achieve the Core", "icon":"fas fa-bullseye", "pill":"free", "audiences":["primary","secondary"], "top":True,
                     "desc":"Free Common Core-aligned tasks, lessons and unit planning tools from the team that wrote the standards — ELA and math."},
                    {"href":"https://www.thecorestandards.org", "title":"Common Core State Standards", "icon":"fas fa-list-check", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"The official Common Core State Standards portal — full English Language Arts and Math standards, free and searchable."},
                    {"href":"https://www.nextgenscience.org", "title":"NGSS Hub", "icon":"fas fa-microscope", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free Next Generation Science Standards portal — performance expectations, evidence statements and exemplar lessons."},
                    {"href":"https://www.iste.org/standards/iste-standards-for-teachers", "title":"ISTE Standards for Educators", "icon":"fas fa-award", "pill":"free", "audiences":["all"],
                     "desc":"Free ISTE Standards portal — framework for innovative teaching with technology, with descriptors and rubrics."},
                    {"href":"https://wida.wisc.edu/teach/standards", "title":"WIDA Standards Framework", "icon":"fas fa-language", "pill":"free", "audiences":["all"],
                     "desc":"Free WIDA English Language Development Standards — used in 40+ US states for ELL/EAL planning and assessment."},
                    {"href":"https://www.authenticeducation.org/ubd/ubd.lasso", "title":"UbD Backward Design", "icon":"fas fa-compass-drafting", "pill":"free", "audiences":["all"],
                     "desc":"Wiggins & McTighe's Understanding by Design templates and articles — backward design from learning goals to evidence to instruction."},
                    {"href":"https://www.bloomstaxonomy.net", "title":"Bloom's Taxonomy Wheel", "icon":"fas fa-circle-nodes", "pill":"free", "audiences":["all"],
                     "desc":"Free reference and verb wheels for Bloom's revised taxonomy — write higher-order objectives in seconds with action verbs."},
                    {"href":"https://pamhook.com/solo-taxonomy/", "title":"SOLO Taxonomy", "icon":"fas fa-layer-group", "pill":"free", "audiences":["all"],
                     "desc":"Pam Hook's free SOLO Taxonomy resources — the Structure of Observed Learning Outcomes for clear progression in objectives."},
                    {"href":"https://eduprotocols.com", "title":"EduProtocols", "icon":"fas fa-puzzle-piece", "pill":"free", "audiences":["all"],
                     "desc":"Free reusable lesson frames tied to learning targets — Cyber Sandwich, Iron Chef, Worst Preso Ever and more."},
                    {"href":"https://www.curriki.org", "title":"Curriki", "icon":"fas fa-graduation-cap", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free open educational resources library — 50,000+ free lessons, units and full courses tagged by standard."},
                    {"href":"https://www.oercommons.org", "title":"OER Commons", "icon":"fas fa-globe", "pill":"free-signup", "audiences":["primary","secondary","higher"],
                     "desc":"Largest free OER repository — 70,000+ resources tagged by Common Core, NGSS and state standards, plus quality reviews."},
                    {"href":"https://www.visiblelearningmetax.com", "title":"Visible Learning MetaX", "icon":"fas fa-chart-line", "pill":"free-signup", "audiences":["all"],
                     "desc":"John Hattie's free database of 320+ influences on student achievement, ranked by effect size — pick high-impact strategies."},
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # 🔵 DURING CLASS — Teaching & Learning
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "during", "color": "#3b82f6", "color_bg": "#eff6ff",
        "icon": "fas fa-school",
        "tab_label": "During Class", "tag": "Teaching & Learning",
        "subclusters": [
            # ── 5. Explaining content ──
            {
                "key": "explaining", "color": "#f97316", "color_bg": "#fff7ed",
                "icon": "fas fa-display",
                "chip_label": "Explaining Content",
                "label": "Slides, Video & Screencast",
                "title": "Explaining Content — Slides, Video & Screencast",
                "desc": "Deliver lessons that stick — interactive slides, embedded video questions, screencasts and curated mini-lectures.",
                "cards": [
                    {"href":"https://nearpod.com", "title":"Nearpod", "icon":"fas fa-display", "pill":"freemium", "audiences":["primary","secondary"], "top":True,
                     "desc":"Interactive slide lessons with built-in polls, quizzes, drawings and VR — free Silver tier covers most classroom needs."},
                    {"href":"https://edpuzzle.com", "title":"Edpuzzle", "icon":"fas fa-circle-play", "pill":"freemium", "audiences":["primary","secondary","higher"],
                     "desc":"Embed questions and notes directly in any video — free for teachers (up to 20 stored videos) with full analytics."},
                    {"href":"https://www.loom.com/education", "title":"Loom for Education", "icon":"fas fa-video", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free unlimited screen-recording for verified teachers — record flipped-classroom videos with built-in viewer engagement."},
                    {"href":"https://screenpal.com", "title":"ScreenPal Edu", "icon":"fas fa-camera-retro", "pill":"freemium", "audiences":["all"],
                     "desc":"Free screencasting tool with classroom-friendly captions and easy hosting — used by millions of educators."},
                    {"href":"https://classroomscreen.com", "title":"Classroomscreen", "icon":"fas fa-tv", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free all-in-one classroom display — timer, random name picker, traffic light, work-symbols and noise meter on one screen."},
                    {"href":"https://wakelet.com", "title":"Wakelet", "icon":"fas fa-bookmark", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free curation tool — organise videos, articles, tweets and student work into shareable collections for any lesson."},
                    {"href":"https://www.genial.ly", "title":"Genially", "icon":"fas fa-shapes", "pill":"freemium", "audiences":["all"],
                     "desc":"Create interactive presentations, escape rooms and infographics — free tier with hundreds of educator templates."},
                    {"href":"https://www.thinglink.com", "title":"ThingLink", "icon":"fas fa-link", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Add hotspots to images and videos with text, audio and links — free Basic tier covers small-class use."},
                    {"href":"https://www.khanacademy.org", "title":"Khan Academy", "icon":"fas fa-play-circle", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free K-12 video lessons with mastery practice — calculus, biology, history, finance and SAT prep, all free forever."},
                    {"href":"https://ed.ted.com", "title":"TED-Ed", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free animated educational videos with built-in lesson tools — Think, Dig Deeper and Discuss prompts attached to every clip."},
                    {"href":"https://thecrashcourse.com", "title":"Crash Course", "icon":"fas fa-bolt", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free YouTube lecture series across history, science, literature and economics — exceptional production, hosted by experts."},
                    {"href":"https://www.brainpop.com", "title":"BrainPOP", "icon":"fas fa-brain", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Animated curriculum-aligned videos with quizzes and concept maps across every K-12 subject — free trial plus free topics."},
                    {"href":"https://www.prowise.com/en/", "title":"Prowise Present", "icon":"fas fa-display", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free interactive lesson software for any touchscreen — slides, tools and templates for whole-class teaching, English UI."},
                ],
            },
            # ── 6. Interactive activities (STEM + Art/Music) ──
            {
                "key": "interactive", "color": "#0891b2", "color_bg": "#ecfeff",
                "icon": "fas fa-flask",
                "chip_label": "Interactive Activities",
                "label": "STEM Labs, Art & Music Studios",
                "title": "Interactive Activities — STEM Labs, Art & Music Studios",
                "desc": "Hands-on simulations, virtual labs and creative studios — let students DO physics, biology, music and art in your lesson.",
                "cards": [
                    {"href":"https://phet.colorado.edu", "title":"PhET Simulations", "icon":"fas fa-atom", "pill":"free", "audiences":["primary","secondary","higher"], "top":True,
                     "desc":"University of Colorado's 160+ free interactive physics, chem, biology and maths simulations — translated into 90+ languages."},
                    {"href":"https://www.geogebra.org", "title":"GeoGebra", "icon":"fas fa-shapes", "pill":"free-signup", "audiences":["primary","secondary","higher"],
                     "desc":"Free dynamic mathematics — geometry, algebra, calculus, 3D and statistics in one tool. Used by 100M+ students worldwide."},
                    {"href":"https://www.tinkercad.com", "title":"Tinkercad", "icon":"fas fa-cube", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free 3D design, electronics simulation and code-blocks platform from Autodesk — built specifically for classrooms."},
                    {"href":"https://scratch.mit.edu", "title":"Scratch", "icon":"fas fa-cat", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"MIT's free block-based coding platform — 100M+ projects worldwide, the entry point to programming for kids 8+."},
                    {"href":"https://musiclab.chromeexperiments.com", "title":"Chrome Music Lab", "icon":"fas fa-music", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free playful music experiments from Google — Song Maker, Rhythm, Spectrogram, Kandinsky. Zero login, runs in any browser."},
                    {"href":"https://musescore.org", "title":"MuseScore", "icon":"fas fa-music", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free open-source music notation software — write, play and print sheet music for any instrument or ensemble."},
                    {"href":"https://www.soundtrap.com/edu", "title":"Soundtrap for Education", "icon":"fas fa-headphones", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Browser-based collaborative DAW — record podcasts and music with students in real time. Generous free tier."},
                    {"href":"https://krita.org", "title":"Krita", "icon":"fas fa-brush", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free open-source professional digital painting and animation software — comprehensive brush engine, used in art schools."},
                    {"href":"https://stellarium-web.org", "title":"Stellarium Web", "icon":"fas fa-star", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free planetarium in your browser — show students the night sky from anywhere, any time, perfect for astronomy lessons."},
                    {"href":"https://www.desmos.com", "title":"Desmos", "icon":"fas fa-chart-line", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free graphing calculator and classroom activities — the gold standard for visualising functions in maths classes."},
                    {"href":"https://code.org", "title":"Code.org", "icon":"fas fa-code", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free K-12 computer science curriculum — Hour of Code, full year courses, AI Lab and Dance Party. Used by 60M+ students."},
                    {"href":"https://earth.google.com", "title":"Google Earth", "icon":"fas fa-earth-americas", "pill":"free", "audiences":["primary","secondary","higher"],
                     "desc":"Free 3D globe in the browser — Voyager tours of culture, history and science; build your own placemarks for any geography lesson."},
                ],
            },
            # ── 7. Collaboration (Visual thinking & boards) ──
            {
                "key": "collab", "color": "#a855f7", "color_bg": "#faf5ff",
                "icon": "fas fa-diagram-project",
                "chip_label": "Collaboration",
                "label": "Whiteboards, Mind Maps & Brainstorming",
                "title": "Collaboration — Visual Thinking & Brainstorming",
                "desc": "Make student thinking visible — collaborative whiteboards, mind maps, sticky-note boards and concept-mapping tools.",
                "cards": [
                    {"href":"https://miro.com/education", "title":"Miro for Education", "icon":"fas fa-chalkboard-user", "pill":"freemium", "audiences":["secondary","higher"], "top":True,
                     "desc":"Free Education plan with unlimited boards and templates for verified teachers — the most-loved visual collaboration tool."},
                    {"href":"https://www.figma.com/education/", "title":"FigJam Education", "icon":"fab fa-figma", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free FigJam for educators and students — collaborative whiteboarding with delightful templates and engagement features."},
                    {"href":"https://padlet.com", "title":"Padlet", "icon":"fas fa-thumbtack", "pill":"freemium", "audiences":["all"],
                     "desc":"Free 'sticky note wall' for posting ideas, photos, links and audio — three free padlets and beloved by teachers."},
                    {"href":"https://excalidraw.com", "title":"Excalidraw", "icon":"fas fa-pencil", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source virtual whiteboard with hand-drawn aesthetic — instant collaboration, no login required, end-to-end encrypted."},
                    {"href":"https://whiteboard.fi", "title":"Whiteboard.fi", "icon":"fas fa-chalkboard", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free instant teacher dashboard — every student gets their own whiteboard, the teacher sees them all live."},
                    {"href":"https://www.mindmeister.com", "title":"MindMeister", "icon":"fas fa-brain", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free 3 mind maps with collaboration — ideal for class concept mapping and student group projects."},
                    {"href":"https://www.coggle.it", "title":"Coggle", "icon":"fas fa-circle-nodes", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free unlimited public mind maps — clean visual hierarchy, real-time collaboration and image embedding."},
                    {"href":"https://lucidspark.com/education", "title":"Lucidspark Edu", "icon":"fas fa-bolt-lightning", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free education tier of Lucid's whiteboard — sticky notes, voting and infinite canvas for class brainstorming."},
                    {"href":"https://www.mural.co/use-cases/education", "title":"Mural Education", "icon":"fas fa-paint-brush", "pill":"freemium", "audiences":["higher"],
                     "desc":"Free for verified higher-ed students and instructors — collaborative visual workspace for design thinking and group work."},
                    {"href":"https://app.diagrams.net", "title":"Diagrams.net (draw.io)", "icon":"fas fa-sitemap", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free open-source diagramming — flowcharts, ER diagrams, UML, mind maps. Saves directly to Drive or OneDrive."},
                    {"href":"https://www.openboard.ch", "title":"OpenBoard", "icon":"fas fa-display", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source interactive whiteboard for schools — works with any beamer or interactive screen, no subscription."},
                    {"href":"https://whiteboard.microsoft.com", "title":"Microsoft Whiteboard", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free collaborative whiteboard inside Teams and Office — sticky notes, ink, images and templates with auto-save."},
                    {"href":"https://www.popplet.com", "title":"Popplet", "icon":"fas fa-diagram-project", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Simple visual mind-mapping for classrooms — students brainstorm, organise ideas and share boards in real time."},
                ],
            },
            # ── 8. Classroom instruction (live response/polls) ──
            {
                "key": "instruction", "color": "#ec4899", "color_bg": "#fdf2f8",
                "icon": "fas fa-bell-concierge",
                "chip_label": "Live Instruction",
                "label": "Polls, Quizzes & Response Systems",
                "title": "Classroom Instruction — Live Response & Polls",
                "desc": "Run engaging live activities — game-show quizzes, polls, exit tickets and response systems that keep every student active.",
                "cards": [
                    {"href":"https://kahoot.com", "title":"Kahoot!", "icon":"fas fa-gamepad", "pill":"freemium", "audiences":["all"], "top":True,
                     "desc":"The classic game-show quiz format — free Basic tier supports up to 40 players for live formative assessment."},
                    {"href":"https://quizizz.com", "title":"Quizizz", "icon":"fas fa-dice", "pill":"freemium", "audiences":["all"],
                     "desc":"Self-paced AI-powered quizzes and lessons — free for teachers with extensive question banks and live mode."},
                    {"href":"https://www.mentimeter.com", "title":"Mentimeter", "icon":"fas fa-chart-bar", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Live polls, word clouds and Q&A from the audience — free tier covers small-class formative assessment perfectly."},
                    {"href":"https://peardeck.com", "title":"Pear Deck", "icon":"fas fa-pear", "pill":"freemium", "audiences":["primary","secondary","higher"],
                     "desc":"Add interactive questions to Google Slides or PowerPoint — free tier supports the most-loved formative-assessment formats."},
                    {"href":"https://www.slido.com", "title":"Slido", "icon":"fas fa-comment-dots", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Live polls, surveys and Q&A overlay for any meeting or class — free tier supports up to 100 participants."},
                    {"href":"https://socrative.com", "title":"Socrative", "icon":"fas fa-bell-concierge", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Quick quizzes, exit tickets and Space Race game — free for up to 50 students per room."},
                    {"href":"https://plickers.com", "title":"Plickers", "icon":"fas fa-qrcode", "pill":"freemium", "audiences":["primary"],
                     "desc":"Paper QR cards plus phone scan — formative assessment with zero student devices, free for up to 60 cards."},
                    {"href":"https://wordwall.net", "title":"Wordwall", "icon":"fas fa-th", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Templated quiz games — match-up, anagram, gameshow — generate any activity from one wordlist; free up to 5 saved."},
                    {"href":"https://www.formative.com", "title":"Formative", "icon":"fas fa-clipboard-list", "pill":"freemium", "audiences":["primary","secondary","higher"],
                     "desc":"See student responses live as they type — drawings, equations, paragraphs. Free Bronze tier covers core formative use."},
                    {"href":"https://answergarden.ch", "title":"AnswerGarden", "icon":"fas fa-seedling", "pill":"free", "audiences":["all"],
                     "desc":"Free instant word-cloud feedback tool — pose a question, students answer in 20 chars or less, watch responses grow live."},
                    {"href":"https://pollev.com", "title":"Poll Everywhere", "icon":"fas fa-square-poll-vertical", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Live audience-response polls embedded in PowerPoint or Google Slides — free tier supports up to 25 responses per poll."},
                    {"href":"https://www.blooket.com", "title":"Blooket", "icon":"fas fa-gamepad", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Game-based quiz platform massively popular with teens — host live games or assign self-paced sets. Free tier covers full classroom use."},
                    {"href":"https://www.bookwidgets.com", "title":"BookWidgets", "icon":"fas fa-puzzle-piece", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"40+ ready-made interactive widget templates — quizzes, crosswords, exit tickets, randomness wheels — auto-graded, embeddable."},
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # 🟣 AFTER CLASS — Assessment & Follow-up
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "after", "color": "#a855f7", "color_bg": "#faf5ff",
        "icon": "fas fa-clipboard-check",
        "tab_label": "After Class", "tag": "Assessment & Follow-up",
        "subclusters": [
            # ── 9. Grading ──
            {
                "key": "grading", "color": "#475569", "color_bg": "#f1f5f9",
                "icon": "fas fa-clipboard-check",
                "chip_label": "Grading",
                "label": "LMS, Gradebooks & Auto-grading",
                "title": "Grading — LMS, Gradebooks & Auto-marking",
                "desc": "Cut grading time in half — free LMS gradebooks, auto-marked quizzes, rubric tools and standards-based reporting.",
                "cards": [
                    {"href":"https://classroom.google.com", "title":"Google Classroom", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"The default free LMS for millions of teachers — assignments, grading, communication and file sharing in one place."},
                    {"href":"https://www.microsoft.com/en-us/education/products/teams", "title":"Microsoft Teams Edu", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free education plan with classes, assignments, OneNote class notebooks and 1TB OneDrive storage per student."},
                    {"href":"https://www.canvas.net", "title":"Canvas Free for Teacher", "icon":"fas fa-paint-roller", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free version of the leading higher-ed LMS — full assignments, grading and rubrics for individual teachers."},
                    {"href":"https://moodle.com/getstarted", "title":"Moodle", "icon":"fas fa-graduation-cap", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free open-source LMS used by universities worldwide — self-host or use MoodleCloud free tier for small classes."},
                    {"href":"https://www.schoology.com/k-12/basic", "title":"Schoology Basic", "icon":"fas fa-school", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free LMS for individual teachers — assignments, gradebook, quizzes and parent communication in one platform."},
                    {"href":"https://www.jupitered.com", "title":"Jupiter Grades", "icon":"fas fa-table", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Standards-based gradebook trusted by 5M+ students — free for solo teachers; paid plans for schools and districts."},
                    {"href":"https://www.engradepro.com", "title":"Engrade", "icon":"fas fa-chart-line", "pill":"freemium", "audiences":["secondary"],
                     "desc":"Web-based gradebook and reporting tool — free tier covers classroom needs; integrates with major LMS systems."},
                    {"href":"https://forms.google.com", "title":"Google Forms (Quiz)", "icon":"fas fa-pen-to-square", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free auto-graded quizzes with instant feedback and analytics — the workhorse for grading in Google Classroom."},
                    {"href":"https://forms.office.com", "title":"Microsoft Forms (Quiz)", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free quizzes and surveys with auto-grading and branching logic — included with any Microsoft account."},
                    {"href":"https://rubistar.4teachers.org", "title":"RubiStar", "icon":"fas fa-table-cells", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free rubric maker — pick a template, customise the criteria, print or save. Used by teachers for over 20 years."},
                    {"href":"https://www.rcampus.com/indexrubric.cfm", "title":"iRubric (RCampus)", "icon":"fas fa-list-check", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free rubric builder and gallery with thousands of teacher-shared templates — adapt and reuse with attribution."},
                    {"href":"https://progressbook.com", "title":"ProgressBook", "icon":"fas fa-book", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"K-12 student information system with gradebook and standards-based reporting — free trial; many districts offer access."},
                ],
            },
            # ── 10. Feedback (writing/grammar/feedback) ──
            {
                "key": "feedback", "color": "#06b6d4", "color_bg": "#ecfeff",
                "icon": "fas fa-pen-fancy",
                "chip_label": "Feedback",
                "label": "Writing, Grammar & Voice Notes",
                "title": "Feedback — Writing Help, Grammar & Comments",
                "desc": "Give meaningful, fast feedback on student writing — grammar checkers, voice notes, rubric tools and writing-help platforms.",
                "cards": [
                    {"href":"https://www.grammarly.com/edu", "title":"Grammarly for Edu", "icon":"fas fa-spell-check", "pill":"freemium", "audiences":["secondary","higher"], "top":True,
                     "desc":"Free Grammarly tier — grammar, clarity and tone suggestions for student writing in browser, Word and Docs."},
                    {"href":"https://hemingwayapp.com", "title":"Hemingway Editor", "icon":"fas fa-pen-fancy", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free web app that highlights complex sentences, passive voice and adverbs — clearer student writing in seconds."},
                    {"href":"https://www.kamiapp.com", "title":"Kami", "icon":"fas fa-file-pdf", "pill":"freemium", "audiences":["primary","secondary","higher"],
                     "desc":"Free PDF and document annotation — drop comments, voice notes, drawings and stickers right on student work in seconds."},
                    {"href":"https://corubrics-en.tecnocentres.org", "title":"CoRubrics", "icon":"fas fa-table-cells", "pill":"free", "audiences":["all"],
                     "desc":"Free Google Sheets add-on for self-, peer- and teacher-rubric assessment — generates personalised feedback per student."},
                    {"href":"https://www.brisk.ai", "title":"Brisk Teaching", "icon":"fas fa-rocket", "pill":"freemium", "audiences":["all"],
                     "desc":"Free Chrome extension that adds an AI sidebar to Google Docs and Slides — instant feedback, leveling and rubrics."},
                    {"href":"https://www.justmote.me", "title":"Mote Voice Notes", "icon":"fas fa-microphone-lines", "pill":"freemium", "audiences":["all"],
                     "desc":"Free voice-comment Chrome extension for Google Docs, Slides and Classroom — leave 30-sec audio feedback in seconds."},
                    {"href":"https://kaizena.com", "title":"Kaizena", "icon":"fas fa-volume-high", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free voice-feedback tool for student writing — link rubric tags to comments and reuse common feedback across students."},
                    {"href":"https://floop.app", "title":"Floop", "icon":"fas fa-comments", "pill":"freemium", "audiences":["secondary"],
                     "desc":"Lightning-fast feedback for math and science — students upload work, teachers comment with reusable feedback bank."},
                    {"href":"https://joezoo.com", "title":"JoeZoo", "icon":"fas fa-pen", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free Google Docs add-on for batch writing feedback — drop in standard comments from a teacher feedback library."},
                    {"href":"https://www.noredink.com", "title":"NoRedInk", "icon":"fas fa-pen-clip", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Adaptive grammar and writing practice — free for teachers with auto-graded feedback on every student response."},
                    {"href":"https://www.quill.org", "title":"Quill.org", "icon":"fas fa-feather", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free interactive writing and grammar tools — adaptive sentence-level practice for grades 3-12 with instant feedback."},
                    {"href":"https://prowritingaid.com", "title":"ProWritingAid", "icon":"fas fa-pen-nib", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free style editor with 25+ writing reports — grammar, readability, transitions and overused words for student writing."},
                ],
            },
            # ── 11. Reflection ──
            {
                "key": "reflection", "color": "#84cc16", "color_bg": "#f7fee7",
                "icon": "fas fa-rotate-left",
                "chip_label": "Reflection",
                "label": "Exit Tickets, Journals & Portfolios",
                "title": "Reflection — Exit Tickets, Journals & Portfolios",
                "desc": "Help students think about their learning — video reflections, journals, exit tickets, e-books and portfolios.",
                "cards": [
                    {"href":"https://www.flip.com", "title":"Flip (Flipgrid)", "icon":"fas fa-video", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"Free Microsoft video discussion platform — students post short video reflections; teachers create safe topics in seconds."},
                    {"href":"https://web.seesaw.me", "title":"Seesaw", "icon":"fas fa-leaf", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Student-created digital portfolios with parent visibility — free Seesaw for Schools tier covers single classrooms."},
                    {"href":"https://bookcreator.com", "title":"Book Creator", "icon":"fas fa-book", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Students design e-books for reflection or projects — free for one library of 40 books per teacher."},
                    {"href":"https://www.onenote.com/classnotebook", "title":"OneNote Class Notebook", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Microsoft tool — every student gets a private notebook for journals and reflections, plus a shared content library and collaboration space."},
                    {"href":"https://reflect.microsoft.com", "title":"Microsoft Reflect", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free emotional check-in tool inside Teams for Education — students choose feelings; teachers see class wellbeing trends."},
                    {"href":"https://app.edu.buncee.com", "title":"Buncee", "icon":"fas fa-bolt-lightning", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free creation platform for student stories and digital reflections — combine text, voice, video and animation in one canvas."},
                    {"href":"https://www.notion.so/product/notion-for-education", "title":"Notion for Education", "icon":"fas fa-pen-fancy", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free Plus plan for verified educators — student reflection journals, learning logs and project portfolios in one workspace."},
                    {"href":"https://edublogs.org", "title":"Edublogs", "icon":"fas fa-blog", "pill":"freemium", "audiences":["primary","secondary","higher"],
                     "desc":"Free WordPress-powered class and student blogs — great for reflection journals, with teacher moderation built in."},
                    {"href":"https://www.sutori.com", "title":"Sutori", "icon":"fas fa-timeline", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free interactive timelines and stories for student-built reflections and project narratives — collaborative and printable."},
                    {"href":"https://yoteachapp.com", "title":"Yo Teach!", "icon":"fas fa-comments", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"Free anonymous backchannel for class discussion — collect quick text and image reflections from any device."},
                    {"href":"https://storymaps.arcgis.com", "title":"Esri Story Maps", "icon":"fas fa-map", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free map-based stories from ArcGIS — students reflect on a topic by combining text, photos, video and geographic data."},
                    {"href":"https://www.swivl.com/recap", "title":"Recap by Swivl", "icon":"fas fa-record-vinyl", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free video Q&A reflection tool — pose a question, students record short responses, the class reviews together."},
                ],
            },
            # ── 12. Tracking progress (homework & family) ──
            {
                "key": "tracking", "color": "#10b981", "color_bg": "#ecfdf5",
                "icon": "fas fa-house-user",
                "chip_label": "Tracking Progress",
                "label": "Homework, Practice & Family Learning",
                "title": "Tracking Progress — Homework & Family Learning",
                "desc": "Recommend safe, effective resources to families — homework support, revision tools and at-home learning for parents.",
                "cards": [
                    {"href":"https://www.khanacademy.org/parents", "title":"Khan Academy Parents", "icon":"fas fa-house-chimney", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Free parent dashboards across all subjects K-12 — track progress, see strengths and weak spots, share with teachers."},
                    {"href":"https://www.bbc.co.uk/bitesize/parents", "title":"BBC Bitesize Parents", "icon":"fas fa-graduation-cap", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free UK-curriculum revision aligned to year groups — guides for parents on supporting homework and exam prep."},
                    {"href":"https://www.ixl.com/membership/family", "title":"IXL Family", "icon":"fas fa-chart-pie", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free 10 questions/day across 8,500 skills — comprehensive K-12 practice with parent-friendly progress reports."},
                    {"href":"https://www.commonsense.org/education/parent-resources", "title":"Common Sense Parents", "icon":"fas fa-shield-halved", "pill":"free", "audiences":["all"],
                     "desc":"Free reviews of every kids' app, game and movie — help families make smart media choices supported by research."},
                    {"href":"https://www.abcmouse.com", "title":"ABCmouse", "icon":"fas fa-mouse", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Free 30-day trial of the comprehensive early-learning curriculum — phonics, maths, art and music for ages 2-8."},
                    {"href":"https://readingeggs.com", "title":"Reading Eggs", "icon":"fas fa-egg", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Free trial of the leading early-reading program — phonics, sight words and decodable books for ages 3-13."},
                    {"href":"https://www.mathletics.com", "title":"Mathletics", "icon":"fas fa-calculator", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Adaptive maths practice for K-12 with worldwide tournaments — free home trials and parent progress tracking."},
                    {"href":"https://www.prodigygame.com/parents/", "title":"Prodigy Math Parents", "icon":"fas fa-dragon", "pill":"freemium", "audiences":["primary"],
                     "desc":"Free game-based maths for grades 1-8 — kids battle monsters by answering questions, parents see weekly reports."},
                    {"href":"https://senecalearning.com", "title":"Seneca Learning", "icon":"fas fa-mountain", "pill":"freemium", "audiences":["secondary"],
                     "desc":"Free GCSE/A-level revision platform for UK families — interactive courses based on cognitive-science research."},
                    {"href":"https://quizlet.com", "title":"Quizlet for Families", "icon":"fas fa-rectangle-list", "pill":"freemium", "audiences":["all"],
                     "desc":"Free flashcards and study modes — over half a billion study sets covering every subject and exam syllabus."},
                    {"href":"https://www.twinkl.com/parents", "title":"Twinkl Parents", "icon":"fas fa-star", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Free curriculum-aligned printables, worksheets and activity packs — UK-based but used in 200+ countries."},
                    {"href":"https://www.getepic.com", "title":"Epic! for Families", "icon":"fas fa-book-open-reader", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"40,000+ children's ebooks, audiobooks and videos — free for verified educators, low-cost for families."},
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # 🟠 SUPPORTING — Across All Phases
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "supp", "color": "#f59e0b", "color_bg": "#fffbeb",
        "icon": "fas fa-gear",
        "tab_label": "Supporting", "tag": "Across All Phases",
        "subclusters": [
            # ── 13. Classroom management ──
            {
                "key": "mgmt", "color": "#14b8a6", "color_bg": "#f0fdfa",
                "icon": "fas fa-school",
                "chip_label": "Classroom Management",
                "label": "Behaviour, Routines & Engagement",
                "title": "Classroom Management & Engagement",
                "desc": "Build positive routines, recognise good behaviour, and run smooth daily classroom systems — free tools that respect students.",
                "cards": [
                    {"href":"https://www.classdojo.com", "title":"ClassDojo", "icon":"fas fa-medal", "pill":"free-signup", "audiences":["prek","primary","sen"], "top":True,
                     "desc":"Build a positive classroom culture — points, parent messages and student portfolios. Free for all teachers and parents."},
                    {"href":"https://www.classcraft.com", "title":"Classcraft", "icon":"fas fa-dragon", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Gamified classroom-management platform — students earn XP and powers for good behaviour. Generous free tier."},
                    {"href":"https://www.too-noisy.com", "title":"Too Noisy", "icon":"fas fa-volume-high", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Visual classroom noise meter that animates with sound levels — free Lite version is loved by primary teachers."},
                    {"href":"https://www.bouncyballs.org", "title":"Bouncy Balls", "icon":"fas fa-circle", "pill":"free", "audiences":["prek","primary"],
                     "desc":"Free fun visual noise meter — bouncing balls react to classroom volume. Perfect background tool during group work."},
                    {"href":"https://wheelofnames.com", "title":"Wheel of Names", "icon":"fas fa-arrows-rotate", "pill":"free", "audiences":["all"],
                     "desc":"Free random name picker — spin the wheel to choose students fairly. Saved lists, custom colours and ad-free."},
                    {"href":"https://www.online-stopwatch.com/classroom-timers/", "title":"Classroom Timers", "icon":"fas fa-stopwatch", "pill":"free", "audiences":["all"],
                     "desc":"Free fun classroom timers — bombs, candles, race cars — keep activities on schedule with engaging visuals."},
                    {"href":"https://www.classcharts.com", "title":"Class Charts", "icon":"fas fa-table-list", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free seating-plan generator with behaviour-points tracking — used in thousands of UK schools, free for individual teachers."},
                    {"href":"https://www.pbisrewards.com", "title":"PBIS Rewards", "icon":"fas fa-trophy", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Schoolwide positive-behaviour reinforcement platform — free trial; many free PBIS resources available on the site."},
                    {"href":"https://www.gonoodle.com", "title":"GoNoodle", "icon":"fas fa-person-running", "pill":"free-signup", "audiences":["prek","primary"],
                     "desc":"Free movement and mindfulness videos — short brain breaks proven to refocus K-5 students mid-lesson."},
                    {"href":"https://www.responsiveclassroom.org/free-resources/", "title":"Responsive Classroom", "icon":"fas fa-handshake", "pill":"free", "audiences":["primary"],
                     "desc":"Free morning meeting greetings, activities and message ideas — research-based social-emotional classroom community."},
                    {"href":"https://www.casel.org/casel-cares/", "title":"CASEL CARES", "icon":"fas fa-heart", "pill":"free", "audiences":["all"],
                     "desc":"Free SEL resources and weekly webinars from the gold-standard org for social-emotional learning research."},
                    {"href":"https://teachertoolkit.co.uk", "title":"TeacherToolkit", "icon":"fas fa-toolbox", "pill":"free", "audiences":["all"],
                     "desc":"The UK's most-followed teaching blog — free practical strategies for behaviour, engagement and routines."},
                    {"href":"https://teacherspick.com", "title":"Teacher's Pick", "icon":"fas fa-hand-pointer", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free random student picker — fair, animated name selection that keeps cold-calling unpredictable and engaging for the whole class."},
                ],
            },
            # ── 14. Communication ──
            {
                "key": "comms", "color": "#22c55e", "color_bg": "#f0fdf4",
                "icon": "fas fa-comments",
                "chip_label": "Communication",
                "label": "Parents, Students & Newsletters",
                "title": "Communication — Parents, Students & Translation",
                "desc": "Reach every family in their language and on their terms — secure messaging, newsletters and translation tools.",
                "cards": [
                    {"href":"https://www.remind.com", "title":"Remind", "icon":"fas fa-bell", "pill":"freemium", "audiences":["all"], "top":True,
                     "desc":"Send safe one-way messages to students and parents — free tier covers daily classroom announcements with auto-translate."},
                    {"href":"https://talkingpts.org", "title":"TalkingPoints", "icon":"fas fa-language", "pill":"free", "audiences":["primary","secondary","sen"],
                     "desc":"Free family-engagement messenger that auto-translates between teachers and parents in 100+ languages."},
                    {"href":"https://www.classdojo.com/messaging/", "title":"ClassDojo Messenger", "icon":"fas fa-envelope", "pill":"free-signup", "audiences":["prek","primary","sen"],
                     "desc":"Free secure parent messaging with photo and video sharing — translates messages automatically into 35+ languages."},
                    {"href":"https://www.bloomz.com", "title":"Bloomz", "icon":"fas fa-flower", "pill":"freemium", "audiences":["prek","primary"],
                     "desc":"Free parent communication and conference scheduler — early-childhood and elementary favourite with photo sharing."},
                    {"href":"https://www.smore.com", "title":"Smore Newsletters", "icon":"fas fa-newspaper", "pill":"freemium", "audiences":["all"],
                     "desc":"Beautiful drag-and-drop classroom newsletters — free tier supports 5 newsletters with full design tools."},
                    {"href":"https://www.parentsquare.com", "title":"ParentSquare", "icon":"fas fa-square-parking", "pill":"freemium", "audiences":["all"],
                     "desc":"Whole-school communication platform with auto-translation — many districts offer free teacher accounts via school plans."},
                    {"href":"https://translate.google.com", "title":"Google Translate", "icon":"fas fa-globe", "pill":"free", "audiences":["all"],
                     "desc":"Free instant translation in 130+ languages — text, photos, conversations and documents for parent communication."},
                    {"href":"https://www.deepl.com/translator", "title":"DeepL Translator", "icon":"fas fa-globe", "pill":"freemium", "audiences":["all"],
                     "desc":"Higher-quality translations than Google for European languages — free tier covers most teacher communication needs."},
                    {"href":"https://www.microsoft.com/en-us/translator/education/", "title":"Microsoft Translator", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free real-time conversation translation for parent meetings — phones speak each language and the app subtitles live."},
                    {"href":"https://www.signupgenius.com", "title":"SignUpGenius", "icon":"fas fa-calendar-check", "pill":"freemium", "audiences":["all"],
                     "desc":"Free conference scheduling, class-party signups and volunteer rosters — the parent-coordination workhorse."},
                    {"href":"https://mailchimp.com", "title":"Mailchimp Free", "icon":"fas fa-envelope-open", "pill":"freemium", "audiences":["all"],
                     "desc":"Free email tier (up to 500 contacts) — great for class newsletters, parent updates and PTA communication."},
                    {"href":"https://sway.cloud.microsoft", "title":"Microsoft Sway", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Microsoft tool for interactive newsletters and reports — beautiful templates, autoflow design, no formatting needed."},
                ],
            },
            # ── 15. Administration & file storage ──
            {
                "key": "admin", "color": "#71717a", "color_bg": "#f4f4f5",
                "icon": "fas fa-folder-tree",
                "chip_label": "Administration & Files",
                "label": "Cloud Storage, Tasks & Calendars",
                "title": "Administration & File Storage",
                "desc": "Cut down on paperwork — free cloud storage, kanban task boards, scheduling tools and team workspaces.",
                "cards": [
                    {"href":"https://drive.google.com", "title":"Google Drive", "icon":"fab fa-google-drive", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Free 15GB cloud storage with Docs, Sheets and Slides — share lesson materials and collect assignments seamlessly."},
                    {"href":"https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage", "title":"Microsoft OneDrive", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free 5GB cloud storage with Office Online — Word, Excel, PowerPoint with full classroom-friendly sharing controls."},
                    {"href":"https://www.dropbox.com/edu", "title":"Dropbox for Education", "icon":"fab fa-dropbox", "pill":"freemium", "audiences":["all"],
                     "desc":"Free 2GB tier with classroom sharing and collaborative folders — discounted education plans available."},
                    {"href":"https://www.box.com/industries/education", "title":"Box for Education", "icon":"fas fa-box", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free 10GB storage tier — strong on permissions and audit trails, popular with district admin and higher-ed."},
                    {"href":"https://www.notion.so/product/notion-for-education", "title":"Notion for Education", "icon":"fas fa-pen-fancy", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free Plus plan for verified educators — wikis, lesson notes, student trackers and collaborative classroom hubs."},
                    {"href":"https://airtable.com/solutions/education", "title":"Airtable for Edu", "icon":"fas fa-table", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free flexible database — great for tracking student data, IEP goals, project portfolios and curriculum maps."},
                    {"href":"https://trello.com/teachers", "title":"Trello for Teachers", "icon":"fab fa-trello", "pill":"freemium", "audiences":["all"],
                     "desc":"Free kanban boards — track lesson planning, student projects, school committees and personal teacher to-dos."},
                    {"href":"https://asana.com/education", "title":"Asana for Edu", "icon":"fas fa-list-check", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free for teams up to 15 people — manage school improvement projects, department workflows and admin tasks."},
                    {"href":"https://calendly.com", "title":"Calendly", "icon":"fas fa-calendar-day", "pill":"freemium", "audiences":["all"],
                     "desc":"Free booking tool — share a link, parents pick a slot for parent-teacher conferences. No more email back-and-forth."},
                    {"href":"https://doodle.com", "title":"Doodle Polls", "icon":"fas fa-square-poll-horizontal", "pill":"freemium", "audiences":["all"],
                     "desc":"Free meeting-time poll for staff and parents — find when everyone can meet without endless email threads."},
                    {"href":"https://slack.com/solutions/education", "title":"Slack for Edu", "icon":"fab fa-slack", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free workspace for staff teams — channels for departments, DMs and integrations with Drive, Calendar and more."},
                    {"href":"https://www.icloud.com", "title":"iCloud (Apple)", "icon":"fab fa-apple", "pill":"freemium", "audiences":["all"],
                     "desc":"Free 5GB Apple cloud storage with Pages, Numbers and Keynote in browser — great for Apple-using classrooms."},
                ],
            },
            # ── 16. Stress Management & Wellbeing ──
            {
                "key": "wellbeing", "color": "#d946ef", "color_bg": "#fdf4ff",
                "icon": "fas fa-heart-pulse",
                "chip_label": "Stress Mgmt & Wellbeing",
                "label": "Mental Health, Mindfulness & Burnout Prevention",
                "title": "Stress Management & Wellbeing",
                "desc": "Look after yourself first — free mental-health, mindfulness and burnout-prevention resources made for educators.",
                "cards": [
                    {"href":"https://www.calm.com/schools", "title":"Calm Schools", "icon":"fas fa-spa", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Calm app's free initiative for K-12 teachers — full app access including sleep stories, meditations and music."},
                    {"href":"https://www.headspace.com/educators", "title":"Headspace for Educators", "icon":"fas fa-cloud", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Headspace Plus for verified K-12 teachers in the US, UK, Canada and Australia — mindfulness and meditation."},
                    {"href":"https://insighttimer.com", "title":"Insight Timer", "icon":"fas fa-stopwatch-20", "pill":"freemium", "audiences":["all"],
                     "desc":"Free meditation app with the largest free library — over 200,000 guided meditations and teacher-specific tracks."},
                    {"href":"https://www.mindful.org", "title":"Mindful.org", "icon":"fas fa-leaf", "pill":"free", "audiences":["all"],
                     "desc":"Free articles, guided practices and research on mindfulness — accessible introduction for stressed teachers."},
                    {"href":"https://greatergood.berkeley.edu/education", "title":"Greater Good in Education", "icon":"fas fa-heart", "pill":"free", "audiences":["all"],
                     "desc":"Berkeley's free science-based SEL resources for teachers — practices for gratitude, kindness and resilience in classrooms."},
                    {"href":"https://www.teacherwellbeing.com.au", "title":"Teacher Wellbeing", "icon":"fas fa-shield-heart", "pill":"free", "audiences":["all"],
                     "desc":"Free podcast and articles by Daniela Falecki — practical wellbeing strategies and burnout prevention for teachers."},
                    {"href":"https://www.educationsupport.org.uk", "title":"Education Support (UK)", "icon":"fas fa-life-ring", "pill":"free", "audiences":["all"],
                     "desc":"UK charity — free 24/7 helpline, counselling and mental-health resources for any teacher, regardless of country."},
                    {"href":"https://www.happyteachersrevolution.org", "title":"Happy Teacher Revolution", "icon":"fas fa-face-smile", "pill":"free", "audiences":["all"],
                     "desc":"Free global movement of teacher mental-health support meetings — 100+ chapters worldwide, online and in-person."},
                    {"href":"https://www.cult-of-pedagogy.com/category/teacher-self-care/", "title":"Cult of Pedagogy: Self-Care", "icon":"fas fa-podcast", "pill":"free", "audiences":["all"],
                     "desc":"Jennifer Gonzalez's free articles and podcast episodes on teacher self-care — practical, honest, no toxic positivity."},
                    {"href":"https://www.dontstresstheteacher.com", "title":"Don't Stress the Teacher", "icon":"fas fa-mug-hot", "pill":"free", "audiences":["all"],
                     "desc":"Free blog with realistic strategies for managing stress, parents and admin — written by classroom teachers."},
                    {"href":"https://www.mhanational.org", "title":"Mental Health America", "icon":"fas fa-brain", "pill":"free", "audiences":["all"],
                     "desc":"Free MHA toolkits — burnout self-screening, evidence-based coping strategies, and crisis support directories."},
                    {"href":"https://moodgym.com.au", "title":"MoodGYM", "icon":"fas fa-dumbbell", "pill":"freemium", "audiences":["all"],
                     "desc":"Free interactive cognitive-behavioural therapy program — proven self-help for stress and low mood, used worldwide."},
                ],
            },
            # ── 18. AI co-pilots ──
            {
                "key": "ai", "color": "#8b5cf6", "color_bg": "#f5f3ff",
                "icon": "fas fa-robot",
                "chip_label": "AI Co-pilots",
                "label": "AI Assistants for Teachers",
                "title": "AI Co-pilots — Cross-Phase Helpers",
                "desc": "Generate lesson plans, rubrics, differentiated worksheets and feedback in seconds — free AI tools that span the whole workflow.",
                "cards": [
                    {"href":"https://magicschool.ai", "title":"MagicSchool", "icon":"fas fa-wand-magic-sparkles", "pill":"freemium", "audiences":["all"], "top":True,
                     "desc":"60+ teacher-built AI tools — lesson plans, IEP goals, rubrics, differentiation and feedback. Generous free tier for educators."},
                    {"href":"https://www.curipod.com", "title":"Curipod", "icon":"fas fa-bolt", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"AI-generated interactive lessons in 30 seconds — slides, polls, drawings and exit tickets, with a strong free plan for teachers."},
                    {"href":"https://www.eduaide.ai", "title":"Eduaide.Ai", "icon":"fas fa-helmet-safety", "pill":"freemium", "audiences":["all"],
                     "desc":"100+ generators for lesson plans, assessments and accommodations — free tier covers most everyday classroom needs."},
                    {"href":"https://www.schoolai.com", "title":"SchoolAI", "icon":"fas fa-user-graduate", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Safe, monitored AI chat 'spaces' for students plus an AI assistant for teachers — generous free tier for K-12."},
                    {"href":"https://claude.ai", "title":"Claude", "icon":"fas fa-comments", "pill":"free-signup", "audiences":["all"],
                     "desc":"Anthropic's flagship AI assistant — exceptional for lesson planning, rubric writing, parent emails and feedback drafting."},
                    {"href":"https://chatgpt.com", "title":"ChatGPT", "icon":"fas fa-brain", "pill":"free-signup", "audiences":["all"],
                     "desc":"OpenAI's free tier covers GPT-4o mini — strong for question generation, summaries and worksheet creation."},
                    {"href":"https://gemini.google.com", "title":"Gemini", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"],
                     "desc":"Google's AI deeply integrated with Docs, Slides and Drive — ideal for teachers already living in Google Workspace."},
                    {"href":"https://copilot.microsoft.com", "title":"Microsoft Copilot", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free AI inside Word, OneNote, PowerPoint — generate lesson outlines, slide decks and student handouts in place."},
                    {"href":"https://notebooklm.google.com", "title":"NotebookLM", "icon":"fas fa-book-open", "pill":"free-signup", "audiences":["all"],
                     "desc":"Upload your textbook chapters and notes — Google's AI answers strictly from your sources, with audio summaries for revision."},
                    {"href":"https://www.anthropic.com/ai-fluency", "title":"AI Fluency Course", "icon":"fas fa-compass", "pill":"free", "audiences":["all"],
                     "desc":"Anthropic's free course on the four core AI competencies — delegation, description, discernment, diligence. Built for educators."},
                    {"href":"https://www.khanmigo.ai", "title":"Khanmigo (Khan Academy)", "icon":"fas fa-leaf", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Khan Academy's free AI tutor for teachers — lesson planning, parent emails and student-Socratic tutoring across K-12 subjects."},
                    {"href":"https://www.perplexity.ai", "title":"Perplexity", "icon":"fas fa-magnifying-glass", "pill":"freemium", "audiences":["all"],
                     "desc":"AI search engine that cites every claim — perfect when teachers need verifiable sources rather than hallucinated answers."},
                    {"href":"https://questionwell.org", "title":"QuestionWell", "icon":"fas fa-circle-question", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Paste any text, get aligned essential questions and learning objectives plus auto-generated quizzes — free unlimited tier."},
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # 🎓 FURTHER DEVELOPMENT — Grow as a Teacher
    # ═══════════════════════════════════════════════════════════════════════
    {
        "key": "furtherdev", "color": "#e11d48", "color_bg": "#fff1f2",
        "icon": "fas fa-user-graduate",
        "tab_label": "Further Development", "tag": "Grow as a Teacher",
        "subclusters": [
            # ── FD1. Where to Start ──
            {
                "key": "fd_start", "color": "#e11d48", "color_bg": "#fff1f2",
                "icon": "fas fa-map-signs",
                "chip_label": "Where to Start",
                "label": "New to CPD? Begin Here",
                "title": "Where to Start with Further Development",
                "desc": "Not sure where to begin your professional development journey? These trusted starting points will help you plan a path that works for you.",
                "cards": [
                    {"href":"https://tdtrust.org/about-tdt/what-makes-great-cpd/", "title":"What Makes Great CPD?", "icon":"fas fa-star", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"Teacher Development Trust's free guide — research on what professional development actually improves teaching and student outcomes."},
                    {"href":"https://learningforward.org/standards/", "title":"Learning Forward Standards", "icon":"fas fa-list-check", "pill":"free", "audiences":["all"],
                     "desc":"The global standards for effective professional learning — a clear framework for evaluating and planning your own CPD."},
                    {"href":"https://www.edutopia.org/professional-development", "title":"Edutopia PD Hub", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Free curated PD articles, videos and guides on every aspect of teaching — the best all-in-one starting point."},
                    {"href":"https://www.teachthought.com/professional-development/", "title":"TeachThought PD Paths", "icon":"fas fa-road", "pill":"free", "audiences":["all"],
                     "desc":"Free structured paths into modern pedagogy — what to read, watch and try as you grow your teaching practice."},
                    {"href":"https://educationendowmentfoundation.org.uk", "title":"EEF Teacher Toolkit", "icon":"fas fa-toolbox", "pill":"free", "audiences":["all"],
                     "desc":"The Education Endowment Foundation's free teacher toolkit — evidence-rated strategies with clear guidance on where to focus."},
                    {"href":"https://tntp.org/resources/", "title":"TNTP Free Resources", "icon":"fas fa-door-open", "pill":"free", "audiences":["all"],
                     "desc":"The New Teacher Project's free guides on what effective teaching looks like and how to build toward it step by step."},
                    {"href":"https://teachertapp.co.uk", "title":"TeacherTapp", "icon":"fas fa-mobile-screen", "pill":"free-signup", "audiences":["all"],
                     "desc":"Weekly 3-question teacher survey + PD resources — see how thousands of colleagues think and benchmark your own practice."},
                    {"href":"https://www.coursera.org/learn/learning-how-to-learn", "title":"Learning How to Learn", "icon":"fas fa-brain", "pill":"free", "audiences":["all"],
                     "desc":"Start with yourself — Barbara Oakley's free MOOC on memory, chunking and focus. Essential before designing learning for others."},
                    {"href":"https://www.reflectivepractice.net/", "title":"Reflective Practice Guide", "icon":"fas fa-mirror", "pill":"free", "audiences":["all"],
                     "desc":"Free introduction to Gibbs' Reflective Cycle and other models — turn your teaching experiences into structured growth."},
                    {"href":"https://www.nea.org/professional-excellence", "title":"NEA Professional Excellence", "icon":"fas fa-medal", "pill":"free-signup", "audiences":["all"],
                     "desc":"National Education Association's free PD portal — courses, webinars and resources mapped to every career stage."},
                    {"href":"https://chartered.college/membership/", "title":"Chartered College (Free Tier)", "icon":"fas fa-certificate", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free associate membership — access the Impact journal, research digests and teaching community for evidence-led teachers."},
                    {"href":"https://www.open.edu/openlearn/education-development", "title":"OpenLearn Education", "icon":"fas fa-globe-europe", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Open University taster courses in education — inclusive teaching, mentoring and school leadership. No entry requirements."},
                ],
            },
            # ── FD2. Free Courses & Certs ──
            {
                "key": "fd_courses", "color": "#0ea5e9", "color_bg": "#f0f9ff",
                "icon": "fas fa-award",
                "chip_label": "Free Courses & Certs",
                "label": "MOOCs, Badges & Certificates",
                "title": "Free Courses & Certifications",
                "desc": "Earn recognised certificates and badges for free — from Coursera, edX, Google, Microsoft, Apple and the Open University.",
                "cards": [
                    {"href":"https://www.coursera.org/browse/social-sciences/education", "title":"Coursera Educator Track", "icon":"fas fa-chalkboard-user", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Audit Stanford, Penn and Johns Hopkins teaching courses for free — paid certificates available but all content is free."},
                    {"href":"https://www.edx.org/learn/teaching", "title":"edX Teaching Courses", "icon":"fas fa-school", "pill":"free-signup", "audiences":["all"],
                     "desc":"Harvard, MIT and HarvardX education courses — free to audit, with optional paid MicroMasters for school leadership."},
                    {"href":"https://www.futurelearn.com/subjects/teaching-courses", "title":"FutureLearn Teaching", "icon":"fas fa-users-between-lines", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free short teaching courses from UK universities — practical pedagogy, EdTech and subject-specific CPD."},
                    {"href":"https://edu.google.com/teacher-center/certifications/", "title":"Google Certified Educator", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free training leading to Level 1 and Level 2 Google Certified Educator exams — globally recognised classroom tech credential."},
                    {"href":"https://learn.microsoft.com/en-us/training/educator-center/", "title":"Microsoft Educator Center", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Microsoft Innovative Educator badges — Teams, OneNote, Minecraft Edu, AI tools and global collaboration."},
                    {"href":"https://education.apple.com", "title":"Apple Teacher Program", "icon":"fab fa-apple", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free self-paced Apple Teacher recognition program — earn Swift badges and classroom creativity credentials."},
                    {"href":"https://alison.com/courses/teaching", "title":"Alison Teaching Certificates", "icon":"fas fa-graduation-cap", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free accredited teaching and education certificates — classroom management, special needs, early childhood and more."},
                    {"href":"https://www.open.edu/openlearn/education-development", "title":"OpenLearn (Open University)", "icon":"fas fa-globe-europe", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free OU courses with statements of participation — inclusive teaching, mentoring, school leadership and digital skills."},
                    {"href":"https://ocw.mit.edu/courses/find-by-topic/", "title":"MIT OpenCourseWare Edu", "icon":"fas fa-university", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"MIT's full course materials freely available — lecture videos, problem sets and teaching notes from real MIT classes."},
                    {"href":"https://learn.saylor.org", "title":"Saylor Academy", "icon":"fas fa-book-open", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free accredited university-level courses — complete full courses and receive transcripts at no cost."},
                    {"href":"https://www.commonsense.org/education/digital-citizenship", "title":"Common Sense Digital Cert", "icon":"fas fa-shield-halved", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Common Sense Educator Certification in digital citizenship — practical and internationally recognised."},
                    {"href":"https://www.iste.org/professional-development", "title":"ISTE Free Resources", "icon":"fas fa-laptop-code", "pill":"freemium", "audiences":["all"],
                     "desc":"Free ISTE webinars, articles and PD from the world's leading EdTech organisation — community membership included."},
                ],
            },
            # ── FD3. Teaching Methods ──
            {
                "key": "fd_methods", "color": "#f59e0b", "color_bg": "#fffbeb",
                "icon": "fas fa-chalkboard-user",
                "chip_label": "Teaching Methods",
                "label": "PBL, Flipped, Inquiry & More",
                "title": "Teaching Methods — How to Teach Better",
                "desc": "Explore proven instructional approaches from project-based to flipped learning — free guides, courses and classroom-ready resources.",
                "cards": [
                    {"href":"https://www.pblworks.org", "title":"PBL Works (Buck Institute)", "icon":"fas fa-project-diagram", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"The gold-standard project-based learning resource — free starter kits, rubrics and project libraries from the global PBL authority."},
                    {"href":"https://flippedlearning.org/resources/", "title":"Flipped Learning Network", "icon":"fas fa-rotate", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free resources on flipped classroom design — how to record, flip and make better use of in-class time for active learning."},
                    {"href":"https://www.nsta.org/inquiry-based-learning", "title":"Inquiry-Based Learning (NSTA)", "icon":"fas fa-magnifying-glass-chart", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"NSTA's free guide to inquiry-based science — how to move from demonstration to student-led investigation."},
                    {"href":"https://www.kaganonline.com/free_articles/", "title":"Kagan Cooperative Learning", "icon":"fas fa-people-group", "pill":"free", "audiences":["all"],
                     "desc":"Free introductory articles on Kagan Structures — Think-Pair-Share, Jigsaw and 200+ cooperative learning techniques."},
                    {"href":"https://www.cast.org/impact/universal-design-for-learning-udl", "title":"UDL (CAST)", "icon":"fas fa-universal-access", "pill":"free", "audiences":["all","sen"],
                     "desc":"Free Universal Design for Learning guidelines — how to design every lesson to work for the full range of learners."},
                    {"href":"https://www.designthinkingforeducators.com/", "title":"Design Thinking for Edu", "icon":"fas fa-pencil-ruler", "pill":"free", "audiences":["all"],
                     "desc":"IDEO's free educator toolkit — apply human-centred design thinking to both classroom challenges and lesson creation."},
                    {"href":"https://pz.harvard.edu/thinking-routines", "title":"Harvard Thinking Routines", "icon":"fas fa-sitemap", "pill":"free", "audiences":["all"],
                     "desc":"Harvard PZ's 30+ thinking routines — structured protocols that deepen student thinking in any subject."},
                    {"href":"https://www.ascd.org/topics/differentiated-instruction", "title":"Differentiation (ASCD)", "icon":"fas fa-arrows-split-up-and-left", "pill":"free", "audiences":["all"],
                     "desc":"Free ASCD resources on differentiated instruction — how to tier tasks, flex grouping and adjust pacing for every learner."},
                    {"href":"https://eleducation.org/resources", "title":"EL Education Methods", "icon":"fas fa-mountain-sun", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free Expeditionary Learning instructional resources — character, habits of work and mastery-based assessment in action."},
                    {"href":"https://www.visiblelearningplus.com/resources", "title":"Visible Learning (Hattie)", "icon":"fas fa-chart-bar", "pill":"freemium", "audiences":["all"],
                     "desc":"250+ effect sizes — discover which teaching methods have the highest impact on student achievement and why."},
                    {"href":"https://www.teachlikeachampion.com/resources/", "title":"Teach Like a Champion", "icon":"fas fa-star", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free video library of classroom techniques — cold call, no opt out, check for understanding and 60+ more strategies."},
                    {"href":"https://www.edutopia.org/teaching-strategies", "title":"Edutopia Teaching Strategies", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Practical how-to articles on every major instructional approach — with classroom video examples and implementation tips."},
                ],
            },
            # ── FD4. Your Subject ──
            {
                "key": "fd_subject", "color": "#10b981", "color_bg": "#ecfdf5",
                "icon": "fas fa-book-bookmark",
                "chip_label": "Your Subject",
                "label": "Deepen Your Subject Knowledge",
                "title": "Your Subject — Deepen Your Knowledge",
                "desc": "Go deeper in your subject area — free resources, enrichment tools and content-specific guidance for maths, literacy, science, humanities and more.",
                "cards": [
                    {"href":"https://nrich.maths.org", "title":"NRICH (Cambridge Maths)", "icon":"fas fa-square-root-variable", "pill":"free", "audiences":["primary","secondary"], "top":True,
                     "desc":"Cambridge's free maths enrichment tasks — rich problems that develop reasoning, not just calculation. Searchable by age and topic."},
                    {"href":"https://www.readingrockets.org", "title":"Reading Rockets", "icon":"fas fa-rocket", "pill":"free", "audiences":["prek","primary"],
                     "desc":"Free literacy teaching resources — reading strategies, phonics guidance, fluency tools and family engagement resources."},
                    {"href":"https://phet.colorado.edu", "title":"PhET Simulations", "icon":"fas fa-atom", "pill":"free", "audiences":["primary","secondary","higher"],
                     "desc":"University of Colorado's free interactive science and maths simulations — teacher guides for every simulation included."},
                    {"href":"https://www.nextgenscience.org/resources", "title":"NGSS Resources", "icon":"fas fa-flask", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free Next Generation Science Standards implementation resources — storyline units, phenomena and three-dimensional teaching guides."},
                    {"href":"https://education.nationalgeographic.org/resource/resource-library-educator", "title":"National Geographic Education", "icon":"fas fa-globe-americas", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free geography, science and history lessons from National Geographic — maps, videos, articles and teacher guides."},
                    {"href":"https://www.commonlit.org", "title":"CommonLit ELA", "icon":"fas fa-book-open", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free ELA platform for teachers — standards-aligned texts, discussion questions and assessments for grades 3–12."},
                    {"href":"https://www.teachit.co.uk", "title":"Teachit English", "icon":"fas fa-pen-nib", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Thousands of free English teaching resources — poetry, drama, creative writing and exam prep for secondary English teachers."},
                    {"href":"https://www.historytoday.com/education", "title":"History Today Teaching", "icon":"fas fa-landmark", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free history teaching resources from the UK's leading history magazine — articles, source documents and lesson ideas."},
                    {"href":"https://www.rsc.org/learn-chemistry/resource/teacher-resources", "title":"RSC Teacher Resources", "icon":"fas fa-vial", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free chemistry teaching resources from the Royal Society of Chemistry — lesson plans, CPD and practical guides."},
                    {"href":"https://mathpickle.com", "title":"MathPickle", "icon":"fas fa-dice", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free challenging maths puzzles and unsolved problems for K-12 — designed to create beautiful struggle and deep thinking."},
                    {"href":"https://ed.ted.com", "title":"TED-Ed Lessons", "icon":"fas fa-tv", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Curated TED-Ed animated lessons across every subject — free lesson planning tools, discussion guides and quizzes."},
                    {"href":"https://www.pobble.com", "title":"Pobble (Writing)", "icon":"fas fa-feather-pointed", "pill":"freemium", "audiences":["primary"],
                     "desc":"Free writing inspiration photos and stimulus — use real published pupil work as models to raise writing standards."},
                ],
            },
            # ── FD5. Lead & Mentor ──
            {
                "key": "fd_lead", "color": "#6366f1", "color_bg": "#eef2ff",
                "icon": "fas fa-user-tie",
                "chip_label": "Lead & Mentor",
                "label": "Instructional Coaching & Teacher Leadership",
                "title": "Lead & Mentor — Become a Lead Teacher",
                "desc": "Move into leadership, coaching and mentoring — free resources for teachers who want to support colleagues and grow their school's practice.",
                "cards": [
                    {"href":"https://www.instructionalcoaching.com/resources/", "title":"Instructional Coaching Group", "icon":"fas fa-user-tie", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"Jim Knight's free resources on the impact cycle — a research-backed framework for teacher coaching and self-improvement."},
                    {"href":"https://newteachercenter.org/approach/mentoring/", "title":"New Teacher Center Mentoring", "icon":"fas fa-handshake", "pill":"free", "audiences":["all"],
                     "desc":"Free mentoring resources from NTC — how to structure mentoring conversations, observe effectively and give useful feedback."},
                    {"href":"https://www.ascd.org/topics/teacher-leadership", "title":"ASCD Teacher Leadership", "icon":"fas fa-sitemap", "pill":"free", "audiences":["all"],
                     "desc":"Free ASCD resources on teacher leadership — how to lead from the classroom without a formal title."},
                    {"href":"https://www.edutopia.org/topic/teacher-coaching", "title":"Edutopia Coaching Hub", "icon":"fas fa-comments", "pill":"free", "audiences":["all"],
                     "desc":"Free articles and videos on instructional coaching — peer observation, feedback cycles and building a coaching culture."},
                    {"href":"https://www.leadingeducators.org/resources", "title":"Leading Educators", "icon":"fas fa-users-gear", "pill":"free", "audiences":["all"],
                     "desc":"Free resources on building a professional learning community — how teacher leaders drive school-wide improvement."},
                    {"href":"https://www.nbpts.org/national-board-certification/", "title":"National Board Certification", "icon":"fas fa-certificate", "pill":"free-signup", "audiences":["all"],
                     "desc":"National Board for Professional Teaching Standards — free preparation resources for the gold-standard teacher credential."},
                    {"href":"https://learningforward.org/standards/", "title":"Learning Forward", "icon":"fas fa-arrow-up-right-dots", "pill":"free", "audiences":["all"],
                     "desc":"Free standards for professional learning — how to design and lead CPD that actually improves teaching and outcomes."},
                    {"href":"https://www.teachlikeachampion.com/resources/", "title":"TLAC for Leaders", "icon":"fas fa-binoculars", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Teach Like a Champion resources for instructional leaders — observation frameworks, feedback tools and coaching videos."},
                    {"href":"https://www.teacherfirst.com/resources", "title":"TeacherFirst Resources", "icon":"fas fa-seedling", "pill":"free", "audiences":["all"],
                     "desc":"Free resources for educators taking on leadership — curriculum mapping, collaborative planning and community building."},
                    {"href":"https://www.teachertoolkit.co.uk/leadership/", "title":"TeacherToolkit Leadership", "icon":"fas fa-chart-gantt", "pill":"free", "audiences":["all"],
                     "desc":"Free middle-leadership guides — managing upwards, leading a team, workload management and holding difficult conversations."},
                    {"href":"https://www.edweek.org/leadership", "title":"EdWeek Leadership", "icon":"fas fa-newspaper", "pill":"freemium", "audiences":["all"],
                     "desc":"Education Week's free leadership resources — research, case studies and policy analysis for teacher leaders and heads."},
                    {"href":"https://www.iste.org/iste-standards/iste-standards-for-education-leaders", "title":"ISTE Leadership Standards", "icon":"fas fa-laptop-code", "pill":"freemium", "audiences":["all"],
                     "desc":"Free ISTE standards framework for EdTech leaders — a roadmap for leading digital learning in any school or district."},
                ],
            },
            # ── FD6. Evidence & Insights ──
            {
                "key": "fd_evidence", "color": "#475569", "color_bg": "#f1f5f9",
                "icon": "fas fa-microscope",
                "chip_label": "Evidence & Insights",
                "label": "Research Made Useful for Teachers",
                "title": "Evidence & Insights — What the Research Shows",
                "desc": "Access the best education research in plain English — evidence-rated strategies, key findings and research communities built for busy teachers.",
                "cards": [
                    {"href":"https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit", "title":"EEF Teaching Toolkit", "icon":"fas fa-toolbox", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"The gold standard — free evidence ratings for 50+ teaching strategies, with effect size, cost and implementation guidance."},
                    {"href":"https://www.visiblelearningplus.com/content/250-influences-student-achievement", "title":"Visible Learning (Hattie)", "icon":"fas fa-chart-bar", "pill":"freemium", "audiences":["all"],
                     "desc":"Hattie's 250+ effect sizes on student achievement — understand which strategies work and which are education myths."},
                    {"href":"https://researched.org.uk", "title":"researchED", "icon":"fas fa-flask", "pill":"free", "audiences":["all"],
                     "desc":"Free conference talks, blog posts and a global community dedicated to improving research literacy in education."},
                    {"href":"https://ies.ed.gov/ncee/wwc/", "title":"What Works Clearinghouse", "icon":"fas fa-check-double", "pill":"free", "audiences":["all"],
                     "desc":"US Dept of Education's free reviews of education interventions — rigorous, unbiased evidence ratings for programmes and practices."},
                    {"href":"https://www.learningscientists.org/research-summaries", "title":"The Learning Scientists", "icon":"fas fa-book-open", "pill":"free", "audiences":["all"],
                     "desc":"Free evidence-based study strategy summaries — spaced practice, retrieval, interleaving and more, explained for teachers."},
                    {"href":"https://www.danielwillingham.com/articles", "title":"Daniel Willingham", "icon":"fas fa-brain", "pill":"free", "audiences":["all"],
                     "desc":"Cognitive scientist's free articles on why students think and learn the way they do — directly applicable to lesson design."},
                    {"href":"https://www.nfer.ac.uk/research/", "title":"NFER Research", "icon":"fas fa-chart-line", "pill":"free", "audiences":["all"],
                     "desc":"Free NFER research reports and summaries — independent, rigorous UK education research on teaching, wellbeing and leadership."},
                    {"href":"https://www.brookings.edu/topics/education/", "title":"Brookings Education", "icon":"fas fa-building-columns", "pill":"free", "audiences":["all"],
                     "desc":"Free Brookings Institution education research — evidence-based policy analysis and teacher-facing research digests."},
                    {"href":"https://www.rand.org/topics/education.html", "title":"RAND Education Research", "icon":"fas fa-scroll", "pill":"free", "audiences":["all"],
                     "desc":"Free RAND research on teacher effectiveness, curriculum and education systems — rigorous, peer-reviewed and free to access."},
                    {"href":"https://www.edutopia.org/research-evidence", "title":"Edutopia Research", "icon":"fas fa-magnifying-glass", "pill":"free", "audiences":["all"],
                     "desc":"Research translated into classroom practice — each article clearly states the evidence base and implementation steps."},
                    {"href":"https://marzanoresources.com/resources", "title":"Marzano Research", "icon":"fas fa-list-ol", "pill":"freemium", "audiences":["all"],
                     "desc":"Free Marzano resources on instructional strategies — nine high-yield strategies grounded in 35 years of classroom research."},
                    {"href":"https://ies.ed.gov", "title":"Institute of Education Sciences", "icon":"fas fa-landmark", "pill":"free", "audiences":["all"],
                     "desc":"US government's free education research hub — ERIC database, practice guides and What Works Clearinghouse all in one place."},
                ],
            },
            # ── FD7. Teacher Communities ──
            {
                "key": "fd_community", "color": "#22c55e", "color_bg": "#f0fdf4",
                "icon": "fas fa-people-group",
                "chip_label": "Teacher Communities",
                "label": "Forums, Groups & Professional Networks",
                "title": "Teacher Communities — Find Your People",
                "desc": "Connect with teachers around the world — free forums, social communities, subject networks and live events where great teaching ideas spread.",
                "cards": [
                    {"href":"https://teachertapp.co.uk", "title":"TeacherTapp", "icon":"fas fa-mobile-screen-button", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Daily 3-question teacher survey + weekly PD content — see how 10,000+ colleagues respond and benchmark your own views."},
                    {"href":"https://www.tes.com/en/community", "title":"TES Community", "icon":"fas fa-comments", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free forums for every subject and age range — resource sharing, advice threads and career discussions from a global teacher community."},
                    {"href":"https://x.com/hashtag/EduTwitter", "title":"X / EduTwitter", "icon":"fab fa-x-twitter", "pill":"free", "audiences":["all"],
                     "desc":"The world's largest informal teacher PLN — #EduTwitter, #EduChat and hundreds of subject hashtags connect educators globally."},
                    {"href":"https://www.reddit.com/r/Teachers/", "title":"Reddit r/Teachers", "icon":"fab fa-reddit", "pill":"free", "audiences":["all"],
                     "desc":"Anonymous, honest teacher discussion — real talk on workload, behaviour, admin and what actually works in classrooms."},
                    {"href":"https://researched.org.uk/community/", "title":"researchED Community", "icon":"fas fa-flask", "pill":"free", "audiences":["all"],
                     "desc":"Free global community of evidence-minded teachers — annual conferences, regional events and online discussions."},
                    {"href":"https://www.teachmeet.net", "title":"TeachMeet", "icon":"fas fa-microphone", "pill":"free", "audiences":["all"],
                     "desc":"Free informal teacher unconferences — 7-minute and 2-minute teacher-to-teacher shares, held locally and online worldwide."},
                    {"href":"https://edu.google.com/teacher-center/google-educator-groups/", "title":"Google Educator Groups", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"],
                     "desc":"Local and online Google Educator Groups in 100+ countries — professional learning, events and peer support for Google-using teachers."},
                    {"href":"https://educationblog.microsoft.com/en-us/community", "title":"Microsoft Educator Community", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Microsoft educator community — share lessons, earn badges and connect with innovators using Microsoft tools in education."},
                    {"href":"https://www.edutopia.org/community", "title":"Edutopia Community", "icon":"fas fa-globe", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Edutopia blogging and discussion community — share your teaching story and read what's working in classrooms worldwide."},
                    {"href":"https://www.nea.org/about-nea", "title":"NEA Member Network", "icon":"fas fa-people-roof", "pill":"free-signup", "audiences":["all"],
                     "desc":"National Education Association's free member network — professional connections, advocacy tools and peer support for US teachers."},
                    {"href":"https://www.linkedin.com/groups/4929842/", "title":"LinkedIn Educators", "icon":"fab fa-linkedin", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free LinkedIn educator groups — professional networking, career development and thought leadership in education."},
                    {"href":"https://www.iste.org/connect", "title":"ISTE Connect", "icon":"fas fa-wifi", "pill":"freemium", "audiences":["all"],
                     "desc":"ISTE's educator network — free community spaces, special interest groups and discussions on EdTech and innovative learning."},
                ],
            },
        ],
    },
]

# ---------------- Sanity asserts ----------------
assert len(PHASES) == 6, f"Expected 6 phases, got {len(PHASES)}"
all_subs = []
for p in PHASES:
    for s in p["subclusters"]:
        assert len(s["cards"]) >= 12, f"Sub-cluster {s['key']} has {len(s['cards'])} cards, expected >=12"
        all_subs.append(s)
expected_subs = 4 + 4 + 4 + 4 + 5 + 7
assert len(all_subs) == expected_subs, f"Expected {expected_subs} sub-clusters, got {len(all_subs)}"
TOTAL_CARDS = sum(len(s["cards"]) for s in all_subs)
TOTAL_SUBS = len(all_subs)

# ---------------- Templates ----------------
def domain_of(href):
    return href.split("//")[-1].split("/")[0].replace("www.", "")

_CARD_COUNTER = [0]
CARD_DESC_KEYS = {}  # cd_t_NNN -> EN description

def render_card(c):
    pill_text = PILL_LABELS[c["pill"]]
    pill_class = PILL_CLASS[c["pill"]]
    badges = "".join(
        f'<span class="grade-badge {AUD_CLASS[a]}">{AUD_LABELS[a]}</span>'
        for a in c["audiences"]
    )
    top = '\n            <span class="top-pick-badge"><i class="fas fa-star"></i> Top Pick</span>' if c.get("top") else ''
    cd_key = f"cd_t_{_CARD_COUNTER[0]:03d}"
    CARD_DESC_KEYS[cd_key] = c["desc"]
    _CARD_COUNTER[0] += 1
    return (
        f'\n          <a href="{c["href"]}" target="_blank" rel="noopener" class="resource-card">'
        f'{top}'
        f'\n            <div class="card-pills"><span class="pricing-pill {pill_class}">{pill_text}</span>{badges}</div>'
        f'\n            <div class="card-top">'
        f'\n              <div class="card-icon"><i class="{c["icon"]}"></i></div>'
        f'\n              <div class="card-meta"><h4>{c["title"]}</h4></div>'
        f'\n            </div>'
        f'\n            <p data-i18n="{cd_key}">{c["desc"]}</p>'
        f'\n            <span class="card-link">{domain_of(c["href"])} <i class="fas fa-arrow-right"></i></span>'
        f'\n          </a>'
    )

def render_subcluster_panel(p, s, is_first):
    panel_active = " active" if is_first else ""
    hidden_attr = "" if is_first else " hidden"
    cards_html = "".join(render_card(c) for c in s["cards"])
    return (
        f'\n    <!-- ═══════════════════ {s["title"].upper()} ═══════════════════ -->\n'
        f'    <section id="{s["key"]}" class="panel sec-{s["key"]} phase-{p["key"]}{panel_active}" '
        f'role="tabpanel" aria-labelledby="tab-{s["key"]}" data-phase="{p["key"]}"{hidden_attr}>\n'
        f'      <div class="container">\n'
        f'        <div class="subject-header">\n'
        f'          <div class="subject-icon" style="background:{s["color_bg"]};color:{s["color"]}"><i class="{s["icon"]}"></i></div>\n'
        f'          <div class="subject-header-text">\n'
        f'            <span class="section-label section-label-orange" data-i18n="teachers.sec.{s["key"]}.label">{s["label"]}</span>\n'
        f'            <h2 data-i18n="teachers.sec.{s["key"]}.h2">{s["title"]}</h2>\n'
        f'            <p data-i18n="teachers.sec.{s["key"]}.desc">{s["desc"]}</p>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'        <div class="resource-grid">{cards_html}\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </section>'
    )

def render_phase_tab(p, is_first):
    active_cls = " phase-active" if is_first else ""
    aria_sel = "true" if is_first else "false"
    sub_count = len(p["subclusters"])
    return (
        f'      <button type="button" class="phase-tab{active_cls}" role="tab" data-phase="{p["key"]}" '
        f'aria-selected="{aria_sel}" style="--ph-color:{p["color"]};--ph-bg:{p["color_bg"]}">'
        f'<span class="ph-icon"><i class="{p["icon"]}"></i></span>'
        f'<span class="ph-name" data-i18n="teachers.phase.{p["key"]}.name">{p["tab_label"]}</span>'
        f'<span class="ph-sub" data-i18n="teachers.phase.{p["key"]}.tag">{p["tag"]}</span>'
        f'</button>'
    )

def render_subchip(p, s, is_first_in_phase):
    active_cls = " chip-active" if is_first_in_phase else ""
    aria_sel = "true" if is_first_in_phase else "false"
    return (
        f'      <button type="button" class="subject-tab{active_cls}" role="tab" data-tab="{s["key"]}" '
        f'data-phase="{p["key"]}" aria-selected="{aria_sel}" aria-controls="{s["key"]}" '
        f'style="--chip-color:{p["color"]}">'
        f'<i class="{s["icon"]} chip-icon" style="color:{s["color"]}"></i> '
        f'<span data-i18n="teachers.chip.{s["key"]}">{s["chip_label"]}</span></button>'
    )

def render_sec_css():
    """Per-subcluster card border + icon background colors."""
    rules = []
    for s in all_subs:
        rules.append(f'    .sec-{s["key"]}  .resource-card {{ border-top-color: {s["color"]}; }}')
    for s in all_subs:
        rules.append(f'    .sec-{s["key"]}  .resource-card:hover {{ border-color: {s["color"]}; }}')
    for s in all_subs:
        rules.append(f'    .sec-{s["key"]}  .card-icon {{ background: {s["color_bg"]}; color: {s["color"]}; }}')
    return "\n".join(rules)

# ---------------- Build the full HTML ----------------
phase_tabs_html = "\n".join(render_phase_tab(p, i == 0) for i, p in enumerate(PHASES))
subchips_html_parts = []
for pi, p in enumerate(PHASES):
    for si, s in enumerate(p["subclusters"]):
        subchips_html_parts.append(render_subchip(p, s, pi == 0 and si == 0))
subchips_html = "\n".join(subchips_html_parts)

panels_html_parts = []
panel_first = True
for p in PHASES:
    for s in p["subclusters"]:
        panels_html_parts.append(render_subcluster_panel(p, s, panel_first))
        panel_first = False
panels_html = "\n".join(panels_html_parts)

sec_css = render_sec_css()

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{TOTAL_CARDS} free curated tools across 4 teaching phases (Before, During, After, Supporting) — lesson planning, AI co-pilots, classroom management, assessment, STEM labs, art &amp; music, family learning and teacher PD.">
  <meta name="keywords" content="free teacher resources, lesson planning, AI for teachers, classroom management, assessment tools, PhET, GeoGebra, Chrome Music Lab, teacher PD">
  <meta name="author" content="CTWP Educational Empowerment">
  <meta name="robots" content="index, follow">
  <title>Free Teacher Resources | CTWP Educational Empowerment</title>
  <link rel="canonical" href="https://www.ctwp-education.eu.org/teachers.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.ctwp-education.eu.org/teachers.html">
  <meta property="og:site_name" content="CTWP Educational Empowerment">
  <meta property="og:title" content="Free Teacher Resources | CTWP Educational Empowerment">
  <meta property="og:description" content="{TOTAL_CARDS} free tools organised by the teaching workflow.">
  <meta property="og:image" content="https://www.ctwp-education.eu.org/assets/images/Malawi_Salima_Classroom.webp">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Free Teacher Resources | CTWP Educational Empowerment">
  <meta name="twitter:description" content="{TOTAL_CARDS} free tools organised by the teaching workflow.">
  <meta name="twitter:image" content="https://www.ctwp-education.eu.org/assets/images/Malawi_Salima_Classroom.webp">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{"@type": "WebPage", "@id": "https://www.ctwp-education.eu.org/teachers.html", "url": "https://www.ctwp-education.eu.org/teachers.html", "name": "Free Teacher Resources", "description": "{TOTAL_CARDS} free tools organised by the teaching workflow.", "isPartOf": {{"@id": "https://www.ctwp-education.eu.org/"}}, "publisher": {{"@type": "NGO", "name": "CTWP Educational Empowerment", "url": "https://www.ctwp-education.eu.org/"}}}},
      {{"@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ctwp-education.eu.org/"}}, {{"@type": "ListItem", "position": 2, "name": "Teacher Resources", "item": "https://www.ctwp-education.eu.org/teachers.html"}}]}}
    ]
  }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdnjs.cloudflare.com">
  <link rel="preconnect" href="https://cdn.jsdelivr.net">
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"></noscript>
  <link rel="preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"></noscript>
  <link rel="preload" as="style" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.2.3/css/flag-icons.min.css" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.2.3/css/flag-icons.min.css"></noscript>
  <link rel="preload" as="image" href="assets/images/Logos/ctwp logo round.webp" type="image/webp" fetchpriority="high">
  <link rel="stylesheet" href="assets/css/style.css?v=18">
  <link rel="icon" type="image/webp" href="assets/images/Logos/ctwp logo round.webp">
  <style>
    .subpage-hero {{ background: var(--green-900); color: var(--white); padding: 7rem 0 2.5rem; text-align: center; }}
    .subpage-hero .hero-badge {{ display: inline-block; background: rgba(76,175,80,0.15); color: var(--green-300); padding: 0.4rem 1.2rem; border-radius: var(--radius-full); font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1rem; }}
    .subpage-hero h1 {{ font-family: var(--font-display); font-size: clamp(1.9rem, 3.5vw, 2.8rem); font-weight: 400; margin-bottom: 0.75rem; }}
    .subpage-hero p {{ color: var(--gray-400); font-size: 1rem; max-width: 640px; margin: 0 auto 1.25rem; }}
    .subpage-hero .back-link {{ display: inline-flex; align-items: center; gap: 0.5rem; color: var(--orange-300); font-size: 0.85rem; font-weight: 500; margin-bottom: 1.25rem; transition: color var(--transition); }}
    .subpage-hero .back-link:hover {{ color: var(--orange-400); }}
    .hero-stats {{ display: flex; justify-content: center; gap: 2.25rem; margin-top: 1.5rem; flex-wrap: wrap; }}
    .hero-stat {{ text-align: center; }}
    .hero-stat strong {{ display: block; font-size: 1.5rem; font-weight: 700; color: var(--white); line-height: 1; }}
    .hero-stat span {{ font-size: 0.72rem; color: var(--gray-400); text-transform: uppercase; letter-spacing: 0.06em; }}

    /* ── Phase tabs (4 large cards) ──────────── */
    .phase-picker {{
      background: var(--cream, #f8f5ef);
      padding: 2rem 0 0.5rem;
      border-bottom: 1px solid var(--gray-200);
    }}
    .phase-picker-heading {{
      text-align: center;
      max-width: 720px;
      margin: 0 auto 1.4rem;
      padding: 0 1.5rem;
    }}
    .phase-picker-heading .section-label {{
      margin-bottom: 0.75rem;
      padding: 0.3rem 0.9rem;
      border-radius: var(--radius-full);
    }}
    .phase-picker-heading h2 {{
      font-family: var(--font-display);
      font-size: clamp(1.4rem, 2.4vw, 1.75rem);
      font-weight: 400;
      color: var(--gray-900);
      line-height: 1.3;
      margin: 0;
    }}
    .phase-picker-heading h2 em {{
      font-style: italic;
      color: var(--green-700);
    }}
    .phase-tabs-inner {{
      display: grid;
      grid-template-columns: 1.15fr 1fr 1fr 1fr 1.15fr;
      grid-template-rows: auto auto;
      gap: 0.7rem;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}
    /* Spatial placement: Fundamentals left tall, Before/During/After top-middle, Supporting bottom-middle, Further Dev right tall */
    .phase-tab[data-phase="fundamentals"] {{ grid-column: 1; grid-row: 1 / 3; }}
    .phase-tab[data-phase="before"]       {{ grid-column: 2; grid-row: 1; }}
    .phase-tab[data-phase="during"]       {{ grid-column: 3; grid-row: 1; }}
    .phase-tab[data-phase="after"]        {{ grid-column: 4; grid-row: 1; }}
    .phase-tab[data-phase="supp"]         {{ grid-column: 2 / 5; grid-row: 2; }}
    .phase-tab[data-phase="furtherdev"]   {{ grid-column: 5; grid-row: 1 / 3; }}
    .phase-tab {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.3rem;
      padding: 0.85rem 0.95rem 0.95rem;
      background: var(--white);
      border: 2px solid var(--gray-200);
      border-radius: 14px;
      cursor: pointer;
      text-align: left;
      transition: border-color 0.2s, box-shadow 0.2s, transform 0.15s;
      position: relative;
      font-family: var(--font-body);
      height: 100%;
      box-sizing: border-box;
    }}
    /* Supporting: wider card gets horizontal icon+text layout */
    .phase-tab[data-phase="supp"] {{
      flex-direction: row;
      align-items: center;
      gap: 1rem;
      padding: 0.75rem 1.2rem;
    }}
    .phase-tab[data-phase="supp"] .ph-count {{ top: 0.5rem; }}
    .phase-tab:hover {{
      border-color: var(--ph-color);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08);
      transform: translateY(-2px);
    }}
    .phase-tab.phase-active {{
      border-color: var(--ph-color);
      box-shadow: 0 8px 22px rgba(0,0,0,0.12);
      background: var(--ph-bg);
    }}
    .phase-tab .ph-count {{
      position: absolute;
      top: 0.6rem;
      right: 0.7rem;
      font-size: 0.6rem;
      font-weight: 700;
      color: var(--gray-400);
    }}
    .phase-tab.phase-active .ph-count {{ color: var(--ph-color); }}
    .phase-tab .ph-icon {{
      width: 38px;
      height: 38px;
      border-radius: 9px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--ph-color);
      color: var(--white);
      font-size: 1.05rem;
      margin-bottom: 0.35rem;
    }}
    .phase-tab .ph-name {{
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--gray-900);
      display: block;
    }}
    .phase-tab .ph-sub {{
      font-size: 0.7rem;
      color: var(--gray-600);
      display: block;
      margin-top: 0.05rem;
    }}

    /* ── Sub-chip bar ────────────────────────── */
    .subchip-bar {{
      background: #f0f9ff; /* updated dynamically by JS to match active phase color_bg */
      padding: 0.9rem 0 1.5rem;
      border-bottom: 1px solid var(--gray-200);
    }}
    .subchip-inner {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.5rem;
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}
    .subject-tab {{
      display: none;  /* hidden until its phase is active */
      height: 2.5rem;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0 0.85rem;
      font-family: var(--font-body);
      font-size: 0.76rem;
      font-weight: 600;
      letter-spacing: 0.01em;
      color: var(--gray-700);
      background-color: var(--white);
      border: 1px solid rgba(0,0,0,0.08);
      border-radius: var(--radius-full);
      text-align: center;
      white-space: nowrap;
      cursor: pointer;
      transition: color 0.2s, background-color 0.2s, border-color 0.2s, box-shadow 0.2s, transform 0.15s;
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
      line-height: 1;
    }}
    .subject-tab.in-active-phase {{ display: inline-flex; }}
    .subject-tab:not(.chip-active):hover {{
      color: var(--chip-color, var(--gray-900));
      border-color: var(--chip-color, var(--gray-400));
      box-shadow: 0 6px 16px rgba(0,0,0,0.10);
      transform: translateY(-2px);
    }}
    .subject-tab.chip-active {{
      background-color: var(--chip-color);
      color: var(--white);
      border-color: var(--chip-color);
      box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    }}
    .subject-tab.chip-active:hover {{ transform: translateY(-2px); }}
    .chip-icon {{
      font-size: 0.82rem;
      flex-shrink: 0;
      opacity: 0.8;
    }}
    .subject-tab:not(.chip-active):hover .chip-icon {{ opacity: 1; }}
    .subject-tab.chip-active .chip-icon {{ opacity: 1; color: currentColor !important; }}

    /* ── Filter Bar ──────────────────────────── */
    .filter-bar {{
      background: #f1f5f4;
      border-bottom: 1px solid var(--gray-200);
      padding: 1rem 0;
    }}
    .filter-bar-inner {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.7rem 1.5rem;
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 2rem;
    }}
    .filter-group {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      flex-wrap: wrap;
      justify-content: center;
    }}
    .filter-label {{
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--gray-500);
      margin-right: 0.15rem;
      white-space: nowrap;
    }}
    .filter-btn {{
      font-family: var(--font-body);
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.3rem 0.8rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--gray-300);
      background: transparent;
      color: var(--gray-600);
      cursor: pointer;
      transition: all 0.18s;
      white-space: nowrap;
      letter-spacing: 0.02em;
    }}
    .filter-btn:hover {{
      border-color: var(--gray-500);
      color: var(--gray-800);
    }}
    .filter-btn.filter-active {{
      background: var(--green-700);
      color: var(--white);
      border-color: var(--green-700);
    }}
    .panel.has-no-results .resource-grid::after {{
      content: "No tools match the current filter — try a different stage.";
      display: block;
      text-align: center;
      padding: 2.5rem 1rem;
      color: var(--gray-500);
      font-size: 0.88rem;
      grid-column: 1 / -1;
    }}

    .panel {{ display: none; padding: 2.5rem 0 4rem; }}
    .panel.active {{ display: block; animation: panelFade 0.25s ease; }}
    @keyframes panelFade {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    .subject-header {{ display: flex; align-items: flex-start; gap: 1.1rem; margin-bottom: 2rem; }}
    .subject-icon {{ width: 50px; height: 50px; border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; }}
    .subject-header-text .section-label {{ margin-bottom: 0.25rem; }}
    .subject-header-text h2 {{ font-family: var(--font-display); font-size: clamp(1.4rem, 2.5vw, 1.7rem); font-weight: 400; color: var(--gray-900); margin: 0 0 0.3rem; }}
    .subject-header-text p {{ font-size: 0.88rem; color: var(--gray-500); margin: 0; }}

    .resource-grid {{ grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
    a.resource-card {{ display: flex; flex-direction: column; text-decoration: none; color: inherit; border-top: 3px solid transparent; }}
{sec_css}
    .resource-card i {{ color: inherit; margin-bottom: 0; font-size: 0.95rem; }}
    .card-icon {{ width: 36px; height: 36px; border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; font-size: 0.95rem; flex-shrink: 0; }}
    .card-top {{ display: flex; align-items: flex-start; gap: 0.7rem; margin-bottom: 0.55rem; }}
    .card-meta {{ flex: 1; min-width: 0; }}
    .card-meta h4 {{ font-family: var(--font-display); font-size: 0.98rem; font-weight: 400; color: var(--gray-900); margin: 0 0 0.3rem; }}

    .card-pills {{ display: flex; flex-wrap: wrap; gap: 0.28rem; margin-bottom: 0.55rem; align-items: center; }}
    .pricing-pill {{ display: inline-flex; align-items: center; gap: 0.22rem; font-size: 0.62rem; font-weight: 700; padding: 0.12rem 0.5rem; border-radius: var(--radius-full); text-transform: uppercase; letter-spacing: 0.04em; line-height: 1.5; }}
    .pill-free         {{ background: var(--green-50);   color: var(--green-700); }}
    .pill-free-signup  {{ background: #e0e7ff;           color: #3730a3; }}
    .pill-freemium     {{ background: var(--orange-100); color: var(--orange-500); }}
    .grade-badges {{ display: flex; flex-wrap: wrap; gap: 0.22rem; }}
    .grade-badge {{ font-size: 0.66rem; font-weight: 600; padding: 0.1rem 0.42rem; border-radius: var(--radius-full); background: var(--gray-100); color: var(--gray-600); line-height: 1.55; }}
    .top-pick-badge {{ display: inline-flex; align-items: center; gap: 0.18rem; font-size: 0.62rem; font-weight: 700; color: #b45309; background: #fef3c7; padding: 0.12rem 0.48rem; border-radius: var(--radius-full); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.3rem; }}

    .resource-card p {{ font-size: 0.82rem; color: var(--gray-500); line-height: 1.55; flex: 1; margin-bottom: 0; }}
    .card-link {{ display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.76rem; color: var(--orange-500); font-weight: 500; margin-top: 0.75rem; transition: gap var(--transition); }}
    a.resource-card:hover .card-link {{ gap: 0.55rem; }}

    @media (max-width: 900px) {{
      .phase-tabs-inner {{
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: unset;
        gap: 0.5rem;
      }}
      .phase-tab[data-phase="fundamentals"],
      .phase-tab[data-phase="before"],
      .phase-tab[data-phase="during"],
      .phase-tab[data-phase="after"],
      .phase-tab[data-phase="supp"],
      .phase-tab[data-phase="furtherdev"] {{
        grid-column: unset; grid-row: unset; height: auto;
      }}
      .phase-tab[data-phase="supp"] {{ grid-column: 1 / 4; flex-direction: row; }}
      .phase-tab {{ padding: 0.7rem 0.8rem 0.8rem; }}
      .phase-tab .ph-icon {{ width: 32px; height: 32px; font-size: 0.9rem; }}
      .phase-tab .ph-name {{ font-size: 0.85rem; }}
      .phase-tab .ph-sub {{ font-size: 0.66rem; }}
    }}
    @media (max-width: 560px) {{
      .phase-tabs-inner {{ padding: 0 1rem; }}
      .subchip-inner {{ padding: 0 1rem; gap: 0.4rem; }}
      .subject-tab {{ font-size: 0.72rem; padding: 0 0.65rem; height: 2.35rem; }}
      .hero-stats {{ gap: 1.25rem; }}
      .subject-header {{ flex-direction: column; gap: 0.75rem; }}
      .panel {{ padding: 1.75rem 0 2.5rem; }}
      .filter-bar-inner {{ gap: 0.5rem 1rem; }}
    }}
  </style>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-W6JYDY61WX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-W6JYDY61WX');
  </script>
</head>
<body>
  <header id="navbar">
    <nav class="nav-container">
      <a href="index.html" class="nav-logo">
        <img src="assets/images/Logos/ctwp logo round.webp" alt="CTWP Logo" class="logo-img" fetchpriority="high">
        <div class="logo-text">
          <span class="logo-name">CTWP</span>
          <span class="logo-tagline">EDUCATIONAL EMPOWERMENT</span>
        </div>
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="index.html" class="nav-link">Home</a></li>
        <li><a href="index.html#about" class="nav-link" data-i18n="nav.about">About</a></li>
        <li><a href="index.html#resources" class="nav-link" data-i18n="nav.resources">Resources</a></li>
        <li><a href="index.html#support" class="nav-link" data-i18n="nav.support">Support Us</a></li>
        <li><a href="index.html#contact" class="nav-link" data-i18n="nav.contact">Contact</a></li>
        <li><a href="lab.html" class="nav-btn-lab" data-i18n="nav.lab">Our Lab</a></li>
      </ul>
      <button id="langToggle" class="lang-toggle"><span class="lang-opt" data-lang="en"><span class="fi fi-us"></span> EN</span><span class="lang-sep">|</span><span class="lang-opt" data-lang="de"><span class="fi fi-de"></span> DE</span></button>
      <button class="hamburger" id="hamburger" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
    </nav>
  </header>

  <div class="mobile-menu" id="mobileMenu">
    <ul class="mobile-nav-links">
      <li><a href="index.html" class="mobile-link">Home</a></li>
      <li><a href="index.html#about" class="mobile-link" data-i18n="nav.about">About</a></li>
      <li><a href="index.html#resources" class="mobile-link" data-i18n="nav.resources">Resources</a></li>
      <li><a href="index.html#support" class="mobile-link" data-i18n="nav.support">Support Us</a></li>
      <li><a href="index.html#contact" class="mobile-link" data-i18n="nav.contact">Contact</a></li>
      <li><a href="lab.html" class="nav-btn-lab" data-i18n="nav.lab" style="margin-left:0;margin-top:0.25rem;">Our Lab</a></li>
    </ul>
  </div>

  <section class="subpage-hero">
    <div class="container">
      <a href="index.html#resources" class="back-link">
        <i class="fas fa-arrow-left"></i> <span data-i18n="sub.teachers.back">Back to Resources</span>
      </a>
      <div class="hero-badge"><span data-i18n="sub.teachers.badge">Free Tools for Teachers &amp; Educators</span></div>
      <h1 data-i18n="sub.teachers.title">Resources for Teachers</h1>
      <p data-i18n="sub.teachers.desc">{TOTAL_CARDS} curated free tools organised by the teaching workflow. Pick a phase, then a topic, to find the right tool.</p>
      <div class="hero-stats">
        <div class="hero-stat"><strong>{TOTAL_CARDS}</strong><span data-i18n="teachers.stat.tools">Free Tools</span></div>
        <div class="hero-stat"><strong>{TOTAL_SUBS}</strong><span data-i18n="teachers.stat.topics">Topics</span></div>
        <div class="hero-stat"><strong>4</strong><span data-i18n="teachers.stat.phases">Workflow Phases</span></div>
        <div class="hero-stat"><strong>100%</strong><span data-i18n="teachers.stat.free">Free</span></div>
      </div>
    </div>
  </section>

  <!-- ── Phase Picker (4 tabs) ── -->
  <nav class="phase-picker" role="tablist" aria-label="Choose a phase of the teaching workflow">
    <div class="phase-picker-heading">
      <span class="section-label section-label-orange" data-i18n="teachers.picker.label">Explore by Phase</span>
      <h2 data-i18n-html="teachers.picker.heading">Choose a <em>phase of the teaching workflow</em>, then a topic</h2>
    </div>
    <div class="phase-tabs-inner">
{phase_tabs_html}
    </div>
  </nav>

  <!-- ── Sub-chip Bar (visible chips depend on active phase) ── -->
  <nav class="subchip-bar" role="tablist" aria-label="Choose a topic within the active phase">
    <div class="subchip-inner">
{subchips_html}
    </div>
  </nav>

  <!-- ── Filter Bar (audience) ── -->
  <div class="filter-bar" id="filterBar">
    <div class="filter-bar-inner">
      <div class="filter-group">
        <span class="filter-label" data-i18n="teachers.filter.label">Filter by stage:</span>
        <button class="filter-btn filter-active" data-filter="audience" data-value="all" data-i18n="teachers.filter.all">All Stages</button>
        <button class="filter-btn" data-filter="audience" data-value="prek" data-i18n="teachers.grade.prek">Pre-K</button>
        <button class="filter-btn" data-filter="audience" data-value="primary" data-i18n="teachers.grade.primary">Primary</button>
        <button class="filter-btn" data-filter="audience" data-value="secondary" data-i18n="teachers.grade.secondary">Secondary</button>
        <button class="filter-btn" data-filter="audience" data-value="higher" data-i18n="teachers.grade.higher">Higher Ed</button>
        <button class="filter-btn" data-filter="audience" data-value="sen" data-i18n="teachers.grade.sen">Special Ed</button>
      </div>
    </div>
  </div>

  <main>
{panels_html}

  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="nav-logo">
            <img src="assets/images/Logos/ctwp logo round.webp" alt="CTWP Logo" class="logo-img" loading="lazy">
            <div class="logo-text">
              <span class="logo-name">CTWP</span>
              <span class="logo-tagline">EDUCATIONAL EMPOWERMENT</span>
            </div>
          </a>
          <p class="footer-description">Empowering every child through access to free education using technology.</p>
        </div>
        <div class="footer-links-group">
          <h4>Navigation</h4>
          <ul>
            <li><a href="index.html#about">About</a></li>
            <li><a href="index.html#gallery">Our Work</a></li>
            <li><a href="index.html#resources">Resources</a></li>
            <li><a href="index.html#support">Support Us</a></li>
          </ul>
        </div>
        <div class="footer-links-group">
          <h4>Connect</h4>
          <ul>
            <li><a href="index.html#contact">Contact Us</a></li>
            <li><a href="https://ch.linkedin.com/company/ctwp-educationlempowerment" target="_blank" rel="noopener">LinkedIn</a></li>
            <li><a href="https://www.instagram.com/ctwp_educationalempowerment/" target="_blank" rel="noopener">Instagram</a></li>
            <li><a href="https://www.facebook.com/profile.php?id=100091277141645" target="_blank" rel="noopener">Facebook</a></li>
            <li><a href="https://bongai-shamwari.org/en/" target="_blank" rel="noopener">Bongai Shamwari</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CTWP Educational Empowerment. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <button id="backToTop" class="back-to-top" aria-label="Back to top"><i class="fas fa-chevron-up"></i></button>

  <div id="gdprBanner" class="gdpr-banner" role="dialog" aria-label="Cookie consent" aria-live="polite">
    <div class="gdpr-inner">
      <div class="gdpr-text">
        <strong data-i18n="gdpr.title">Cookie &amp; Storage Notice</strong>
        <p data-i18n="gdpr.text">We use browser local storage solely to remember your language preference. No tracking cookies or personal data are collected or shared.</p>
      </div>
      <div class="gdpr-actions">
        <button class="gdpr-btn gdpr-accept" id="gdprAccept" data-i18n="gdpr.accept">Accept</button>
        <button class="gdpr-btn gdpr-decline" id="gdprDecline" data-i18n="gdpr.decline">Decline</button>
      </div>
    </div>
  </div>

  <script defer src="assets/js/i18n.js?v=17"></script>
  <script defer src="assets/js/main.js"></script>
  <script>
    /* Phase tabs + sub-chips: two-level navigation */
    (function () {{
      var phaseTabs = document.querySelectorAll('.phase-tab');
      var subChips = document.querySelectorAll('.subject-tab');
      var panels = document.querySelectorAll('.panel');
      var phasePicker = document.querySelector('.phase-picker');
      var subChipBar = document.querySelector('.subchip-bar');

      function activateSubcluster(targetId, scroll) {{
        var found = false;
        subChips.forEach(function (c) {{
          var match = c.dataset.tab === targetId;
          if (match) found = true;
          c.setAttribute('aria-selected', match ? 'true' : 'false');
          c.classList.toggle('chip-active', match);
        }});
        panels.forEach(function (p) {{
          var match = p.id === targetId;
          p.classList.toggle('active', match);
          if (match) {{ p.removeAttribute('hidden'); }} else {{ p.setAttribute('hidden', ''); }}
        }});
        if (scroll) {{
          var navTop = phasePicker.getBoundingClientRect().top;
          if (navTop < 0) {{
            var stickyOffset = 4.5 * parseFloat(getComputedStyle(document.documentElement).fontSize);
            window.scrollTo({{ top: window.scrollY + navTop - stickyOffset, behavior: 'smooth' }});
          }}
        }}
        if (window._applyCardFilters) window._applyCardFilters();
        return found;
      }}

      function activatePhase(phaseKey, scroll) {{
        phaseTabs.forEach(function (t) {{
          var match = t.dataset.phase === phaseKey;
          t.setAttribute('aria-selected', match ? 'true' : 'false');
          t.classList.toggle('phase-active', match);
          if (match && subChipBar) {{
            subChipBar.style.background = t.style.getPropertyValue('--ph-bg');
          }}
        }});
        var firstSubInPhase = null;
        subChips.forEach(function (c) {{
          var inPhase = c.dataset.phase === phaseKey;
          c.classList.toggle('in-active-phase', inPhase);
          if (inPhase && !firstSubInPhase) firstSubInPhase = c;
        }});
        if (firstSubInPhase) {{
          activateSubcluster(firstSubInPhase.dataset.tab, scroll);
        }}
      }}

      phaseTabs.forEach(function (t) {{
        t.addEventListener('click', function (e) {{
          e.preventDefault();
          activatePhase(t.dataset.phase, true);
          history.replaceState(null, '', '#' + t.dataset.phase);
        }});
      }});

      subChips.forEach(function (c) {{
        c.addEventListener('click', function (e) {{
          e.preventDefault();
          activateSubcluster(c.dataset.tab, true);
          history.replaceState(null, '', '#' + c.dataset.tab);
        }});
      }});

      // Init: show first phase's chips, activate first chip + panel
      var firstPhase = phaseTabs[0].dataset.phase;
      activatePhase(firstPhase, false);

      // Honor URL hash if it matches a phase or sub-cluster
      var initial = window.location.hash.slice(1);
      if (initial) {{
        var phaseMatch = Array.prototype.find.call(phaseTabs, function (t) {{ return t.dataset.phase === initial; }});
        var subMatch   = Array.prototype.find.call(subChips,  function (c) {{ return c.dataset.tab === initial; }});
        if (phaseMatch) {{
          activatePhase(initial, false);
        }} else if (subMatch) {{
          activatePhase(subMatch.dataset.phase, false);
          activateSubcluster(initial, false);
        }}
      }}
    }})();
  </script>
  <script>
    /* Card filter: audience (matches gb-* class on grade badges; gb-all always shows) */
    (function () {{
      var activeAud = 'all';

      function applyFilters() {{
        var activePanel = document.querySelector('.panel.active');
        if (!activePanel) return;
        var cards = activePanel.querySelectorAll('.resource-card');
        var visible = 0;
        cards.forEach(function (card) {{
          var show = true;
          if (activeAud !== 'all') {{
            show = !!card.querySelector('.grade-badge.gb-' + activeAud)
                || !!card.querySelector('.grade-badge.gb-all');
          }}
          card.style.display = show ? '' : 'none';
          if (show) visible++;
        }});
        activePanel.classList.toggle('has-no-results', cards.length > 0 && visible === 0);
      }}

      window._applyCardFilters = applyFilters;

      document.querySelectorAll('.filter-btn[data-filter="audience"]').forEach(function (btn) {{
        btn.addEventListener('click', function () {{
          document.querySelectorAll('.filter-btn[data-filter="audience"]').forEach(function (b) {{
            b.classList.toggle('filter-active', b === btn);
          }});
          activeAud = btn.dataset.value;
          applyFilters();
        }});
      }});
    }})();
  </script>
  <script>
    (function () {{
      var GDPR_KEY = 'ctwp-gdpr';
      var banner = document.getElementById('gdprBanner');
      if (!banner) return;
      function hideBanner() {{ banner.style.transition = 'transform 0.4s ease'; banner.style.transform = 'translateY(110%)'; }}
      function showBanner() {{
        banner.style.display = 'block';
        banner.style.transform = 'translateY(110%)';
        banner.style.transition = 'none';
        requestAnimationFrame(function () {{ requestAnimationFrame(function () {{
          banner.style.transition = 'transform 0.45s cubic-bezier(.4,0,.2,1)';
          banner.style.transform = 'translateY(0)';
        }}); }});
      }}
      if (!localStorage.getItem(GDPR_KEY)) setTimeout(showBanner, 900);
      document.getElementById('gdprAccept').addEventListener('click', function () {{ localStorage.setItem(GDPR_KEY, 'accepted'); hideBanner(); }});
      document.getElementById('gdprDecline').addEventListener('click', function () {{ localStorage.setItem(GDPR_KEY, 'declined'); hideBanner(); }});
    }})();
  </script>
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"Wrote {OUT} ({len(HTML):,} bytes, {HTML.count(chr(10))} lines)")

# ---------------- i18n keys ----------------
import json
i18n_data = {
    "sub.teachers.back": "Back to Resources",
    "sub.teachers.badge": "Free Tools for Teachers & Educators",
    "sub.teachers.title": "Resources for Teachers",
    "sub.teachers.desc": f"{TOTAL_CARDS} curated free tools organised by the teaching workflow. Pick a phase, then a topic, to find the right tool.",
    "teachers.stat.tools": "Free Tools",
    "teachers.stat.topics": "Topics",
    "teachers.stat.phases": "Workflow Phases",
    "teachers.stat.free": "Free",
    "teachers.grade.prek": "Pre-K",
    "teachers.grade.primary": "Primary",
    "teachers.grade.secondary": "Secondary",
    "teachers.grade.higher": "Higher Ed",
    "teachers.grade.sen": "Special Ed",
    "teachers.grade.all": "All Stages",
    "teachers.picker.label": "Explore by Phase",
    "teachers.picker.heading": "Choose a <em>phase of the teaching workflow</em>, then a topic",
    "teachers.filter.label": "Filter by stage:",
    "teachers.filter.all": "All Stages",
}
for p in PHASES:
    i18n_data[f"teachers.phase.{p['key']}.name"] = p["tab_label"]
    i18n_data[f"teachers.phase.{p['key']}.tag"] = p["tag"]
    for s in p["subclusters"]:
        i18n_data[f"teachers.chip.{s['key']}"] = s["chip_label"]
        i18n_data[f"teachers.sec.{s['key']}.label"] = s["label"]
        i18n_data[f"teachers.sec.{s['key']}.h2"] = s["title"]
        i18n_data[f"teachers.sec.{s['key']}.desc"] = s["desc"]
i18n_data.update(CARD_DESC_KEYS)

(ROOT / "_teachers_i18n_keys.json").write_text(json.dumps(i18n_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {ROOT / '_teachers_i18n_keys.json'} ({len(i18n_data)} keys)")
