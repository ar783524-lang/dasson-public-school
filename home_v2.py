import urllib.parse

MAPS = "https://www.google.com/maps/search/?api=1&query=Dasson+Public+High+School+Rajgarh+Sirmaur+Himachal+Pradesh"
BLANK_GIF = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="

MAIL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18v12H3z"/><path d="M3 7l9 6 9-6"/></svg>'
CODE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8" cy="12" r="2"/><path d="M13 10h6M13 14h4"/></svg>'

IC_CAP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 2 8l10 5 10-5-10-5z"/><path d="M6 10v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></svg>'
IC_CLIP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 4h6v3H9z"/><path d="M6 6h12v15H6z"/><path d="m9 13 2 2 4-4"/></svg>'
IC_PEOPLE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3"/><path d="M4 20c0-3 2-5 5-5s5 2 5 5"/><circle cx="17" cy="9" r="2.3"/><path d="M15.2 20c.2-2 1.3-3.6 2.8-4.2"/></svg>'
IC_BALL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><path d="M4 12h16M12 3.5c-3 3-3 14 0 17M12 3.5c3 3 3 14 0 17"/></svg>'
IC_BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h9v17H4z"/><path d="M13 6h7v15h-7"/><path d="M7 9h3M7 12h3"/></svg>'
IC_FLASK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 3h6M10 3v6l-6 10a1 1 0 0 0 1 1.5h14a1 1 0 0 0 1-1.5L14 9V3"/></svg>'
IC_ART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="9" r="5.2"/><circle cx="7.4" cy="8" r=".9" fill="currentColor" stroke="none"/><circle cx="10.5" cy="6.6" r=".9" fill="currentColor" stroke="none"/><circle cx="11.2" cy="10.2" r=".9" fill="currentColor" stroke="none"/><path d="M17 5l1.3 3.1L21 9.4l-2.7 1.3L17 14l-1.3-3.3L13 9.4l2.7-1.3z"/></svg>'
IC_HALL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 21V9l8-5 8 5v12"/><path d="M9 21v-7h6v7"/></svg>'
IC_STAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l2.4 5.5L20 8l-4.4 3.8L17 18l-5-3.2L7 18l1.4-6.2L4 8l5.6-.5z"/></svg>'


def links(mode):
    if mode == "site":
        return lambda p: f"{p}.html"
    return lambda p: f"#{p}"


def logo_tag(mode, logo, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    if mode == "preview":
        return f'<img{c} data-logo src="{BLANK_GIF}" alt="{alt}">'
    return f'<img{c} src="{logo}" alt="{alt}">'


def art_uri(c1, c2, sun):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" preserveAspectRatio="xMidYMax slice">'
        f'<circle cx="{sun}" cy="120" r="46" fill="#c99a3d" opacity=".6"/>'
        f'<path d="M0 420 L160 230 L230 300 L340 160 L430 300 L520 230 L620 420 Z" fill="{c1}" opacity=".55"/>'
        f'<path d="M480 420 L660 190 L740 280 L860 120 L980 280 L1060 220 L1200 420 Z" fill="{c2}" opacity=".45"/>'
        '<path d="M0 470 C 200 440 300 490 520 460 C 760 425 900 480 1200 445 L1200 500 L0 500 Z" fill="#0b1a12" opacity=".35"/>'
        '</svg>'
    )
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe="")


# --------------------------------------------------------------------------- header / footer

def header_html(mode, logo):
    L = links(mode)
    return f"""<header>
  <div class="topbar">
    <div class="wrap">
      <div class="topbar-links">
        <span class="school-code">{CODE_ICON}School Code: 4084</span>
        <a class="topbar-mail" href="mailto:dpsrajgarh444@gmail.com">{MAIL_ICON}dpsrajgarh444@gmail.com</a>
      </div>
      <span class="topbar-loc">Rajgarh, Sirmaur, Himachal Pradesh</span>
    </div>
  </div>
  <div class="navbar-outer">
    <nav class="wrap navbar">
      <a class="brand" href="{L('index')}">
        <img src="{logo}" alt="Dasson Public High School logo">
        <span>Dasson Public High School<small>Rajgarh &middot; Affiliated to HPBOSE</small></span>
      </a>
      <ul class="navlinks">
        <li><a href="{L('index')}">Home</a></li>
        <li><a href="{L('about')}">About</a></li>
        <li><a href="{L('admissions')}">Admissions</a></li>
        <li class="has-dropdown">
          <a href="{L('result-10th')}">Result</a>
          <ul class="dropdown">
            <li><a href="{L('result-5th')}">5th Result</a></li>
            <li><a href="{L('result-9th')}">9th Result</a></li>
            <li><a href="{L('result-10th')}">10th Result</a></li>
          </ul>
        </li>
        <li><a href="{L('faculty')}">Faculty</a></li>
        <li><a href="{L('gallery')}">Gallery</a></li>
        <li><a href="{L('contact')}">Contact</a></li>
        <li class="mobile-apply-item"><a href="{L('admissions')}" class="mobile-apply">Apply Now</a></li>
      </ul>
      <a class="btn btn-primary nav-apply" href="{L('admissions')}">Apply Now</a>
      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </nav>
  </div>
</header>
"""


def footer_html(mode, logo):
    L = links(mode)
    top = "#" if mode == "site" else "#index"
    return f"""<footer>
  <div class="wrap footer-motto">
    <p>&ldquo;Every classroom here is a step toward the summit of a child's potential.&rdquo;</p>
  </div>
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <div class="footer-logo-row">
        {logo_tag(mode, logo, "Dasson Public High School logo")}
        <span>Dasson Public High School</span>
      </div>
      <p>Affiliated to HPBOSE</p>
      <p>School Code: 4084</p>
      <p>Rajgarh, Sirmaur, Himachal Pradesh</p>
    </div>
    <div>
      <h4>Info Links</h4>
      <a href="{L('about')}">About Us</a>
      <a href="{L('courses')}">Courses</a>
      <a href="{L('admissions')}">Admissions</a>
      <a href="{L('faculty')}">Faculty</a>
      <a href="{L('gallery')}">Gallery</a>
      <a href="{L('contact')}">Contact Details</a>
    </div>
    <div>
      <h4>Administration</h4>
      <a href="tel:+919805334882">+91 98053 34882</a>
      <a href="mailto:dpsrajgarh444@gmail.com">dpsrajgarh444@gmail.com</a>
      <a href="{MAPS}" target="_blank" rel="noopener">Google Map Location</a>
      <div class="footer-btns">
        <a class="footer-btn" href="{L('admissions')}">Admission Info</a>
        <a class="footer-btn" href="{L('contact')}">Contact Us</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; 2026 Dasson Public High School, Rajgarh</span>
    <a href="{top}">Back to top &uarr;</a>
  </div>
</footer>
"""


# --------------------------------------------------------------------------- home page

def home_body(mode, logo, founder_img="assets/founder.jpg", news_items=None):
    L = links(mode)

    def photo(n):
        return f"url('assets/slides/slide{n}.jpg')," if mode == "site" else ""

    slides_data = [
        ("Rajgarh's First Private School",
         "Educating the children of Rajgarh with care and character since 1992, affiliated to HPBOSE.",
         "Learn About Us", L("about"),
         "linear-gradient(160deg,#0f2a1a 0%,#1e4d2f 55%,#3d7a52 100%)", art_uri("#3d7a52", "#bcd6c3", 960)),
        ("Nursery to Class 10",
         "Strong academics, sports, and co-curricular activities on a safe, close-knit campus set in the hills.",
         "View Courses", L("courses"),
         "linear-gradient(160deg,#10303a 0%,#1d5a55 55%,#3d8a78 100%)", art_uri("#2f9e8f", "#bfe3dc", 240)),
        ("Admissions Open",
         "Give your child a place in the Dasson Public High School family. Visit the school office or contact us today.",
         "Apply for Admission", L("admissions"),
         "linear-gradient(160deg,#2b2a12 0%,#3f5a24 55%,#6f8f3f 100%)", art_uri("#8fae4a", "#e6eec8", 700)),
        ("Experienced, Caring Faculty",
         "14 dedicated teachers guiding students from Nursery through Class 10, in academics and beyond.",
         "Meet Our Faculty", L("faculty"),
         "linear-gradient(160deg,#241533 0%,#4a2d63 55%,#7a4fa3 100%)", art_uri("#7a4fa3", "#d9c8ea", 880)),
        ("A Look at School Life",
         "Sports days, cultural events, and everyday moments from around our Rajgarh campus.",
         "View Gallery", L("gallery"),
         "linear-gradient(160deg,#2a1420 0%,#5c2c45 55%,#b1487a 100%)", art_uri("#b1487a", "#f0cfe0", 320)),
    ]
    slides = ""
    for i, (title, text, cta, href, grad, art) in enumerate(slides_data, start=1):
        tag = "h1" if i == 1 else "h2"
        slides += f"""    <div class="hs-slide" style="background-image:{photo(i)}url('{art}'),{grad};">
      <div class="hs-caption">
        <div class="hs-logo">{logo_tag(mode, logo, "")}</div>
        <div class="hs-box">
          <{tag} class="hs-title">{title}</{tag}>
          <p class="hs-text">{text}</p>
        </div>
        <div class="hs-cta"><a class="btn btn-gold" href="{href}">{cta}</a></div>
      </div>
    </div>
"""

    hero = f"""<section class="hero-slider" id="home" aria-label="School highlights">
  <div class="hs-track">
{slides}  </div>
  <button type="button" class="hs-arrow prev" aria-label="Previous slide">&#8249;</button>
  <button type="button" class="hs-arrow next" aria-label="Next slide">&#8250;</button>
  <div class="hs-dots"></div>
</section>
"""

    news_founder = f"""<section id="news">
  <div class="wrap nf-grid">
    <div class="news-box reveal-left">
      <h3 class="news-head">News &amp; Events</h3>
      <ul class="news-list">
        <li><a href="{L('contact')}">Mandatory Public Disclosure</a></li>
        <li><a href="{L('contact')}">Vacancies for Session 2026-27</a></li>
        <li><a href="{L('admissions')}">Admissions are open for Nursery to Class 10</a></li>
        <li><a href="{L('courses')}">See our classes and student strength</a></li>
        <li><a href="{L('faculty')}">Meet our teaching staff</a></li>
      </ul>
    </div>
    <div class="founder-block reveal-right">
      <div class="founder-side">
        <div class="founder-circle"><img src="{founder_img}" alt="Late Sh. P.N. Dasson"></div>
        <div class="founder-cap">Late Sh. P.N. Dasson<span>Founder &middot; Prem Nath Dasson</span></div>
      </div>
      <div class="founder-text">
        <h2>Our Founder</h2>
        <p>Dasson Public High School was founded in 1992 by Late Sh. P.N. Dasson, after years of determined effort to bring quality education to the children of Rajgarh. It holds the distinction of being Rajgarh's first private school, and remains affiliated with the Himachal Pradesh Board of School Education (HPBOSE) to this day.</p>
        <p><a class="btn btn-primary" href="{L('about')}">Know more about us</a></p>
      </div>
    </div>
  </div>
</section>
"""

    chairman = """<section class="alt" id="chairman">
  <div class="wrap">
    <div class="section-head center reveal"><h2>Chairman's Message</h2><div class="dots-line"><span>&bull;&bull;&bull;</span></div></div>
    <div class="pr-grid">
      <div class="pr-side reveal-left">
        <div class="pr-avatar">RD</div>
        <div class="founder-cap">Rajni Dasson<span>Chairman</span></div>
      </div>
      <div class="pr-text reveal-right">
        <p class="pr-quote">We carry forward a legacy built on hard work, values, and belief in every child.</p>
        <p>As Chairman of Dasson Public High School, I am committed to continuing the vision on which this institution was founded in 1992. We work every day to give the children of Rajgarh an education that builds both knowledge and character, and to keep raising the standard our school is known for.</p>
        <p class="fac-note">Sample message and portrait: replace with the Chairman's own words and photo.</p>
      </div>
    </div>
  </div>
</section>
"""

    principal = """<section id="principal">
  <div class="wrap">
    <div class="section-head center reveal"><h2>From the Desk of the Principal</h2><div class="dots-line"><span>&bull;&bull;&bull;</span></div></div>
    <div class="pr-grid">
      <div class="pr-side reveal-left">
        <div class="pr-avatar">NS</div>
        <div class="founder-cap">Neena Sharma<span>Principal</span></div>
      </div>
      <div class="pr-text reveal-right">
        <p class="pr-quote">At Dasson Public High School we want every child to feel supported, challenged, and encouraged.</p>
        <p>We are committed to giving each student a strong academic foundation and the confidence to grow into a responsible citizen. Teachers and parents work together so that every child can reach their full potential.</p>
        <p class="fac-note">Sample message and portrait: replace with the Principal's own words and photo.</p>
      </div>
    </div>
  </div>
</section>
"""

    quote = """<section class="quote-strip">
  <div class="wrap reveal"><div class="mark">&ldquo;</div><p>Every classroom here is a step toward the summit of a child's potential.</p></div>
</section>
"""

    tiles = f"""<section id="explore">
  <div class="wrap">
    <div class="tiles-intro">
      <h2 class="reveal-left">Everything Your Child Needs to <em>Grow</em></h2>
      <p class="reveal-right">Solid classroom learning, regular sports, music, art, and cultural events: a balanced school life that builds confident, well-rounded children.</p>
    </div>
    <div class="tiles" data-stagger>
      <a class="tile t-blue reveal" href="{L('courses')}">{IC_CAP}<span>Academics</span></a>
      <a class="tile t-orange reveal" href="{L('gallery')}">{IC_BALL}<span>Co-Curricular Activities</span></a>
      <a class="tile t-teal reveal" href="{L('faculty')}">{IC_PEOPLE}<span>Faculty</span></a>
      <a class="tile t-gold reveal" href="{L('admissions')}">{IC_CLIP}<span>Admissions</span></a>
    </div>
  </div>
</section>
"""

    items = [
        ("c-blue", IC_BOOK, "Library"), ("c-purple", IC_FLASK, "Science Labs"), ("c-orange", IC_BALL, "Sports Ground"),
        ("c-pink", IC_ART, "Arts &amp; Music"), ("c-teal", IC_HALL, "Auditorium"), ("c-gold", IC_STAR, "Annual Events"),
    ]
    car_items = "".join(
        f'<a class="car-item {c}" href="{L("gallery")}"><div class="car-ic">{ic}</div><h3>{name}</h3></a>'
        for c, ic, name in items
    )
    events = f"""<section class="alt" id="events-gallery">
  <div class="wrap">
    <div class="section-head center reveal"><h2>Events Gallery</h2><div class="dots-line"><span>&bull;&bull;&bull;</span></div></div>
    <div class="carousel reveal">
      <button type="button" class="car-arrow prev" aria-label="Previous">&#8249;</button>
      <div class="car-track">{car_items}</div>
      <button type="button" class="car-arrow next" aria-label="Next">&#8250;</button>
    </div>
  </div>
</section>
"""
    news_icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M8 13h10M8 16h10M8 19h6"/></svg>'
    default_news = [
        {"caption": "Annual Function Covered in Local Press", "photo": ""},
        {"caption": "Sports Day Makes News Day", "photo": ""},
        {"caption": "Board Exam Toppers Felicitated", "photo": ""},
        {"caption": "Independence Day Celebrations", "photo": ""},
        {"caption": "Cultural Fest Highlights", "photo": ""},
        {"caption": "Community Outreach Drive", "photo": ""},
        {"caption": "Science Exhibition Feature", "photo": ""},
        {"caption": "School Foundation Day Coverage", "photo": ""},
    ]
    items = news_items if news_items else default_news

    def clip_card(item, idx):
        tilt = ("t1", "t2", "t3")[idx % 3]
        photo = item.get("photo") or ""
        media_html = f'<img src="{photo}" alt="{item["caption"]}">' if photo else news_icon
        media_cls = "clip-photo" if photo else "clip-icon"
        return f'''<div class="clip-card {tilt}">
      <div class="{media_cls}">{media_html}</div>
      <p class="clip-caption">{item["caption"]}</p>
      <span class="clip-tag">Press Clipping</span>
    </div>'''

    clip_cards = "".join(clip_card(c, i) for i, c in enumerate(items))
    media = f"""<section class="alt" id="media">
  <div class="wrap">
    <div class="section-head center reveal"><h2>In the News</h2><div class="dots-line"><span>&bull;&bull;&bull;</span></div></div>
  </div>
  <div class="clip-marquee">
    <div class="clip-track">{clip_cards}{clip_cards}</div>
  </div>
  <div class="wrap"><p class="fac-note" style="text-align:center;">Sample placeholders &mdash; replace with your school's real newspaper clippings and press photos.</p></div>
</section>
"""
    return hero + news_founder + chairman + principal + quote + tiles + events + media


# --------------------------------------------------------------------------- CSS

HOME_CSS = """
/* ===== v2: no sideways scroll from slide-in animations ===== */
html{overflow-x:hidden;}
body{overflow-x:clip;}

/* ===== v2: header restructure (only the nav bar sticks) ===== */
header{position:static; display:contents;}
.navbar-outer{position:sticky; top:0; z-index:50; background:var(--paper-100); border-bottom:1px solid var(--border-soft);}
.navbar-outer::after{content:""; position:absolute; left:0; right:0; bottom:-1px; height:2px; background:linear-gradient(90deg,var(--forest-700),var(--sun-500)); opacity:.65; pointer-events:none;}
nav.navbar{background:transparent; border-bottom:none; -webkit-backdrop-filter:none; backdrop-filter:none;}
nav.navbar::after{display:none;}
.brand img{flex:none;}

/* ===== hero slider ===== */
.hero-slider{position:relative; overflow:hidden; height:clamp(440px,64vh,620px); background:#12301f;}
.hs-track{position:absolute; inset:0;}
.hs-slide{position:absolute; inset:0; transform:translateX(100%); visibility:hidden; transition:transform .8s ease; background-size:cover; background-position:center; background-repeat:no-repeat;}
.hs-slide:first-child{transform:none; visibility:visible;}
.hs-slide.show{visibility:visible;}
.hs-slide::before{content:""; position:absolute; inset:0; background:linear-gradient(90deg,rgba(8,24,14,.72) 0%,rgba(8,24,14,.35) 55%,rgba(8,24,14,.08) 100%);}
.hs-caption{position:absolute; left:0; right:0; top:50%; transform:translateY(-50%); padding:0 clamp(20px,7vw,96px); z-index:2;}
.hs-logo{margin-bottom:14px;}
.hs-logo img{width:68px; height:68px; border-radius:50%; border:2px solid var(--sun-500); background:#fff; box-shadow:0 8px 20px rgba(0,0,0,.35);}
.hs-box{max-width:560px;}
.hs-title{display:block; margin:0; background:var(--sun-500); color:var(--forest-900); font-size:clamp(1.35rem,4vw,2.3rem); line-height:1.2; padding:10px 18px; border-radius:6px 6px 0 0;}
.hs-text{margin:0; background:rgba(8,20,13,.66); color:#f5f1e6; padding:14px 18px; font-size:clamp(.92rem,2.3vw,1.08rem); line-height:1.6; border-radius:0 0 6px 6px;}
.hs-cta{margin-top:16px;}
.btn-gold{background:var(--sun-500); color:var(--forest-900); box-shadow:0 10px 22px rgba(0,0,0,.3);}
.btn-gold:hover{transform:translateY(-2px); background:#d8a94a;}
.hs-slide.active .hs-logo{animation:slideInLeft .7s ease both;}
.hs-slide.active .hs-box{animation:slideInLeft .7s ease .12s both;}
.hs-slide.active .hs-cta{animation:slideInRight .7s ease .3s both;}
.hs-arrow{position:absolute; top:50%; transform:translateY(-50%); z-index:5; width:44px; height:44px; border-radius:50%; border:none; background:rgba(255,255,255,.2); color:#fff; font-size:1.7rem; line-height:1; cursor:pointer; display:flex; align-items:center; justify-content:center;}
.hs-arrow:hover{background:var(--sun-500); color:var(--forest-900);}
.hs-arrow.prev{left:16px;} .hs-arrow.next{right:16px;}
.hs-dots{position:absolute; bottom:16px; left:0; right:0; display:flex; justify-content:center; gap:9px; z-index:5;}
.hs-dots button{width:11px; height:11px; border-radius:50%; border:none; background:rgba(255,255,255,.5); cursor:pointer; padding:0;}
.hs-dots button.on{background:var(--sun-500); transform:scale(1.25);}

/* ===== news + founder ===== */
.nf-grid{display:grid; grid-template-columns:.85fr 1.6fr; gap:44px; align-items:start;}
.news-box{border-radius:14px; overflow:hidden; box-shadow:var(--shadow-soft); background:var(--card-bg); border:1px solid var(--border-soft);}
.news-head{margin:0; background:var(--forest-700); color:var(--paper-000); font-size:1.3rem; padding:14px 20px; text-align:center;}
.news-list{list-style:none; margin:0; padding:6px 20px 14px;}
.news-list li{border-bottom:1px solid var(--border-soft);}
.news-list li:last-child{border-bottom:none;}
.news-list a{display:block; padding:12px 0; text-decoration:none; color:var(--forest-700); font-size:.95rem; line-height:1.45;}
.news-list a:hover{color:var(--sun-500);}
.founder-block{display:grid; grid-template-columns:200px 1fr; gap:30px; align-items:center;}
.founder-circle{width:170px; height:212px; border-radius:18px; background:var(--paper-100); border:3px solid var(--sun-500); display:flex; align-items:center; justify-content:center; margin:0 auto; box-shadow:var(--shadow-soft); overflow:hidden;}
.founder-circle img{width:100%; height:100%; object-fit:cover; display:block;}
.founder-circle svg{width:58%; height:58%; color:var(--forest-700);}
.founder-cap{text-align:center; font-family:'Spectral',serif; font-style:italic; margin-top:12px; font-size:1.05rem;}
.founder-cap span{display:block; font-family:'Work Sans',sans-serif; font-style:normal; font-size:.8rem; color:var(--forest-500);}
.founder-text h2{font-size:clamp(1.5rem,3vw,2rem); color:var(--forest-700);}

/* ===== principal ===== */
.section-head.center{text-align:center; margin-left:auto; margin-right:auto;}
.section-head.center::before{margin-left:auto; margin-right:auto;}
.dots-line{display:flex; align-items:center; gap:14px; max-width:420px; margin:14px auto 0;}
.dots-line::before,.dots-line::after{content:""; flex:1; height:1px; background:var(--sun-500);}
.dots-line span{color:var(--sun-500); letter-spacing:4px; font-size:.8rem;}
.pr-grid{display:grid; grid-template-columns:220px 1fr; gap:38px; align-items:center; max-width:860px; margin:0 auto;}
.pr-avatar{width:170px; height:212px; border-radius:18px; background:var(--forest-700); color:var(--paper-000); display:flex; align-items:center; justify-content:center; font-family:'Spectral',serif; font-size:2.6rem; font-weight:600; border:3px solid var(--sun-500); margin:0 auto; box-shadow:var(--shadow-soft); overflow:hidden;}
.pr-avatar img{width:100%; height:100%; object-fit:cover; display:block;}
.pr-quote{font-family:'Spectral',serif; font-style:italic; font-size:1.2rem; color:var(--forest-700); margin-top:0;}

/* ===== tiles ===== */
.tiles-intro{display:grid; grid-template-columns:1fr 1fr; gap:40px; align-items:center; margin-bottom:36px;}
.tiles-intro h2{font-size:clamp(1.6rem,3.4vw,2.4rem); margin:0;}
.tiles-intro h2 em{color:var(--sun-500);}
.tiles-intro p{margin:0; color:var(--forest-500);}
.tiles{display:grid; grid-template-columns:repeat(4,1fr); gap:16px;}
.tile{--accent:#2f6fa3; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; min-height:220px; padding:20px; text-align:center; border-radius:12px; text-decoration:none; color:#fff; background:linear-gradient(150deg,var(--accent),color-mix(in srgb,var(--accent) 55%,#0b1a12)); box-shadow:0 10px 24px color-mix(in srgb,var(--accent) 35%,transparent); transition:transform .18s ease, box-shadow .18s ease;}
.tile:hover{transform:translateY(-6px); box-shadow:0 0 0 2px var(--accent), 0 22px 40px color-mix(in srgb,var(--accent) 45%,transparent);}
.tile svg{width:44px; height:44px;}
.tile span{font-family:'Spectral',serif; font-size:1.25rem; font-weight:600; line-height:1.25;}
.tile.t-blue{--accent:#2f6fa3;} .tile.t-orange{--accent:#c9702f;} .tile.t-teal{--accent:#2f9e8f;} .tile.t-gold{--accent:#a97c1f;}

/* ===== events carousel ===== */
.carousel{position:relative; padding:0 28px;}
.car-track{display:flex; gap:16px; overflow-x:auto; scroll-snap-type:x mandatory; scroll-behavior:smooth; scrollbar-width:none; padding:8px 4px 18px;}
.car-track::-webkit-scrollbar{display:none;}
.car-item{--accent:var(--forest-700); flex:0 0 calc(25% - 12px); scroll-snap-align:start; text-decoration:none; text-align:center; background:var(--card-bg); border:1px solid var(--border-soft); border-radius:12px; padding:18px 14px; box-shadow:0 8px 18px rgba(18,48,31,.10); transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;}
.car-item:hover{transform:translateY(-5px); border-color:var(--accent); box-shadow:0 0 0 1px var(--accent), 0 18px 34px color-mix(in srgb,var(--accent) 38%,transparent);}
.car-ic{background:color-mix(in srgb,var(--accent) 16%,var(--paper-000)); border-radius:8px; padding:34px 10px; margin-bottom:12px;}
.car-ic svg{width:44px; height:44px; color:var(--accent);}
.car-item h3{font-size:1rem; margin:0; color:var(--ink-900);}
.car-item.c-blue{--accent:#2f6fa3;} .car-item.c-purple{--accent:#7a4fa3;} .car-item.c-orange{--accent:#c9702f;}
.car-item.c-pink{--accent:#b1487a;} .car-item.c-teal{--accent:#2f9e8f;} .car-item.c-gold{--accent:#c99a3d;}
.car-arrow{position:absolute; top:42%; transform:translateY(-50%); z-index:3; width:38px; height:38px; border-radius:50%; border:none; background:var(--forest-700); color:#fff; font-size:1.5rem; line-height:1; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 6px 14px rgba(18,48,31,.3);}
.car-arrow:hover{background:var(--sun-500); color:var(--forest-900);}
.car-arrow.prev{left:-4px;} .car-arrow.next{right:-4px;}

/* ===== footer (dark, richer) ===== */
.footer-bottom{padding-left:24px; padding-right:24px;}
.footer-motto{text-align:center; padding-bottom:30px;}
.footer-motto p{font-family:'Spectral',serif; font-style:italic; font-size:clamp(1.05rem,2.2vw,1.35rem); color:rgba(245,241,230,.85); margin:0;}
.footer-brand p{margin:0 0 4px;}
.footer-grid a.footer-btn{display:inline-block; border:1px solid rgba(245,241,230,.5); padding:8px 14px; font-size:.85rem; margin:8px 8px 0 0; border-radius:4px;}
.footer-grid a.footer-btn:hover{border-color:var(--sun-500);}

/* ===== responsive ===== */
@media (max-width:900px){
  .nf-grid{grid-template-columns:1fr; gap:32px;}
  .tiles-intro{grid-template-columns:1fr; gap:14px;}
  .tiles{grid-template-columns:repeat(2,1fr);}
  .car-item{flex:0 0 calc(50% - 8px);}
}
@media (max-width:700px){
  .founder-block, .pr-grid{grid-template-columns:1fr; gap:18px;}
  .founder-text, .pr-text{text-align:center;}
}
@media (max-width:600px){
  .topbar .wrap{justify-content:center; padding:6px 16px;}
  .topbar{font-size:.72rem;}
  .topbar .topbar-mail, .topbar .topbar-loc{display:none;}
  .affil-bar{font-size:.7rem;}
  .hero-slider{height:480px;}
  .hs-caption{top:auto; bottom:48px; transform:none; padding:0 16px;}
  .hs-arrow{display:none;}
  .hs-logo{margin-bottom:10px;}
  .hs-logo img{width:54px; height:54px;}
  .hs-title{padding:8px 14px;}
  .hs-text{padding:12px 14px;}
  .hs-cta{margin-top:12px;}
  .tile{min-height:150px; padding:14px;}
  .tile span{font-size:1.05rem;}
  .car-item{flex:0 0 72%;}
  .carousel{padding:0;}
  .car-arrow{display:none;}
}
@media (prefers-reduced-motion: reduce){
  .hs-slide{transition:none;}
  .hs-slide.active .hs-logo,.hs-slide.active .hs-box,.hs-slide.active .hs-cta{animation:none !important;}
}

/* ===== previous-year toppers (inside class modal) ===== */
.toppers{margin-top:18px; padding-top:14px; border-top:1px dashed var(--border-soft);}
.toppers h4{margin:0 0 10px; font-size:.85rem; color:var(--forest-500); font-weight:600;}
.topper-row{display:flex; align-items:center; gap:10px; padding:7px 0;}
.rank-badge{width:22px; height:22px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:.72rem; font-weight:700; color:#fff; flex:none;}
.rank-badge.rank-1{background:#c99a3d;}
.rank-badge.rank-2{background:#9aa5ad;}
.rank-badge.rank-3{background:#b5723a;}
.topper-avatar{width:30px; height:30px; border-radius:50%; background:var(--forest-200); color:var(--forest-700); display:flex; align-items:center; justify-content:center; font-size:.66rem; font-weight:700; flex:none;}
.topper-name{flex:1; font-size:.88rem;}
.topper-pct{font-size:.85rem; font-weight:600; color:var(--forest-700); white-space:nowrap;}

/* ===== nav dropdown (Result) ===== */
.navlinks li.has-dropdown{position:relative;}
.navlinks .dropdown{list-style:none; margin:0; padding:8px 0; position:absolute; top:100%; left:0; min-width:170px; background:var(--card-bg); border:1px solid var(--border-soft); border-radius:8px; box-shadow:var(--shadow-soft); opacity:0; visibility:hidden; transform:translateY(6px); transition:opacity .18s ease, transform .18s ease, visibility .18s; z-index:10;}
.navlinks li.has-dropdown:hover .dropdown, .navlinks li.has-dropdown:focus-within .dropdown{opacity:1; visibility:visible; transform:translateY(0);}
.navlinks .dropdown li{width:100%;}
.navlinks .dropdown a{display:block; padding:9px 18px; font-size:.88rem; border-bottom:none; white-space:nowrap;}
.navlinks .dropdown a:hover{background:var(--paper-100); color:var(--sun-500);}
@media (max-width:820px){
  .navlinks .dropdown{position:static; opacity:1; visibility:visible; transform:none; border:none; box-shadow:none; background:transparent; padding:0; margin-top:0; max-height:0; overflow:hidden; transition:max-height .25s ease;}
  .navlinks li.has-dropdown.open .dropdown{max-height:220px; padding-left:16px; margin-top:4px;}
  .navlinks li.has-dropdown > a{font-weight:600;}
  .navlinks .dropdown a{padding:10px 0; border-bottom:1px solid var(--border-soft); font-size:.92rem;}
}

/* ===== result tables & charts ===== */
.table-wrap{overflow-x:auto; margin-bottom:28px; border-radius:10px; box-shadow:var(--shadow-soft);}
table.result-table{width:100%; border-collapse:collapse; min-width:560px; background:var(--card-bg);}
table.result-table th{background:var(--forest-700); color:var(--paper-000); padding:11px 14px; font-size:.86rem; font-weight:600; text-align:center;}
table.result-table td{padding:10px 14px; text-align:center; font-size:.9rem; border-bottom:1px solid var(--border-soft);}
table.result-table tr:nth-child(even) td{background:var(--paper-100);}
.chart-legend{display:flex; gap:22px; justify-content:center; margin-bottom:10px; flex-wrap:wrap;}
.chart-legend span{display:inline-flex; align-items:center; gap:7px; font-size:.86rem; color:var(--forest-500);}
.chart-legend i{width:12px; height:12px; border-radius:3px; display:inline-block;}
.chart-box{background:var(--card-bg); border:1px solid var(--border-soft); border-radius:12px; padding:16px; box-shadow:var(--shadow-soft); margin-bottom:20px;}
.result-chart{width:100%; height:auto; display:block;}

/* ===== in the news: floating press clippings ===== */
#media{padding-bottom:52px;}
.clip-marquee{overflow:hidden; padding:26px 0 10px; -webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent); mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);}
.clip-track{display:flex; gap:22px; width:max-content; animation:clipScroll 34s linear infinite;}
.clip-marquee:hover .clip-track{animation-play-state:paused;}
.clip-card{--tilt:0deg; flex:0 0 220px; background:var(--paper-000); border:1px solid var(--border-soft); border-radius:4px; padding:22px 18px 16px; text-align:center; box-shadow:0 8px 18px rgba(18,48,31,0.12); transform:rotate(var(--tilt));}
.clip-card.t1{--tilt:-2deg;}
.clip-card.t2{--tilt:1.5deg;}
.clip-card.t3{--tilt:-1deg;}
.clip-icon{width:44px; height:44px; margin:0 auto 14px; color:var(--forest-700);}
.clip-icon svg{width:100%; height:100%;}
.clip-photo{width:100%; height:120px; margin:0 0 14px; border-radius:3px; overflow:hidden;}
.clip-photo img{width:100%; height:100%; object-fit:cover; display:block;}
.clip-caption{font-family:'Spectral',serif; font-size:.96rem; line-height:1.35; margin:0 0 10px; color:var(--ink-900);}
.clip-tag{display:block; font-size:.66rem; letter-spacing:.05em; color:var(--sun-500); border-top:1px dashed var(--border-soft); padding-top:8px; text-transform:uppercase;}
@keyframes clipScroll{from{transform:translateX(0);} to{transform:translateX(-50%);}}
@media (prefers-reduced-motion: reduce){.clip-track{animation:none;}}
@media (max-width:600px){.clip-card{flex:0 0 170px; padding:18px 14px 14px;}}

/* ===== admissions sub-sections ===== */
.adm-block{margin-bottom:44px;}
.adm-block:last-of-type{margin-bottom:0;}
.adm-block h3{font-family:'Spectral',serif; font-size:1.3rem; color:var(--forest-700); margin:0 0 18px; padding-bottom:8px; border-bottom:2px solid var(--sun-500); display:inline-block;}
.elig-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-bottom:12px;}
.elig-card{background:var(--card-bg); border:1px solid var(--border-soft); border-radius:12px; padding:20px 14px; text-align:center; box-shadow:0 4px 14px rgba(18,48,31,0.06);}
.elig-age{display:block; font-family:'Spectral',serif; font-size:1.4rem; font-weight:700; color:var(--forest-700); margin-bottom:6px; line-height:1.2;}
.elig-class{display:block; font-size:.82rem; color:var(--forest-500);}
.doc-list{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:12px 22px;}
.doc-list li{display:flex; align-items:flex-start; gap:10px; font-size:.92rem; padding:12px 14px; background:var(--card-bg); border:1px solid var(--border-soft); border-radius:8px;}
.doc-check{color:var(--forest-700); font-weight:700; flex:none;}
@media (max-width:700px){
  .elig-grid{grid-template-columns:repeat(2,1fr);}
  .doc-list{grid-template-columns:1fr;}
}
"""

# --------------------------------------------------------------------------- JS

HOME_JS = """
(function(){
  function initHome(){
    var first = document.querySelector('.brand img');
    if(first){
      document.querySelectorAll('img[data-logo]').forEach(function(im){ im.src = first.src; });
    }
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---------- mobile accordion for nav dropdown (Result) ---------- */
    var ddParent = document.querySelector('.navlinks li.has-dropdown');
    if(ddParent){
      var ddLink = ddParent.querySelector(':scope > a');
      ddLink.addEventListener('click', function(e){
        if(window.matchMedia('(max-width:820px)').matches){
          e.preventDefault();
          ddParent.classList.toggle('open');
        }
      });
    }

    /* ---------- hero slider ---------- */
    var hs = document.querySelector('.hero-slider');
    if(hs){
      var slides = Array.prototype.slice.call(hs.querySelectorAll('.hs-slide'));
      var n = slides.length;
      var dotsBox = hs.querySelector('.hs-dots');
      var dots = [];
      var idx = 0, busy = false, timer = null;

      slides.forEach(function(s, i){ s.style.transform = i === 0 ? 'translateX(0)' : 'translateX(100%)'; });
      slides[0].classList.add('show', 'active');

      for(var i = 0; i < n; i++){
        (function(k){
          var b = document.createElement('button');
          b.type = 'button';
          b.setAttribute('aria-label', 'Go to slide ' + (k + 1));
          b.addEventListener('click', function(){ go(k, k > idx ? 1 : -1); restart(); });
          dotsBox.appendChild(b);
          dots.push(b);
        })(i);
      }
      dots[0].classList.add('on');

      function go(k, dir){
        if(busy || k === idx || n < 2) return;
        busy = true;
        dir = dir || 1;
        var cur = slides[idx], nxt = slides[k];
        nxt.style.transition = 'none';
        nxt.style.transform = 'translateX(' + (100 * dir) + '%)';
        nxt.classList.add('show');
        void nxt.offsetWidth;
        nxt.style.transition = reduce ? 'none' : '';
        cur.style.transition = reduce ? 'none' : '';
        nxt.classList.add('active');
        cur.style.transform = 'translateX(' + (-100 * dir) + '%)';
        nxt.style.transform = 'translateX(0)';
        dots[idx].classList.remove('on');
        dots[k].classList.add('on');
        idx = k;
        setTimeout(function(){
          cur.classList.remove('show', 'active');
          busy = false;
        }, reduce ? 0 : 850);
      }
      function next(){ go((idx + 1) % n, 1); }
      function prev(){ go((idx - 1 + n) % n, -1); }
      function restart(){
        if(reduce) return;
        if(timer) clearInterval(timer);
        timer = setInterval(function(){ if(hs.offsetParent !== null) next(); }, 5500);
      }
      hs.querySelector('.hs-arrow.next').addEventListener('click', function(){ next(); restart(); });
      hs.querySelector('.hs-arrow.prev').addEventListener('click', function(){ prev(); restart(); });

      var sx = null;
      hs.addEventListener('touchstart', function(e){ sx = e.touches[0].clientX; }, {passive:true});
      hs.addEventListener('touchend', function(e){
        if(sx === null) return;
        var dx = e.changedTouches[0].clientX - sx;
        sx = null;
        if(Math.abs(dx) > 40){ if(dx < 0){ next(); } else { prev(); } restart(); }
      }, {passive:true});
      restart();
    }

    /* ---------- events carousel ---------- */
    var car = document.querySelector('.carousel');
    if(car){
      var track = car.querySelector('.car-track');
      var paused = false;
      function step(){
        var it = track.querySelector('.car-item');
        return it ? it.getBoundingClientRect().width + 16 : 240;
      }
      function nextC(){
        if(track.scrollLeft + track.clientWidth >= track.scrollWidth - 4){ track.scrollTo({left:0, behavior:'smooth'}); }
        else { track.scrollBy({left:step(), behavior:'smooth'}); }
      }
      function prevC(){
        if(track.scrollLeft <= 4){ track.scrollTo({left:track.scrollWidth, behavior:'smooth'}); }
        else { track.scrollBy({left:-step(), behavior:'smooth'}); }
      }
      car.querySelector('.car-arrow.next').addEventListener('click', nextC);
      car.querySelector('.car-arrow.prev').addEventListener('click', prevC);
      car.addEventListener('mouseenter', function(){ paused = true; });
      car.addEventListener('mouseleave', function(){ paused = false; });
      car.addEventListener('touchstart', function(){ paused = true; }, {passive:true});
      car.addEventListener('touchend', function(){ setTimeout(function(){ paused = false; }, 2500); }, {passive:true});
      if(!reduce){
        setInterval(function(){ if(!paused && track.offsetParent !== null) nextC(); }, 3500);
      }
    }
  }
  if(document.readyState === 'loading'){ document.addEventListener('DOMContentLoaded', initHome); }
  else { initHome(); }
})();
"""

# --------------------------------------------------------------------------- faculty (CMS-driven)

def faculty_card_html(item, idx):
    name = item.get("name", "")
    role = item.get("role", "")
    qualification = item.get("qualification", "")
    subject = item.get("subject", "")
    bio = item.get("bio", "")
    photo = item.get("photo") or ""
    initials = "".join(w[0] for w in name.split() if w)[:2].upper()
    if photo:
        avatar = f'<img src="{photo}" alt="{name}">'
        photo_attr = f' data-photo="{photo}"'
    else:
        avatar = initials
        photo_attr = ""
    return f'''<button type="button" class="fac-card reveal" data-name="{name}" data-role="{role}" data-qualification="{qualification}" data-subject="{subject}" data-bio="{bio}"{photo_attr}>
        <div class="fac-avatar">{avatar}</div><h3>{name}</h3><p class="role">{role}</p><p>{bio}</p>
      </button>'''


def faculty_section_html(items):
    cards = "".join(faculty_card_html(it, i) for i, it in enumerate(items))
    return f"""<section id="faculty">
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Our Faculty</h2>
      <p>Experienced teachers guiding every stage of school life. Tap a profile to learn more.</p>
    </div>
    <div class="fac-grid" data-stagger>{cards}
    </div>
    <p class="fac-note">Faculty profiles are managed from the admin panel.</p>
  </div>
</section>
"""

# --------------------------------------------------------------------------- results

RESULT_DATA = {
    "5th": [
        ("2018-19", 24, 24, 71.2), ("2019-20", 27, 27, 73.5), ("2020-21", 30, 30, 74.8),
        ("2021-22", 32, 32, 72.9), ("2022-23", 29, 29, 75.6), ("2023-24", 28, 28, 76.3),
        ("2024-25", 30, 30, 77.1),
    ],
    "9th": [
        ("2018-19", 19, 19, 68.4), ("2019-20", 22, 22, 70.1), ("2020-21", 26, 26, 71.8),
        ("2021-22", 29, 28, 69.5), ("2022-23", 25, 25, 72.4), ("2023-24", 24, 24, 73.9),
        ("2024-25", 26, 26, 74.6),
    ],
    "10th": [
        ("2018-19", 21, 21, 69.5), ("2019-20", 30, 30, 74.7), ("2020-21", 41, 41, 75.4),
        ("2021-22", 52, 52, 71.6), ("2022-23", 43, 43, 67.7), ("2023-24", 37, 37, 73.5),
        ("2024-25", 42, 42, 75.4),
    ],
}


def bar_chart_svg(rows):
    W, H = 760, 340
    padL, padR, padT, padB = 38, 16, 16, 40
    plotW = W - padL - padR
    plotH = H - padT - padB
    n = len(rows)
    groupW = plotW / n
    barW = groupW * 0.22
    gap = groupW * 0.07
    yMax = 100

    def y(v):
        return padT + plotH - (v / yMax) * plotH

    parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" class="result-chart" role="img" aria-label="Bar chart of year-wise results">']
    for g in (0, 25, 50, 75, 100):
        gy = y(g)
        parts.append(f'<line x1="{padL}" y1="{gy:.1f}" x2="{W-padR}" y2="{gy:.1f}" stroke="var(--border-soft)" stroke-width="1"/>')
        parts.append(f'<text x="{padL-8}" y="{gy+4:.1f}" text-anchor="end" font-size="10.5" fill="#7a8a80">{g}</text>')
    colors = ("#3d7a52", "#c99a3d", "#2f6fa3")
    for i, (yr, appeared, passed, pct) in enumerate(rows):
        gx = padL + i * groupW
        pass_pct = round((passed / appeared) * 100, 1) if appeared else 0
        vals = (appeared, passed, pass_pct)
        for j, val in enumerate(vals):
            bx = gx + gap + j * (barW + gap)
            by = y(val)
            bh = (padT + plotH) - by
            parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{barW:.1f}" height="{bh:.1f}" fill="{colors[j]}" rx="2"/>')
            parts.append(f'<text x="{bx+barW/2:.1f}" y="{by-4:.1f}" text-anchor="middle" font-size="9.5" fill="var(--ink-900)">{val}</text>')
        parts.append(f'<text x="{gx+groupW/2:.1f}" y="{H-14}" text-anchor="middle" font-size="10.5" fill="var(--forest-700)">{yr}</text>')
    parts.append('</svg>')
    return "".join(parts)


def result_page(class_label, page_banner_fn, rows_json=None):
    if rows_json:
        rows = [(r["session"], int(r["appeared"]), int(r["passed"]), float(r["average"])) for r in rows_json]
    else:
        rows = RESULT_DATA[class_label]
    trs = ""
    for yr, appeared, passed, avg in rows:
        pct = round((passed / appeared) * 100, 1) if appeared else 0
        trs += f"<tr><td>{yr}</td><td>{appeared}</td><td>{passed}</td><td>{pct}%</td><td>{avg}</td></tr>"
    chart = bar_chart_svg(rows)
    banner = page_banner_fn(f"Result \u2014 Class {class_label}", "Year-wise board examination performance.")
    return f"""{banner}
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Class {class_label} &middot; Session-wise Result</h2>
      <p>Appeared, passed, pass percentage and average score over recent sessions.</p>
    </div>
    <div class="table-wrap reveal">
      <table class="result-table">
        <thead><tr><th>Session</th><th>Appeared</th><th>Passed</th><th>Pass %</th><th>Average</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
    </div>
    <div class="chart-legend reveal"><span><i style="background:#3d7a52"></i>Appeared</span><span><i style="background:#c99a3d"></i>Passed</span><span><i style="background:#2f6fa3"></i>Pass %</span></div>
    <div class="chart-box reveal">{chart}</div>
    <p class="fac-note">Results are managed from the admin panel.</p>
  </div>
</section>
"""

