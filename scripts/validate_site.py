#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_STRIPE = {
    "elternschutzpaket": "https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c",
    "akteneinsicht": "https://buy.stripe.com/eVqbJ378og6d0b2ar78og0e",
    "umgangsblockade": "https://buy.stripe.com/7sY28tboE9HP9LC56N8og0i",
    "durchsetzung": "https://buy.stripe.com/fZu4gBboE5rz5vmgPv8og0h",
    "gutachten": "https://buy.stripe.com/aFafZj3Wc8DL2jabvb8og0f",
    "jugendamt-antwort": "https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b",
    "protokollberichtigung": "https://buy.stripe.com/eVq8wR0K08DLe1SfLr8og0g",
}

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.ids=set()
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if 'id' in d:
            self.ids.add(d['id'])
        if tag == 'a' and 'href' in d:
            self.links.append(d)

def parse(path):
    p=Parser()
    p.feed(path.read_text(encoding='utf-8'))
    return p

def main():
    errors=[]
    index=ROOT/'index.html'
    parsed=parse(index)

    by_product={}
    for link in parsed.links:
        href=link.get('href','')
        product=link.get('data-product')
        if product:
            by_product.setdefault(product,[]).append(href)

    for product,url in EXPECTED_STRIPE.items():
        hrefs=by_product.get(product,[])
        if not hrefs:
            errors.append(f"missing product button: {product}")
            continue
        for href in hrefs:
            if href != url:
                errors.append(f"stripe mismatch for {product}: {href} != {url}")

    for link in parsed.links:
        href=link.get('href','')
        if href.startswith('#') and href != '#':
            target=href[1:]
            if target not in parsed.ids:
                errors.append(f"missing anchor target: {href}")
        if href == '#' and link.get('data-product'):
            errors.append(f"buy button still uses href=# for {link.get('data-product')}")

    for required in ['problemfinder','produkte','vertrauen','faq','analyse','elternschutzpaket']:
        if required not in parsed.ids:
            errors.append(f"missing required section id: {required}")

    # local legal/docs links referenced in footer
    for local in ['impressum.html','datenschutz.html','relunched/index.html']:
        if not (ROOT/local).exists():
            errors.append(f"missing local linked file: {local}")

    # all local HTML links resolve
    html_files = [p for p in ROOT.rglob('*.html') if '.git' not in p.parts]
    local_links_checked = 0
    for html_file in html_files:
        p = parse(html_file)
        for link in p.links:
            href = link.get('href','')
            local_links_checked += 1
            if href.startswith(('http://','https://','mailto:','tel:')):
                continue
            if href == '/':
                continue
            if href.startswith('#'):
                if len(href) > 1 and href[1:] not in p.ids:
                    errors.append(f"missing local anchor in {html_file.relative_to(ROOT)}: {href}")
                continue
            path, _, frag = href.partition('#')
            target = (html_file.parent / unquote(path or html_file.name)).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"local link escapes root in {html_file.relative_to(ROOT)}: {href}")
                continue
            if not target.exists():
                errors.append(f"missing local file in {html_file.relative_to(ROOT)}: {href}")

    print(f"links_total={len(parsed.links)}")
    print(f"ids_total={len(parsed.ids)}")
    print(f"stripe_products={len(by_product)}")
    print(f"html_files={len(html_files)}")
    print(f"local_links_checked={local_links_checked}")
    if errors:
        print("FAIL")
        for e in errors:
            print("-",e)
        return 1
    print("PASS")
    for product,url in EXPECTED_STRIPE.items():
        print(f"{product}: {url}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
