#!/usr/bin/env python3
"""
Generate university.html with 12 future-skill sections × 12 cards = 144 cards.
Architecture: sticky-tabs (one panel visible at a time), like the existing page.
"""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "university.html"

# ---------------- Audience badge + pricing pill labels ----------------
AUD_LABELS = {
    "undergrad": "Undergrad",
    "grad": "Grad",
    "phd": "PhD",
    "self": "Self-Learner",
    "all": "All Levels",
    "adult": "Adult Learner",
    "switcher": "Career Switcher",
}
AUD_CLASS = {k: f"gb-{k}" for k in AUD_LABELS}
PILL_LABELS = {"free": "Free", "free-signup": "Free (sign-up)", "freemium": "Freemium"}
PILL_CLASS = {"free": "pill-free", "free-signup": "pill-free-signup", "freemium": "pill-freemium"}

# ---------------- Sections + cards ----------------
SECTIONS = [
    # 1. AI FLUENCY
    {
        "key": "ai", "color": "#6366f1", "color_bg": "#eef2ff", "icon": "fas fa-robot",
        "tab_label": "AI Fluency",
        "label": "AI Tutors & Co-pilots",
        "title": "AI Fluency & Co-working with AI",
        "desc": "Top free assistants, courses on prompt design, and the literacy you need to think with AI rather than against it.",
        "cards": [
            {"href":"https://claude.ai", "title":"Claude", "icon":"fas fa-comments", "pill":"free-signup", "audiences":["all"], "top":True,
             "desc":"Anthropic's flagship assistant — a generous free tier covers writing, code and research with strong reasoning."},
            {"href":"https://chatgpt.com", "title":"ChatGPT", "icon":"fas fa-brain", "pill":"free-signup", "audiences":["all"],
             "desc":"OpenAI's ChatGPT — free tier covers GPT-4o mini, voice mode, image understanding and basic data analysis."},
            {"href":"https://gemini.google.com", "title":"Gemini", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all"],
             "desc":"Google's multimodal assistant with deep integration into Docs, Drive and Gmail — strong free tier with image and code support."},
            {"href":"https://copilot.microsoft.com", "title":"Microsoft Copilot", "icon":"fab fa-microsoft", "pill":"free-signup", "audiences":["all"],
             "desc":"Free Copilot with GPT-4-class reasoning, image generation and Microsoft 365 integration — included free with any Microsoft account."},
            {"href":"https://www.perplexity.ai", "title":"Perplexity", "icon":"fas fa-magnifying-glass", "pill":"freemium", "audiences":["all"],
             "desc":"AI search engine that cites every claim — perfect when you need verifiable sources rather than hallucinated answers."},
            {"href":"https://notebooklm.google.com", "title":"NotebookLM", "icon":"fas fa-book-open", "pill":"free-signup", "audiences":["all"],
             "desc":"Upload your own notes and PDFs — Google's AI answers strictly from your sources, with citations and audio summaries."},
            {"href":"https://huggingface.co", "title":"Hugging Face", "icon":"fas fa-cube", "pill":"freemium", "audiences":["undergrad","grad"],
             "desc":"Run thousands of open-source AI models in your browser — text, vision, speech, agents — and host your own free Spaces."},
            {"href":"https://www.deeplearning.ai/short-courses/", "title":"DeepLearning.AI Short Courses", "icon":"fas fa-graduation-cap", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free 1-hour courses by Andrew Ng on prompting, RAG, agents and fine-tuning — taught with leading AI labs."},
            {"href":"https://www.anthropic.com/ai-fluency", "title":"Anthropic AI Fluency", "icon":"fas fa-compass", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free open-source course teaching the four core competencies of working with AI — delegation, description, discernment, diligence."},
            {"href":"https://www.elementsofai.com", "title":"Elements of AI", "icon":"fas fa-atom", "pill":"free-signup", "audiences":["all","adult"],
             "desc":"University of Helsinki's free MOOC — 30 hours covering AI fundamentals, ethics and limits, taken by a million learners."},
            {"href":"https://grow.google/aiessentials/", "title":"Google AI Essentials", "icon":"fas fa-seedling", "pill":"free", "audiences":["all","adult"],
             "desc":"Free Google curriculum on generative AI basics, prompt design and responsible use — no prior experience required."},
            {"href":"https://www.promptingguide.ai", "title":"Prompt Engineering Guide", "icon":"fas fa-terminal", "pill":"free", "audiences":["all"],
             "desc":"Open-source community guide to prompting — techniques, examples and research papers, all free and frequently updated."},
        ],
    },
    # 2. CODING & DATA LITERACY
    {
        "key": "coding", "color": "#0ea5e9", "color_bg": "#f0f9ff", "icon": "fas fa-code",
        "tab_label": "Coding & Data",
        "label": "Programming & Data Science",
        "title": "Coding & Data Literacy",
        "desc": "Learn to code, practise with real datasets, and build a portfolio — free courses, sandboxes and certifications.",
        "cards": [
            {"href":"https://cs50.harvard.edu", "title":"Harvard CS50", "icon":"fas fa-university", "pill":"free-signup", "audiences":["undergrad","self"], "top":True,
             "desc":"Harvard's legendary intro to CS — free videos, problem sets and a free certificate via edX audit. Still the best first CS course online."},
            {"href":"https://www.freecodecamp.org", "title":"freeCodeCamp", "icon":"fas fa-laptop-code", "pill":"free-signup", "audiences":["undergrad","self","switcher"],
             "desc":"Thousands of hours of hands-on coding lessons and free certifications — web dev, data analysis and machine learning."},
            {"href":"https://www.theodinproject.com", "title":"The Odin Project", "icon":"fas fa-dharmachakra", "pill":"free", "audiences":["self","switcher","adult"],
             "desc":"Free, full-stack web development curriculum used by self-taught devs landing real jobs — community-driven and battle-tested."},
            {"href":"https://www.codecademy.com", "title":"Codecademy", "icon":"fas fa-terminal", "pill":"freemium", "audiences":["all"],
             "desc":"Interactive browser-based coding lessons — Python, JS, SQL, HTML/CSS — with a solid free tier covering all the foundations."},
            {"href":"https://www.kaggle.com/learn", "title":"Kaggle Learn", "icon":"fas fa-database", "pill":"free-signup", "audiences":["undergrad","grad"],
             "desc":"Short, hands-on data-science and ML micro-courses — plus thousands of real datasets and competitions to practise on."},
            {"href":"https://colab.research.google.com", "title":"Google Colab", "icon":"fas fa-microchip", "pill":"free-signup", "audiences":["undergrad","grad"],
             "desc":"Free Jupyter notebooks in the browser with free GPU — perfect for ML, data science and research prototyping with no setup."},
            {"href":"https://www.fast.ai", "title":"fast.ai", "icon":"fas fa-bolt", "pill":"free", "audiences":["undergrad","grad","adult"],
             "desc":"Practical Deep Learning for Coders — a free top-down course that turns coders into deep-learning practitioners in seven weeks."},
            {"href":"https://www.datacamp.com", "title":"DataCamp Free", "icon":"fas fa-chart-line", "pill":"freemium", "audiences":["all"],
             "desc":"Free first chapters of every course — solid intro to Python, R, SQL and data visualisation with browser-based exercises."},
            {"href":"https://mode.com/sql-tutorial", "title":"Mode SQL Tutorial", "icon":"fas fa-table", "pill":"free", "audiences":["all"],
             "desc":"The clearest free SQL tutorial online — analytics-focused, with real datasets and a built-in editor in the browser."},
            {"href":"https://replit.com", "title":"Replit", "icon":"fas fa-play", "pill":"freemium", "audiences":["all"],
             "desc":"Code in 50+ languages directly in your browser — no setup, free hosting, instant collaboration and AI-assisted coding."},
            {"href":"https://exercism.org", "title":"Exercism", "icon":"fas fa-dumbbell", "pill":"free-signup", "audiences":["all"],
             "desc":"Free practice exercises in 70+ languages with mentor feedback — sharpen syntax and idioms beyond what tutorials cover."},
            {"href":"https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/", "title":"MIT 6.0001 Intro CS Python", "icon":"fas fa-graduation-cap", "pill":"free", "audiences":["undergrad"],
             "desc":"MIT's introduction to computer science using Python — free lectures, problem sets and exams from the campus course."},
        ],
    },
    # 3. CYBERSECURITY & DIGITAL PRIVACY
    {
        "key": "security", "color": "#dc2626", "color_bg": "#fef2f2", "icon": "fas fa-shield-halved",
        "tab_label": "Cybersecurity",
        "label": "Privacy & Online Safety",
        "title": "Cybersecurity & Digital Privacy",
        "desc": "Protect your accounts, data and identity online — and learn the security skills nobody else is teaching you.",
        "cards": [
            {"href":"https://bitwarden.com", "title":"Bitwarden", "icon":"fas fa-key", "pill":"free-signup", "audiences":["all"], "top":True,
             "desc":"Open-source password manager with a generous free tier — unlimited devices, passwords and end-to-end encryption."},
            {"href":"https://haveibeenpwned.com", "title":"Have I Been Pwned", "icon":"fas fa-skull-crossbones", "pill":"free", "audiences":["all"],
             "desc":"Free check whether your email or password has been exposed in a data breach — by security researcher Troy Hunt."},
            {"href":"https://signal.org", "title":"Signal", "icon":"fas fa-comment-dots", "pill":"free", "audiences":["all"],
             "desc":"Free end-to-end encrypted messenger — gold standard for private chats, voice and video. Used by journalists worldwide."},
            {"href":"https://2fas.com", "title":"2FAS Auth", "icon":"fas fa-mobile-screen", "pill":"free", "audiences":["all"],
             "desc":"Free open-source two-factor authentication app — far safer than SMS codes and protects your accounts even if passwords leak."},
            {"href":"https://www.torproject.org", "title":"Tor Browser", "icon":"fas fa-user-secret", "pill":"free", "audiences":["all"],
             "desc":"Free anonymity browser that routes traffic through volunteer relays — essential for journalists, activists and high-risk users."},
            {"href":"https://foundation.mozilla.org/privacynotincluded/", "title":"Privacy Not Included", "icon":"fas fa-lock", "pill":"free", "audiences":["all","adult"],
             "desc":"Mozilla's free buyer's guide grading the privacy of consumer tech — phones, smart speakers, mental-health apps. Easy to scan before you buy."},
            {"href":"https://ssd.eff.org", "title":"EFF Surveillance Self-Defense", "icon":"fas fa-eye-slash", "pill":"free", "audiences":["all","adult"],
             "desc":"Electronic Frontier Foundation's free guide to digital security — practical playbooks for students, activists and everyday users."},
            {"href":"https://tryhackme.com", "title":"TryHackMe", "icon":"fas fa-bug", "pill":"freemium", "audiences":["undergrad","self","switcher"],
             "desc":"Gamified cybersecurity training — free rooms cover networking, Linux and web security; the most beginner-friendly hacking platform."},
            {"href":"https://www.cybrary.it", "title":"Cybrary", "icon":"fas fa-shield-virus", "pill":"freemium", "audiences":["self","switcher"],
             "desc":"Free intro courses on cybersecurity fundamentals, ethical hacking and CompTIA Security+ exam preparation."},
            {"href":"https://www.cisa.gov/topics/cybersecurity-best-practices", "title":"CISA Cybersecurity", "icon":"fas fa-flag-usa", "pill":"free", "audiences":["all","adult"],
             "desc":"Free cybersecurity guidance from the US Cybersecurity & Infrastructure Security Agency — practical for individuals and small orgs."},
            {"href":"https://owasp.org", "title":"OWASP", "icon":"fas fa-spider", "pill":"free", "audiences":["undergrad","grad","switcher"],
             "desc":"Open Worldwide Application Security Project — free top-10 lists, cheatsheets and frameworks every web developer should know."},
            {"href":"https://cs155.stanford.edu", "title":"Stanford CS155", "icon":"fas fa-shield-alt", "pill":"free", "audiences":["grad","phd"],
             "desc":"Stanford's Computer and Network Security course — free lecture slides, notes and reading lists from a flagship program."},
        ],
    },
    # 4. CRITICAL THINKING
    {
        "key": "critical", "color": "#f59e0b", "color_bg": "#fef3c7", "icon": "fas fa-magnifying-glass-chart",
        "tab_label": "Critical Thinking",
        "label": "Reasoning & Information Literacy",
        "title": "Critical Thinking & Information Literacy",
        "desc": "Evaluate evidence, recognise bias and reason clearly under uncertainty — the WEF's #1 skill of the next decade.",
        "cards": [
            {"href":"https://www.callingbullshit.org", "title":"Calling Bullshit (UW)", "icon":"fas fa-bullhorn", "pill":"free", "audiences":["all"], "top":True,
             "desc":"Free University of Washington course on spotting BS in numbers, charts and stories — every video and reading openly online."},
            {"href":"https://www.khanacademy.org/math/statistics-probability", "title":"Khan Academy Statistics", "icon":"fas fa-chart-pie", "pill":"free-signup", "audiences":["undergrad","self","adult"],
             "desc":"Free, complete intro to statistics and probability — the literacy you need to question any chart you see in the news."},
            {"href":"https://www.allsides.com", "title":"AllSides", "icon":"fas fa-balance-scale", "pill":"free", "audiences":["all"],
             "desc":"Shows news headlines from left, centre and right side-by-side — calibrate your media diet and spot bias daily."},
            {"href":"https://ground.news", "title":"Ground News", "icon":"fas fa-globe", "pill":"freemium", "audiences":["all"],
             "desc":"Compares how the same story is covered across the political spectrum — free tier highlights blind spots and bias."},
            {"href":"https://www.snopes.com", "title":"Snopes", "icon":"fas fa-search", "pill":"free", "audiences":["all"],
             "desc":"The original fact-checking site — free, transparent verdicts on viral claims, urban legends and political rumours."},
            {"href":"https://www.bbc.co.uk/programmes/b006qshd", "title":"BBC More or Less", "icon":"fas fa-podcast", "pill":"free", "audiences":["all","adult"],
             "desc":"Tim Harford's free BBC podcast and articles unpicking the numbers behind the headlines — the most readable training in statistical thinking."},
            {"href":"https://www.coursera.org/learn/mindware", "title":"Coursera 'Mindware' (UMich)", "icon":"fas fa-lightbulb", "pill":"free-signup", "audiences":["undergrad","grad","adult"],
             "desc":"Richard Nisbett's free audit of the most useful concepts in psychology and statistics for everyday reasoning."},
            {"href":"https://www.readthesequences.com", "title":"LessWrong Sequences", "icon":"fas fa-cogs", "pill":"free", "audiences":["all"],
             "desc":"Free book-length intro to rationality — cognitive biases, probabilistic thinking, scientific reasoning and decision-making."},
            {"href":"https://yourlogicalfallacyis.com", "title":"Your Logical Fallacy Is", "icon":"fas fa-comment-slash", "pill":"free", "audiences":["all"],
             "desc":"Free interactive guide to 24 common logical fallacies — bookmark-worthy for spotting bad arguments online and offline."},
            {"href":"https://thedecisionlab.com", "title":"The Decision Lab", "icon":"fas fa-brain", "pill":"free", "audiences":["all","adult"],
             "desc":"Free encyclopaedia of cognitive biases and behavioural science — clear, well-illustrated explanations of how we think wrong."},
            {"href":"https://www.poynter.org/mediawise/", "title":"MediaWise", "icon":"fas fa-newspaper", "pill":"free-signup", "audiences":["all"],
             "desc":"Free media-literacy courses for teens and adults from the Poynter Institute — practical fact-checking with real-world examples."},
            {"href":"https://www.badscience.net", "title":"Bad Science (Goldacre)", "icon":"fas fa-vial", "pill":"free", "audiences":["all","adult"],
             "desc":"Ben Goldacre's free articles dismantling bad statistics in medicine and journalism — the canonical antidote to dodgy headlines."},
        ],
    },
    # 5. OPEN COURSEWARE
    {
        "key": "courseware", "color": "#3b82f6", "color_bg": "#eff6ff", "icon": "fas fa-graduation-cap",
        "tab_label": "Open Courseware",
        "label": "Lectures & MOOCs",
        "title": "Open Courseware & Lifelong Learning",
        "desc": "Full courses from MIT, Harvard, Stanford, Yale and other top universities — free to audit, learn anything from anywhere.",
        "cards": [
            {"href":"https://ocw.mit.edu", "title":"MIT OpenCourseWare", "icon":"fas fa-university", "pill":"free", "audiences":["undergrad","grad"], "top":True,
             "desc":"2,500+ MIT courses free — lecture notes, problem sets, exams, and often full video lectures from the world's top engineering school."},
            {"href":"https://www.coursera.org", "title":"Coursera (Audit)", "icon":"fas fa-chalkboard-teacher", "pill":"free-signup", "audiences":["undergrad","adult","switcher"],
             "desc":"Audit most courses from Stanford, Yale, Michigan and more for free — videos and readings included on the no-cost track."},
            {"href":"https://www.edx.org", "title":"edX", "icon":"fas fa-school", "pill":"free-signup", "audiences":["undergrad","grad","adult"],
             "desc":"Harvard, MIT, Berkeley courses — free to audit, with optional paid certificates and MicroMasters programs for credit."},
            {"href":"https://online.stanford.edu/free-courses", "title":"Stanford Online", "icon":"fas fa-landmark", "pill":"free-signup", "audiences":["undergrad","grad","adult"],
             "desc":"Curated free courses from Stanford faculty — AI, engineering, medicine, education and entrepreneurship."},
            {"href":"https://oyc.yale.edu", "title":"Open Yale Courses", "icon":"fas fa-book-reader", "pill":"free", "audiences":["undergrad","adult"],
             "desc":"Complete Yale undergraduate lectures — philosophy, economics, astronomy, literature — full video and reading lists."},
            {"href":"https://www.open.edu/openlearn", "title":"OpenLearn (UK)", "icon":"fas fa-globe-europe", "pill":"free-signup", "audiences":["undergrad","adult","switcher"],
             "desc":"Free courses from The Open University — 1,000+ topics with statements of participation available at no charge."},
            {"href":"https://www.saylor.org", "title":"Saylor Academy", "icon":"fas fa-certificate", "pill":"free-signup", "audiences":["undergrad","adult","switcher"],
             "desc":"Self-paced college courses with free certificates — some credit-eligible through ACE partnerships, no degree-fee required."},
            {"href":"https://oli.cmu.edu", "title":"CMU Open Learning Initiative", "icon":"fas fa-microscope", "pill":"free-signup", "audiences":["undergrad"],
             "desc":"Research-backed adaptive courses from Carnegie Mellon — statistics, psychology, biology and logic."},
            {"href":"https://www.khanacademy.org", "title":"Khan Academy", "icon":"fas fa-play-circle", "pill":"free-signup", "audiences":["undergrad","self","adult"],
             "desc":"Foundational courses with mastery tracking — calculus, linear algebra, physics, economics and exam prep, fully free."},
            {"href":"https://www.futurelearn.com", "title":"FutureLearn", "icon":"fas fa-users", "pill":"free-signup", "audiences":["undergrad","adult","switcher"],
             "desc":"Short free courses from European and Commonwealth universities — discussion-based learning with peers worldwide."},
            {"href":"https://www.classcentral.com", "title":"Class Central", "icon":"fas fa-compass", "pill":"free", "audiences":["all"],
             "desc":"Free search engine for 200,000+ MOOCs — the easiest way to find the best free version of any course on the web."},
            {"href":"https://www.coursera.org/learn/learning-how-to-learn", "title":"Learning How to Learn", "icon":"fas fa-brain", "pill":"free-signup", "audiences":["all","adult"],
             "desc":"The most-popular MOOC ever — free auditable course on meta-learning, focused practice and beating procrastination."},
        ],
    },
    # 6. RESEARCH & CITATION
    {
        "key": "research", "color": "#16a34a", "color_bg": "#f0fdf4", "icon": "fas fa-flask",
        "tab_label": "Research",
        "label": "Finding & Citing Sources",
        "title": "Research, Citation & Open Knowledge",
        "desc": "Discover peer-reviewed papers, manage citations, and read free open textbooks — everything for your thesis or paper, free.",
        "cards": [
            {"href":"https://scholar.google.com", "title":"Google Scholar", "icon":"fas fa-search", "pill":"free", "audiences":["all"], "top":True,
             "desc":"The largest free academic search engine — papers, citations, and often direct links to free PDFs across every discipline."},
            {"href":"https://www.zotero.org", "title":"Zotero", "icon":"fas fa-bookmark", "pill":"free", "audiences":["all"],
             "desc":"Free, open-source reference manager — capture any source with one click and auto-format bibliographies in any style."},
            {"href":"https://www.semanticscholar.org", "title":"Semantic Scholar", "icon":"fas fa-brain", "pill":"free-signup", "audiences":["grad","phd"],
             "desc":"AI-powered academic search from the Allen Institute — surfaces influential citations and related work for any paper."},
            {"href":"https://www.connectedpapers.com", "title":"Connected Papers", "icon":"fas fa-project-diagram", "pill":"freemium", "audiences":["grad","phd"],
             "desc":"Visual graph of papers related to any key article — a literature-review game changer for thesis and review work."},
            {"href":"https://core.ac.uk", "title":"CORE", "icon":"fas fa-database", "pill":"free", "audiences":["all"],
             "desc":"World's largest aggregator of open-access research — 300 million papers across 11,000 repositories, fully searchable."},
            {"href":"https://pubmed.ncbi.nlm.nih.gov", "title":"PubMed", "icon":"fas fa-heartbeat", "pill":"free", "audiences":["undergrad","grad"],
             "desc":"Free NIH database of 35M+ biomedical citations — essential for life sciences, medicine and psychology."},
            {"href":"https://doaj.org", "title":"DOAJ", "icon":"fas fa-journal-whills", "pill":"free", "audiences":["all"],
             "desc":"Directory of Open Access Journals — 20,000+ vetted peer-reviewed journals with free full text, no paywalls."},
            {"href":"https://openstax.org", "title":"OpenStax", "icon":"fas fa-atlas", "pill":"free", "audiences":["undergrad"],
             "desc":"Rice University's free peer-reviewed textbooks — biology, physics, economics, sociology and calculus, fully downloadable."},
            {"href":"https://libretexts.org", "title":"LibreTexts", "icon":"fas fa-book", "pill":"free", "audiences":["undergrad","grad"],
             "desc":"The largest open-textbook library — chemistry, engineering, humanities and medicine, freely remixable for educators."},
            {"href":"https://arxiv.org", "title":"arXiv", "icon":"fas fa-file-alt", "pill":"free", "audiences":["grad","phd"],
             "desc":"Free preprint server for physics, math, CS and quantitative biology — see new research months before formal publication."},
            {"href":"https://www.gutenberg.org", "title":"Project Gutenberg", "icon":"fas fa-scroll", "pill":"free", "audiences":["all"],
             "desc":"75,000+ free classic books in the public domain — ideal for literature, history and philosophy courses."},
            {"href":"https://archive.org", "title":"Internet Archive", "icon":"fas fa-landmark", "pill":"free", "audiences":["all"],
             "desc":"Millions of free books, academic papers and historic documents — including the Open Library lending service."},
        ],
    },
    # 7. WRITING, COMMUNICATION & PUBLIC SPEAKING
    {
        "key": "writing", "color": "#f97316", "color_bg": "#fff7ed", "icon": "fas fa-pen-fancy",
        "tab_label": "Writing & Speaking",
        "label": "Essays, Comms & Voice",
        "title": "Writing, Communication & Public Speaking",
        "desc": "Write cleaner essays, present with confidence, and translate clearly — the human complement to AI assistance.",
        "cards": [
            {"href":"https://www.grammarly.com", "title":"Grammarly", "icon":"fas fa-spell-check", "pill":"freemium", "audiences":["all"], "top":True,
             "desc":"Real-time grammar, spelling and clarity checks in your browser or Word — the free tier covers all the daily-use essentials."},
            {"href":"https://hemingwayapp.com", "title":"Hemingway Editor", "icon":"fas fa-highlighter", "pill":"free", "audiences":["all"],
             "desc":"Highlights convoluted sentences, passive voice and adverbs — makes academic and professional writing dramatically clearer."},
            {"href":"https://languagetool.org", "title":"LanguageTool", "icon":"fas fa-language", "pill":"freemium", "audiences":["all"],
             "desc":"Open-source grammar checker supporting 30+ languages — strong free tier, ideal for essays in German, French and Spanish."},
            {"href":"https://www.overleaf.com", "title":"Overleaf", "icon":"fas fa-file-code", "pill":"freemium", "audiences":["undergrad","grad","phd"],
             "desc":"Online LaTeX editor — collaborative thesis and paper writing with live preview and journal templates, free tier covers most students."},
            {"href":"https://typst.app", "title":"Typst", "icon":"fas fa-bolt", "pill":"free-signup", "audiences":["undergrad","grad"],
             "desc":"Modern open-source alternative to LaTeX — faster compile, cleaner syntax, still produces beautiful PDFs for academic work."},
            {"href":"https://owl.purdue.edu", "title":"Purdue OWL", "icon":"fas fa-feather", "pill":"free", "audiences":["undergrad","adult"],
             "desc":"The web's most-used free writing reference — APA/MLA/Chicago style guides, grammar tips and academic-writing playbooks."},
            {"href":"https://ed.ted.com/topics/public-speaking-and-presentation", "title":"TED-Ed Public Speaking", "icon":"fas fa-microphone", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free TED-Ed lessons on public speaking, storytelling and presentation — taught by people who actually deliver TED talks."},
            {"href":"https://www.toastmasters.org", "title":"Toastmasters", "icon":"fas fa-users-rectangle", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"World's largest public-speaking community — many local clubs let you visit free, with structured pathways for growth."},
            {"href":"https://www.coursera.org/specializations/good-with-words", "title":"UMich 'Good with Words'", "icon":"fas fa-pen", "pill":"free-signup", "audiences":["undergrad","adult"],
             "desc":"Free-to-audit specialisation by Patrick Barry on writing and editing for persuasion — practical for essays, applications and pitches."},
            {"href":"https://yoodli.ai", "title":"Yoodli", "icon":"fas fa-microphone-alt", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free AI speech coach — practise presentations on video and get feedback on filler words, pace, clarity and confidence."},
            {"href":"https://docs.google.com", "title":"Google Docs", "icon":"fas fa-file-alt", "pill":"free-signup", "audiences":["all"],
             "desc":"Free collaborative word processor with real-time editing, comments, version history and voice typing — universal for student work."},
            {"href":"https://www.deepl.com/write", "title":"DeepL Write", "icon":"fas fa-magic", "pill":"free", "audiences":["all","adult"],
             "desc":"Free AI writing assistant from DeepL — rewrites for tone and clarity in English, German and other major languages."},
        ],
    },
    # 8. PRODUCTIVITY, FOCUS & DEEP WORK
    {
        "key": "productivity", "color": "#ec4899", "color_bg": "#fdf2f8", "icon": "fas fa-bullseye",
        "tab_label": "Productivity",
        "label": "Notes, Focus, Deadlines",
        "title": "Productivity, Focus & Deep Work",
        "desc": "Note systems, task managers and focus tools to win back your attention — the prerequisite for everything else.",
        "cards": [
            {"href":"https://www.notion.so/students", "title":"Notion (Students)", "icon":"fas fa-layer-group", "pill":"free-signup", "audiences":["all"], "top":True,
             "desc":"Free Plus plan for students with .edu email — notes, databases, task lists and wikis all in one workspace."},
            {"href":"https://obsidian.md", "title":"Obsidian", "icon":"fas fa-network-wired", "pill":"free", "audiences":["all"],
             "desc":"Local-first markdown note-taking with back-links — the best free tool for building a personal academic knowledge graph."},
            {"href":"https://apps.ankiweb.net", "title":"Anki", "icon":"fas fa-clone", "pill":"free", "audiences":["all"],
             "desc":"Free open-source spaced-repetition flashcards — used by med students and language learners worldwide; the proven memory tool."},
            {"href":"https://todoist.com", "title":"Todoist", "icon":"fas fa-check-square", "pill":"freemium", "audiences":["all"],
             "desc":"Clean task manager that handles recurring assignments and deadlines across all your devices — free tier handles most workflows."},
            {"href":"https://www.forestapp.cc", "title":"Forest", "icon":"fas fa-tree", "pill":"freemium", "audiences":["all"],
             "desc":"Gamified focus timer — plant a virtual tree that dies if you leave the app. Free web version reliably blocks distractions."},
            {"href":"https://pomofocus.io", "title":"Pomofocus", "icon":"fas fa-stopwatch", "pill":"free", "audiences":["all"],
             "desc":"Simple free Pomodoro timer — start focused 25-minute sessions in your browser with no signup or setup."},
            {"href":"https://getcoldturkey.com", "title":"Cold Turkey Blocker", "icon":"fas fa-ban", "pill":"freemium", "audiences":["all","adult","switcher"],
             "desc":"Free site and app blocker that's actually hard to bypass — schedule deep-work blocks that even you can't override."},
            {"href":"https://www.calnewport.com", "title":"Cal Newport's Deep Work", "icon":"fas fa-headset", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free essays, podcasts and guides from the author of Deep Work — practical playbooks for sustained, distraction-free focus."},
            {"href":"https://logseq.com", "title":"Logseq", "icon":"fas fa-diagram-project", "pill":"free", "audiences":["all"],
             "desc":"Open-source local-first knowledge graph — daily notes, outlines and back-links; a free, privacy-respecting Roam alternative."},
            {"href":"https://trello.com", "title":"Trello", "icon":"fas fa-columns", "pill":"freemium", "audiences":["all"],
             "desc":"Free Kanban-style project boards — visual task management for group projects, theses and side projects."},
            {"href":"https://calendar.google.com", "title":"Google Calendar", "icon":"fas fa-calendar-alt", "pill":"free-signup", "audiences":["all"],
             "desc":"Free time-blocking calendar with shared events and natural-language input — the backbone of any deep-work practice."},
            {"href":"https://toggl.com/track/", "title":"Toggl Track", "icon":"fas fa-hourglass-half", "pill":"freemium", "audiences":["all","adult","switcher"],
             "desc":"Free time-tracking app with one-click timers — see where your study hours actually go and design better routines."},
        ],
    },
    # 9. MENTAL HEALTH & RESILIENCE
    {
        "key": "mental", "color": "#14b8a6", "color_bg": "#f0fdfa", "icon": "fas fa-heart-pulse",
        "tab_label": "Mental Health",
        "label": "Wellbeing & Resilience",
        "title": "Mental Health & Resilience",
        "desc": "Sleep, stress, anxiety and mood — free, evidence-based resources to support the most important asset you have.",
        "cards": [
            {"href":"https://www.coursera.org/learn/the-science-of-well-being", "title":"Yale 'Science of Well-Being'", "icon":"fas fa-sun", "pill":"free-signup", "audiences":["all"], "top":True,
             "desc":"Yale's most-popular course ever — free to audit, taught by Laurie Santos, covering the psychology of happiness with daily practices."},
            {"href":"https://www.headspace.com/studentplan", "title":"Headspace for Students", "icon":"fas fa-cloud", "pill":"free-signup", "audiences":["undergrad","grad"],
             "desc":"Free Headspace Plus for students at over 1,000 universities — guided meditations, sleep stories and stress courses."},
            {"href":"https://www.calm.com", "title":"Calm", "icon":"fas fa-spa", "pill":"freemium", "audiences":["all"],
             "desc":"Free guided meditations, breathing exercises and sleep stories — the basics of mindfulness without the paywall."},
            {"href":"https://moodgym.com.au", "title":"MoodGym", "icon":"fas fa-dumbbell", "pill":"free-signup", "audiences":["all","adult"],
             "desc":"Free CBT-based program from Australian National University — proven to reduce symptoms of depression and anxiety."},
            {"href":"https://woebothealth.com", "title":"Woebot", "icon":"fas fa-robot", "pill":"free-signup", "audiences":["all","adult"],
             "desc":"Free chatbot-based mental-health support — uses CBT techniques to help with mood, anxiety and stressful thinking."},
            {"href":"https://www.nhs.uk/every-mind-matters/", "title":"NHS Every Mind Matters", "icon":"fas fa-hospital", "pill":"free", "audiences":["all","adult"],
             "desc":"Free UK National Health Service mental-health hub — practical advice for anxiety, sleep, low mood and stress."},
            {"href":"https://self-compassion.org", "title":"Self-Compassion (Kristin Neff)", "icon":"fas fa-hand-holding-heart", "pill":"free", "audiences":["all","adult"],
             "desc":"Kristin Neff's free meditations and exercises — research-backed self-compassion practices proven to build resilience."},
            {"href":"https://insighttimer.com", "title":"Insight Timer", "icon":"fas fa-bell", "pill":"free-signup", "audiences":["all"],
             "desc":"The largest free meditation app — 200,000+ free guided meditations, talks and music from teachers worldwide."},
            {"href":"https://www.7cups.com", "title":"7 Cups", "icon":"fas fa-mug-hot", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free emotional support from trained listeners — 24/7 anonymous chats, plus low-cost online therapy if you need more."},
            {"href":"https://www.crisistextline.org", "title":"Crisis Text Line", "icon":"fas fa-phone", "pill":"free", "audiences":["all"],
             "desc":"Free 24/7 crisis support by text — confidential, trained counsellors in the US, UK, Ireland and Canada."},
            {"href":"https://healthysleep.med.harvard.edu", "title":"Harvard Healthy Sleep", "icon":"fas fa-moon", "pill":"free", "audiences":["all","adult"],
             "desc":"Free Harvard Medical School educational resource on sleep biology, hygiene and disorders — clear, evidence-based and accessible."},
            {"href":"https://actionforhappiness.org", "title":"Action for Happiness", "icon":"fas fa-smile", "pill":"free", "audiences":["all","adult"],
             "desc":"Free monthly calendars of evidence-based daily actions — small, sustainable habits proven to lift mood and resilience."},
        ],
    },
    # 10. PERSONAL FINANCE
    {
        "key": "finance", "color": "#84cc16", "color_bg": "#f7fee7", "icon": "fas fa-coins",
        "tab_label": "Personal Finance",
        "label": "Money, Taxes, Investing",
        "title": "Personal Finance & Economic Literacy",
        "desc": "Budgeting, taxes, compound interest and investing basics — the financial skills schools rarely teach but you need by 25.",
        "cards": [
            {"href":"https://www.khanacademy.org/college-careers-more/personal-finance", "title":"Khan Academy Personal Finance", "icon":"fas fa-wallet", "pill":"free-signup", "audiences":["all"], "top":True,
             "desc":"Free, complete personal-finance course — taxes, credit, investing, retirement and real estate, taught at high-school clarity."},
            {"href":"https://www.investopedia.com", "title":"Investopedia", "icon":"fas fa-book-open", "pill":"freemium", "audiences":["all"],
             "desc":"Free encyclopaedia of finance and investing — 30,000+ articles plus a free simulator for paper-trading stocks risk-free."},
            {"href":"https://www.nerdwallet.com", "title":"NerdWallet", "icon":"fas fa-money-check-alt", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free guides comparing credit cards, student loans, savings accounts and investment platforms — vendor-independent advice."},
            {"href":"https://www.bogleheads.org/wiki/", "title":"Bogleheads Wiki", "icon":"fas fa-chart-line", "pill":"free", "audiences":["all","adult"],
             "desc":"Free community wiki on low-cost index investing — based on John Bogle's principles, the gold standard for passive investors."},
            {"href":"https://www.consumerfinance.gov/consumer-tools/", "title":"CFPB Tools", "icon":"fas fa-landmark", "pill":"free", "audiences":["all","adult"],
             "desc":"Free tools and guides from the US Consumer Financial Protection Bureau — student loans, credit, scams and money basics."},
            {"href":"https://moneysmart.gov.au", "title":"MoneySmart", "icon":"fas fa-piggy-bank", "pill":"free", "audiences":["all","adult"],
             "desc":"Free Australian government finance hub — calculators, guides and budget tools usable internationally."},
            {"href":"https://www.coursera.org/learn/financial-markets", "title":"Yale 'Financial Markets'", "icon":"fas fa-university", "pill":"free-signup", "audiences":["undergrad","grad","adult"],
             "desc":"Robert Shiller's Nobel-laureate free course — auditable on Coursera, covers risk, behavioural finance and modern markets."},
            {"href":"https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/", "title":"MIT 15.401 Finance Theory", "icon":"fas fa-flask", "pill":"free", "audiences":["undergrad","grad"],
             "desc":"MIT Sloan's intro to finance theory — free lectures and problem sets covering valuation, portfolios and capital markets."},
            {"href":"https://www.youtube.com/@thefinancialdiet", "title":"The Financial Diet", "icon":"fab fa-youtube", "pill":"free", "audiences":["all","adult"],
             "desc":"Free practical money videos for young adults — budgeting, investing, salary negotiation and lifestyle inflation, all jargon-free."},
            {"href":"https://www.getrichslowly.org", "title":"Get Rich Slowly", "icon":"fas fa-seedling", "pill":"free", "audiences":["all","adult"],
             "desc":"Free 15+ years of accessible personal-finance writing by JD Roth — debt payoff, savings, investing and mindful spending."},
            {"href":"https://www.mrmoneymustache.com", "title":"Mr. Money Mustache", "icon":"fas fa-fire", "pill":"free", "audiences":["all","adult"],
             "desc":"Free essays on financial independence and frugality — the founding text of the FIRE movement, opinionated but practical."},
            {"href":"https://www.youneedabudget.com/students/", "title":"YNAB (Students)", "icon":"fas fa-clipboard-list", "pill":"free-signup", "audiences":["undergrad","grad"],
             "desc":"Free 12-month YNAB subscription for university students — the most-loved budgeting method, with classes included."},
        ],
    },
    # 11. CAREER, NETWORKING & ENTREPRENEURSHIP
    {
        "key": "career", "color": "#8b5cf6", "color_bg": "#f5f3ff", "icon": "fas fa-briefcase",
        "tab_label": "Career & Entrepreneurship",
        "chip_label": "Career",
        "label": "Job, Networking, Founding",
        "title": "Career, Networking & Entrepreneurship",
        "desc": "Land internships, switch careers, freelance, or start a company — the practical skills for portfolio-career life.",
        "cards": [
            {"href":"https://www.startupschool.org", "title":"YC Startup School", "icon":"fas fa-rocket", "pill":"free-signup", "audiences":["all","switcher"], "top":True,
             "desc":"Free 10-week course from the world's top accelerator — 1M+ founders trained, with library of YC essays and talks."},
            {"href":"https://www.linkedin.com/learning/", "title":"LinkedIn Learning", "icon":"fab fa-linkedin", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Many public libraries grant free LinkedIn Learning access — thousands of courses on careers, tools and soft skills."},
            {"href":"https://resumeworded.com", "title":"Resume Worded", "icon":"fas fa-file-signature", "pill":"free-signup", "audiences":["undergrad","grad","switcher"],
             "desc":"Free AI resume and LinkedIn profile feedback — built by ex-recruiters, scores your CV against real hiring rubrics."},
            {"href":"https://standout-cv.com", "title":"Standout CV", "icon":"fas fa-file-alt", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free downloadable CV templates and writing guides — practical for first jobs, internships and career switchers."},
            {"href":"https://www.themuse.com/advice", "title":"The Muse Career Advice", "icon":"fas fa-comments", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free archive of career articles — interview prep, salary negotiation, navigating workplace politics and switching careers."},
            {"href":"https://www.levels.fyi", "title":"Levels.fyi", "icon":"fas fa-dollar-sign", "pill":"free-signup", "audiences":["undergrad","grad","switcher"],
             "desc":"Free salary data crowdsourced from real offers — see what tech, finance and consulting roles actually pay before you negotiate."},
            {"href":"https://www.glassdoor.com", "title":"Glassdoor", "icon":"fas fa-building", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free reviews, salary ranges and interview questions for thousands of companies — the standard read before any interview."},
            {"href":"https://80000hours.org", "title":"80,000 Hours", "icon":"fas fa-compass", "pill":"free", "audiences":["undergrad","grad","adult","switcher"],
             "desc":"Free career advice focused on doing the most good with your work — research-driven guides on impactful career paths."},
            {"href":"https://startupclass.samaltman.com", "title":"Stanford How to Start a Startup", "icon":"fas fa-chalkboard", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free Stanford CS183B taught by Sam Altman and Y Combinator partners — 20 free lectures on building a startup from zero."},
            {"href":"https://www.indiehackers.com", "title":"Indie Hackers", "icon":"fas fa-laptop-house", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free community of bootstrapped founders — interviews, podcasts and forum threads on building profitable side businesses."},
            {"href":"https://academy.hubspot.com", "title":"HubSpot Academy", "icon":"fas fa-bullhorn", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free certifications in marketing, sales, content and SEO — recognised by employers, completed online in a few hours each."},
            {"href":"https://www.coursera.org/google-career-certificates", "title":"Google Career Certificates", "icon":"fab fa-google", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free-to-audit Google certificates in IT support, data analytics, UX and project management — recognised by 150+ employers."},
        ],
    },
    # 12. CIVIC, MEDIA & CLIMATE LITERACY
    {
        "key": "civic", "color": "#06b6d4", "color_bg": "#ecfeff", "icon": "fas fa-globe",
        "tab_label": "Civic, Media & Climate",
        "chip_label": "Civic & Climate",
        "label": "Citizenship & Sustainability",
        "title": "Civic, Media & Climate Literacy",
        "desc": "Big-picture citizenship — understand democracy, evaluate media, grasp climate science and the ethics of technology.",
        "cards": [
            {"href":"https://ourworldindata.org", "title":"Our World in Data", "icon":"fas fa-chart-area", "pill":"free", "audiences":["all"], "top":True,
             "desc":"Free, openly licensed data visualisations on the world's biggest issues — climate, poverty and health — built by Oxford researchers."},
            {"href":"https://climate.mit.edu", "title":"MIT Climate Portal", "icon":"fas fa-cloud-sun", "pill":"free", "audiences":["all"],
             "desc":"Free MIT-curated explainers on climate change — the science, the solutions, the policy — accessible and rigorously sourced."},
            {"href":"https://drawdown.org", "title":"Project Drawdown", "icon":"fas fa-leaf", "pill":"free", "audiences":["all","adult"],
             "desc":"Free, ranked list of the most effective climate solutions — searchable database with deep technical analyses for each."},
            {"href":"https://yaleclimateconnections.org", "title":"Yale Climate Connections", "icon":"fas fa-tree", "pill":"free", "audiences":["all","adult"],
             "desc":"Free daily climate journalism from Yale — accurate, accessible reporting on climate science, impacts and solutions."},
            {"href":"https://www.khanacademy.org/humanities/us-government-and-civics", "title":"Khan Academy Civics", "icon":"fas fa-flag", "pill":"free-signup", "audiences":["undergrad","adult"],
             "desc":"Free, complete intro to US civics — Constitution, branches, elections — useful even for non-US students learning democracy basics."},
            {"href":"https://www.icivics.org", "title":"iCivics", "icon":"fas fa-gavel", "pill":"free-signup", "audiences":["all","adult"],
             "desc":"Free games and lessons on democratic participation — built by Justice O'Connor, used in 50,000+ classrooms."},
            {"href":"https://www.scu.edu/ethics/", "title":"Markkula Ethics Center", "icon":"fas fa-balance-scale-right", "pill":"free", "audiences":["all","adult"],
             "desc":"Santa Clara University's free ethics resource hub — frameworks for thinking through tech, business, AI and biomedical ethics."},
            {"href":"https://hai.stanford.edu", "title":"Stanford HAI", "icon":"fas fa-microscope", "pill":"free", "audiences":["grad","phd","adult"],
             "desc":"Free reports, primers and policy briefs from Stanford's Human-Centered AI Institute — the leading source on AI's societal impact."},
            {"href":"https://www.bellingcat.com/resources/how-tos/", "title":"Bellingcat Toolkit", "icon":"fas fa-search-location", "pill":"free", "audiences":["all","adult","switcher"],
             "desc":"Free open-source-investigation playbook — verify videos, geolocate photos and fact-check viral claims like the pros."},
            {"href":"https://www.solutionsjournalism.org", "title":"Solutions Journalism Network", "icon":"fas fa-lightbulb", "pill":"free", "audiences":["all","adult"],
             "desc":"Free archive of evidence-based reporting on what's working — antidote to doom-scrolling, focuses on responses to social problems."},
            {"href":"https://www.eff.org/issues", "title":"EFF Civil Liberties", "icon":"fas fa-fist-raised", "pill":"free", "audiences":["all","adult"],
             "desc":"Electronic Frontier Foundation's free guides on free speech, surveillance and digital rights — the leading digital civil liberties group."},
            {"href":"https://www.unsdglearn.org", "title":"UN SDG Learn", "icon":"fas fa-globe-americas", "pill":"free-signup", "audiences":["all","adult","switcher"],
             "desc":"Free courses on the UN Sustainable Development Goals — climate, equality, poverty and governance, taught by UN agencies and partners."},
        ],
    },
]

assert len(SECTIONS) == 12, f"Expected 12 sections, got {len(SECTIONS)}"
for s in SECTIONS:
    assert len(s["cards"]) == 12, f"Section {s['key']} has {len(s['cards'])} cards, expected 12"

# ---------------- Templates ----------------
def domain_of(href):
    return href.split("//")[-1].split("/")[0].replace("www.", "")

_CARD_COUNTER = [0]
CARD_DESC_KEYS = {}  # cd_uni_NNN -> EN description

def render_card(c):
    pill_text = PILL_LABELS[c["pill"]]
    pill_class = PILL_CLASS[c["pill"]]
    badges = "".join(
        f'<span class="grade-badge {AUD_CLASS[a]}">{AUD_LABELS[a]}</span>'
        for a in c["audiences"]
    )
    top = '\n            <span class="top-pick-badge"><i class="fas fa-star"></i> Top Pick</span>' if c.get("top") else ''
    cd_key = f"cd_uni_{_CARD_COUNTER[0]:03d}"
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

def render_section(s, is_first):
    panel_active = " active" if is_first else ""
    hidden_attr = "" if is_first else " hidden"
    cards_html = "".join(render_card(c) for c in s["cards"])
    return (
        f'\n    <!-- ═══════════════════ {s["title"].upper()} ═══════════════════ -->\n'
        f'    <section id="{s["key"]}" class="panel sec-{s["key"]}{panel_active}" role="tabpanel" aria-labelledby="tab-{s["key"]}"{hidden_attr}>\n'
        f'      <div class="container">\n'
        f'        <div class="subject-header">\n'
        f'          <div class="subject-icon" style="background:{s["color_bg"]};color:{s["color"]}"><i class="{s["icon"]}"></i></div>\n'
        f'          <div class="subject-header-text">\n'
        f'            <span class="section-label section-label-orange" data-i18n="uni.sec.{s["key"]}.label">{s["label"]}</span>\n'
        f'            <h2 data-i18n="uni.sec.{s["key"]}.h2">{s["title"]}</h2>\n'
        f'            <p data-i18n="uni.sec.{s["key"]}.desc">{s["desc"]}</p>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'        <div class="resource-grid">{cards_html}\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </section>'
    )

def render_chip(s, is_first):
    chip_label = s.get("chip_label", s["tab_label"])
    active_cls = " chip-active" if is_first else ""
    aria_sel = "true" if is_first else "false"
    return (
        f'      <button type="button" class="subject-tab{active_cls}" role="tab" data-tab="{s["key"]}" '
        f'aria-selected="{aria_sel}" aria-controls="{s["key"]}" '
        f'style="--chip-color:{s["color"]}">'
        f'<i class="{s["icon"]} chip-icon"></i> '
        f'<span data-i18n="uni.chip.{s["key"]}">{chip_label}</span></button>'
    )

def render_sec_css():
    """Per-section card border + icon background colors."""
    rules = []
    for s in SECTIONS:
        rules.append(f'    .sec-{s["key"]}  .resource-card {{ border-top-color: {s["color"]}; }}')
    for s in SECTIONS:
        rules.append(f'    .sec-{s["key"]}  .resource-card:hover {{ border-color: {s["color"]}; }}')
    for s in SECTIONS:
        rules.append(f'    .sec-{s["key"]}  .card-icon {{ background: {s["color_bg"]}; color: {s["color"]}; }}')
    return "\n".join(rules)

# ---------------- Build the full HTML ----------------
chips_html = "\n".join(render_chip(s, i == 0) for i, s in enumerate(SECTIONS))
sections_html = "\n".join(render_section(s, i == 0) for i, s in enumerate(SECTIONS))
sec_css = render_sec_css()

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="144 free curated tools across 12 future-skill clusters for university students and lifelong learners — AI fluency, coding, critical thinking, mental health, finance, careers and more.">
  <meta name="keywords" content="free university resources, future skills, AI fluency, critical thinking, personal finance, mental health, career resources, MIT OpenCourseWare, Khan Academy, free MOOCs">
  <meta name="author" content="CTWP Educational Empowerment">
  <meta name="robots" content="index, follow">
  <title>Free University & Lifelong-Learner Resources | CTWP Educational Empowerment</title>
  <link rel="canonical" href="https://www.ctwp-education.eu.org/university.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.ctwp-education.eu.org/university.html">
  <meta property="og:site_name" content="CTWP Educational Empowerment">
  <meta property="og:title" content="Free University & Lifelong-Learner Resources | CTWP Educational Empowerment">
  <meta property="og:description" content="144 free tools across 12 future-skill clusters for students and lifelong learners.">
  <meta property="og:image" content="https://www.ctwp-education.eu.org/assets/images/Malawi_Salima_Classroom.webp">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Free University & Lifelong-Learner Resources | CTWP Educational Empowerment">
  <meta name="twitter:description" content="144 free tools across 12 future-skill clusters.">
  <meta name="twitter:image" content="https://www.ctwp-education.eu.org/assets/images/Malawi_Salima_Classroom.webp">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{"@type": "WebPage", "@id": "https://www.ctwp-education.eu.org/university.html", "url": "https://www.ctwp-education.eu.org/university.html", "name": "Free University & Lifelong-Learner Resources", "description": "144 free tools across 12 future-skill clusters.", "isPartOf": {{"@id": "https://www.ctwp-education.eu.org/"}}, "publisher": {{"@type": "NGO", "name": "CTWP Educational Empowerment", "url": "https://www.ctwp-education.eu.org/"}}}},
      {{"@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ctwp-education.eu.org/"}}, {{"@type": "ListItem", "position": 2, "name": "University & Lifelong-Learner Resources", "item": "https://www.ctwp-education.eu.org/university.html"}}]}}
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

    /* ── Skill Picker (chip grid) ─────────── */
    .skill-picker {{
      background: var(--cream, #f8f5ef);
      padding: 2rem 0 1.6rem;
      border-bottom: 1px solid var(--gray-200);
    }}
    .skill-picker-heading {{
      text-align: center;
      max-width: 720px;
      margin: 0 auto 1.4rem;
      padding: 0 1.5rem;
    }}
    .skill-picker-heading .section-label {{
      margin-bottom: 0.75rem;
      padding: 0.3rem 0.9rem;
      border-radius: var(--radius-full);
    }}
    .skill-picker-heading h2 {{
      font-family: var(--font-display);
      font-size: clamp(1.4rem, 2.4vw, 1.75rem);
      font-weight: 400;
      color: var(--gray-900);
      line-height: 1.3;
      margin: 0;
    }}
    .skill-picker-heading h2 em {{
      font-style: italic;
      color: var(--green-700);
    }}
    .skill-picker-inner {{
      display: grid;
      grid-template-columns: repeat(6, 165px);
      justify-content: center;
      gap: 0.65rem;
      max-width: 100%;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}
    .subject-tab {{
      height: 2.6rem;
      min-width: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0 0.9rem;
      font-family: var(--font-body);
      font-size: 0.78rem;
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
      opacity: 0.7;
      color: var(--chip-color, currentColor);
    }}
    .subject-tab:not(.chip-active):hover .chip-icon {{ opacity: 1; }}
    .subject-tab.chip-active .chip-icon {{ opacity: 1; color: currentColor; }}

    /* ── Filter Bar ──────────────────────────────── */
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
      content: "No tools match the current filter — try a different audience.";
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

    /* ── Pricing Pills + Card Pills row ───────────────────────────────── */
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

    @media (max-width: 1080px) {{
      .skill-picker-inner {{ grid-template-columns: repeat(4, 165px); }}
    }}
    @media (max-width: 780px) {{
      .skill-picker-inner {{ grid-template-columns: repeat(3, 150px); }}
    }}
    @media (max-width: 560px) {{
      .skill-picker-inner {{ grid-template-columns: repeat(2, 1fr); padding: 0 1rem; gap: 0.5rem; }}
      .subject-tab {{ font-size: 0.74rem; padding: 0 0.5rem; height: 2.5rem; }}
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
        <i class="fas fa-arrow-left"></i> <span data-i18n="sub.uni.back">Back to Resources</span>
      </a>
      <div class="hero-badge"><span data-i18n="sub.uni.badge">Future-Skill Tools for Higher Ed &amp; Lifelong Learners</span></div>
      <h1 data-i18n="sub.uni.title">Resources for University Students &amp; Lifelong Learners</h1>
      <p data-i18n="sub.uni.desc">144 curated free tools across 12 future-skill clusters. Pick a topic below to explore the 12 best resources.</p>
      <div class="hero-stats">
        <div class="hero-stat"><strong>144</strong><span data-i18n="uni.stat.tools">Free Tools</span></div>
        <div class="hero-stat"><strong>12</strong><span data-i18n="uni.stat.topics">Future-Skill Topics</span></div>
        <div class="hero-stat"><strong data-i18n="uni.stat.levels.val">Undergrad→Adult</strong><span data-i18n="uni.stat.levels.lbl">All Levels</span></div>
        <div class="hero-stat"><strong>100%</strong><span data-i18n="uni.stat.free">Free</span></div>
      </div>
    </div>
  </section>

  <!-- ── Skill Picker (12 chips) ── -->
  <nav class="skill-picker" role="tablist" aria-label="Choose a future-skill cluster">
    <div class="skill-picker-heading">
      <span class="section-label section-label-orange" data-i18n="uni.picker.label">Explore by Skill</span>
      <h2 data-i18n-html="uni.picker.heading">Choose one of the <em>12 future-skill clusters</em> to discover the best free tools</h2>
    </div>
    <div class="skill-picker-inner">
{chips_html}
    </div>
  </nav>

  <!-- ── Filter Bar (audience) ── -->
  <div class="filter-bar" id="filterBar">
    <div class="filter-bar-inner">
      <div class="filter-group">
        <span class="filter-label" data-i18n="uni.filter.label">Filter by audience:</span>
        <button class="filter-btn filter-active" data-filter="audience" data-value="all" data-i18n="uni.filter.all">All Audiences</button>
        <button class="filter-btn" data-filter="audience" data-value="undergrad" data-i18n="uni.grade.undergrad">Undergrad</button>
        <button class="filter-btn" data-filter="audience" data-value="grad" data-i18n="uni.grade.grad">Grad</button>
        <button class="filter-btn" data-filter="audience" data-value="phd" data-i18n="uni.grade.phd">PhD</button>
        <button class="filter-btn" data-filter="audience" data-value="self" data-i18n="uni.grade.self">Self-Learner</button>
        <button class="filter-btn" data-filter="audience" data-value="adult" data-i18n="uni.grade.adult">Adult Learner</button>
        <button class="filter-btn" data-filter="audience" data-value="switcher" data-i18n="uni.grade.switcher">Career Switcher</button>
      </div>
    </div>
  </div>

  <main>
{sections_html}

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

  <script defer src="assets/js/i18n.js?v=16"></script>
  <script defer src="assets/js/main.js"></script>
  <script>
    /* Chip-grid panels: click chip -> swap panel + reapply filter */
    (function () {{
      var tabs = document.querySelectorAll('.subject-tab');
      var panels = document.querySelectorAll('.panel');
      var nav = document.querySelector('.skill-picker');

      function activate(targetId, scroll) {{
        var found = false;
        tabs.forEach(function (t) {{
          var match = t.dataset.tab === targetId;
          if (match) found = true;
          t.setAttribute('aria-selected', match ? 'true' : 'false');
          t.classList.toggle('chip-active', match);
        }});
        if (!found) {{
          targetId = tabs[0].dataset.tab;
          tabs[0].setAttribute('aria-selected', 'true');
          tabs[0].classList.add('chip-active');
        }}
        panels.forEach(function (p) {{
          var match = p.id === targetId;
          p.classList.toggle('active', match);
          if (match) {{ p.removeAttribute('hidden'); }} else {{ p.setAttribute('hidden', ''); }}
        }});
        if (scroll) {{
          var navTop = nav.getBoundingClientRect().top;
          if (navTop < 0) {{
            var stickyOffset = 4.5 * parseFloat(getComputedStyle(document.documentElement).fontSize);
            window.scrollTo({{ top: window.scrollY + navTop - stickyOffset, behavior: 'smooth' }});
          }}
        }}
        if (window._applyCardFilters) window._applyCardFilters();
      }}

      tabs.forEach(function (t) {{
        t.addEventListener('click', function (e) {{
          e.preventDefault();
          var target = t.dataset.tab;
          activate(target, true);
          history.replaceState(null, '', '#' + target);
        }});
      }});

      nav.addEventListener('keydown', function (e) {{
        if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
        var focused = document.activeElement;
        var idx = Array.prototype.indexOf.call(tabs, focused);
        if (idx < 0) return;
        var next = e.key === 'ArrowRight' ? (idx + 1) % tabs.length : (idx - 1 + tabs.length) % tabs.length;
        tabs[next].focus();
        tabs[next].click();
      }});

      // Init from URL hash, otherwise stay on default first chip
      var initial = window.location.hash.slice(1);
      if (initial) activate(initial, false);
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

# Also dump i18n keys we need
import json
i18n_data = {
    "sub.uni.badge": "Future-Skill Tools for Higher Ed & Lifelong Learners",
    "sub.uni.title": "Resources for University Students & Lifelong Learners",
    "sub.uni.desc": "144 curated free tools across 12 future-skill clusters. Pick a topic below to explore the 12 best resources.",
    "uni.stat.tools": "Free Tools",
    "uni.stat.topics": "Future-Skill Topics",
    "uni.stat.levels.val": "Undergrad→Adult",
    "uni.stat.levels.lbl": "All Levels",
    "uni.stat.free": "Free",
    "uni.grade.undergrad": "Undergrad",
    "uni.grade.grad": "Grad",
    "uni.grade.phd": "PhD",
    "uni.grade.self": "Self-Learner",
    "uni.grade.all": "All Levels",
    "uni.grade.adult": "Adult Learner",
    "uni.grade.switcher": "Career Switcher",
    "uni.picker.label": "Explore by Skill",
    "uni.picker.heading": "Choose one of the <em>12 future-skill clusters</em> to discover the best free tools",
    "uni.filter.label": "Filter by audience:",
    "uni.filter.all": "All Audiences",
}
for s in SECTIONS:
    i18n_data[f"uni.tab.{s['key']}"] = s["tab_label"]
    i18n_data[f"uni.chip.{s['key']}"] = s.get("chip_label", s["tab_label"])
    i18n_data[f"uni.sec.{s['key']}.label"] = s["label"]
    i18n_data[f"uni.sec.{s['key']}.h2"] = s["title"]
    i18n_data[f"uni.sec.{s['key']}.desc"] = s["desc"]
i18n_data.update(CARD_DESC_KEYS)

(ROOT / "_uni_i18n_keys.json").write_text(json.dumps(i18n_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {ROOT / '_uni_i18n_keys.json'} ({len(i18n_data)} keys)")
