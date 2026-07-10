# STRIPE_LINK_VALIDATION.md

Erstellt: 2026-07-10
Arbeitsbranch: `rebuild/tiktok-revenue-funnel`

## Prüfmethode

- Automatisiert: `python scripts/validate_site.py`
- Browser-DOM: lokale Seite `http://127.0.0.1:8029/`, DOM-Abfrage aller `a[href^="https://buy.stripe.com/"]`
- Extern: HTTP-HEAD gegen jede Stripe-URL, keine Testzahlung, keine Checkout-Auslösung über Kaufabschluss
- Manuell/visuell: Browser-Snapshot der lokalen Seite plus Mobile-Screenshots 360/390/412px erzeugt

## Automatisches Testergebnis

```text
links_total=30
ids_total=14
stripe_products=7
html_files=19
local_links_checked=103
PASS
elternschutzpaket: https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c
akteneinsicht: https://buy.stripe.com/eVqbJ378og6d0b2ar78og0e
umgangsblockade: https://buy.stripe.com/7sY28tboE9HP9LC56N8og0i
durchsetzung: https://buy.stripe.com/fZu4gBboE5rz5vmgPv8og0h
gutachten: https://buy.stripe.com/aFafZj3Wc8DL2jabvb8og0f
jugendamt-antwort: https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b
protokollberichtigung: https://buy.stripe.com/eVq8wR0K08DLe1SfLr8og0g
```

## Vorher/Nachher-Vergleich

| ursprüngliche URL | neue Fundstelle | sichtbarer Buttontext | zugeordnetes Produkt | technische Prüfung | manuelle Prüfung | Abweichung |
|---|---|---|---|---|---|---|
| `https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c` | `index.html`, Hero-Card + Produktkarte | `Paket für 27€ kaufen →`, `Elternschutzpaket kaufen →` | Elternschutzpaket | Ja | Ja | Nein |
| `https://buy.stripe.com/eVqbJ378og6d0b2ar78og0e` | `index.html#akteneinsicht` | `Akteneinsicht kaufen →` | Akteneinsicht PRO | Ja | Ja | Nein |
| `https://buy.stripe.com/7sY28tboE9HP9LC56N8og0i` | `index.html#umgangsblockade` | `Umgangsblockade kaufen →` | Umgangsblockade | Ja | Ja | Nein |
| `https://buy.stripe.com/fZu4gBboE5rz5vmgPv8og0h` | `index.html#durchsetzung` | `Durchsetzung kaufen →` | Durchsetzung nach Beschluss | Ja | Ja | Nein |
| `https://buy.stripe.com/aFafZj3Wc8DL2jabvb8og0f` | `index.html#gutachten` | `Gutachten-Modul kaufen →` | Gutachten verstehen & angreifen | Ja | Ja | Nein |
| `https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b` | `index.html#jugendamt-antwort` | `Jugendamt-Antwort kaufen →` | Jugendamt Antwort | Ja | Ja | Nein |
| `https://buy.stripe.com/eVq8wR0K08DLe1SfLr8og0g` | `index.html#protokollberichtigung` | `Protokoll-Modul kaufen →` | Protokollberichtigung | Ja | Ja | Nein |

## Externe Stripe-Erreichbarkeit

Alle sieben eindeutigen Stripe-Links lieferten per HTTP-HEAD Status `200`. Es wurde keine Testzahlung ausgelöst.

## Ergebnis

- Anzahl eindeutiger Stripe-Links vorher: 7
- Anzahl eindeutiger Stripe-Links nachher: 7
- Unveränderte URLs: 7/7
- Fehlende bestehende Links: 0
- Unklare Zuordnungen: 0
- Buttons mit `href="#"` und `data-product` auf Homepage nach Umbau: 0
- Festgestellte Abweichungen: 0

## Hinweis

`relunched/index.html` enthält weiterhin die bestehenden JS-Produktlinks. Der Hauptumbau betrifft die produktive Homepage `index.html`; die dortigen Hauptkaufbuttons sind jetzt direkte Stripe-hrefs.
