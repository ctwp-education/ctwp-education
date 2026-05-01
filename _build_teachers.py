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

# ---------------- PHASES (4) -> sub-clusters (18) -> cards (12 each) ----------------
PHASES = [
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
                "chip_label": "Lesson Planning",
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
                    {"href":"https://eduprotocols.com", "title":"EduProtocols", "icon":"fas fa-puzzle-piece", "pill":"free", "audiences":["all"],
                     "desc":"Free reusable lesson frames any teacher can drop content into — Cyber Sandwich, Iron Chef, Worst Preso Ever and more."},
                    {"href":"https://www.ck12.org", "title":"CK-12 Foundation", "icon":"fas fa-book-bookmark", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free customisable digital textbooks (FlexBooks) for every K-12 subject — adapt content, add notes, share with students."},
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
                ],
            },
            # ── 3. Selecting & adapting (Differentiation, Inclusion & SEN) ──
            {
                "key": "differentiation", "color": "#f59e0b", "color_bg": "#fffbeb",
                "icon": "fas fa-universal-access",
                "chip_label": "Differentiation & SEN",
                "label": "Inclusion, SEN & Adapting Resources",
                "title": "Selecting & Adapting Resources — Differentiation, Inclusion & SEN",
                "desc": "Reach every learner — adaptive readers, accessibility tools, dyslexia-friendly fonts and SEN-specific resources.",
                "cards": [
                    {"href":"https://www.understood.org", "title":"Understood.org", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"], "top":True,
                     "desc":"Comprehensive free resources for teachers and parents on dyslexia, ADHD and learning differences — research-backed and practical."},
                    {"href":"https://www.cast.org/our-work/about-udl.html", "title":"CAST UDL Guidelines", "icon":"fas fa-universal-access", "pill":"free", "audiences":["all"],
                     "desc":"The definitive Universal Design for Learning framework — free guidelines, examples and implementation tools for every classroom."},
                    {"href":"https://www.bookshare.org", "title":"Bookshare", "icon":"fas fa-book-reader", "pill":"free-signup", "audiences":["primary","secondary","sen"],
                     "desc":"Free for US students with reading disabilities — over 1.4M accessible audiobooks and ebooks with text-to-speech."},
                    {"href":"https://www.naturalreaders.com", "title":"Natural Reader", "icon":"fas fa-volume-high", "pill":"freemium", "audiences":["all"],
                     "desc":"Free text-to-speech with natural voices — read PDFs, web pages and Word docs aloud to support reading access."},
                    {"href":"https://www.opendyslexic.org", "title":"OpenDyslexic Font", "icon":"fas fa-font", "pill":"free", "audiences":["all"],
                     "desc":"Free open-source dyslexia-friendly typeface — designed to reduce letter rotation, includes browser extensions."},
                    {"href":"https://www.texthelp.com/products/read-and-write-education/", "title":"Read&Write (Texthelp)", "icon":"fas fa-book", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free 30-day trial of the leading literacy support tool — text-to-speech, predictive typing, picture dictionary."},
                    {"href":"https://diffit.me", "title":"Diffit for Teachers", "icon":"fas fa-arrows-split-up-and-left", "pill":"freemium", "audiences":["primary","secondary","sen"],
                     "desc":"Adapt any text to any reading level instantly — leveled passages, vocabulary and questions; the gold-standard differentiation AI."},
                    {"href":"https://newsela.com", "title":"Newsela", "icon":"fas fa-newspaper", "pill":"freemium", "audiences":["primary","secondary"],
                     "desc":"Free leveled news articles — every article available at 5 reading levels for differentiated content access across subjects."},
                    {"href":"https://www.do2learn.com", "title":"Do2Learn", "icon":"fas fa-puzzle-piece", "pill":"free", "audiences":["sen","prek","primary"],
                     "desc":"Free social skills, autism and behaviour resources — picture cards, songs, games and printable visual schedules."},
                    {"href":"https://www.theottoolbox.com/sensory-resources/", "title":"OT Toolbox Sensory", "icon":"fas fa-hands", "pill":"free", "audiences":["sen","prek","primary"],
                     "desc":"Free curated sensory and fine-motor activities for SEN classrooms — calm corners, sensory bins and OT-recommended ideas."},
                    {"href":"https://education.microsoft.com/en-us/resource/35d33d56", "title":"Immersive Reader", "icon":"fab fa-microsoft", "pill":"free", "audiences":["all"],
                     "desc":"Free Microsoft tool — read any text aloud with line focus, syllable splitting, picture dictionary and 60+ languages."},
                    {"href":"https://www.bdadyslexia.org.uk/advice/educators", "title":"BDA Free Resources", "icon":"fas fa-flag", "pill":"free", "audiences":["all"],
                     "desc":"British Dyslexia Association's free downloadable guides for teachers — best-practice classroom adaptations and assessments."},
                ],
            },
            # ── 4. Setting objectives & standards alignment ──
            {
                "key": "objectives", "color": "#6366f1", "color_bg": "#eef2ff",
                "icon": "fas fa-bullseye",
                "chip_label": "Objectives & Standards",
                "label": "Standards, Frameworks & Backward Design",
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
                    {"href":"https://www.curriki.org", "title":"Curriki", "icon":"fas fa-graduation-cap", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free open educational resources library — 50,000+ free lessons, units and full courses tagged by standard."},
                    {"href":"https://www.oercommons.org", "title":"OER Commons", "icon":"fas fa-globe", "pill":"free-signup", "audiences":["primary","secondary","higher"],
                     "desc":"Largest free OER repository — 70,000+ resources tagged by Common Core, NGSS and state standards, plus quality reviews."},
                    {"href":"https://www.ascd.org/free-resources", "title":"ASCD Free Resources", "icon":"fas fa-book-open-reader", "pill":"free", "audiences":["all"],
                     "desc":"Free articles, webinars and book excerpts on curriculum design, standards alignment and instructional leadership."},
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
                    {"href":"https://www.beepbox.co", "title":"Beepbox", "icon":"fas fa-wave-square", "pill":"free", "audiences":["primary","secondary"],
                     "desc":"Free retro chiptune music maker — students compose 8-bit melodies and beats in minutes, no account needed."},
                    {"href":"https://www.sketchbook.com", "title":"Autodesk Sketchbook", "icon":"fas fa-paint-brush", "pill":"free", "audiences":["all"],
                     "desc":"Free professional drawing app from Autodesk — clean interface, full brush set, available on web, desktop and mobile."},
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
                    {"href":"https://jamboard.google.com", "title":"Google Jamboard", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Free shared whiteboard from Google — sticky notes, drawings, images and live collaboration up to 50 students."},
                    {"href":"https://miro.com/education", "title":"Miro for Education", "icon":"fas fa-chalkboard-user", "pill":"freemium", "audiences":["secondary","higher"],
                     "desc":"Free Education plan with unlimited boards and templates for verified teachers — the most-loved visual collaboration tool."},
                    {"href":"https://www.figma.com/education/", "title":"FigJam Education", "icon":"fab fa-figma", "pill":"free-signup", "audiences":["secondary","higher"],
                     "desc":"Free FigJam for educators and students — collaborative whiteboarding with delightful templates and engagement features."},
                    {"href":"https://padlet.com", "title":"Padlet", "icon":"fas fa-thumbtack", "pill":"freemium", "audiences":["all"],
                     "desc":"Free 'sticky note wall' for posting ideas, photos, links and audio — three free padlets and beloved by teachers."},
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
                    {"href":"https://www.vevox.com", "title":"Vevox", "icon":"fas fa-comments", "pill":"freemium", "audiences":["higher"],
                     "desc":"Anonymous live polling and Q&A — free tier with unlimited polls, popular in higher-ed lecture halls."},
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
                    {"href":"https://rewordify.com", "title":"Rewordify", "icon":"fas fa-book-bookmark", "pill":"free", "audiences":["primary","secondary","sen"],
                     "desc":"Paste any difficult text — Rewordify replaces hard words with simpler ones inline, with definitions on hover."},
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
                    {"href":"https://padlet.com", "title":"Padlet (Exit Walls)", "icon":"fas fa-thumbtack", "pill":"freemium", "audiences":["all"],
                     "desc":"Free 'sticky note wall' — perfect for end-of-lesson exit tickets, KWL boards and quick written reflections."},
                    {"href":"https://reflect.microsoft.com", "title":"Microsoft Reflect", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["primary","secondary"],
                     "desc":"Free emotional check-in tool inside Teams for Education — students choose feelings; teachers see class wellbeing trends."},
                    {"href":"https://en.linoit.com", "title":"Lino It", "icon":"fas fa-note-sticky", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free sticky-note canvas — collect anonymous reflections, peer feedback and class discussion threads on one shared board."},
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
                "chip_label": "Tracking & Family",
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
                "chip_label": "Classroom Mgmt",
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
                ],
            },
            # ── 14. Communication ──
            {
                "key": "comms", "color": "#22c55e", "color_bg": "#f0fdf4",
                "icon": "fas fa-comments",
                "chip_label": "Comms",
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
                "chip_label": "Admin & Files",
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
            # ── 16. Professional development ──
            {
                "key": "pd", "color": "#e11d48", "color_bg": "#fff1f2",
                "icon": "fas fa-user-graduate",
                "chip_label": "PD & Further Ed",
                "label": "Courses, Certificates & CPD",
                "title": "Professional Development & Further Education",
                "desc": "Free CPD, micro-credentials and certificates from Coursera, edX, Microsoft, Google, Apple and the Open University.",
                "cards": [
                    {"href":"https://www.coursera.org/browse/social-sciences/education", "title":"Coursera Educator Track", "icon":"fas fa-chalkboard-teacher", "pill":"free-signup", "audiences":["all"], "top":True,
                     "desc":"Audit Stanford, Penn and Johns Hopkins teaching courses for free — paid certificates available, full content always free."},
                    {"href":"https://www.edx.org/learn/teaching", "title":"edX Teaching Courses", "icon":"fas fa-school", "pill":"free-signup", "audiences":["all"],
                     "desc":"Harvard, MIT and HarvardX education courses — free to audit, with optional paid MicroMasters for school leadership."},
                    {"href":"https://www.futurelearn.com/subjects/teaching-courses", "title":"FutureLearn Teaching", "icon":"fas fa-users", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free short teaching courses from UK universities — practical pedagogy, EdTech and subject-specific PD."},
                    {"href":"https://www.open.edu/openlearn/education-development", "title":"OpenLearn Education", "icon":"fas fa-globe-europe", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Open University courses with statements of participation — full PD on inclusive teaching, mentoring, leadership."},
                    {"href":"https://ocw.mit.edu/courses/find-by-topic/", "title":"MIT OCW Educator", "icon":"fas fa-university", "pill":"free", "audiences":["secondary","higher"],
                     "desc":"MIT's free educator portal — videos of MIT classes alongside teaching insights, problem sets and exam questions."},
                    {"href":"https://learn.microsoft.com/en-us/training/educator-center/", "title":"Microsoft Educator Center", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Microsoft Innovative Educator badges — courses on Teams, OneNote, Minecraft Edu, Flip and global collaboration."},
                    {"href":"https://education.apple.com", "title":"Apple Teacher", "icon":"fab fa-apple", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Apple Teacher self-paced PD program — earn badges and recognition for skills with iPad, Mac and Apple apps."},
                    {"href":"https://teachercenter.withgoogle.com", "title":"Google for Education", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free training on Google Workspace for teachers, with Level 1 and 2 Certified Educator paid exams."},
                    {"href":"https://www.iste.org/professional-development", "title":"ISTE Free Resources", "icon":"fas fa-award", "pill":"freemium", "audiences":["all"],
                     "desc":"International Society for Tech in Education — free webinars, articles and many free PD resources from the leading EdTech org."},
                    {"href":"https://www.khanacademy.org/teacher-essentials", "title":"Khan Academy Teacher", "icon":"fas fa-leaf", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free Khan Academy training for teachers — onboarding, classroom integration and student-progress reporting."},
                    {"href":"https://www.teachthought.com/professional-development", "title":"TeachThought PD", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all"],
                     "desc":"Hundreds of free articles on innovative pedagogy, project-based learning and classroom design."},
                    {"href":"https://www.edweek.org/events/webinars", "title":"EdWeek Webinars", "icon":"fas fa-newspaper", "pill":"free-signup", "audiences":["all"],
                     "desc":"Free live and on-demand webinars from Education Week — leading-edge research, policy and classroom practice."},
                ],
            },
            # ── 17. Teacher wellbeing ──
            {
                "key": "wellbeing", "color": "#d946ef", "color_bg": "#fdf4ff",
                "icon": "fas fa-heart-pulse",
                "chip_label": "Wellbeing",
                "label": "Mental Health, Mindfulness & Self-Care",
                "title": "Teacher Wellbeing & Self-Care",
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
                ],
            },
        ],
    },
]

# ---------------- Sanity asserts ----------------
assert len(PHASES) == 4, f"Expected 4 phases, got {len(PHASES)}"
all_subs = []
for p in PHASES:
    for s in p["subclusters"]:
        assert len(s["cards"]) == 12, f"Sub-cluster {s['key']} has {len(s['cards'])} cards, expected 12"
        all_subs.append(s)
expected_subs = 4 + 4 + 4 + 6
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
        f'            <h2 data-i18n="teachers.sec.{s["key"]}.h2">{s["title"]} — 12 Best Free Tools</h2>\n'
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
        f'<span class="ph-count">{sub_count}</span>'
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
      grid-template-columns: repeat(4, 1fr);
      gap: 0.7rem;
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}
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
    }}
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
      background: var(--cream, #f8f5ef);
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
      background: var(--white);
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

    @media (max-width: 880px) {{
      .phase-tabs-inner {{ grid-template-columns: repeat(2, 1fr); gap: 0.5rem; }}
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
        i18n_data[f"teachers.sec.{s['key']}.h2"] = f"{s['title']} — 12 Best Free Tools"
        i18n_data[f"teachers.sec.{s['key']}.desc"] = s["desc"]
i18n_data.update(CARD_DESC_KEYS)

(ROOT / "_teachers_i18n_keys.json").write_text(json.dumps(i18n_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {ROOT / '_teachers_i18n_keys.json'} ({len(i18n_data)} keys)")
