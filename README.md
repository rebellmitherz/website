# Rebellsystem · Website-Service Landingpage

Statische Verkaufsseite für **website.rebellsystem.com** — „Verkaufsstarke Websites für
Dienstleister, schnell & günstig" (Geldidee: 3. Angebot / Website-Service).

## Inhalt
- `index.html` — die Seite (eine Datei, keine Build-Tools)
- `impressum.html` / `datenschutz.html` — Pflichtseiten (gleiche Firma wie akquise-Seite)
- `fonts/` — Inter lokal (0 externe Requests, DSGVO)
- `.nojekyll` — GitHub Pages liefert unverändert aus

## Vor dem Live-Gang
- [ ] (Optional) Festpreis-Anker einbauen, falls du eine Zahl zeigen willst
- [ ] Telefonnummer im Footer prüfen (`0151 28141644`)
- [ ] Impressum/Datenschutz juristisch prüfen lassen (Anbieter in Spanien)

## Deploy via GitHub Pages (eigenes Repo!)
> Wichtig: NICHT ins selbe Repo wie akquise — GitHub Pages erlaubt nur 1 Custom Domain pro Repo.
1. Neues GitHub-Repo anlegen, z. B. `rebellsystem-website` → diesen Ordner pushen.
2. Repo → Settings → Pages → Source: `main` / root → speichern.
3. Auf der normalen `<user>.github.io/rebellsystem-website/`-URL testen.
4. Wenn's passt: Settings → Pages → Custom domain `website.rebellsystem.com` eintragen
   (legt CNAME-Datei an + HTTPS) → später „Enforce HTTPS".
5. IONOS DNS für `rebellsystem.com`: Typ **CNAME**, Host `website`, Ziel `<dein-github-user>.github.io`

**Push = live.** Erst veröffentlichen, wenn Impressum/Datenschutz geprüft sind.

## Verkaufs-Anschluss
Im KundenAgent ein Multi-Offer-Angebot „Website-Service" anlegen, das der Bot bewirbt
(Mailtext + Link auf website.rebellsystem.com).
