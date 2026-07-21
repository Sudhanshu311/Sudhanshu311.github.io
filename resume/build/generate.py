"""Generate /resume/index.html from data.py — a self-contained interactive resume."""

from __future__ import annotations
import json
import re
from datetime import date
from pathlib import Path

from data import (
    PROFILE, METRICS, ROLES, PROGRAMS, SKILL_RADAR, TECH_HEATMAP,
    CERTIFICATIONS, EDUCATION, QA, QA_SUGGESTIONS, EASTER_EGGS,
)

OUT = Path(__file__).resolve().parent.parent / "index.html"

# ---------- Helpers ----------
def yr(iso):
    return int(iso.split("-")[0])
def mo(iso):
    return int(iso.split("-")[1])
def to_frac(iso, epoch_year, span_years):
    y, m = yr(iso), mo(iso)
    return ((y - epoch_year) * 12 + (m - 1)) / (span_years * 12)
def fmt_range(role):
    def pretty(iso, current=False):
        if current: return "Present"
        y, m = yr(iso), mo(iso)
        mn = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][m-1]
        return f"{mn} {y}"
    a = pretty(role["start"])
    b = "Present" if role["current"] else pretty(role["end"])
    return f"{a} – {b}"


# ---------- Section renderers ----------
def render_hero():
    metric_html = []
    for m in METRICS:
        prefix = m.get("prefix", "")
        suffix = m.get("suffix", "")
        target = m["value"]
        # Detect decimal targets like 99.99
        step = "0.01" if isinstance(target, float) else "1"
        metric_html.append(f'''
        <div class="metric" data-target="{target}" data-prefix="{prefix}" data-suffix="{suffix}">
          <div class="metric-value">{prefix}<span class="val">0</span>{suffix}</div>
          <div class="metric-label">{m["label"]}</div>
        </div>''')
    return f'''
  <section class="hero" id="hero">
    <div class="hero-shell">
      <div class="prompt-line">
        <span class="prompt">~/sudhanshu</span><span class="prompt-sep">$</span>
        <span class="typed" data-typed="whoami"></span><span class="caret">▍</span>
      </div>
      <h1 class="hero-name">{PROFILE["name"]}</h1>
      <p class="hero-title">{PROFILE["title"]}</p>
      <p class="hero-tagline">{PROFILE["tagline"]}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="assets/files/Sudhanshu-Bhatnagar.pdf" download>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download PDF
        </a>
        <a class="btn btn-ghost" href="{PROFILE["linkedin"]}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 1 1 8.25 6.5a1.75 1.75 0 0 1-1.75 1.75zM19 19h-3v-4.74c0-1.42-.6-2.1-1.7-2.1-1.2 0-1.8.85-1.8 2.1V19h-3v-9h3v1.05a3.55 3.55 0 0 1 3-1.35c2 0 3.5 1.2 3.5 3.72Z"/></svg>
          LinkedIn
        </a>
        <a class="btn btn-ghost" href="mailto:{PROFILE["email"]}">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          Email
        </a>
      </div>
    </div>
    <div class="metrics-grid">
      {"".join(metric_html)}
    </div>
  </section>'''


def render_repl():
    return '''
  <section class="repl-section" id="terminal">
    <h2 class="section-h">
      <span class="section-num">01</span>
      <span class="section-name">Interactive Terminal</span>
      <span class="section-hint mono">try: help · whoami · experience · programs · skills · contact · resume · theme</span>
    </h2>
    <div class="terminal">
      <div class="terminal-chrome">
        <span class="tc-dot tc-r"></span>
        <span class="tc-dot tc-y"></span>
        <span class="tc-dot tc-g"></span>
        <span class="tc-title">bash — ~/sudhanshu</span>
      </div>
      <div class="terminal-body">
        <div id="repl-output">
          <div class="repl-line mono muted">Type <b>help</b> and press Enter, or click a suggestion below.</div>
        </div>
        <form class="repl-form" onsubmit="return REPL.run(event)">
          <span class="repl-prompt mono">$</span>
          <input class="repl-input mono" type="text" autocomplete="off" spellcheck="false" placeholder="type a command..."/>
        </form>
        <div class="repl-chips">
          <button type="button" class="chip" onclick="REPL.runCmd('help')">help</button>
          <button type="button" class="chip" onclick="REPL.runCmd('whoami')">whoami</button>
          <button type="button" class="chip" onclick="REPL.runCmd('experience')">experience</button>
          <button type="button" class="chip" onclick="REPL.runCmd('programs')">programs</button>
          <button type="button" class="chip" onclick="REPL.runCmd('skills')">skills</button>
          <button type="button" class="chip" onclick="REPL.runCmd('contact')">contact</button>
          <button type="button" class="chip" onclick="REPL.runCmd('resume')">resume</button>
          <button type="button" class="chip" onclick="REPL.runCmd('theme')">theme</button>
          <button type="button" class="chip" onclick="REPL.runCmd('clear')">clear</button>
        </div>
      </div>
    </div>
  </section>'''


def render_timeline():
    if not ROLES:
        return ""
    epoch = min(yr(r["start"]) for r in ROLES)
    end_year = date.today().year
    span = end_year - epoch + 1
    # Bars — reverse ROLES so oldest is bottom, current is top
    bars = []
    for i, r in enumerate(ROLES):
        left = to_frac(r["start"], epoch, span) * 100
        end_iso = f"{end_year:04d}-{date.today().month:02d}" if r["current"] else r["end"]
        right = to_frac(end_iso, epoch, span) * 100
        width = max(right - left, 1.5)
        bars.append(f'''
        <div class="tl-row">
          <div class="tl-label mono">{r["company"]}</div>
          <div class="tl-track">
            <button class="tl-bar" data-role="{r["id"]}" style="left:{left:.2f}%;width:{width:.2f}%" title="{r["company"]} · {fmt_range(r)}">
              <span class="tl-bar-label">{fmt_range(r)}</span>
            </button>
          </div>
        </div>''')
    # Year ruler ticks (every 2 years)
    ticks = []
    for y in range(epoch, end_year + 1):
        if (y - epoch) % 2 == 0 or y == end_year:
            pct = ((y - epoch) / span) * 100
            ticks.append(f'<span class="tl-tick" style="left:{pct:.2f}%">{y}</span>')
    # Detail cards (all rendered, one shown at a time)
    details = []
    for r in ROLES:
        lis = "".join(f"<li>{h}</li>" for h in r["highlights"])
        details.append(f'''
        <article class="tl-detail" data-role="{r["id"]}" hidden>
          <header class="tl-detail-head">
            <div class="tl-logo">{r["logo"]}</div>
            <div>
              <div class="tl-detail-role">{r["role"]}</div>
              <div class="tl-detail-company mono">{r["company"]} · {r["location"]} · {fmt_range(r)}</div>
            </div>
          </header>
          <ul class="tl-detail-highlights">{lis}</ul>
        </article>''')
    return f'''
  <section class="timeline-section" id="career">
    <h2 class="section-h">
      <span class="section-num">02</span>
      <span class="section-name">Career Timeline</span>
      <span class="section-hint">{epoch} → present · {end_year - epoch}+ years · click any bar</span>
    </h2>
    <div class="timeline">
      <div class="tl-ruler">{"".join(ticks)}</div>
      <div class="tl-bars">{"".join(bars)}</div>
    </div>
    <div class="tl-details" id="tl-details">
      {"".join(details)}
    </div>
  </section>'''


def render_cases():
    cards = []
    for i, p in enumerate(PROGRAMS):
        outcome_lis = "".join(f"<li>{o}</li>" for o in p["outcome"])
        cards.append(f'''
      <article class="case" data-case="{p["id"]}">
        <button class="case-head" onclick="CASES.toggle(this)" aria-expanded="{'true' if i==0 else 'false'}">
          <div class="case-meta">
            <div class="case-company mono">{p["company"]}</div>
            <div class="case-period mono">{p["period"]}</div>
          </div>
          <h3 class="case-title">{p["title"]}</h3>
          <span class="case-chev" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><polyline points="6 9 12 15 18 9"/></svg>
          </span>
        </button>
        <div class="case-body" {'' if i==0 else 'hidden'}>
          <div class="case-block">
            <div class="case-label">Problem</div>
            <p>{p["problem"]}</p>
          </div>
          <div class="case-block">
            <div class="case-label">Approach</div>
            <p>{p["approach"]}</p>
          </div>
          <div class="case-block">
            <div class="case-label">Outcome</div>
            <ul class="case-outcome">{outcome_lis}</ul>
          </div>
          <div class="case-block case-tech">
            <div class="case-label">Tech</div>
            <p class="mono muted">{p["tech"]}</p>
          </div>
        </div>
      </article>''')
    return f'''
  <section class="cases-section" id="programs">
    <h2 class="section-h">
      <span class="section-num">03</span>
      <span class="section-name">Flagship Programs</span>
      <span class="section-hint">{len(PROGRAMS)} case studies · click to expand</span>
    </h2>
    <div class="cases-grid">
      {"".join(cards)}
    </div>
  </section>'''


def render_skills():
    # Radar chart — SVG. 6 axes.
    n = len(SKILL_RADAR)
    cx, cy, r_max = 200, 200, 150
    # Compute polygon points from values
    points = []
    label_pos = []
    for i, s in enumerate(SKILL_RADAR):
        theta = (i / n) * 2 * 3.14159265 - 3.14159265 / 2  # start at top
        rv = (s["value"] / 100) * r_max
        import math
        x = cx + rv * math.cos(theta)
        y = cy + rv * math.sin(theta)
        points.append(f"{x:.1f},{y:.1f}")
        # Labels a bit further out
        lx = cx + (r_max + 30) * math.cos(theta)
        ly = cy + (r_max + 30) * math.sin(theta)
        label_pos.append((lx, ly, s["axis"], s["value"]))

    # Concentric grid rings
    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{r_max * (k/4):.1f}" class="radar-ring"/>'
        for k in (1, 2, 3, 4)
    )
    # Radial axes
    import math
    axes_lines = ""
    for i in range(n):
        theta = (i / n) * 2 * math.pi - math.pi / 2
        ex = cx + r_max * math.cos(theta)
        ey = cy + r_max * math.sin(theta)
        axes_lines += f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" class="radar-axis"/>'
    # Labels
    labels_svg = ""
    for (lx, ly, name, val) in label_pos:
        anchor = "middle"
        if lx < cx - 20: anchor = "end"
        elif lx > cx + 20: anchor = "start"
        labels_svg += f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" class="radar-label">{name}<tspan class="radar-val" dx="6">{val}</tspan></text>'

    # Tech heatmap tags — sorted by years descending
    heat = sorted(TECH_HEATMAP, key=lambda t: -t[1])
    max_yr = max(y for _, y in heat)
    heat_html = ""
    for name, years in heat:
        # Weight by years: font size 12-16, opacity 0.55-1.0
        w = years / max_yr
        fs = 11 + w * 4
        op = 0.55 + w * 0.45
        heat_html += f'<span class="heat-tag" style="font-size:{fs:.1f}px;--heat-op:{op:.2f}"><span class="heat-name">{name}</span><span class="heat-yr mono">{years}y</span></span>'

    return f'''
  <section class="skills-section" id="skills">
    <h2 class="section-h">
      <span class="section-num">04</span>
      <span class="section-name">Skills & Technology</span>
      <span class="section-hint">where I've spent my time</span>
    </h2>
    <div class="skills-grid">
      <div class="skills-radar">
        <svg viewBox="0 0 400 400" role="img" aria-label="Skill radar chart">
          {rings}
          {axes_lines}
          <polygon points="{" ".join(points)}" class="radar-poly"/>
          {labels_svg}
        </svg>
      </div>
      <div class="skills-heatmap">
        <div class="heat-title">Technology heat-map · years hands-on</div>
        <div class="heat-tags">
          {heat_html}
        </div>
      </div>
    </div>
  </section>'''


def render_chat():
    suggestions = "".join(
        f'<button type="button" class="chip" onclick="CHAT.ask(\'{q}\')">{q}</button>'
        for q in QA_SUGGESTIONS
    )
    return f'''
  <section class="chat-section" id="ask">
    <h2 class="section-h">
      <span class="section-num">05</span>
      <span class="section-name">Ask Me Anything</span>
      <span class="section-hint">keyword-driven · no AI API cost · try a suggestion</span>
    </h2>
    <div class="chat-box">
      <div class="chat-log" id="chat-log">
        <div class="chat-msg chat-bot">
          <div class="chat-avatar">SB</div>
          <div class="chat-body">Ask about my experience — AWS, GenAI, composable commerce, team size, global scale, etc. Try a suggestion below.</div>
        </div>
      </div>
      <div class="chat-chips">{suggestions}</div>
      <form class="chat-form" onsubmit="return CHAT.ask()">
        <input class="chat-input" type="text" placeholder="type a question, e.g. 'AWS experience?'" autocomplete="off"/>
        <button class="chat-send btn btn-primary" type="submit">Ask</button>
      </form>
    </div>
  </section>'''


def render_creds():
    cert_html = "".join(f'<li>{c}</li>' for c in CERTIFICATIONS)
    edu_html = "".join(f'''
      <div class="edu-card">
        <div class="edu-title">{e["title"]}</div>
        <div class="edu-school mono">{e["school"]}</div>
        <div class="edu-period muted mono">{e["period"]}</div>
      </div>''' for e in EDUCATION)
    return f'''
  <section class="creds-section" id="credentials">
    <h2 class="section-h">
      <span class="section-num">06</span>
      <span class="section-name">Education & Certifications</span>
    </h2>
    <div class="creds-grid">
      <div class="creds-cell">
        <h3 class="creds-h">Education</h3>
        {edu_html}
      </div>
      <div class="creds-cell">
        <h3 class="creds-h">Certifications</h3>
        <ul class="cert-list">{cert_html}</ul>
      </div>
    </div>
  </section>'''


def render_contact():
    return f'''
  <section class="contact-section" id="contact">
    <h2 class="section-h">
      <span class="section-num">07</span>
      <span class="section-name">Get in Touch</span>
    </h2>
    <div class="contact-grid">
      <a class="contact-card" href="mailto:{PROFILE["email"]}">
        <div class="contact-label mono">$ email</div>
        <div class="contact-val">{PROFILE["email"]}</div>
      </a>
      <a class="contact-card" href="{PROFILE["linkedin"]}" target="_blank" rel="noopener">
        <div class="contact-label mono">$ linkedin</div>
        <div class="contact-val">linkedin.com/in/sudhanshubhatnagar</div>
      </a>
      <a class="contact-card" href="tel:{PROFILE["phone"]}">
        <div class="contact-label mono">$ phone</div>
        <div class="contact-val">{PROFILE["phone"]}</div>
      </a>
      <div class="contact-card contact-card--static">
        <div class="contact-label mono">$ location</div>
        <div class="contact-val">{PROFILE["location"]}</div>
      </div>
    </div>
  </section>'''


# ---------- HEAD (SEO / OG / PWA / JSON-LD) ----------
def render_head():
    person_ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": PROFILE["name"],
        "jobTitle": PROFILE["title"],
        "email": f"mailto:{PROFILE['email']}",
        "telephone": PROFILE["phone"],
        "address": {"@type": "PostalAddress", "addressLocality": "Seattle", "addressRegion": "WA"},
        "url": PROFILE["site"],
        "sameAs": [PROFILE["linkedin"], PROFILE["github"]],
        "description": PROFILE["tagline"],
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": e["school"]} for e in EDUCATION
        ],
    }
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{PROFILE["name"]} — Principal TPM · Cloud · Composable Commerce · AI/ML</title>
  <meta name="description" content="{PROFILE["tagline"]}"/>
  <meta name="author" content="{PROFILE["name"]}"/>
  <meta name="theme-color" content="#0d1117"/>

  <!-- Open Graph / Twitter -->
  <meta property="og:type" content="profile"/>
  <meta property="og:title" content="{PROFILE["name"]} — {PROFILE["title"]}"/>
  <meta property="og:description" content="{PROFILE["tagline"]}"/>
  <meta property="og:url" content="{PROFILE["site"]}"/>
  <meta property="profile:first_name" content="Sudhanshu"/>
  <meta property="profile:last_name" content="Bhatnagar"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="{PROFILE["name"]} — {PROFILE["title"]}"/>
  <meta name="twitter:description" content="{PROFILE["tagline"]}"/>

  <link rel="canonical" href="{PROFILE["site"]}"/>
  <link rel="shortcut icon" href="favicon.ico"/>
  <link rel="manifest" href="manifest.json"/>

  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>

  <script type="application/ld+json">
{json.dumps(person_ld, indent=2)}
  </script>
  <style>{CSS}</style>
</head>'''


# ---------- CSS ----------
CSS = """
:root{
  --bg:#0d1117; --panel:#161b22; --panel-hi:#1f2630; --line:#30363d;
  --ink:#e6edf3; --ink-2:#9ba7b4; --ink-3:#6e7681; --ink-4:#4a5563;
  --green:#7ee787; --blue:#79c0ff; --purple:#d2a8ff; --orange:#ffa657; --pink:#ff7b72; --yellow:#f2cc60;
  --accent:var(--green); --accent-2:var(--blue);
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  --radius:12px; --radius-sm:8px;
  --shadow-1:0 4px 24px rgba(0,0,0,.35);
  --shadow-2:0 12px 48px rgba(0,0,0,.45);
  --hero-bg-1:rgba(126,231,135,.06); --hero-bg-2:rgba(121,192,255,.05);
}
body.view-classic{
  --bg:#ffffff; --panel:#f6f8fa; --panel-hi:#eaedf1; --line:#d0d7de;
  --ink:#1f2328; --ink-2:#57606a; --ink-3:#6b7280; --ink-4:#9aa0a6;
  --green:#1a7f37; --blue:#0969da; --purple:#8250df; --orange:#bc4c00; --pink:#cf222e; --yellow:#9a6700;
  --accent:var(--blue); --accent-2:var(--purple);
  --shadow-1:0 2px 12px rgba(15,23,42,.06);
  --shadow-2:0 8px 32px rgba(15,23,42,.10);
  --hero-bg-1:rgba(9,105,218,.05); --hero-bg-2:rgba(130,80,223,.04);
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;padding:0;
  background:var(--bg);color:var(--ink);
  font-family:var(--sans);font-size:15px;line-height:1.6;
  -webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,var(--hero-bg-1) 0%,transparent 40%),radial-gradient(circle at 80% 60%,var(--hero-bg-2) 0%,transparent 45%);
  background-attachment:fixed;
  transition:background .3s,color .3s;
}
a{color:var(--accent-2);text-decoration:none}
a:hover{text-decoration:underline;text-decoration-color:var(--accent);text-underline-offset:3px}
.mono{font-family:var(--mono)}
.muted{color:var(--ink-3)}
h1,h2,h3{margin:0;line-height:1.25}
ul{margin:0;padding:0;list-style:none}

/* Sticky top nav */
.topbar{
  position:sticky;top:0;z-index:50;
  background:color-mix(in oklab,var(--bg) 92%,transparent);
  backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);
}
.topbar-inner{
  max-width:1120px;margin:0 auto;padding:12px 20px;
  display:flex;align-items:center;gap:16px;flex-wrap:wrap;
}
.tb-brand{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-weight:600;color:var(--ink)}
.tb-brand .b-avatar{
  width:32px;height:32px;border-radius:50%;background:var(--panel-hi);
  display:inline-flex;align-items:center;justify-content:center;
  color:var(--accent);font-weight:700;font-size:12.5px;letter-spacing:.5px;
  border:1px solid var(--line);
}
.tb-brand .b-role{color:var(--ink-2);font-weight:500;font-size:13px}
body.view-classic .tb-brand{font-family:var(--sans)}
.tb-spacer{flex:1}
.tb-nav{display:flex;gap:14px;font-size:13px}
.tb-nav a{color:var(--ink-2)}
.tb-nav a:hover{color:var(--accent)}
.view-switch{
  display:inline-flex;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:3px;
}
.view-switch button{
  background:transparent;color:var(--ink-2);border:0;padding:5px 13px;font:600 12.5px/1 var(--mono);
  border-radius:999px;cursor:pointer;
}
.view-switch button.is-active{background:var(--accent);color:var(--bg)}
body.view-classic .view-switch button.is-active{color:#fff}

.container{max-width:1120px;margin:0 auto;padding:32px 20px 96px}

/* Hero */
.hero{padding:20px 0 8px}
.hero-shell{margin-bottom:36px}
.prompt-line{font-family:var(--mono);font-size:13.5px;color:var(--ink-3);margin-bottom:16px}
.prompt-line .prompt{color:var(--accent-2)}
.prompt-line .prompt-sep{color:var(--ink-3);margin:0 8px}
.prompt-line .typed{color:var(--ink)}
.prompt-line .caret{color:var(--accent);animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.hero-name{font-family:var(--sans);font-size:56px;font-weight:800;letter-spacing:-1.5px;line-height:1.05;margin:0 0 6px}
body.view-classic .hero-name{color:var(--ink)}
.hero-title{font-size:20px;color:var(--accent);font-weight:600;margin:0 0 12px;font-family:var(--mono)}
body.view-classic .hero-title{font-family:var(--sans);color:var(--accent)}
.hero-tagline{font-size:16.5px;color:var(--ink-2);max-width:780px;margin:0 0 26px}
.hero-cta{display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:8px;padding:9px 16px;border-radius:999px;font:600 13.5px/1 var(--sans);cursor:pointer;transition:transform .12s,background .2s,border-color .2s;border:1px solid transparent}
.btn:hover{transform:translateY(-1px);text-decoration:none}
.btn-primary{background:var(--accent);color:var(--bg);border-color:var(--accent)}
body.view-classic .btn-primary{color:#fff}
.btn-primary:hover{background:color-mix(in oklab,var(--accent) 88%,#fff)}
.btn-ghost{background:transparent;color:var(--ink);border-color:var(--line)}
.btn-ghost:hover{background:var(--panel);border-color:var(--ink-4)}

.metrics-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
  gap:12px;margin-top:14px;
}
.metric{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:18px 18px 16px;box-shadow:var(--shadow-1)}
.metric-value{font:800 30px/1.1 var(--sans);color:var(--accent);letter-spacing:-.5px}
.metric-value .val{font-variant-numeric:tabular-nums}
.metric-label{font-size:12.5px;color:var(--ink-2);margin-top:6px;line-height:1.45}

/* Section headings */
.section-h{
  display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;
  margin:56px 0 20px;padding-bottom:12px;border-bottom:1px solid var(--line);
}
.section-num{
  font:700 12px/1 var(--mono);color:var(--accent);letter-spacing:2px;
  padding:5px 8px;background:color-mix(in oklab,var(--accent) 15%,transparent);border-radius:6px;
}
.section-name{font-size:26px;font-weight:700;color:var(--ink);margin-right:auto}
.section-hint{font:500 12.5px/1.4 var(--mono);color:var(--ink-3)}

/* Terminal REPL */
.terminal{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-1)}
.terminal-chrome{display:flex;align-items:center;gap:6px;padding:10px 14px;background:var(--panel-hi);border-bottom:1px solid var(--line)}
.tc-dot{width:12px;height:12px;border-radius:50%}
.tc-r{background:#ff5f56}.tc-y{background:#ffbd2e}.tc-g{background:#27c93f}
.tc-title{margin-left:12px;font:500 12px/1 var(--mono);color:var(--ink-3);letter-spacing:.5px}
.terminal-body{padding:16px 18px 12px;max-height:520px;overflow-y:auto;font-family:var(--mono);font-size:13.5px;line-height:1.65}
.repl-line{margin-bottom:8px;white-space:pre-wrap;word-break:break-word}
.repl-line b{color:var(--accent)}
.repl-line em{color:var(--yellow);font-style:normal}
.repl-line .in{color:var(--blue)}
.repl-line .err{color:var(--pink)}
.repl-form{display:flex;align-items:center;gap:10px;padding-top:8px;border-top:1px dashed var(--line);margin-top:6px}
.repl-prompt{color:var(--accent);font-weight:600}
.repl-input{flex:1;background:transparent;border:0;color:var(--ink);font:400 13.5px/1.5 var(--mono);outline:none;padding:6px 2px}
.repl-input::placeholder{color:var(--ink-4)}
.repl-chips{display:flex;flex-wrap:wrap;gap:6px;padding:10px 0 0}
.chip{background:transparent;border:1px solid var(--line);color:var(--ink-2);font:500 12px/1 var(--mono);padding:6px 10px;border-radius:999px;cursor:pointer}
.chip:hover{border-color:var(--accent);color:var(--accent)}

/* Timeline */
.timeline{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px 20px 30px;position:relative}
.tl-ruler{position:relative;height:20px;margin-bottom:14px;border-bottom:1px dashed var(--line)}
.tl-tick{position:absolute;top:0;transform:translateX(-50%);color:var(--ink-3);font:500 11px/1 var(--mono);padding-top:2px}
.tl-bars{display:flex;flex-direction:column;gap:8px;position:relative}
.tl-row{display:flex;align-items:center;gap:12px}
.tl-label{width:140px;flex-shrink:0;font-size:12.5px;color:var(--ink-2);text-align:right}
.tl-track{flex:1;position:relative;height:26px;background:color-mix(in oklab,var(--panel-hi) 60%,transparent);border-radius:6px}
.tl-bar{
  position:absolute;top:0;height:26px;
  background:linear-gradient(90deg,color-mix(in oklab,var(--accent) 70%,transparent),color-mix(in oklab,var(--accent) 40%,transparent));
  border:1px solid color-mix(in oklab,var(--accent) 50%,var(--line));
  border-radius:5px;cursor:pointer;
  transition:transform .12s,filter .12s;
  color:var(--ink);
  padding:0 10px;font:500 11.5px/26px var(--mono);text-align:left;overflow:hidden;
  white-space:nowrap;text-overflow:ellipsis;
}
.tl-bar:hover{filter:brightness(1.15);transform:scale(1.02);z-index:2}
.tl-bar.is-active{
  background:linear-gradient(90deg,var(--accent),color-mix(in oklab,var(--accent) 70%,transparent));
  color:var(--bg);
  box-shadow:0 0 0 2px color-mix(in oklab,var(--accent) 40%,transparent);
}
body.view-classic .tl-bar.is-active{color:#fff}
.tl-details{margin-top:18px;min-height:60px}
.tl-detail{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px 22px 18px}
.tl-detail-head{display:flex;align-items:center;gap:14px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px dashed var(--line)}
.tl-logo{
  width:48px;height:48px;border-radius:10px;
  background:color-mix(in oklab,var(--accent) 15%,transparent);
  color:var(--accent);
  display:flex;align-items:center;justify-content:center;font:700 18px/1 var(--mono);
}
.tl-detail-role{font-size:17px;font-weight:700;color:var(--ink);margin-bottom:2px}
.tl-detail-company{font-size:12.5px;color:var(--ink-2)}
.tl-detail-highlights{display:grid;gap:6px}
.tl-detail-highlights li{padding-left:20px;position:relative;font-size:14px;color:var(--ink-2);line-height:1.55}
.tl-detail-highlights li::before{content:"▸";position:absolute;left:0;top:0;color:var(--accent)}

/* Cases */
.cases-grid{display:grid;gap:14px}
.case{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;transition:border-color .2s,transform .12s}
.case:hover{border-color:var(--ink-4)}
.case-head{
  display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:16px;
  width:100%;padding:20px 22px;background:transparent;border:0;cursor:pointer;text-align:left;color:inherit;
}
.case-meta{display:flex;flex-direction:column;gap:2px;min-width:150px}
.case-company{font-size:12px;color:var(--accent);font-weight:600;letter-spacing:.5px;text-transform:uppercase}
.case-period{font-size:11.5px;color:var(--ink-3)}
.case-title{font-size:17px;font-weight:600;color:var(--ink)}
.case-chev{color:var(--ink-3);transition:transform .2s}
.case[open] .case-chev,.case-head[aria-expanded="true"] .case-chev{transform:rotate(180deg);color:var(--accent)}
.case-body{padding:0 22px 22px;border-top:1px dashed var(--line);padding-top:18px;display:grid;gap:16px}
.case-body[hidden]{display:none}
.case-label{font:700 10.5px/1 var(--mono);color:var(--accent);letter-spacing:2px;text-transform:uppercase;margin-bottom:6px}
.case-block p{margin:0;color:var(--ink-2);font-size:14.5px}
.case-outcome{display:grid;gap:6px}
.case-outcome li{position:relative;padding-left:20px;font-size:14px;color:var(--ink-2)}
.case-outcome li::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:700}
.case-tech p{font-size:12.5px}

/* Skills */
.skills-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:14px}
@media (max-width:900px){.skills-grid{grid-template-columns:1fr}}
.skills-radar,.skills-heatmap{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:20px}
.skills-radar svg{width:100%;height:auto;max-height:380px}
.radar-ring{fill:none;stroke:var(--line);stroke-width:1;opacity:.5}
.radar-axis{stroke:var(--line);stroke-width:1;opacity:.4}
.radar-poly{fill:color-mix(in oklab,var(--accent) 25%,transparent);stroke:var(--accent);stroke-width:2;stroke-linejoin:round}
.radar-label{fill:var(--ink);font:600 12px var(--sans)}
.radar-val{fill:var(--accent);font:700 11px var(--mono)}
.heat-title{font:600 12px/1 var(--mono);letter-spacing:1.5px;text-transform:uppercase;color:var(--ink-3);margin-bottom:14px}
.heat-tags{display:flex;flex-wrap:wrap;gap:6px}
.heat-tag{
  display:inline-flex;align-items:center;gap:6px;
  padding:5px 10px 5px 10px;background:color-mix(in oklab,var(--panel-hi) 90%,transparent);
  border:1px solid var(--line);border-radius:999px;
  color:var(--ink);opacity:var(--heat-op);
}
.heat-tag:hover{opacity:1;border-color:var(--accent)}
.heat-yr{color:var(--accent);font-weight:600;font-size:11px}

/* Chat */
.chat-box{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px 18px;display:grid;gap:12px}
.chat-log{display:grid;gap:10px;max-height:520px;overflow-y:auto;padding:6px 4px}
.chat-msg{display:flex;gap:12px;align-items:flex-start}
.chat-msg.chat-user{flex-direction:row-reverse}
.chat-avatar{
  width:32px;height:32px;flex-shrink:0;border-radius:50%;
  background:var(--panel-hi);color:var(--accent);border:1px solid var(--line);
  display:flex;align-items:center;justify-content:center;font:700 11px/1 var(--mono);
}
.chat-user .chat-avatar{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.chat-body{background:var(--panel-hi);border:1px solid var(--line);border-radius:12px;padding:10px 14px;font-size:14px;color:var(--ink);max-width:80%}
.chat-user .chat-body{background:color-mix(in oklab,var(--accent) 20%,var(--panel-hi));border-color:color-mix(in oklab,var(--accent) 40%,var(--line))}
.chat-chips{display:flex;flex-wrap:wrap;gap:6px}
.chat-form{display:flex;gap:8px;margin-top:4px}
.chat-input{
  flex:1;background:var(--panel-hi);border:1px solid var(--line);border-radius:999px;
  color:var(--ink);font:400 14px var(--sans);padding:10px 16px;outline:none;
}
.chat-input:focus{border-color:var(--accent)}

/* Creds */
.creds-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width:800px){.creds-grid{grid-template-columns:1fr}}
.creds-cell{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px}
.creds-h{font-size:14.5px;font-weight:700;color:var(--ink);margin-bottom:14px;font-family:var(--mono);letter-spacing:.5px}
.edu-card{padding:12px 0;border-bottom:1px dashed var(--line)}
.edu-card:last-child{border-bottom:0}
.edu-title{font-size:14.5px;font-weight:600;color:var(--ink);margin-bottom:2px}
.edu-school{font-size:12.5px;color:var(--ink-2)}
.edu-period{font-size:11.5px;margin-top:2px}
.cert-list{display:grid;gap:8px}
.cert-list li{padding-left:22px;position:relative;font-size:14px;color:var(--ink-2);line-height:1.55}
.cert-list li::before{content:"🎓";position:absolute;left:0;top:0}

/* Contact */
.contact-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.contact-card{
  display:block;background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);
  padding:18px 20px;color:inherit;transition:border-color .2s,transform .12s;
}
.contact-card:hover{border-color:var(--accent);transform:translateY(-2px);text-decoration:none}
.contact-card--static:hover{transform:none;border-color:var(--line)}
.contact-label{font-size:11px;color:var(--ink-3);letter-spacing:.5px;text-transform:lowercase;margin-bottom:6px}
.contact-val{font-size:14.5px;color:var(--ink);word-break:break-all}

/* Footer */
.doc-footer{
  max-width:1120px;margin:60px auto 0;padding:32px 20px;border-top:1px solid var(--line);
  display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;
  font-size:12.5px;color:var(--ink-3);font-family:var(--mono);
}
.doc-footer a{color:var(--ink-2)}
.doc-footer .fkey{color:var(--accent)}

/* Print — force classic + simplify */
@media print{
  body{background:#fff;color:#111}
  .topbar,.view-switch,.repl-section,.chat-section,.hero-cta,.repl-chips,.chat-chips,.chat-form,.section-hint,.doc-footer{display:none !important}
  .container{padding:0;max-width:none}
  .section-h{page-break-after:avoid;border-color:#ccc;margin:24px 0 12px}
  .section-name{font-size:20px;color:#111}
  .section-num{background:#eee;color:#333}
  .metric,.terminal,.timeline,.case,.creds-cell,.skills-radar,.skills-heatmap,.contact-card{
    background:#fff !important;border:1px solid #ddd !important;box-shadow:none !important;
    page-break-inside:avoid;
  }
  .case-body{display:grid !important}
  .case-body[hidden]{display:grid !important}
  .hero-name{font-size:32px}
  .hero-title{color:#0969da;font-family:sans-serif}
  * {print-color-adjust:exact;-webkit-print-color-adjust:exact}
}

/* Reveal-on-scroll animation */
.reveal{opacity:0;transform:translateY(12px);transition:opacity .55s ease-out,transform .55s ease-out}
.reveal.is-shown{opacity:1;transform:none}

@media (max-width:600px){
  .hero-name{font-size:38px}
  .hero-title{font-size:17px}
  .metric-value{font-size:24px}
  .tl-label{width:100px;font-size:11.5px}
  .tl-bar-label{display:none}
  .case-head{grid-template-columns:1fr auto;padding:16px 18px}
  .case-meta{margin-bottom:6px}
  .terminal-body{max-height:400px}
}
"""


# ---------- JS ----------
def js_bundle():
    qa_data = json.dumps(QA)
    easter_data = json.dumps(EASTER_EGGS)
    roles_data = json.dumps([{
        "id": r["id"], "company": r["company"], "role": r["role"],
        "period": fmt_range(r), "location": r["location"],
        "highlights": r["highlights"],
    } for r in ROLES])
    return f"""
// ---- View toggle ----
const View = {{
  KEY: 'wsr-view',
  init(){{
    const saved = localStorage.getItem(this.KEY) || 'terminal';
    this.apply(saved);
    document.querySelectorAll('.view-switch button').forEach(b=>{{
      b.addEventListener('click',()=>this.apply(b.dataset.view));
    }});
  }},
  apply(v){{
    document.body.classList.toggle('view-classic', v==='classic');
    document.body.classList.toggle('view-terminal', v==='terminal');
    document.querySelectorAll('.view-switch button').forEach(b=>{{
      b.classList.toggle('is-active', b.dataset.view===v);
    }});
    localStorage.setItem(this.KEY, v);
  }}
}};

// ---- Counters ----
const Counters = {{
  init(){{
    const els = document.querySelectorAll('.metric');
    if(!('IntersectionObserver' in window)){{
      els.forEach(el=>this.animate(el)); return;
    }}
    const io = new IntersectionObserver(entries=>{{
      entries.forEach(e=>{{
        if(e.isIntersecting){{ this.animate(e.target); io.unobserve(e.target); }}
      }});
    }},{{threshold:.3}});
    els.forEach(el=>io.observe(el));
  }},
  animate(el){{
    const target = parseFloat(el.dataset.target);
    const isFloat = String(target).indexOf('.')>=0;
    const dur=1400; const start=performance.now();
    const valEl = el.querySelector('.val');
    const tick=(now)=>{{
      const t = Math.min(1,(now-start)/dur);
      const eased = 1-Math.pow(1-t,3);
      const v = target*eased;
      valEl.textContent = isFloat ? v.toFixed(2) : Math.floor(v).toLocaleString();
      if(t<1) requestAnimationFrame(tick);
      else valEl.textContent = isFloat ? target.toFixed(2) : target.toLocaleString();
    }};
    requestAnimationFrame(tick);
  }}
}};

// ---- Reveal-on-scroll ----
const Reveal = {{
  init(){{
    if(!('IntersectionObserver' in window)) return;
    document.querySelectorAll('section, .case, .creds-cell, .contact-card').forEach(el=>el.classList.add('reveal'));
    const io = new IntersectionObserver(entries=>{{
      entries.forEach(e=>{{
        if(e.isIntersecting){{ e.target.classList.add('is-shown'); io.unobserve(e.target); }}
      }});
    }},{{threshold:.1}});
    document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  }}
}};

// ---- Typed "whoami" effect in hero prompt ----
const Typed = {{
  init(){{
    document.querySelectorAll('.typed').forEach(el=>{{
      const text = el.dataset.typed || ''; let i=0;
      const step = ()=>{{
        el.textContent = text.slice(0,i++);
        if(i<=text.length) setTimeout(step, 70);
      }};
      setTimeout(step, 260);
    }});
  }}
}};

// ---- Timeline ----
const Timeline = {{
  roles: {roles_data},
  init(){{
    document.querySelectorAll('.tl-bar').forEach(b=>{{
      b.addEventListener('click',()=>this.select(b.dataset.role));
    }});
    if(this.roles.length) this.select(this.roles[0].id);
  }},
  select(id){{
    document.querySelectorAll('.tl-bar').forEach(b=>b.classList.toggle('is-active', b.dataset.role===id));
    document.querySelectorAll('.tl-detail').forEach(d=>d.hidden = d.dataset.role!==id);
  }}
}};

// ---- Cases (expand/collapse) ----
const CASES = {{
  toggle(btn){{
    const open = btn.getAttribute('aria-expanded')==='true';
    btn.setAttribute('aria-expanded', open? 'false':'true');
    const body = btn.parentElement.querySelector('.case-body');
    if(body) body.hidden = open;
  }}
}};

// ---- Terminal REPL ----
const REPL = {{
  history: [], histIdx: 0,
  init(){{
    this.out = document.getElementById('repl-output');
    this.input = document.querySelector('.repl-input');
    this.input.addEventListener('keydown', (e)=>{{
      if(e.key==='ArrowUp'){{ if(this.histIdx>0){{ this.histIdx--; this.input.value = this.history[this.histIdx]||''; }} e.preventDefault(); }}
      if(e.key==='ArrowDown'){{ if(this.histIdx<this.history.length){{ this.histIdx++; this.input.value = this.history[this.histIdx]||''; }} e.preventDefault(); }}
      if(e.key==='Tab'){{
        e.preventDefault();
        const cmds = ['help','whoami','experience','programs','skills','contact','resume','theme','clear','ls','linkedin','github'];
        const cur = this.input.value;
        const hit = cmds.find(c=>c.startsWith(cur));
        if(hit) this.input.value = hit;
      }}
    }});
  }},
  run(e){{
    e.preventDefault();
    const cmd = (this.input.value||'').trim();
    if(cmd) this.runCmd(cmd);
    this.input.value=''; this.histIdx = this.history.length;
    return false;
  }},
  runCmd(cmd){{
    this.history.push(cmd); this.histIdx = this.history.length;
    this.write('<span class="in">$ '+this.escape(cmd)+'</span>');
    this.dispatch(cmd);
    if(this.out.parentElement) this.out.parentElement.scrollTop = this.out.parentElement.scrollHeight;
  }},
  write(html){{
    const div = document.createElement('div');
    div.className='repl-line';
    div.innerHTML = html;
    this.out.appendChild(div);
  }},
  escape(s){{ return s.replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c])); }},
  dispatch(cmd){{
    const [c, ...rest] = cmd.split(/\\s+/);
    const arg = rest.join(' ');
    const easter = {easter_data};
    if(cmd in easter) return this.write(easter[cmd]);
    switch(c){{
      case 'help': return this.write(
        '<b>Available commands:</b><br>'+
        '  <b>whoami</b>       intro<br>'+
        '  <b>experience</b>   career log<br>'+
        '  <b>programs</b>     flagship program list<br>'+
        '  <b>skills</b>       technology summary<br>'+
        '  <b>contact</b>      email, phone, LinkedIn<br>'+
        '  <b>resume</b>       download PDF<br>'+
        '  <b>theme</b>        toggle terminal/classic<br>'+
        '  <b>ls</b>           list sections<br>'+
        '  <b>clear</b>        clear the terminal<br>'+
        '  <b>linkedin</b>     open LinkedIn<br>'+
        '  <b>github</b>       open GitHub'
      );
      case 'whoami': return this.write(
        '<b>Sudhanshu Bhatnagar</b><br>'+
        'Principal Technical Program Manager · Seattle, WA<br>'+
        '22+ years delivering cloud, composable commerce, and AI/ML programs.<br>'+
        'Currently: Lululemon (B2B e-Commerce + Global POS). Previously: Nordstrom, Amazon, T-Mobile.'
      );
      case 'experience':
      case 'exp': {{
        let out = '';
        Timeline.roles.forEach(r=>{{
          out += '<em>'+r.company+'</em>  <span class="muted">'+r.period+'</span><br>';
          out += '  '+r.role+'<br>';
          r.highlights.slice(0,2).forEach(h=>{{ out += '    • '+h+'<br>'; }});
          out += '<br>';
        }});
        return this.write(out);
      }}
      case 'programs':
      case 'prog': {{
        let out = '<b>Flagship programs</b> (see full detail in the section below):<br>';
        {json.dumps([{"c":p["company"],"t":p["title"],"p":p["period"]} for p in PROGRAMS])}.forEach(p=>{{
          out += '  <em>'+p.c+'</em>  '+p.t+'  <span class="muted">'+p.p+'</span><br>';
        }});
        return this.write(out);
      }}
      case 'skills': return this.write(
        'Cloud: <em>AWS</em>, Azure, EKS, Kubernetes<br>'+
        'Commerce: <em>Commercetools</em>, MACH, headless, API-first<br>'+
        'AI/ML: <em>Bedrock</em>, LangChain, RAG, LLM<br>'+
        'Engineering: microservices, Spring-Boot, Node, React, Kafka<br>'+
        'Program: PgMP, PMP, SAFe, JIRA, Confluence, Tableau, Grafana, Datadog<br>'+
        '<span class="muted">(see the Skills section below for the full heat-map)</span>'
      );
      case 'contact': return this.write(
        '📧 <a href="mailto:{PROFILE["email"]}">{PROFILE["email"]}</a><br>'+
        '📞 <a href="tel:{PROFILE["phone"]}">{PROFILE["phone"]}</a><br>'+
        '💼 <a href="{PROFILE["linkedin"]}" target="_blank">linkedin.com/in/sudhanshubhatnagar</a><br>'+
        '📍 {PROFILE["location"]}'
      );
      case 'resume':
      case 'pdf':
      case 'download': return this.write('<a href="assets/files/Sudhanshu-Bhatnagar.pdf" download>Download the PDF</a>');
      case 'theme': {{
        const now = document.body.classList.contains('view-classic') ? 'terminal' : 'classic';
        View.apply(now);
        return this.write('theme switched to <em>'+now+'</em>');
      }}
      case 'ls': return this.write('hero  terminal  career  programs  skills  ask  credentials  contact');
      case 'clear': this.out.innerHTML=''; return;
      case 'linkedin': window.open('{PROFILE["linkedin"]}','_blank'); return this.write('opened LinkedIn ↗');
      case 'github':   window.open('{PROFILE["github"]}','_blank');   return this.write('opened GitHub ↗');
      case '':         return;
      default: return this.write('<span class="err">command not found:</span> '+this.escape(cmd)+'  <span class="muted">— try `help`</span>');
    }}
  }}
}};

// ---- Chat (static Q&A) ----
const CHAT = {{
  qa: {qa_data},
  init(){{
    this.log = document.getElementById('chat-log');
    this.input = document.querySelector('.chat-input');
  }},
  ask(txt){{
    const q = txt || this.input.value; if(!q) return false;
    this.append('user', q);
    const a = this.answer(q);
    setTimeout(()=>this.append('bot', a), 220);
    if(!txt) this.input.value='';
    return false;
  }},
  answer(q){{
    const s = q.toLowerCase();
    for(const [keys, resp] of this.qa){{
      if(keys.some(k=>s.includes(k))) return resp;
    }}
    return "Not sure about that specific one — try keywords like <em>AWS</em>, <em>GenAI</em>, <em>composable commerce</em>, <em>team size</em>, or <em>global scale</em>. Or hit <em>Contact</em> and just ask directly.";
  }},
  append(kind, html){{
    const wrap = document.createElement('div');
    wrap.className = 'chat-msg chat-' + kind;
    wrap.innerHTML = '<div class="chat-avatar">'+(kind==='user'?'You':'SB')+'</div>'+
                     '<div class="chat-body">'+html+'</div>';
    this.log.appendChild(wrap);
    this.log.scrollTop = this.log.scrollHeight;
  }}
}};

// ---- Register service worker (PWA offline) ----
if('serviceWorker' in navigator){{
  window.addEventListener('load',()=>{{
    navigator.serviceWorker.register('sw.js').catch(()=>{{}});
  }});
}}

// ---- Boot ----
document.addEventListener('DOMContentLoaded',()=>{{
  View.init();
  Counters.init();
  Reveal.init();
  Typed.init();
  Timeline.init();
  REPL.init();
  CHAT.init();
}});
"""


# ---------- Nav + Footer ----------
def render_nav():
    return f'''
<nav class="topbar">
  <div class="topbar-inner">
    <div class="tb-brand">
      <span class="b-avatar">SB</span>
      <div>
        <div>Sudhanshu Bhatnagar</div>
        <div class="b-role">Principal TPM · Seattle</div>
      </div>
    </div>
    <div class="tb-spacer"></div>
    <div class="tb-nav">
      <a href="#terminal">Terminal</a>
      <a href="#career">Career</a>
      <a href="#programs">Programs</a>
      <a href="#skills">Skills</a>
      <a href="#ask">Ask</a>
      <a href="#contact">Contact</a>
    </div>
    <div class="view-switch" role="group" aria-label="View theme">
      <button data-view="terminal" class="is-active">Terminal</button>
      <button data-view="classic">Classic</button>
    </div>
  </div>
</nav>'''

def render_footer():
    return f'''
<footer class="doc-footer">
  <div>© {date.today().year} · {PROFILE["name"]} · <span class="fkey">$</span> hosted at <a href="https://github.com/Sudhanshu311/Sudhanshu311.github.io" target="_blank">github.com/Sudhanshu311</a></div>
  <div>Interactive resume · <span class="fkey">v2</span> · Ctrl/⌘+P for print view</div>
</footer>'''


# ---------- Assemble ----------
def main():
    head = render_head()
    body = "\n".join([
        render_nav(),
        '<main class="container">',
        render_hero(),
        render_repl(),
        render_timeline(),
        render_cases(),
        render_skills(),
        render_chat(),
        render_creds(),
        render_contact(),
        '</main>',
        render_footer(),
    ])
    html = head + '\n<body class="view-terminal">\n' + body + '\n<script>' + js_bundle() + '</script>\n</body>\n</html>'
    OUT.write_text(html, encoding='utf-8')
    print(f"wrote {OUT} ({len(html)} bytes, {html.count(chr(10))+1} lines)")


if __name__ == "__main__":
    main()
