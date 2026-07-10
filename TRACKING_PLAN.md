# TRACKING_PLAN.md

## Grundsatz

Kein externes Tracking wurde blind installiert. Die Website enthält nur datensparsame technische Vorbereitungen (`data-event`, `data-product`, `data-situation`, optional `sessionStorage` für UTM). Externe Analytics, Cookies oder Pixel benötigen Datenschutzprüfung und Freigabe.

## UTM-System

Beispielstruktur:

- `utm_source=tiktok`
- `utm_medium=organic`
- `utm_campaign=umgangsblockade`
- `utm_content=video_2026_07_10_01`

Beispiel-Link:

`https://website.rebellsystem.com/?utm_source=tiktok&utm_medium=organic&utm_campaign=umgangsblockade&utm_content=video_2026_07_10_01#umgangsblockade`

Wichtig: UTM-Parameter werden nicht an Stripe-URLs angehängt. Stripe-Links bleiben unverändert.

## Events

| Event | Auslöser | Parameter | geschäftlicher Zweck | Datenschutzrelevanz | technische Implementierung | Freigabe |
|---|---|---|---|---|---|---|
| `page_view` | Seitenaufruf | path, utm | Traffic je TikTok-Kategorie | mittel | Analytics nach Freigabe | nötig |
| `hero_cta_click` | Hero-CTA | text, utm | Hero-Wirkung | niedrig-mittel | `data-event` vorhanden | nötig |
| `situation_select` | Problemfinder-Klick | situation, utm | Message-Match messen | niedrig-mittel | `data-situation` vorhanden | nötig |
| `product_view` | Scroll/Section sichtbar | product | Produktinteresse | mittel | IntersectionObserver möglich | nötig |
| `bundle_click` | Paket-CTA | product=bundle | AOV-Hebel messen | niedrig-mittel | `data-event` vorhanden | nötig |
| `single_product_click` | Einzelprodukt-CTA | product | Einzelprodukt-Nachfrage | niedrig-mittel | `data-product` vorhanden | nötig |
| `checkout_start` | Stripe-Link-Klick | product, href | Checkout-Start vs Kauf | mittel | `data-event` vorhanden | nötig |
| `checkout_return` | Rückkehr von Stripe | status/product | Abschluss/Abbruch schätzen | mittel-hoch | braucht Stripe/Return-URL | Stripe/Legal nötig |
| `analysis_offer_click` | Analyse-CTA | location | Lead-Hebel | mittel | `data-event` vorhanden | nötig |
| `lead_form_start` | späteres Formular | utm | Analyse-Funnel | hoch | nicht implementiert | Legal nötig |
| `lead_form_submit` | Formularversand | keine sensiblen Details in Analytics | qualifizierte Leads | hoch | nicht implementiert | Legal nötig |

## Funnel-Stufen

1. TikTok-Video gesehen.
2. Profil-Link geklickt.
3. Problemfinder genutzt.
4. Produktkarte erreicht.
5. Checkout gestartet.
6. Stripe-Kauf abgeschlossen.
7. Download genutzt.
8. Analyseanfrage oder Wiederkauf.

## Datenschutzabhängigkeiten

- Consent-Mechanismus prüfen, wenn Cookies/Pixel eingesetzt werden.
- Stripe-Conversion-Abgleich nur mit geklärter Rechtsgrundlage.
- Keine sensiblen Fallinhalte in Analytics-Events.
- UTM in eigener Website darf Stripe-Link nicht verändern.

## Dashboard-Vorschlag

Wöchentlich erfassen:

- Sessions nach `utm_campaign`.
- `situation_select` Rate.
- Produkt-Checkout-Starts je Produkt.
- Stripe-Käufe je Produkt.
- Conversion Checkout-Start → Kauf.
- Bundle-Anteil.
- Analyseanfragen.
- Umsatz pro 1.000 qualifizierte Besucher.

## A/B-Test-Plan

- Test A: Hero Problemfinder zuerst vs. Paket zuerst.
- Test B: Produktkarten kurz vs. Lieferumfang ausführlich.
- Test C: Analyseanfrage prominent vs. nach Produktkarten.
- Test D: TikTok-spezifische Ankerlinks vs. allgemeine Homepage.
