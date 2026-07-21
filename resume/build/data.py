"""Single source of truth for all resume content. Consumed by generate.py."""

PROFILE = {
    "name": "Sudhanshu Bhatnagar",
    "title": "Principal Technical Program Manager @ Nike",
    "tagline": "Principal TPM at Nike — Consumer Product & Innovation, Merchandising. 22+ years shipping cloud, composable commerce, and AI/ML programs. Previously Lululemon, Nordstrom, Amazon, and T-Mobile.",
    "location": "Seattle, WA",
    "email": "Bhatnagar.Sudhanshu31@gmail.com",
    "phone": "310-754-6162",
    "linkedin": "https://www.linkedin.com/in/sudhanshubhatnagar/",
    "github": "https://github.com/Sudhanshu311",
    "site": "https://sudhanshu311.github.io/resume/",
}

# Big animated counters for the hero — pick the ~6 most impressive numbers.
METRICS = [
    {"value": 22, "suffix": "+",  "label": "Years shipping enterprise programs"},
    {"value": 1000, "suffix": "+", "label": "Global retail stores under POS ops"},
    {"value": 8,  "suffix": "",    "label": "Countries — real-time pricing launch"},
    {"value": 65, "suffix": "",    "label": "People led at peak (HCL, $10M+ budget)"},
    {"value": 40, "suffix": "M",   "prefix": "$", "label": "Discount stacking issue solved (Amazon B2B)"},
    {"value": 99.99, "suffix": "%", "label": "Availability delivered (B2B platform)"},
]

# Career log — reverse chronological. Dates for timeline math.
ROLES = [
    {
        "id": "nike",
        "company": "Nike",
        "role": "Principal Technical Program Manager",
        "location": "Beaverton, OR",
        "start": "2026-03", "end": None, "current": True,
        "logo": "N",
        "highlights": [
            "Consumer Product & Innovation — Merchandising technology portfolio",
            "Bringing composable-first, governance-forward TPM playbook to Nike's global consumer footprint",
            "22+ years of program leadership across Lululemon, Nordstrom, Amazon, and T-Mobile applied to Nike's Merchandising platforms",
            "Milestones and impact will appear as programs land",
        ],
    },
    {
        "id": "lululemon",
        "company": "Lululemon",
        "role": "Principal Technical Program Manager",
        "location": "Seattle, WA",
        "start": "2023-07", "end": "2026-02", "current": False,
        "logo": "L",
        "highlights": [
            "$5M+ B2B e-Commerce platform transformation; 30% improvement in onboarding",
            "Global POS Infrastructure across 1000+ stores (NA · EMEA · APAC · CA) — Oracle Xstore/Xcenter upgrades, security patching, vulnerability remediation",
            "20+ cross-functional teams aligned across Product · UX · QA · Security · Legal",
            "99.99% availability delivered on next-gen migration with zero revenue impact",
            "GenAI Bulk Order Assistant on Amazon Bedrock + LangChain — 50% cart-build reduction, 30% checkout uplift",
        ],
    },
    {
        "id": "nordstrom",
        "company": "Nordstrom",
        "role": "Sr. Technical Program Manager",
        "location": "Seattle, WA",
        "start": "2021-07", "end": "2023-05", "current": False,
        "logo": "N",
        "highlights": [
            "Customer Identity & Access Management across Nordstrom, Nordstrom Rack, Store, Credit",
            "35% reduction in customer service tickets; 20% faster response times",
            "SOC 2 · ISO 27001 · internal audit alignment for cloud architecture",
            "20% delivery speed improvement across 5+ cross-functional teams",
        ],
    },
    {
        "id": "amazon",
        "company": "Amazon",
        "role": "Sr. Technical Program Manager",
        "location": "Seattle, WA",
        "start": "2019-03", "end": "2021-07", "current": False,
        "logo": "A",
        "highlights": [
            "Volume Aware Pricing (VAP) launched across 8 countries — US · UK · IT · FR · ES · DE · JP · CA",
            "Real-time payment validation improved pricing accuracy by 40%",
            "Resolved $40M/yr discount-stacking issue on Amazon Business",
            "Coordinated 25+ cross-functional teams; strategically avoided launch blocker",
        ],
    },
    {
        "id": "tmobile",
        "company": "T-Mobile (via HCL)",
        "role": "Enterprise Technical Program Manager / Sr. Manager",
        "location": "Bellevue, WA",
        "start": "2016-06", "end": "2019-03", "current": False,
        "logo": "T",
        "highlights": [
            "Digital Commerce Platform — headless, microservices-based, deployed on AWS",
            "Monolith → microservices migration for T-Mobile web channels",
            "700ms improvement in cart performance",
            "Established DevOps (Shift Left/Right, on-call) and end-to-end agile",
        ],
    },
    {
        "id": "trimble",
        "company": "Trimble (via HCL)",
        "role": "Sr. Technical Program Manager / Sr. Software Development Manager",
        "location": "India · US",
        "start": "2014-10", "end": "2016-06", "current": False,
        "logo": "Tr",
        "highlights": [
            "Enterprise Digital e-Commerce Platform with Cortex, Aria billing, Safe-Net entitlement",
            "WSO2 ESB · API-M · Identity; AWS EC2 · Oracle RDS · S3 · Cassandra",
            "Payment: CyberSource · Vertex tax integration",
        ],
    },
    {
        "id": "norton",
        "company": "Norton / Symantec (via HCL)",
        "role": "Software Development Manager",
        "location": "India",
        "start": "2011-08", "end": "2014-10", "current": False,
        "logo": "Sy",
        "highlights": [
            "One.Norton.com · Manage.Norton.com · MobileSecurity.Norton.com",
            ".NET 4.0 · MVC · WCF · REST · Fortify · Selenium · Splunk · Omniture",
        ],
    },
    {
        "id": "cambridge",
        "company": "Cambridge University Assessments (via HCL)",
        "role": "Sr. Technical Lead",
        "location": "India · UK",
        "start": "2009-09", "end": "2011-07", "current": False,
        "logo": "C",
        "highlights": [
            "Shop.Cambridge.org on Microsoft Commerce Server 2009",
            ".NET 3.5 · WCF · SharePoint · Barclays ePDQ payment gateway",
        ],
    },
    {
        "id": "elsevier",
        "company": "Elsevier (via HCL)",
        "role": "Technical Lead → Sr. Software Engineer → Software Engineer",
        "location": "India",
        "start": "2005-03", "end": "2009-09", "current": False,
        "logo": "E",
        "highlights": [
            "Annual Invoicing and Royalty (2007–2009)",
            "Textbooks.Elsevier.com and Books.Elsevier.com (2005–2007)",
            "Electronic Field Notebook (2005)",
        ],
    },
    {
        "id": "early",
        "company": "CMC · Technosys · Connect Technologies",
        "role": "System Integrator · Assistant Software Consultant · Software Programmer",
        "location": "India",
        "start": "2002-07", "end": "2005-03", "current": False,
        "logo": "•",
        "highlights": [
            "First 3 years of career — systems integration and software development in India",
        ],
    },
]

# Flagship program case studies — top 5 by scale/recency.
PROGRAMS = [
    {
        "id": "lulu-b2b",
        "title": "B2B e-Commerce Platform + Global POS Infrastructure",
        "company": "Lululemon",
        "period": "07/2023 – Present",
        "problem": "Legacy B2B commerce and 1000+ store POS platforms lacked composable architecture, slowing new-market rollouts and creating operational risk across 4 global regions (NA, EMEA, APAC, CA).",
        "approach": "Established RACI · governance · change-request process. Built composable, API-first, headless commerce on Commercetools + Frontastic. Directed Oracle Xstore/Xcenter upgrades, security patching, and vulnerability remediation across 1000+ stores. Delivered GenAI Bulk Order Assistant on Amazon Bedrock + LangChain.",
        "outcome": [
            "100% program deadlines met · 95% milestone targets on-time",
            "20% reduction in program delays via governance",
            "50% reduction in bulk-order cart-build time (GenAI Assistant)",
            "30% improvement in checkout success rate",
            "99.99% availability, zero revenue impact on legacy → next-gen migration",
        ],
        "tech": "Commercetools · Frontastic · AWS (DynamoDB, Lambda, S3, API Gateway, EKS) · Kafka · React · Node · APIGEE · CyberSource · Vertex · Amazon Bedrock · LangChain · Datadog · Splunk · Python",
    },
    {
        "id": "nord-ciam",
        "title": "Customer Identity & Access Management",
        "company": "Nordstrom",
        "period": "07/2021 – 05/2023",
        "problem": "Fragmented identity across Nordstrom, Nordstrom Rack, Store, and Credit created customer friction, fraud exposure, and audit gaps.",
        "approach": "Cross-brand CIAM with unified credential store. Partnered with Security · Compliance for SOC 2 · ISO 27001 alignment. Owned Agile + planning maturity across 5+ teams. Wore three hats: Product Owner · Scrum Master · TPM.",
        "outcome": [
            "35% reduction in customer service tickets",
            "20% faster response times",
            "20% improvement in delivery speed, 15% in team performance",
            "100% strategic-objective alignment across 5+ teams",
            "95% of program milestones met",
        ],
        "tech": "Spring-Boot microservices · AWS (DynamoDB, Lambda, S3, API Gateway, EKS) · Kafka · React · Go · Splunk · New-Relic · Tableau · Optimizely · Shape",
    },
    {
        "id": "amzn-vap",
        "title": "Volume-Aware Pricing (VAP) — Amazon B2B",
        "company": "Amazon.com",
        "period": "03/2019 – 07/2021",
        "problem": "Amazon Business needed competitive small-quantity pricing without long-term rebate commitments — a real-time trailing-12-month discount engine across 8 geographies.",
        "approach": "Owned MVP roadmap, technical component articulation, and 8-country rollout program with 25+ cross-functional teams. Strategically identified and avoided a launch-blocker risk.",
        "outcome": [
            "Launched in US · UK · IT · FR · ES · DE · JP · CA",
            "40% improvement in pricing accuracy (real-time payment validation)",
            "Resolved $40M/yr discount-stacking issue",
            "100% on-time milestone delivery",
        ],
        "tech": "Spring-Boot microservices · AWS (SNS, DynamoDB, Lambda, S3, API Gateway) · React",
    },
    {
        "id": "tmo-dcp",
        "title": "Digital Commerce Platform (DCP) — Headless Migration",
        "company": "T-Mobile",
        "period": "06/2016 – 03/2019",
        "problem": "T-Mobile's monolithic web-channel commerce couldn't scale to modern experimentation velocity or personalization needs.",
        "approach": "Migrated monolith to headless microservices deployed on AWS. Introduced DevOps (Shift-Left/Right, on-call), agile end-to-end, and observability across development and operations.",
        "outcome": [
            "Headless e-Commerce platform live on AWS",
            "700ms improvement in cart performance",
            "DevOps + agile maturity established across the org",
        ],
        "tech": "Spring-Boot microservices · APIGEE · AWS · Oracle · Splunk · AppDynamics · Apache Ignite · Elasticsearch · ActiveMQ · DynamoDB · Tableau · Kubernetes",
    },
    {
        "id": "trimble-edc",
        "title": "Enterprise Digital e-Commerce Platform",
        "company": "Trimble",
        "period": "10/2014 – 06/2016",
        "problem": "Trimble needed a global e-commerce platform with subscription billing, entitlement, and tax integration to launch SaaS products at scale.",
        "approach": "Delivered enterprise commerce on Cortex + Aria (billing) + Safe-Net (entitlement) + WSO2 ESB/API-M/Identity, integrated with CyberSource and Vertex for payments and tax.",
        "outcome": [
            "Enterprise SaaS commerce live on AWS",
            "Multi-region billing + entitlement + tax integration operational",
        ],
        "tech": "Spring-Boot · Cortex · Aria · Safe-Net · WSO2 · CyberSource · Vertex · AWS EC2 · Oracle RDS · S3 · Cassandra",
    },
]

# Skill radar — 6 axes, values 0-100. Weighted for what a Principal TPM signals.
SKILL_RADAR = [
    {"axis": "Program Delivery",        "value": 96},
    {"axis": "Cloud & Architecture",    "value": 88},
    {"axis": "Composable Commerce",     "value": 92},
    {"axis": "AI/ML & GenAI",           "value": 78},
    {"axis": "Stakeholder Leadership",  "value": 95},
    {"axis": "Executive Communication", "value": 94},
]

# Tech heatmap — years hands-on per stack.
TECH_HEATMAP = [
    ("AWS (EC2, S3, Lambda, DynamoDB, API GW, EKS)", 8),
    ("Composable Commerce (Commercetools, Elastic Path)", 6),
    ("Microservices (Spring-Boot, Node)",           10),
    ("Kafka · Event streaming",                      6),
    ("Kubernetes / EKS",                              5),
    ("React · Node.js",                              7),
    ("APIGEE · API Gateway",                          6),
    ("Payment: CyberSource · Vertex",                 8),
    ("Observability: Splunk · Datadog · New-Relic · AppDynamics", 10),
    ("Data: Python · SQL · Tableau · Grafana",       9),
    ("AI/ML: Bedrock · LangChain · RAG · LLM",        2),
    ("Azure (Solutions Architect)",                   5),
    (".NET · C# · MVC · WCF",                        14),
    ("Agile: JIRA · Jira-Align · Rally · Confluence", 12),
    ("SAFe · Scrum · PgMP · PMP",                    15),
]

CERTIFICATIONS = [
    "Program Management Professional (PgMP)",
    "Project Management Professional (PMP)",
    "Scrum Master · Scrum Product Owner",
    "SAFe — Leading SAFe",
    "AWS Certified Solutions Architect — Associate",
    "Architecting Microsoft Azure Solutions (70-535)",
    "Product Manager Certification — Indian School of Business",
]

EDUCATION = [
    {
        "title": "Post Graduate Program in Artificial Intelligence & Machine Learning",
        "school": "McCombs School of Business — University of Texas at Austin",
        "period": "May 2024 – Feb 2025",
    },
    {
        "title": "Bachelor of Engineering, Computer Science & Engineering",
        "school": "Rajiv Gandhi Technical University, India",
        "period": "1998 – 2002",
    },
]

# Static Q&A knowledge base — keyword-triggered.
# Order matters: more specific keys first, generic keys later.
QA = [
    (["genai", "gen ai", "bedrock", "langchain", "llm", "rag"],
     "Built the GenAI Bulk Order Assistant at Lululemon on Amazon Bedrock + LangChain — natural-language enterprise bulk orders. Result: 50% cart-build reduction, 30% checkout uplift. Also completed the Post Graduate Program in AI/ML at McCombs School of Business (May 2024 – Feb 2025)."),
    (["ai", "ml", "machine learning", "artificial intelligence"],
     "AI/ML background is post-grad from McCombs (UT Austin, 2024–2025) plus applied GenAI (Bedrock/LangChain/RAG) shipping the Lululemon Bulk Order Assistant. Areas of interest: LLM-assisted enterprise workflows, RAG over program artifacts, TensorFlow-based classification for ops signals."),
    (["aws", "amazon web services"],
     "8+ years hands-on AWS across the stack — EC2, S3, Lambda, DynamoDB, API Gateway, ECS/EKS, SNS. Certified Solutions Architect – Associate. Delivered platforms on AWS at Lululemon, Nordstrom, T-Mobile, Trimble, and Amazon (VAP)."),
    (["azure", "microsoft cloud"],
     "5 years Azure — certified in Architecting Microsoft Azure Solutions (70-535). Multi-cloud awareness informed the composable-commerce architecture choices at Lululemon and Trimble."),
    (["composable", "mach", "commercetools", "headless"],
     "Composable / MACH commerce is my sweet spot — Commercetools + Frontastic at Lululemon, headless migration at T-Mobile (DCP), Elastic Path + Cortex at Trimble. API-first, cloud-native, headless is the through-line."),
    (["b2b", "commerce", "ecommerce", "e-commerce"],
     "B2B e-commerce leadership across Lululemon ($5M+ platform transformation, 20+ teams), Amazon (VAP in 8 countries, $40M savings), T-Mobile (headless DCP), and Trimble. Composable + governance-first is the pattern I run."),
    (["pos", "point of sale", "retail store", "xstore", "xcenter"],
     "Owned global POS infrastructure at Lululemon across 1000+ stores (NA, EMEA, APAC, CA) — Oracle Xstore/Xcenter version upgrades, security patching, vulnerability remediation, quarterly upgrade cadence with regional teams."),
    (["identity", "iam", "ciam", "auth", "authentication", "fraud"],
     "Led CIAM at Nordstrom across Nordstrom, Nordstrom Rack, Store, and Credit — 35% reduction in support tickets, SOC 2 + ISO 27001 alignment, cross-brand credential unification."),
    (["scale", "large-scale", "global", "countries"],
     "Global scale delivery: 1000+ stores at Lululemon, 8-country rollout at Amazon (VAP), monolith→microservices at T-Mobile handling web-channel commerce."),
    (["team", "led", "people", "manage", "headcount"],
     "Team leadership: 65 people at peak (HCL Technologies, $10M+ annual budget). Across Nike, Lululemon, and Nordstrom, coordinating 20+ cross-functional teams (Product, UX, QA, Security, Legal). Approach: RACI + governance + high-touch executive communication."),
    (["agile", "scrum", "safe", "pmp", "pgmp"],
     "Certifications: PgMP · PMP · SAFe (Leading SAFe) · Scrum Master · Product Owner · AWS Solutions Architect · Azure Solutions Architect (70-535) · Product Manager (ISB). 15+ years running SAFe/Scrum/Kanban delivery at scale."),
    (["contact", "email", "phone", "reach"],
     "Best way to reach me: <a href='mailto:Bhatnagar.Sudhanshu31@gmail.com'>Bhatnagar.Sudhanshu31@gmail.com</a> · <a href='https://www.linkedin.com/in/sudhanshubhatnagar/' target='_blank' rel='noopener'>LinkedIn</a> · phone 310-754-6162 · based in Seattle, WA."),
    (["resume", "cv", "pdf", "download"],
     "PDF resume is one click away — <a href='assets/files/Sudhanshu-Bhatnagar.pdf' target='_blank'>Download PDF</a>."),
    (["role", "title", "position", "job", "looking"],
     "Currently Principal Technical Program Manager at <b>Nike</b> — Consumer Product & Innovation, Merchandising (Beaverton, OR — Seattle-based, remote-friendly). Started March 2026. Prior: Lululemon, Nordstrom, Amazon, T-Mobile."),
    (["nike"],
     "Joined <b>Nike</b> in March 2026 as Principal Technical Program Manager in <em>Consumer Product & Innovation — Merchandising</em>. Bringing composable-commerce, cloud, and program-governance experience from Lululemon, Nordstrom, Amazon, and T-Mobile to Nike's global consumer digital footprint. Details on specific programs will surface here as milestones land."),
    (["education", "degree", "school", "university"],
     "PGP in AI/ML from McCombs School of Business (UT Austin), May 2024 – Feb 2025. Bachelor's in Computer Science & Engineering from Rajiv Gandhi Technical University, India (1998–2002)."),
]

# Suggested chat prompts (surfaced as buttons)
QA_SUGGESTIONS = ["AWS experience?", "AI/ML work?", "Team size?", "Composable commerce?", "Global scale?", "Contact?"]

# Fun terminal commands beyond the obvious ones
EASTER_EGGS = {
    "sudo make me a sandwich": "🥪 nice try",
    "hello": "Hello, curious visitor. Type `help` to explore.",
    "hi": "Hi 👋 Type `help` to explore.",
}
