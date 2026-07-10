# STRIPE_LINK_INVENTORY.md

Erstellt: 2026-07-10 05:22:30
Repo: `rebellmitherz/website`
Ausgangsbranch: `main`
Ausgangscommit: `ae6d0ed17a926229bdc03a23032e4d7846602caa`
Live-Seite: https://website.rebellsystem.com

## Suchumfang

Gesucht im gesamten Repository nach: `stripe.com`, `buy.stripe.com`, `checkout.stripe.com`, `href=`, Redirects, JavaScript-Produkt-Mapping, Produkt-/Preisbegriffen.

## Bestehende Stripe-URLs vor Umbau

| Fundstelle | sichtbarer Produktname | Buttontext / technische Verwendung | exakte URL | Zielseite | Status |
|---|---|---|---|---|---|
| `index.html:46` | Elternschutzpaket | `Elternschutzpaket für 27€ holen →` | `https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c` | Stripe Payment Link | direktes href vorhanden |
| `index.html:70`, `130`, `182`, `190` + JS `PRODUCT_LINKS` | Elternschutzpaket | `Jetzt Elternschutzpaket kaufen →`, `Paket kaufen →`, Sticky | `https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c` | Stripe Payment Link | teils nur via JS/href="#" |
| `index.html:134` + JS `PRODUCT_LINKS` | Akteneinsicht PRO | `Kaufen →` | `https://buy.stripe.com/eVqbJ378og6d0b2ar78og0e` | Stripe Payment Link | via JS/href="#" |
| `index.html:135` + JS `PRODUCT_LINKS` | Umgangsblockade | `Kaufen →` | `https://buy.stripe.com/7sY28tboE9HP9LC56N8og0i` | Stripe Payment Link | via JS/href="#" |
| `index.html:136` + JS `PRODUCT_LINKS` | Durchsetzung nach Beschluss | `Kaufen →` | `https://buy.stripe.com/fZu4gBboE5rz5vmgPv8og0h` | Stripe Payment Link | via JS/href="#" |
| `index.html:137` + JS `PRODUCT_LINKS` | Gutachten verstehen & angreifen | `Kaufen →` | `https://buy.stripe.com/aFafZj3Wc8DL2jabvb8og0f` | Stripe Payment Link | via JS/href="#" |
| `index.html:138` + JS `PRODUCT_LINKS` | Protokollberichtigung | `Kaufen →` | `https://buy.stripe.com/eVq8wR0K08DLe1SfLr8og0g` | Stripe Payment Link | via JS/href="#" |
| `index.html:139` + JS `PRODUCT_LINKS` | Jugendamt Antwort | `Kaufen →` | `https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b` | Stripe Payment Link | via JS/href="#" |
| `relunched/index.html:102`, JS `PRODUCT_LINKS` | Elternschutzpaket | `Jetzt kaufen →` | `https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c` | Stripe Payment Link | direkt + JS |
| `relunched/index.html:111-156`, JS `PRODUCT_LINKS` | alle Einzelmodule | `Jetzt kaufen →` | gleiche 6 Einzelprodukt-URLs wie oben | Stripe Payment Links | teils JS/href="#" |

## Eindeutige Stripe-Links

1. Elternschutzpaket — `https://buy.stripe.com/8x23cx8csbPX1f60Qx8og0c`
2. Akteneinsicht PRO — `https://buy.stripe.com/eVqbJ378og6d0b2ar78og0e`
3. Umgangsblockade — `https://buy.stripe.com/7sY28tboE9HP9LC56N8og0i`
4. Durchsetzung nach Beschluss — `https://buy.stripe.com/fZu4gBboE5rz5vmgPv8og0h`
5. Gutachten verstehen & angreifen — `https://buy.stripe.com/aFafZj3Wc8DL2jabvb8og0f`
6. Jugendamt Antwort — `https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b`
7. Protokollberichtigung — `https://buy.stripe.com/eVq8wR0K08DLe1SfLr8og0g`

## Kritische Feststellung vor Umbau

Die meisten Kaufbuttons auf der Homepage hatten vor dem Umbau `href="#"` und wurden erst per JavaScript auf Stripe weitergeleitet. Das ist ein Conversion- und Robustheitsrisiko. Die URLs selbst wurden nicht verändert.
