# WEBSITE_AUDIT.md

Erstellt: 2026-07-10
Live-Seite geprüft: https://website.rebellsystem.com
Repository: https://github.com/rebellmitherz/website.git
Ausgangsbranch: `main`
Ausgangscommit: `ae6d0ed17a926229bdc03a23032e4d7846602caa`
Arbeitsbranch: `rebuild/tiktok-revenue-funnel`

## Ist-Zustand vor Umbau

- Statische GitHub-Pages-Website mit `index.html`, `impressum.html`, `datenschutz.html`, `relunched/` Produkt-/Downloadseiten, `CNAME`, `sitemap.xml`, `robots.txt`.
- Live-Hero war grundsätzlich stark, aber noch nicht problemorientiert genug für TikTok-Link-in-Bio-Traffic.
- Produktkarten existierten, aber Besucher mussten selbst von Thema zu Produkt übersetzen.
- Mehrere Checkout-Buttons nutzten `href="#"` plus JavaScript-Mapping statt direktem Stripe-Link im href.
- Impressum enthält B2B-Aussage, obwohl Website sichtbar B2C-Eltern anspricht.
- Impressum enthält Hinweis auf EU-OS-Plattform, potenziell veraltet/prüfpflichtig.
- Datenschutzerklärung nennt Calendly, aber auf der aktuellen Homepage wurde kein Calendly-CTA gefunden.

## Scores vor Umbau

- Conversion-Score: 6/10 — Angebot vorhanden, aber TikTok-Problem-Match und direkter Produktfinder fehlen.
- Vertrauens-Score: 6/10 — gute Disclaimer-Tendenz, aber Rolle, Grenzen, Lieferumfang und Rechts-/Checkout-Transparenz nicht nah genug an Kaufbuttons.
- Mobile-Score: 7/10 — responsive Grundstruktur vorhanden, aber erster Screen sollte klarer zum Problemfinder führen.
- Umsatz-Score: 5/10 — Paket sichtbar, aber Produktleiter, Analyseweg, UTM-/Trackingplan und problembezogene Wege fehlen.

## Fünffache Kausalprüfung

### Ebene 1 — Traffic- und Message-Match

| TikTok-Thema | Besucherproblem | Erwartung | Landingpage/Section | Angebot | CTA |
|---|---|---|---|---|---|
| Jugendamt | Brief/E-Mail liegt vor | nicht falsch antworten | `#jugendamt-antwort` | Jugendamt Antwort | Jugendamt-Antwort kaufen |
| Umgangsblockade | Kontakt blockiert | erste Schritte, keine Eskalation | `#umgangsblockade` | Umgangsblockade | Modul kaufen |
| Gutachten | Begutachtung droht | Fragen/Fehler erkennen | `#gutachten` | Gutachten-Modul | Modul kaufen |
| Gerichtsfehler/Protokoll | Protokoll falsch | Korrekturstruktur | `#protokollberichtigung` | Protokollberichtigung | Modul kaufen |
| Beschluss wird ignoriert | Beschluss wirkt nicht | Durchsetzung sauber vorbereiten | `#durchsetzung` | Durchsetzung nach Beschluss | Modul kaufen |
| Akteneinsicht | unklar, was in Akten steht | Antrag/Fristen | `#akteneinsicht` | Akteneinsicht PRO | Modul kaufen |
| mehrere Baustellen | alles hängt zusammen | kompletter Werkzeugkasten | `#elternschutzpaket` | Elternschutzpaket | Paket kaufen |
| individuelle Lage | braucht Einordnung | Analyseanfrage | `#analyse` | Anfrage/Analyse-Hypothese | E-Mail-Anfrage |

### Ebene 2 — Vertrauen und Risikoreduktion

- Fehlend/zu schwach: klare Rolle Emilio/Rebell mit Herz, Produktgrenzen, kein Ersatz für Anwalt, externes Stripe-Verfahren nah am CTA.
- Keine echten Testimonials vorhanden; daher keine Fake-Bewertungen verwenden.
- Geeignete Ersatz-Vertrauensmittel: Produktvorschau, Inhaltslisten, typische Nutzung, FAQ, klare Grenzen, E-Mail-Kontakt.

### Ebene 3 — Angebot und Kaufentscheidung

- Einzelmodule und Paket existieren: 9,95€ Einzelmodule, 27€ Elternschutzpaket.
- Paket ist wirtschaftlich sinnvoller Haupthebel.
- Produktfinder senkt kognitive Last und führt kalte TikTok-Besucher schneller zu passendem Modul.
- Analyseanfrage ist sinnvoller nächster Umsatzschritt, aber operativ/rechtlich zu prüfen.

### Ebene 4 — Conversion-UX

- Priorität: 360/390/412px, erster Bildschirm, großer CTA, Problemfinder, direkte Stripe-hrefs, Sticky-Mobile-CTA.
- Jede neue Section hat Funktion: Problem erkennen, Vertrauen, Produkt auswählen, Kauf auslösen, Analyseanfrage.

### Ebene 5 — Messung und Umsatzsystem

- Keine externe Analytics-Implementierung im Code erkannt.
- UTM-Konzept und eventfähige `data-event` Attribute wurden als datensparsame Vorstufe vorgesehen.
- Kein blindes Tracking installiert; Datenschutz/Freigabe nötig.

## P0-Risiken

1. B2C-/B2B-Widerspruch: Eltern/Privatpersonen als Zielgruppe, Impressum behauptet B2B-Angebot.
2. EU-OS-Plattform: Impressum verweist auf `https://ec.europa.eu/consumers/odr`; potenziell veraltet/prüfpflichtig.
3. Verbraucher-/Digitalinhalte-Pflichten: Widerruf, Sofortdownload, Zustimmung zum Erlöschen, Bestellbutton/Bestätigung müssen professionell geprüft werden.
4. Datenschutzerklärung: Calendly wird genannt, aber aktuelle Homepage nutzt keinen Calendly-CTA; tatsächliche Dienste prüfen.
5. Stripe-Transparenz: externe Checkout-Weiterleitung muss klar beschrieben bleiben.

## P1-Umsatzhebel

- Hero auf konkreten TikTok-Problemzustand schärfen.
- Problemorientierten Link-in-Bio-Hub einbauen.
- Direkte, unveränderte Stripe-hrefs in Kaufbuttons.
- Produktkarten mit Situation, Inhalt, Geeignet/Nicht geeignet, Preis, Disclaimer.
- Paket klar als Hauptempfehlung positionieren.
- Analyseanfrage als qualifizierten nächsten Schritt ergänzen.

## Beweise und Fundstellen

- Live-Hero: Browser-Snapshot 2026-07-10.
- Repo-Status: `main`, Commit `ae6d0ed17a926229bdc03a23032e4d7846602caa`, sauber vor Branch.
- Stripe-Fundstellen: siehe `STRIPE_LINK_INVENTORY.md`.
- Impressum B2B/OS: `impressum.html`, Abschnitt Streitbeilegung.
- Datenschutz Calendly: `datenschutz.html`, Abschnitt Terminbuchung.
