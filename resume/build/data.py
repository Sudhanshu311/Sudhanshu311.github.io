"""Single source of truth for all resume content. Consumed by generate.py."""

PROFILE = {
    "name": "Sudhanshu Bhatnagar",
    "title": "Principal Technical Program Manager @ Nike",
    "tagline": "Principal TPM at Nike — Global Merchandising (Consumer Product & Innovation). 22+ years shipping cloud, composable commerce, and AI/ML programs. Previously Lululemon, Nordstrom, Amazon, and T-Mobile.",
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
        "role": "Principal Technical Program Manager · Global Merchandising",
        "location": "Beaverton, OR",
        "start": "2026-03", "end": None, "current": True,
        "logo": "N",
        "highlights": [
            "<b>Strategic technical leadership</b> — end-to-end technical execution and architecture of high-scale enterprise programs within Global Merchandising; aligning technical roadmaps with Nike's consumer product innovation goals",
            "<b>Cross-functional orchestration</b> — leading engineering and product teams to design, build, and deploy digital capabilities that optimize product line planning, assortment, and seasonal expression",
            "<b>Scale & innovation</b> — driving integration of advanced data, analytics, and ML into merchandising systems for inventory efficiency, demand forecasting, and consumer-right product allocation",
            "<b>Stakeholder management</b> — primary technical liaison between executive merchandising leadership and engineering; translating complex business vision into scalable, high-performance systems",
            "<b>Process excellence & mentorship</b> — Agile/TPM governance frameworks that accelerate delivery velocity, manage dependencies, and mitigate risks across multi-million-dollar global initiatives; mentoring senior technical talent",
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

# Flagship program case studies — top by scale/recency.
PROGRAMS = [
    {
        "id": "nike-merch",
        "title": "Global Merchandising Technology — Consumer Product & Innovation",
        "company": "Nike",
        "period": "03/2026 – Present",
        "problem": "Nike's Global Merchandising organization drives consumer-facing decisions on product line planning, assortment, and seasonal expression at massive global scale. The underlying technology needs a unifying strategic architecture, tighter alignment to consumer product innovation goals, and modern data + ML capabilities across inventory, demand forecasting, and consumer-right allocation.",
        "approach": "Owning end-to-end technical execution and architecture for enterprise Merchandising programs. Standing up Agile/TPM governance to accelerate delivery velocity, manage dependencies, and mitigate risk on multi-million-dollar global initiatives. Serving as primary technical liaison between executive merchandising leadership and engineering. Orchestrating cross-functional engineering and product teams designing, building, and deploying digital capabilities across the merchandising lifecycle. Driving integration of advanced data, analytics, and ML into merchandising systems while mentoring senior technical talent.",
        "outcome": [
            "Technical roadmap aligned with Nike's consumer product innovation goals",
            "Cross-functional orchestration across engineering, product, and executive merchandising leadership",
            "Data + analytics + ML integration path defined for inventory efficiency, demand forecasting, and consumer-right allocation",
            "Agile/TPM governance operationalized across global initiatives",
            "In flight — outcomes will be updated as programs land",
        ],
        "tech": "Global Merchandising platforms · Product line planning · Assortment & seasonal-expression systems · Cloud · Data & Analytics · Machine Learning · Demand Forecasting · Agile/TPM governance",
        "tags": {
            "tech":    ["cloud", "data-ml", "governance"],
            "outcome": ["strategic"],
            "scale":   ["global"],
        },
        "deep_dive": {
            "context": "Global Merchandising at Nike sits at the intersection of one of the largest consumer product organizations on the planet and its technology stack — determining what gets designed, produced, allocated, and sold across seasons, regions, and channels. The systems behind those decisions span product line planning, assortment optimization, seasonal expression, inventory allocation, and demand forecasting — each with its own data pipelines, cross-functional dependencies, and downstream commerce impact.",
            "decisions": [
                "<b>End-to-end architecture ownership</b> — chose to own the full technical roadmap for the CP&I Merchandising portfolio rather than delegate to workstream-specific owners. Trade-off: heavier personal coordination load vs. tight strategic coherence across sub-programs.",
                "<b>Governance before delivery velocity</b> — investing early cycles in RACI, dependency mapping, and risk registers on multi-million-dollar initiatives, even at the cost of some short-term throughput. Trade-off: 4–6 week slower start vs. avoiding the churn that kills scaled programs later.",
                "<b>ML integration on plan</b> — data + analytics + ML capabilities on the roadmap for inventory efficiency, demand forecasting, and consumer-right allocation. Trade-off: complexity of getting model-serving right vs. compounded merchandising accuracy gains.",
            ],
            "lessons": [
                "Milestones will populate here as programs land — this is a Q1 2026 role and the story is still being written.",
            ],
        },
    },
    {
        "id": "lulu-b2b",
        "title": "B2B e-Commerce Platform + Global POS Infrastructure",
        "company": "Lululemon",
        "period": "07/2023 – 02/2026",
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
        "tags": {
            "tech":    ["composable", "genai", "aws", "kafka"],
            "outcome": ["revenue", "quality"],
            "scale":   ["global"],
        },
        "deep_dive": {
            "context": "Two parallel workstreams under one Principal-TPM program: (1) a $5M+ B2B commerce transformation moving Lululemon's B2B business off a legacy monolith onto a composable, API-first, headless architecture on Commercetools + Frontastic; and (2) a global POS Infrastructure program spanning 1000+ stores across NA / EMEA / APAC / CA — Oracle Xstore & Xcenter version upgrades, security patching, and vulnerability remediation on a quarterly cadence.",
            "decisions": [
                "<b>Composable over monolithic</b> — chose Commercetools instead of customizing the legacy platform. Trade-off: higher upfront integration effort vs. dramatically better future flexibility on channel/vendor swaps.",
                "<b>GenAI Bulk Order Assistant on Bedrock + LangChain</b> — used Amazon Bedrock foundation models rather than a fine-tuned custom model. Trade-off: less model control vs. faster time-to-value and zero ML-ops burden.",
                "<b>Governance-first rollout</b> — RACI + change-request process established before line-1 of code. Trade-off: 4–6 week upfront investment vs. avoiding the churn that kills most enterprise programs downstream.",
                "<b>Quarterly upgrade cadence for POS</b> — predictable rhythm over event-driven. Trade-off: some peak-window maintenance vs. compounded regional-coordination cost of ad-hoc upgrades.",
            ],
            "lessons": [
                "Executive sponsorship + a real governance model beats every other program tool combined.",
                "GenAI 'wow' features (Bulk Order Assistant) accelerated adoption of the underlying platform more than any pure-migration story could have.",
                "Vulnerability remediation across 1000+ endpoints needs per-region cadence — not a single global timeline.",
            ],
        },
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
        "tags": {
            "tech":    ["microservices", "aws", "security"],
            "outcome": ["quality", "cost"],
            "scale":   ["multi-brand"],
        },
        "deep_dive": {
            "context": "Customer Identity & Access Management across four brands — Nordstrom, Nordstrom Rack, Store, Credit. Prior state: fragmented credential stores, inconsistent fraud posture, and no unified customer view across brand boundaries. Target state: cross-brand credential unification with SOC 2 + ISO 27001 alignment and material fraud reduction.",
            "decisions": [
                "<b>Three hats — Product Owner, Scrum Master, and TPM</b> — instead of hiring specialists. Trade-off: harder personal load vs. faster stakeholder alignment in a matrixed org.",
                "<b>Spring-Boot microservices on EKS</b> instead of serverless. Trade-off: heavier ops footprint vs. team familiarity and easier debugging in a security-critical domain.",
                "<b>Cross-brand credential store as a shared platform</b> rather than merging brand stores. Trade-off: schema-harmonization pain vs. clean architectural boundaries.",
            ],
            "lessons": [
                "35% ticket reduction came from removing customer-journey friction — not from ML. Sometimes the answer is fewer screens, not smarter software.",
                "SOC 2 and ISO 27001 alignment is a byproduct of governance discipline, not a separate workstream. Build for compliance later and you'll build it twice.",
            ],
        },
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
        "tags": {
            "tech":    ["microservices", "aws"],
            "outcome": ["revenue", "cost"],
            "scale":   ["global"],
        },
        "deep_dive": {
            "context": "Amazon Business needed to offer competitive small-quantity pricing to B2B customers WITHOUT rebate or long-term-commitment programs. Solution: Volume-Aware Pricing (VAP) — a real-time engine computing discount tiers based on a customer's trailing-12-month order history. Rolled out across 8 geographies with regional payment validation, currency, tax, and legal considerations.",
            "decisions": [
                "<b>Real-time computation over batch precomputation</b>. Trade-off: higher runtime cost vs. dramatically better customer experience and zero stale-pricing risk.",
                "<b>Phased 8-country launch</b> (US first, then EU cluster, then JP, CA). Trade-off: longer overall timeline vs. lower blast radius and per-region compliance headroom.",
                "<b>Held launch to fix a $40M/yr discount-stacking edge case</b> found at launch-blocker review. Trade-off: schedule slip vs. avoiding a very public revenue leak.",
            ],
            "lessons": [
                "The best launch-blocker discovery is the one you find yourself — not the one the exec review finds for you.",
                "8-country rollouts fail on tax, currency, and legal — not on engineering. Budget 40% of the timeline for the non-code work.",
            ],
        },
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
        "tags": {
            "tech":    ["microservices", "aws", "kubernetes", "composable"],
            "outcome": ["quality", "revenue"],
            "scale":   ["multi-brand"],
        },
        "deep_dive": {
            "context": "T-Mobile.com and My.T-Mobile.com ran on a monolithic e-commerce stack that couldn't scale to modern experimentation or personalization needs. Digital Commerce Platform (DCP) migrated the web channels to a headless microservices architecture on AWS — powered by APIGEE + Elasticsearch + DynamoDB + Apache Ignite. Established DevOps culture (Shift-Left/Right, on-call, observability) alongside the technical migration.",
            "decisions": [
                "<b>Headless-first from day one</b> — not migration-then-headless. Trade-off: harder initial coordination vs. no legacy debt carried forward.",
                "<b>APIGEE as the API management layer</b> instead of API Gateway direct. Trade-off: extra integration cost vs. enterprise-wide policy and rate-limit consistency across channels.",
            ],
            "lessons": [
                "Cart-performance improvements (~700ms) came from Elasticsearch tuning and connection pooling — not architectural changes. Sometimes the payoff is in the observability, not the redesign.",
                "DevOps culture change lagged the technical migration by ~6 months. You can't ship culture — teams have to adopt it in cycles.",
            ],
        },
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
        "tags": {
            "tech":    ["microservices", "aws"],
            "outcome": ["revenue"],
            "scale":   ["global"],
        },
        "deep_dive": {
            "context": "Trimble needed a unified enterprise commerce platform to launch SaaS products globally across multiple business units. Delivered on Cortex 1.13 (commerce engine) + Aria (billing & subscription) + Safe-Net (entitlement) + WSO2 (ESB / API-M / Identity), integrated with CyberSource for payments and Vertex for tax.",
            "decisions": [
                "<b>Elastic Path (Cortex) over Commercetools</b> — Commercetools was less mature at the time. Trade-off: more custom integration work vs. proven track record in complex B2B subscription commerce.",
            ],
            "lessons": [
                "Every SaaS commerce stack needs tax integration earlier than teams think — Vertex integration should have started in month 2, not month 6.",
            ],
        },
    },
]

# Filter definitions used by the UI. Keep values aligned with program tags above.
FILTER_GROUPS = [
    {
        "id": "tech",
        "label": "Tech",
        "options": [
            ("cloud",         "Cloud"),
            ("aws",           "AWS"),
            ("kubernetes",    "Kubernetes"),
            ("microservices", "Microservices"),
            ("composable",    "Composable / Headless"),
            ("genai",         "GenAI / LLM"),
            ("data-ml",       "Data · ML"),
            ("kafka",         "Kafka / Streaming"),
            ("security",      "Identity · Security"),
            ("governance",    "Governance"),
        ],
    },
    {
        "id": "outcome",
        "label": "Outcome",
        "options": [
            ("revenue",   "Revenue"),
            ("cost",      "Cost / Savings"),
            ("quality",   "Quality · Reliability"),
            ("strategic", "Strategic"),
        ],
    },
    {
        "id": "scale",
        "label": "Scale",
        "options": [
            ("global",       "Global (multi-country)"),
            ("multi-brand",  "Multi-brand / Multi-channel"),
        ],
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
    ("Merchandising · Line Planning · Assortment",    1),
    ("ML: Demand Forecasting · Inventory · Allocation", 1),
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

# =============================================================================
# For Recruiters — compact cheat-sheet block for search partners and hiring mgrs.
# Kept intentionally minimal: role fit + geography + must-haves. No comp,
# no availability, no dealbreakers per owner preference.
# =============================================================================
RECRUITER = {
    "roles": [
        "Principal / Sr. Principal Technical Program Manager",
        "Director / Sr. Director of Program Management",
    ],
    "geography": [
        ("$ location",   "Seattle, WA"),
        ("$ modality",   "Hybrid — 2–3 days/week in-office"),
        ("$ travel",     "Willing to travel monthly to HQ (Bay Area · PDX · NYC)"),
    ],
    "must_haves": [
        ("AI/ML at the center", "GenAI, agentic AI, or ML embedded in the product / operating model — not a side project"),
        ("Composable / MACH commerce",  "Or a platform-modernization mandate on API-first, cloud-native architecture"),
        ("Meaningful scale",            "Large org (1,000+ engineers) with real cross-functional dependencies to orchestrate"),
        ("Team leadership",             "Building & mentoring a PM/TPM org — not a solo IC role"),
        ("Mission-driven, values-aligned", "Product that matters, leadership that operates with integrity"),
        ("Modern tech stack",           "Cloud-native, API-first, event-driven — no green-field-only legacy modernization"),
    ],
    "cta": "Reaching out is easy — Bhatnagar.Sudhanshu31@gmail.com or LinkedIn DM.",
}

# =============================================================================
# Impact Dashboard — quantified outcomes grouped by pillar. Each entry:
#   metric, unit, label, source (role/program).
# Grouped visualization; each pillar renders as its own tile.
# =============================================================================
IMPACT_PILLARS = [
    {
        "id": "revenue",
        "icon": "💰",
        "label": "Revenue & Business Impact",
        "hint": "money made or saved",
        "items": [
            {"value": "$40M",  "label": "discount-stacking issue solved",  "context": "Amazon B2B — Volume-Aware Pricing"},
            {"value": "$5M+",  "label": "B2B platform transformation",     "context": "Lululemon"},
            {"value": "30%",   "label": "checkout success uplift",         "context": "Lululemon B2B"},
            {"value": "$10M+", "label": "annual budget managed",           "context": "HCL Technologies"},
        ],
    },
    {
        "id": "efficiency",
        "icon": "⚡",
        "label": "Efficiency & Speed",
        "hint": "cycle time, cost, effort",
        "items": [
            {"value": "50%", "label": "bulk-order cart-build time reduction", "context": "GenAI Bulk Order Assistant · Bedrock + LangChain"},
            {"value": "35%", "label": "CIAM support-ticket reduction",         "context": "Nordstrom CIAM"},
            {"value": "20%", "label": "program-delay reduction via governance", "context": "Lululemon"},
            {"value": "30%", "label": "improvement in B2B onboarding",         "context": "Lululemon"},
        ],
    },
    {
        "id": "scale",
        "icon": "🌐",
        "label": "Scale",
        "hint": "size of the system delivered",
        "items": [
            {"value": "1,000+", "label": "retail stores under POS ops",       "context": "Lululemon · NA / EMEA / APAC / CA"},
            {"value": "8",      "label": "countries — real-time pricing launch", "context": "Amazon VAP"},
            {"value": "20+",    "label": "cross-functional teams orchestrated", "context": "Nike · Lululemon · Nordstrom"},
            {"value": "4",      "label": "e-commerce platforms shipped end-to-end", "context": "Lululemon · T-Mobile · Trimble · Amazon"},
        ],
    },
    {
        "id": "quality",
        "icon": "🛡️",
        "label": "Quality & Compliance",
        "hint": "resilience and controls",
        "items": [
            {"value": "99.99%",  "label": "availability delivered",            "context": "Lululemon B2B platform"},
            {"value": "0",       "label": "revenue-impact incidents on migration", "context": "Lululemon monolith → composable"},
            {"value": "100%",    "label": "program deadlines met · 95% on-time milestones", "context": "Lululemon"},
            {"value": "SOC 2 · ISO 27001", "label": "controls alignment", "context": "Nordstrom CIAM"},
        ],
    },
    {
        "id": "team",
        "icon": "🤝",
        "label": "Team & Leadership",
        "hint": "the people side of the job",
        "items": [
            {"value": "65",  "label": "people led at peak",                       "context": "HCL Technologies"},
            {"value": "20+", "label": "cross-functional teams orchestrated",       "context": "Nike · Lululemon · Nordstrom"},
            {"value": "22+", "label": "years shipping enterprise programs",        "context": "Career-long"},
            {"value": "4",   "label": "global regions — NA · EMEA · APAC · CA",   "context": "Lululemon POS"},
        ],
    },
]

# =============================================================================
# Testimonials — sourced from LinkedIn public recommendations at
# https://www.linkedin.com/in/sudhanshubhatnagar/  ("Recommendations received").
# LinkedIn shows 2 publicly (out of 10 total). Add the rest by pasting them here.
# =============================================================================
TESTIMONIALS = [
    {
        "quote": (
            "Sudhanshu is a pleasure to work with. He is highly organized, communicates "
            "clearly, remains calm under pressure, and he's always open to compromise if "
            "it is for the greater good. He's a strong Technical Program Manager with a "
            "good focus on best practices and team health."
        ),
        "author": "James B.",
        "title":  "Senior Engineering Leader",  # TODO: replace with full title from LinkedIn
        "company": "",                            # TODO: replace with company from LinkedIn
        "source": "LinkedIn",
        "featured": True,
    },
    {
        "quote": (
            "Sudhanshu and I got to know each other when Sudhanshu worked on customer "
            "access management that drives identity for all customers across Nordstrom. "
            "As a TPM, he is a strategic thinker, collaborative and great communicator. "
            "He is always willing to listen to feedback gathered from areas beyond what "
            "the features asked for and translate those into future product features. "
            "I definitely enjoy working with Sudhanshu and strongly recommend him."
        ),
        "author": "Angshu K.",
        "title":  "Product Leader",  # TODO: replace with full title from LinkedIn
        "company": "Nordstrom",       # inferred from context
        "source": "LinkedIn",
        "featured": True,
    },
    # ---- TODO: paste 1-3 more LinkedIn recommendations below to fill the grid ----
    {
        "quote": "[PLACEHOLDER — paste your LinkedIn recommendation here. LinkedIn shows 10 total; add 1-3 more of your favorites and delete this placeholder.]",
        "author": "[Name]",
        "title":  "[Title]",
        "company": "[Company]",
        "source": "LinkedIn",
        "featured": False,
        "placeholder": True,
    },
]

# Featured AI/ML & Agentic AI projects — built during the McCombs PGP program,
# hosted on github.com/Sudhanshu311. Ordered most-advanced first.
AIML_PROJECTS = [
    {
        "slug": "foodhub-agentic-sql-chatbot",
        "title": "FoodHub Agentic Chatbot",
        "domain": "Agentic AI",
        "one_liner": "LangChain SQL agent answering customer order queries from a SQLite DB, with input/output guardrails and human-escalation.",
        "tech": ["LangChain", "OpenAI", "SQL agent", "guardrails"],
        "featured": True,
    },
    {
        "slug": "plant-seedlings-cnn",
        "title": "Plant Seedlings CNN",
        "domain": "Computer Vision",
        "one_liner": "12-class Keras CNN classifier for plant-seedling images — an agriculture use case with augmentation + LR scheduling.",
        "tech": ["Keras", "TensorFlow", "OpenCV", "CNN"],
        "featured": True,
    },
    {
        "slug": "bank-churn-neural-network",
        "title": "Bank Churn Neural Net",
        "domain": "Deep Learning",
        "one_liner": "Feed-forward NN for 6-month bank customer churn, with SMOTE for imbalance and SHAP for per-feature explainability.",
        "tech": ["Keras", "TensorFlow", "SHAP", "imbalanced-learn"],
        "featured": True,
    },
    {
        "slug": "edtech-candidate-attrition-ensemble",
        "title": "EdTech Attrition — Ensembles",
        "domain": "Ensemble ML",
        "one_liner": "Bagging · Boosting · XGBoost with RandomizedSearchCV tuning to predict which trained candidates will leave the company.",
        "tech": ["XGBoost", "scikit-learn", "SMOTE"],
        "featured": True,
    },
    {
        "slug": "personal-loan-decision-tree",
        "title": "Personal Loan Campaign",
        "domain": "Classification",
        "one_liner": "Tuned Decision Tree that identifies liability customers most likely to accept a personal-loan offer.",
        "tech": ["scikit-learn", "GridSearchCV"],
    },
    {
        "slug": "foodhub-eda-nyc",
        "title": "FoodHub NYC — EDA",
        "domain": "Python · EDA",
        "one_liner": "End-to-end exploratory analysis of ~1,900 NYC food-delivery orders — cuisines, cost tiers, weekday demand, delivery time.",
        "tech": ["pandas", "seaborn", "matplotlib"],
    },
]

AIML_INDEX_REPO = "aiml-portfolio"

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
     "AI/ML background is post-grad from McCombs (UT Austin, 2024–2025) plus applied GenAI (Bedrock/LangChain/RAG) shipping the Lululemon Bulk Order Assistant. Now at Nike driving ML integration into merchandising systems — demand forecasting, inventory efficiency, and consumer-right product allocation. "
     "See the <a href='#aiml'>AI/ML Portfolio</a> section for six hands-on projects (Agentic AI chatbot, CNN, neural nets, ensemble ML) — full code on "
     "<a href='https://github.com/Sudhanshu311/aiml-portfolio' target='_blank' rel='noopener'>github.com/Sudhanshu311/aiml-portfolio</a>."),
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
    (["merchandising", "assortment", "line planning", "seasonal", "allocation", "forecast"],
     "At Nike, driving the technical roadmap for <b>Global Merchandising</b> — product line planning, assortment, seasonal expression, and consumer-right product allocation. Also integrating data, analytics, and ML into merchandising systems for inventory efficiency and demand forecasting."),
    (["nike"],
     "Joined <b>Nike</b> in March 2026 as Principal Technical Program Manager in <em>Global Merchandising — Consumer Product & Innovation</em>. Five focus areas:<br>"
     "  1. <em>Strategic technical leadership</em> — end-to-end execution + architecture of enterprise Merchandising programs<br>"
     "  2. <em>Cross-functional orchestration</em> — engineering + product teams shipping product line planning, assortment, and seasonal-expression capabilities<br>"
     "  3. <em>Scale & innovation</em> — data, analytics, and ML into merchandising for inventory, forecasting, and allocation<br>"
     "  4. <em>Stakeholder management</em> — primary technical liaison between executive merchandising leadership and engineering<br>"
     "  5. <em>Process excellence & mentorship</em> — Agile/TPM governance on multi-million-dollar global initiatives, mentoring senior technical talent"),
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
