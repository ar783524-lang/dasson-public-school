# Dasson Public High School — Website Source

This repository builds the school website and powers its admin panel.

## How it works
- `python3 build_site.py` generates the live website into `dist/` (Netlify runs this automatically on every change).
- `content/*.json` holds the editable data (faculty, results, news clippings) — edit these via `/admin` instead of by hand.
- `assets/` holds all images. Anything uploaded through the admin panel is saved here automatically.
- `site.html` and `home_v2.py` hold the page design/layout — edit with care (or ask Claude).

## Admin panel
Visit `/admin` on the live site to log in and edit Faculty, Results, and News content without touching code.
