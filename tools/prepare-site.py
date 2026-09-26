#!/usr/bin/env python3
"""Set canonical metadata for the actual published address. No third-party packages."""
import json, re, sys
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
root = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 tools/prepare-site.py https://ACCOUNT.github.io/REPOSITORY/')
base = sys.argv[1].rstrip('/') + '/'
u = urlsplit(base)
if u.scheme != 'https' or not u.netloc or u.query or u.fragment or u.username or any(c in base for c in '<>"\' '):
    raise SystemExit('A valid, public HTTPS URL without query or fragment is required.')
for name in ('index.html', 'datenschutz.html'):
    page = root / name
    text = page.read_text()
    text = re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>', '', text)
    url = base + ('' if name == 'index.html' else name)
    text = text.replace('</head>', f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}"></head>')
    page.write_text(text)
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(base + n)+'</loc></url>' for n in ('','datenschutz.html'))+'</urlset>\n')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n')
p = root/'404.html'
s = p.read_text()
s = re.sub(r'<a class="home".*?</a>', '', s)
s = s.replace('</main>', f'<p><a class="home" href="{base}">Zur Startseite</a></p></main>')
p.write_text(s)
print('SEO metadata ready for '+base)
