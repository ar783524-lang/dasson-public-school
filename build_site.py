import re, os, shutil, json, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "site.html")
OUT_DIR = os.path.join(ROOT, "dist")
CONTENT_DIR = os.path.join(ROOT, "content")
ASSETS_SRC = os.path.join(ROOT, "assets")
sys.path.insert(0, ROOT)

with open(os.path.join(CONTENT_DIR, "faculty.json")) as f:
    FACULTY_DATA = json.load(f).get("teachers", [])
with open(os.path.join(CONTENT_DIR, "results.json")) as f:
    RESULTS_DATA = json.load(f)
with open(os.path.join(CONTENT_DIR, "news.json")) as f:
    NEWS_DATA = json.load(f).get("clippings", [])

with open(SRC) as f:
    src = f.read()

def extract_between(start_marker, end_marker):
    s = src.index(start_marker)
    e = src.index(end_marker, s)
    return src[s:e]

def extract_section(open_tag):
    s = src.index(open_tag)
    e = src.index("</section>", s) + len("</section>")
    return src[s:e]

# ---- extract raw pieces from the original single-page file ----
style_raw = extract_between("<style>", "</style>")
style_css = style_raw[len("<style>"):].strip()

script_raw = extract_between("<script>", "</script>")
script_js_old = script_raw[len("<script>"):].strip()

hero = extract_section('<section class="hero" id="home">')
quote = extract_section('<section class="quote-strip">')
about = extract_section('<section id="about">')
courses = extract_section('<section id="courses">')
admissions = extract_section('<section class="alt" id="admissions">')
gallery = extract_section('<section class="alt" id="gallery">')
contact = extract_section('<section id="contact">')

modal_html = src[src.index('<div class="modal-overlay"'):src.index('<script>')].strip()

# ---- fix hero: real logo asset + real page links ----
hero = hero.replace('data:image/png;base64,__LOGO_B64__', 'assets/logo.png')
hero = hero.replace('href="#admissions"', 'href="admissions.html"')
hero = hero.replace('href="#about"', 'href="about.html"')

# ---- add scroll-reveal / stagger hooks ----
def add_reveal_to_head(html):
    return html.replace('<div class="section-head">', '<div class="section-head reveal">', 1)

quote = quote.replace('<div class="wrap">', '<div class="wrap reveal">', 1)

about = about.replace('<div class="wrap about-grid">\n    <div>', '<div class="wrap about-grid">\n    <div class="reveal-left">')
about = about.replace('<div class="about-art">', '<div class="about-art reveal-right">')

courses = add_reveal_to_head(courses)
courses = courses.replace('<div class="grade-grid">', '<div class="grade-grid" data-stagger>')
courses = courses.replace('class="grade" data-class=', 'class="grade reveal" data-class=')

admissions = add_reveal_to_head(admissions)
admissions = admissions.replace('<div class="steps">', '<div class="steps" data-stagger>')
admissions = admissions.replace('<div class="step">', '<div class="step reveal">')
admissions = admissions.replace('<div class="adm-block">', '<div class="adm-block reveal">')
admissions = admissions.replace('<div class="elig-grid">', '<div class="elig-grid" data-stagger>')
admissions = admissions.replace('<div class="elig-card">', '<div class="elig-card reveal">')
admissions = admissions.replace('<ul class="doc-list">', '<ul class="doc-list" data-stagger>')
admissions = admissions.replace('<li><span class="doc-check">', '<li class="reveal"><span class="doc-check">')

# faculty section is now generated directly from content/faculty.json (see below, after home_v2 import)

gallery = add_reveal_to_head(gallery)
gallery = gallery.replace('<div class="life-grid">', '<div class="life-grid" data-stagger>')
gallery = re.sub(r'class="life-card (c-\w+)"', r'class="life-card \1 reveal"', gallery)

contact = add_reveal_to_head(contact)
contact = contact.replace('<div class="map-card">', '<div class="map-card reveal-right">')
contact = contact.replace('<div class="contact-grid">\n      <div>', '<div class="contact-grid">\n      <div class="reveal-left">')
contact = contact.replace('<form action="mailto:dpsrajgarh444@gmail.com" method="post" enctype="text/plain">',
                           '<form class="reveal-right" action="mailto:dpsrajgarh444@gmail.com" method="post" enctype="text/plain">')

# ---- shared header / footer (real page links + real logo file) ----
HEADER = """<header>
  <div class="affil-bar">Affiliated to HPBOSE</div>
  <div class="topbar">
    <div class="wrap">
      <div class="topbar-links">
        <span class="school-code"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8" cy="12" r="2"/><path d="M13 10h6M13 14h4"/></svg>School Code: 4084</span>
        <a href="mailto:dpsrajgarh444@gmail.com"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18v12H3z"/><path d="M3 7l9 6 9-6"/></svg>dpsrajgarh444@gmail.com</a>
      </div>
      <span class="topbar-loc">Rajgarh, Sirmaur, Himachal Pradesh</span>
    </div>
  </div>
  <nav class="wrap navbar">
    <a class="brand" href="index.html">
      <img src="assets/logo.png" alt="Dasson Public High School logo">
      <span>Dasson Public High School<small>Rajgarh</small></span>
    </a>
    <ul class="navlinks">
      <li><a href="about.html">About</a></li>
      <li><a href="courses.html">Courses</a></li>
      <li><a href="admissions.html">Admissions</a></li>
      <li><a href="faculty.html">Faculty</a></li>
      <li><a href="gallery.html">Gallery</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li class="mobile-apply-item"><a href="admissions.html" class="mobile-apply">Apply Now</a></li>
    </ul>
    <a class="btn btn-primary nav-apply" href="admissions.html">Apply Now</a>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </nav>
</header>
"""

FOOTER = """<footer>
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <div class="footer-logo-row">
        <img src="assets/logo.png" alt="Dasson Public High School logo">
        <span>Dasson Public High School</span>
      </div>
      <p>Rajgarh, Sirmaur, Himachal Pradesh</p>
    </div>
    <div>
      <h4>Explore</h4>
      <a href="about.html">About</a>
      <a href="courses.html">Courses</a>
      <a href="admissions.html">Admissions</a>
      <a href="faculty.html">Faculty</a>
      <a href="gallery.html">Gallery</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="tel:+917018677970">+91 70186 77970</a>
      <a href="mailto:dpsrajgarh444@gmail.com">dpsrajgarh444@gmail.com</a>
      <a href="https://www.google.com/maps/search/?api=1&query=Dasson+Public+High+School+Rajgarh+Sirmaur+Himachal+Pradesh" target="_blank" rel="noopener">Get Directions</a>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>\u00a9 2026 Dasson Public High School, Rajgarh</span>
    <a href="index.html">Back to top \u2191</a>
  </div>
</footer>
"""

def page_banner(title, subtitle):
    return f"""<section class="page-banner">
  <div class="wrap">
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
</section>
"""

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="google-site-verification" content="GKOIWHa4qLTXc37S3CR-F_NgH7MR1zgbXWs5q6V4sos" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:wght@400;500;600;700&family=Work+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""

FOOT_SCRIPT = """
<script src="script.js"></script>
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
<script>
if (window.netlifyIdentity) {
  window.netlifyIdentity.on("init", function(user) {
    if (!user) {
      window.netlifyIdentity.on("login", function() {
        document.location.href = "/admin/";
      });
    }
  });
}
</script>
</body>
</html>"""

# ---- Home page highlight cards (link out to each section) ----
HIGHLIGHTS = """<section class="alt" id="highlights">
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Explore the School</h2>
      <p>Everything about Dasson Public High School, one click away.</p>
    </div>
    <div class="life-grid" data-stagger>
      <a href="courses.html" class="life-card c-blue reveal">
        <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 2 8l10 5 10-5-10-5z"/><path d="M6 10v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></svg></div>
        <h3>Courses</h3><p>Nursery to Class 10</p>
      </a>
      <a href="admissions.html" class="life-card c-orange reveal">
        <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 4h6v3H9z"/><path d="M6 6h12v15H6z"/><path d="m9 13 2 2 4-4"/></svg></div>
        <h3>Admissions</h3><p>How to join us</p>
      </a>
      <a href="faculty.html" class="life-card c-teal reveal">
        <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3"/><path d="M4 20c0-3 2-5 5-5s5 2 5 5"/><circle cx="17" cy="9" r="2.3"/><path d="M15.2 20c.2-2 1.3-3.6 2.8-4.2"/></svg></div>
        <h3>Faculty</h3><p>Meet our teachers</p>
      </a>
      <a href="gallery.html" class="life-card c-purple reveal">
        <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="M21 16l-5-5-4 4-3-3-6 6"/></svg></div>
        <h3>Gallery</h3><p>A look at school life</p>
      </a>
      <a href="contact.html" class="life-card c-gold reveal">
        <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.5-7-11.5A7 7 0 0 1 19 9.5C19 14.5 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg></div>
        <h3>Contact</h3><p>Visit or reach out</p>
      </a>
    </div>
  </div>
</section>
"""

ABOUT_TEASER = """<section id="about-teaser">
  <div class="wrap about-grid">
    <div class="reveal-left">
      <div class="section-head">
        <h2>About Us</h2>
        <p>Rooted in the hills of Rajgarh, built for the whole child.</p>
      </div>
      <p>Dasson Public High School brings together strong academics, character, and a sense of place, set against the mountains of Rajgarh.</p>
      <p><a href="about.html" style="border-bottom:1px dotted var(--forest-500); text-decoration:none; color:var(--forest-700); font-weight:500;">Learn more about us</a></p>
    </div>
    <div class="about-art reveal-right">
      <svg viewBox="0 0 200 150" fill="none">
        <path d="M20 120 L70 50 L95 85 L120 40 L180 120 Z" fill="var(--paper-100)"/>
        <circle cx="150" cy="35" r="12" fill="var(--sun-500)"/>
        <path d="M60 120 C 90 95 100 130 130 100 C 150 82 160 100 175 90" stroke="var(--paper-000)" stroke-width="7" fill="none" stroke-linecap="round"/>
      </svg>
    </div>
  </div>
</section>
"""

FOUNDER_HTML = """<section class="alt" id="founder">
  <div class="wrap about-grid">
    <div class="founder-portrait reveal-left">
      <svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="50" cy="34" r="18"/><path d="M14 92c0-21 16-36 36-36s36 15 36 36"/></svg>
      <div class="founder-caption">Sh. Dasson<span>Founder</span></div>
    </div>
    <div class="reveal-right">
      <div class="section-head">
        <h2>Our Founder</h2>
        <p>The vision and struggle behind Dasson Public High School.</p>
      </div>
      <p>Dasson Public High School was founded in 1992 by Sh. Dasson, after years of determined effort to bring quality education to the children of Rajgarh. It holds the distinction of being Rajgarh's first private school, and remains affiliated with the Himachal Pradesh Board of School Education (HPBOSE) to this day.</p>
      <p class="fac-note">Portrait placeholder \u2014 replace with a real photograph of Sh. Dasson when available.</p>
    </div>
  </div>
</section>
"""

# ---- v2: slider home page, richer header/footer ----
from home_v2 import header_html, footer_html, home_body, HOME_CSS, HOME_JS, result_page, faculty_section_html
HEADER = header_html("site", "assets/logo.png")
FOOTER = footer_html("site", "assets/logo.png")
HOME = home_body("site", "assets/logo.png", "assets/founder.jpg", news_items=NEWS_DATA)
faculty = faculty_section_html(FACULTY_DATA)

# ---- assemble pages ----
pages = {}

pages["index.html"] = (
    head("Dasson Public High School, Rajgarh", "Dasson Public High School, Rajgarh \u2014 Nursery to Class 10, admissions open.")
    + HEADER + HOME + FOOTER + FOOT_SCRIPT
)

pages["about.html"] = (
    head("About Us - Dasson Public High School", "About Dasson Public High School, Rajgarh.")
    + HEADER + page_banner("About Us", "Rooted in the hills of Rajgarh, built for the whole child.") + about + FOOTER + FOOT_SCRIPT
)

pages["courses.html"] = (
    head("Courses - Dasson Public High School", "Classes offered at Dasson Public High School: Nursery to Class 10.")
    + HEADER + page_banner("Our Courses", "From a child's first classroom to board-exam readiness.") + courses + admissions + modal_html + FOOTER + FOOT_SCRIPT
)

pages["admissions.html"] = (
    head("Admissions - Dasson Public High School", "Admissions process at Dasson Public High School, Rajgarh.")
    + HEADER + page_banner("Admissions", "Four simple steps to join our school community.") + admissions + FOOTER + FOOT_SCRIPT
)

pages["result-5th.html"] = (
    head("Class 5th Result - Dasson Public High School", "Class 5th year-wise result at Dasson Public High School, Rajgarh.")
    + HEADER + result_page("5th", page_banner, RESULTS_DATA.get("5th")) + FOOTER + FOOT_SCRIPT
)

pages["result-9th.html"] = (
    head("Class 9th Result - Dasson Public High School", "Class 9th year-wise result at Dasson Public High School, Rajgarh.")
    + HEADER + result_page("9th", page_banner, RESULTS_DATA.get("9th")) + FOOTER + FOOT_SCRIPT
)

pages["result-10th.html"] = (
    head("Class 10th Result - Dasson Public High School", "Class 10th year-wise result at Dasson Public High School, Rajgarh.")
    + HEADER + result_page("10th", page_banner, RESULTS_DATA.get("10th")) + FOOTER + FOOT_SCRIPT
)

pages["faculty.html"] = (
    head("Faculty - Dasson Public High School", "Meet the faculty of Dasson Public High School, Rajgarh.")
    + HEADER + page_banner("Our Faculty", "Experienced teachers guiding every stage of school life.") + faculty + modal_html + FOOTER + FOOT_SCRIPT
)

pages["gallery.html"] = (
    head("Gallery - Dasson Public High School", "Campus life at Dasson Public High School, Rajgarh.")
    + HEADER + page_banner("Gallery", "A look at everyday school life, from classrooms to the playground.") + gallery + modal_html + FOOTER + FOOT_SCRIPT
)

pages["contact.html"] = (
    head("Contact Us - Dasson Public High School", "Contact and location details for Dasson Public High School, Rajgarh.")
    + HEADER + page_banner("Get in Touch", "We're happy to answer any questions about school life or admissions.") + contact + FOOTER + FOOT_SCRIPT
)

# ---- extra CSS: page banner, reveal animations, nav active state ----
EXTRA_CSS = """

/* ---- multi-page additions ---- */
.page-banner{background:linear-gradient(135deg, var(--forest-900), var(--forest-700)); color:var(--paper-000); padding:56px 0; text-align:center;}
.page-banner h1{color:var(--paper-000); margin:0; font-size:clamp(1.8rem,4vw,2.4rem);}
.page-banner p{color:rgba(245,241,230,0.75); margin:.5em 0 0; font-size:.98rem;}

.navlinks a.active{color:var(--forest-700); font-weight:600;}
.navlinks a.active::after{right:0;}

a.life-card{text-decoration:none; display:block;}

@keyframes slideInLeft{from{transform:translateX(-40px);} to{transform:translateX(0);}}
@keyframes slideInRight{from{transform:translateX(40px);} to{transform:translateX(0);}}
.hero-inner .logo{animation:slideInLeft .7s ease both;}
.hero-inner h1{animation:slideInRight .7s ease .12s both;}
.hero-inner p.tag{animation:slideInRight .7s ease .24s both;}
.hero-inner .cta-row{animation:slideInRight .7s ease .36s both;}

.affil-bar{background:var(--sun-500); color:var(--forest-900); text-align:center; font-size:.74rem; font-weight:600; letter-spacing:.03em; padding:5px 12px; padding-top:calc(5px + env(safe-area-inset-top,0px));}
.school-code{display:inline-flex; align-items:center; gap:6px; white-space:nowrap;}
.school-code svg{width:13px; height:13px; flex:none;}

.founder-portrait{background:var(--paper-000); border:2px solid var(--sun-500); border-radius:var(--radius-lg); box-shadow:var(--shadow-soft); aspect-ratio:4/5; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:24px; max-width:280px; margin:0 auto;}
.founder-portrait svg{width:52%; height:52%; color:var(--forest-700);}
.founder-caption{margin-top:14px; background:var(--forest-900); color:var(--paper-100); padding:8px 22px; border-radius:6px; text-align:center; font-family:'Spectral',serif; font-size:1rem;}
.founder-caption span{display:block; font-family:'Work Sans',sans-serif; font-size:.7rem; color:var(--sun-500); margin-top:2px; letter-spacing:.03em;}

.reveal{opacity:0; transform:translateY(28px); transition:opacity .6s ease, transform .6s ease;}
.reveal.is-visible{opacity:1; transform:translateY(0);}
.reveal-left{opacity:0; transform:translateX(-45px); transition:opacity .6s ease, transform .6s ease;}
.reveal-left.is-visible{opacity:1; transform:translateX(0);}
.reveal-right{opacity:0; transform:translateX(45px); transition:opacity .6s ease, transform .6s ease;}
.reveal-right.is-visible{opacity:1; transform:translateX(0);}

@media (prefers-reduced-motion: reduce){
  .hero-inner .logo, .hero-inner h1, .hero-inner p.tag, .hero-inner .cta-row{animation:none !important; opacity:1 !important; transform:none !important;}
  .reveal, .reveal-left, .reveal-right{opacity:1 !important; transform:none !important; transition:none !important;}
}

/* ---- mobile nav toggle ---- */
.nav-toggle{display:none; background:none; border:none; cursor:pointer; padding:8px; flex:none; margin:0;}
.nav-toggle svg{width:26px; height:26px; color:var(--forest-900); display:block;}
.mobile-apply-item{display:none;}

@media (max-width:820px){
  .nav-toggle{display:inline-flex; align-items:center; justify-content:center;}
  .nav-apply{display:none;}
  .navlinks{
    display:flex; flex-direction:column; gap:0;
    position:absolute; top:100%; left:0; right:0;
    background:var(--paper-100); border-bottom:1px solid var(--border-soft);
    max-height:0; overflow:hidden; padding:0 24px;
    transition:max-height .3s ease;
  }
  .navlinks.open{max-height:420px; padding:10px 24px 22px;}
  .navlinks li{width:100%;}
  .navlinks a{display:block; padding:13px 0; border-bottom:1px solid var(--border-soft); font-size:1rem;}
  .navlinks a::after{display:none;}
  .mobile-apply-item{display:block;}
  .navlinks a.mobile-apply{background:var(--forest-700); color:var(--paper-000); text-align:center; border-radius:8px; border-bottom:none; margin-top:8px; padding:12px;}
}
"""

styles_css_full = style_css + EXTRA_CSS + HOME_CSS

# ---- shared script.js: guarded modal logic + reveal/stagger + nav active state ----
script_js_new = """document.addEventListener('DOMContentLoaded', function(){

  // ---- modal (only runs on pages that include the modal markup) ----
  var overlay = document.getElementById('modalOverlay');
  if(overlay){
    var box = document.getElementById('modalBox');
    var body = document.getElementById('modalBody');
    var titleEl = document.getElementById('modalTitleText');
    var avatarEl = document.getElementById('modalAvatar');

    function openModal(title, html, avatarText){
      titleEl.textContent = title;
      body.innerHTML = html;
      if(avatarText){
        avatarEl.innerHTML = avatarText;
        avatarEl.style.display = 'flex';
        box.classList.add('has-avatar');
      } else {
        avatarEl.style.display = 'none';
        box.classList.remove('has-avatar');
      }
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
    function closeModal(){
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
    document.getElementById('modalClose').addEventListener('click', closeModal);
    overlay.addEventListener('click', function(e){ if(e.target === overlay) closeModal(); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeModal(); });

    function topperRow(entry, rankNum){
      var parts = entry.split('|');
      var pname = parts[0], pct = parts[1];
      var initials = pname.split(' ').map(function(w){ return w[0]; }).join('').slice(0,2).toUpperCase();
      return '<div class="topper-row"><span class="rank-badge rank-' + rankNum + '">' + rankNum + '</span>' +
        '<span class="topper-avatar">' + initials + '</span>' +
        '<span class="topper-name">' + pname + '</span>' +
        '<span class="topper-pct">' + pct + '%</span></div>';
    }
    document.querySelectorAll('.grade').forEach(function(btn){
      btn.addEventListener('click', function(){
        var name = btn.dataset.class;
        var boys = parseInt(btn.dataset.boys, 10);
        var girls = parseInt(btn.dataset.girls, 10);
        var total = boys + girls;
        var html =
          '<p class="modal-sub">Class overview</p>' +
          '<div class="modal-stats">' +
            '<div class="modal-stat"><div class="num">' + boys + '</div><div class="lbl">Boys</div></div>' +
            '<div class="modal-stat"><div class="num">' + girls + '</div><div class="lbl">Girls</div></div>' +
            '<div class="modal-stat"><div class="num">' + total + '</div><div class="lbl">Total</div></div>' +
          '</div>' +
          '<p class="modal-footnote">Sample enrollment figures \u2014 update with your school\\'s real numbers.</p>';
        if(btn.dataset.rank1){
          html += '<div class="toppers"><h4>Previous Year Top Rankers</h4>' +
            topperRow(btn.dataset.rank1, 1) + topperRow(btn.dataset.rank2, 2) + topperRow(btn.dataset.rank3, 3) +
            '<p class="modal-footnote">Sample results \u2014 replace with your school\\'s actual previous-year toppers.</p></div>';
        }
        openModal(name, html);
      });
    });

    document.querySelectorAll('.fac-card').forEach(function(btn){
      btn.addEventListener('click', function(){
        var d = btn.dataset;
        var avatarEl2 = btn.querySelector('.fac-avatar');
        var avatarImg = avatarEl2.querySelector('img');
        var avatarContent = avatarImg ? avatarImg.outerHTML : avatarEl2.textContent;
        var note = d.photo
          ? 'Sample profile details \u2014 replace qualification, focus and bio with the real information.'
          : 'Sample profile \u2014 replace with your staff member\\'s real details and photo.';
        openModal(d.name,
          '<p class="modal-sub">' + d.role + '</p>' +
          '<div class="modal-rows">' +
            '<div class="modal-row"><span>Qualification</span><strong>' + d.qualification + '</strong></div>' +
            '<div class="modal-row"><span>Focus</span><strong>' + d.subject + '</strong></div>' +
          '</div>' +
          '<p class="modal-bio">' + d.bio + '</p>' +
          '<p class="modal-footnote">' + note + '</p>',
          avatarContent
        );
      });
    });

    document.querySelectorAll('.life-card[data-captions]').forEach(function(btn){
      btn.addEventListener('click', function(e){
        e.preventDefault();
        var iconSvg = btn.querySelector('.icon-box svg').outerHTML;
        var name = btn.querySelector('h3').textContent;
        var captions = btn.dataset.captions.split('|');
        var itemsHtml = captions.map(function(cap){
          return '<div class="photo-item"><div class="icon-wrap">' + iconSvg + '</div><span>' + cap + '</span></div>';
        }).join('');
        openModal(name,
          '<p class="modal-sub">Gallery</p>' +
          '<div class="photo-list">' + itemsHtml + '</div>' +
          '<p class="modal-footnote">Illustrative placeholders \u2014 add your school\\'s real photos here.</p>'
        );
      });
    });
  }

  // ---- scroll-reveal animations ----
  var revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  document.querySelectorAll('[data-stagger]').forEach(function(container){
    var items = container.querySelectorAll(':scope > .reveal, :scope > .reveal-left, :scope > .reveal-right');
    items.forEach(function(el, i){ el.style.transitionDelay = (i * 0.08) + 's'; });
  });
  if('IntersectionObserver' in window){
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, {threshold:0.15});
    revealEls.forEach(function(el){ obs.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('is-visible'); });
  }

  // ---- highlight current page in nav ----
  var current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navlinks a').forEach(function(a){
    if(a.getAttribute('href') === current) a.classList.add('active');
  });

  // ---- mobile hamburger menu ----
  var navToggle = document.getElementById('navToggle');
  var navLinksEl = document.querySelector('.navlinks');
  if(navToggle && navLinksEl){
    navToggle.addEventListener('click', function(){
      var isOpen = navLinksEl.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    navLinksEl.querySelectorAll('a').forEach(function(a){
      if(a.parentElement.classList.contains('has-dropdown')) return;
      a.addEventListener('click', function(){
        navLinksEl.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
});
"""

# ---- write everything out ----
if os.path.exists(OUT_DIR):
    shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

for name, html in pages.items():
    with open(os.path.join(OUT_DIR, name), "w") as f:
        f.write(html)

with open(os.path.join(OUT_DIR, "styles.css"), "w") as f:
    f.write(styles_css_full)

with open(os.path.join(OUT_DIR, "script.js"), "w") as f:
    f.write(script_js_new + "\n" + HOME_JS)

# copy the whole assets folder as-is (includes any new photos the CMS/admin panel has added)
if os.path.exists(ASSETS_SRC):
    shutil.copytree(ASSETS_SRC, os.path.join(OUT_DIR, "assets"))

for fname in ("sitemap.xml", "robots.txt"):
    src_path = os.path.join(ROOT, fname)
    if os.path.exists(src_path):
        shutil.copy(src_path, os.path.join(OUT_DIR, fname))

# carry the admin panel (Decap CMS) through to the published site
admin_src = os.path.join(ROOT, "admin")
if os.path.exists(admin_src):
    shutil.copytree(admin_src, os.path.join(OUT_DIR, "admin"))

print("Pages written:", list(pages.keys()))
print("Done.")
