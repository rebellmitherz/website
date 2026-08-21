#!/usr/bin/env python3
"""Generiert das 50EUR Premium-PDF Jugendamt-Meisterkurs"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors

pdf_path = "Jugendamt-Meisterkurs-Premium.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("CustomTitle", parent=styles["Heading1"], fontSize=24, textColor=colors.HexColor("#1a1a1a"), spaceAfter=30, alignment=TA_CENTER, fontName="Helvetica-Bold")
heading_style = ParagraphStyle("CustomHeading", parent=styles["Heading2"], fontSize=16, textColor=colors.HexColor("#2c5aa0"), spaceAfter=12, spaceBefore=20, fontName="Helvetica-Bold")
subheading_style = ParagraphStyle("CustomSubHeading", parent=styles["Heading3"], fontSize=13, textColor=colors.HexColor("#1a1a1a"), spaceAfter=8, spaceBefore=12, fontName="Helvetica-Bold")
body_style = ParagraphStyle("CustomBody", parent=styles["Normal"], fontSize=11, leading=16, spaceAfter=10)
quote_style = ParagraphStyle("Quote", parent=styles["Normal"], fontSize=11, leading=16, leftIndent=20, rightIndent=20, spaceAfter=10, fontName="Helvetica-Oblique", textColor=colors.HexColor("#555555"))
disclaimer_style = ParagraphStyle("Disclaimer", parent=styles["Normal"], fontSize=9, textColor=colors.HexColor("#999999"), spaceAfter=10, alignment=TA_CENTER)

story = []

# TITELSEITE
story.append(Spacer(1, 3*cm))
story.append(Paragraph("JUGENDAMT-MEISTERKURS", title_style))
story.append(Paragraph("Premium-Paket fuer Eltern im Konflikt", ParagraphStyle("Subtitle", parent=styles["Normal"], fontSize=14, alignment=TA_CENTER, textColor=colors.HexColor("#666666"))))
story.append(Spacer(1, 1*cm))
story.append(Paragraph("7 komplette Szenarien &middot; 50 Formulierungen &middot; Dokumentations-System &middot; Rechtliches Wissen", ParagraphStyle("Features", parent=styles["Normal"], fontSize=10, alignment=TA_CENTER, textColor=colors.HexColor("#888888"))))
story.append(Spacer(1, 2*cm))
story.append(Paragraph("Rebell mit Herz", ParagraphStyle("Brand", parent=styles["Normal"], fontSize=12, alignment=TA_CENTER, fontName="Helvetica-Bold")))
story.append(Paragraph("www.rebellsystem.com", disclaimer_style))
story.append(PageBreak())

# INHALT
story.append(Paragraph("Inhalt", heading_style))
story.append(Paragraph("<b>MODUL 1:</b> 7 Komplette Szenario-Vorlagen", body_style))
story.append(Paragraph("1. Erstkontakt Jugendamt (3 Varianten: kooperativ / neutral / bestimmt)", body_style))
story.append(Paragraph("2. Hausbesuch angekuendigt", body_style))
story.append(Paragraph("3. Vorladung zum Gespraech", body_style))
story.append(Paragraph("4. Inobhutnahme angedroht", body_style))
story.append(Paragraph("5. Unterlagen anfordern", body_style))
story.append(Paragraph("6. Fristsetzung", body_style))
story.append(Paragraph("7. Beschwerde ueber anderen Elternteil", body_style))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("<b>MODUL 2:</b> 50 Formulierungen nach Situation", body_style))
story.append(Paragraph("<b>MODUL 3:</b> Dokumentations-System", body_style))
story.append(Paragraph("<b>MODUL 4:</b> Rechtliches Wissen", body_style))
story.append(Paragraph("<b>MODUL 5:</b> Bonus-Material", body_style))
story.append(PageBreak())

# MODUL 1
story.append(Paragraph("MODUL 1: 7 KOMPLETTE SZENARIO-VORLAGEN", heading_style))
story.append(Paragraph("Jede Vorlage ist komplett ausformuliert. Platzhalter in eckigen Klammern ersetzen: [DATUM], [NAME], [KIND NAME].", body_style))
story.append(Paragraph(disclaimer_style.text, disclaimer_style))
story.append(Spacer(1, 0.3*cm))

# 1. Erstkontakt
story.append(Paragraph("1. ERSTKONTAKT JUGENDAMT", subheading_style))
story.append(Paragraph("Wenn sich das Jugendamt zum ersten Mal bei dir meldet.", body_style))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("<b>Variante A: Kooperativ</b>", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>ich habe Ihr Schreiben vom [DATUM] erhalten und danke fuer die Information. Ich bin grundsaetzlich bereit, an einer konstruktiven Loesung mitzuwirken und das Wohl meines Kindes [KIND NAME] in den Mittelpunkt zu stellen.<br/><br/>Um die Situation besser einschaetzen zu koennen, bitte ich um folgende Informationen:<br/>1. Welche konkreten Aspekte sehen Sie aktuell als klaerungsbeduerftig?<br/>2. Auf welche Informationen oder Unterlagen stuetzt sich Ihre Einschaetzung?<br/>3. Welche naechsten Schritte schlagen Sie vor?<br/><br/>Ich bin fuer ein Gespraech offen und bitte um Terminvorschlaege Ihrerseits.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Variante B: Neutral</b>", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>den Eingang Ihres Schreibens vom [DATUM] bestaetige ich hiermit. Zur sachlichen Einordnung meiner Sicht bitte ich um konkrete Informationen zu den von Ihnen angesprochenen Punkten.<br/><br/>Ich bitte um schriftliche Darlegung der aktuellen Einschaetzung sowie der vorgeschlagenen naechsten Schritte.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Variante C: Bestimmt</b>", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>ich habe Ihr Schreiben vom [DATUM] erhalten. Ich weise darauf hin, dass ich meine Rechte als Elternteil kenne und eine konstruktive Zusammenarbeit erwarte, die auf Gegenseitigkeit basiert.<br/><br/>Bevor ich Stellung nehme, bitte ich um vollstaendige Einsicht in die relevanten Unterlagen sowie eine konkrete Darlegung Ihrer Einschaetzung.<br/><br/>Ich behalte mir vor, diese Angelegenheit rechtlich pruefen zu lassen.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# 2. Hausbesuch
story.append(Paragraph("2. HAUSBESUCH ANGEKUENDIGT", subheading_style))
story.append(Paragraph("Wenn das Jugendamt unangemeldet vorbeikommen will.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>Ihre Ankuendigung eines unangemeldeten Hausbesuchs nehme ich zur Kenntnis. Ich weise darauf hin, dass ich ein Hausrecht habe und Besuche nur nach vorheriger Terminabsprache akzeptiere.<br/><br/>Ein unangemeldeter Besuch ist fuer mich nicht akzeptabel. Ich schlage vor, stattdessen einen Termin in Ihrem Buero zu vereinbaren, wo wir die Angelegenheit in angemessenem Rahmen besprechen koennen.<br/><br/>Sollte ein Hausbesuch aus Ihrer Sicht zwingend erforderlich sein, bitte ich um schriftliche Darlegung der rechtlichen Grundlage sowie des konkreten Anlasses.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# 3. Vorladung
story.append(Paragraph("3. VORLADUNG ZUM GESPR AECH", subheading_style))
story.append(Paragraph("Wenn das Jugendamt dich einbestellt.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>Ihre Einladung zum Gespraech am [DATUM] nehme ich zur Kenntnis. Ich bin bereit, an einem konstruktiven Austausch teilzunehmen, unter folgenden Voraussetzungen:<br/><br/>1. Ort: Ich bitte um Durchfuehrung in Ihrem Buero, nicht in meiner Wohnung.<br/>2. Zeit: Der vorgeschlagene Termin passt mir nicht. Ich schlage vor: [ALTERNATIVTERMIN].<br/>3. Beistand: Ich werde von [NAME DES BEISTANDS] begleitet.<br/>4. Protokoll: Ich bitte um ein schriftliches Protokoll, das mir nach dem Gespraech zur Verfuegung gestellt wird.<br/><br/>Bitte bestaetigen Sie mir diese Voraussetzungen schriftlich.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# 4. Inobhutnahme
story.append(Paragraph("4. INOBUTNAHME ANGEDROHT", subheading_style))
story.append(Paragraph("Wenn das Jugendamt mit Wegnahme des Kindes droht.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>Ihre Androhung einer Inobhutnahme nehme ich zur Kenntnis. Ich weise darauf hin, dass eine Inobhutnahme nur unter den engen Voraussetzungen des &sect; 42 SGB VIII zulaessig ist, naemlich bei akuter Gefahr fuer das Kindeswohl.<br/><br/>Eine solche akute Gefahr sehe ich nicht. Ich bin ein verantwortungsvoller Elternteil und sorge fuer das Wohl meines Kindes. Ihre Einschaetzung teile ich nicht.<br/><br/>Ich werde diese Angelegenheit rechtlich pruefen lassen und behalte mir vor, gerichtliche Schritte einzuleiten.<br/><br/>Ich fordere Sie auf, von solchen Drohungen abzusehen und stattdessen eine konstruktive Zusammenarbeit anzustreben.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# 5. Unterlagen
story.append(Paragraph("5. UNTERLAGEN ANFORDERN", subheading_style))
story.append(Paragraph("Wenn das Jugendamt Dokumente will die du nicht hast.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>Ihre Aufforderung zur Vorlage von Unterlagen vom [DATUM] habe ich erhalten.<br/><br/>Die angeforderten Unterlagen liegen mir in der geforderten Form nicht vor. Ich biete an, Ihnen stattdessen folgende Alternativen zur Verfuegung zu stellen: [ALTERNATIVE].<br/><br/>Sollten Sie weitere Dokumente benoetigen, bitte ich um konkrete Benennung, damit ich pruefen kann, ob und in welcher Form ich diese bereitstellen kann.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(Spacer(1, 0.3*cm))

# 6. Fristsetzung
story.append(Paragraph("6. FRISTSETZUNG", subheading_style))
story.append(Paragraph("Wenn das Jugendamt eine Deadline setzt.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>Ihre Fristsetzung bis zum [DATUM] nehme ich zur Kenntnis. Die gesetzte Frist kann ich nicht einhalten, weil [GRUND].<br/><br/>Ich bitte um Verlaengerung der Frist bis zum [NEUES DATUM]. Ich werde Ihnen bis dahin eine vollstaendige Stellungnahme zukommen lassen.<br/><br/>Sollte die Frist nicht verlaengert werden koennen, bitte ich um schriftliche Darlegung der rechtlichen Grundlage.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# 7. Beschwerde
story.append(Paragraph("7. BESCHWERDE UEBER ANDEREN ELTERNTEIL", subheading_style))
story.append(Paragraph("Wenn das Jugendamt einseitig informiert wird.", body_style))
story.append(Paragraph("Sehr geehrte Frau/Herr [NAME],<br/><br/>ich habe Kenntnis davon erhalten, dass [ANDERER ELTERNTEIL] Sie einseitig informiert hat. Ich bitte um Anhoerung beider Seiten, bevor Sie eine Einschaetzung vornehmen oder Massnahmen ergreifen.<br/><br/>Ich bin bereit, meine Sicht der Dinge darzulegen und bitte um einen Termin, in dem beide Elternteile gleichberechtigt zu Wort kommen.<br/><br/>Mit freundlichen Gruessen<br/>[DEIN NAME]", quote_style))
story.append(PageBreak())

# MODUL 2: 50 FORMULIERUNGEN
story.append(Paragraph("MODUL 2: 50 FORMULIERUNGEN NACH SITUATION", heading_style))
story.append(Paragraph("Organisiert nach Situation, nicht generisch. Jede Formulierung ist kontextspezifisch.", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Wenn das Jugendamt Vorwuerfe macht (10 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ich weise Ihre Vermutung zurueck, dass...",
    "Koennen Sie mir zeigen, worauf sich diese Einschaetzung stuetzt?",
    "Diese Behauptung entbehrt jeder Grundlage.",
    "Ich bitte um konkrete Beweise fuer Ihre Annahmen.",
    "Ihre Einschaetzung basiert auf unvollstaendigen Informationen.",
    "Ich bestreite die Richtigkeit Ihrer Darstellung.",
    "Es gibt eine andere Sichtweise auf die Situation, die ich darlegen moechte.",
    "Ihre Bewertung ist subjektiv und nicht nachvollziehbar.",
    "Ich fordere Sie auf, von solchen Unterstellungen abzusehen.",
    "Lassen Sie uns bei den Fakten bleiben, nicht bei Vermutungen."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Wenn du Zeit brauchst (5 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ich benoetige mehr Zeit, um die Unterlagen zusammenzustellen.",
    "Die gesetzte Frist kann ich nicht einhalten. Ich bitte um Verlaengerung bis [DATUM].",
    "Ich werde mich bis zum [DATUM] bei Ihnen melden.",
    "Bitte geben Sie mir bis zum [DATUM] Zeit fuer eine Stellungnahme.",
    "Aufgrund der Komplexitaet der Angelegenheit benoetige ich mehr Bearbeitungszeit."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(PageBreak())

story.append(Paragraph("<b>Wenn du einen Anwalt einschalten willst (5 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ich werde diese Angelegenheit rechtlich pruefen lassen.",
    "Ich habe bereits einen Fachanwalt fuer Familienrecht konsultiert.",
    "Weitere Kommunikation erfolgt ueber meinen Anwalt [NAME].",
    "Ich behalte mir vor, gerichtliche Schritte einzuleiten.",
    "Ich werde mich anwaltlich beraten lassen, bevor ich Stellung nehme."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Wenn du kooperieren willst aber Grenzen hast (10 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ich bin bereit mitzuarbeiten, aber nur unter folgenden Bedingungen...",
    "Ich unterstuetze eine konstruktive Loesung, erwarte aber Fairness.",
    "Ich komme gerne zum Gespraech, aber nur mit Beistand.",
    "Ich bin gespraechsbereit, aber nicht zu den von Ihnen diktierten Bedingungen.",
    "Ich arbeite mit, aber erwarte Gegenseitigkeit.",
    "Ich bin kooperativ, aber nicht bedingungslos.",
    "Ich biete Zusammenarbeit an, aber auf Augenhoehe.",
    "Ich bin offen fuer Loesungen, aber nicht fuer Einseitigkeit.",
    "Ich unterstuetze das Wohl des Kindes, aber nicht Ihre Methode.",
    "Ich bin kompromissbereit, aber nicht bei Grundrechten."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(PageBreak())

story.append(Paragraph("<b>Wenn das Jugendamt Fehler macht (10 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ihr Schreiben enthält unzutreffende Angaben. Richtig ist...",
    "Ihre Darstellung ist unvollstaendig. Folgende Fakten fehlen...",
    "Sie haben den Sachverhalt falsch dargestellt. Tatsaechlich...",
    "Ihre Annahme basiert auf einem Irrtum. Die Realitaet ist...",
    "Ich korrigiere Ihre fehlerhafte Darstellung wie folgt...",
    "Ihre Einschaetzung ist nicht nachvollziehbar, weil...",
    "Sie ignorieren wesentliche Aspekte der Situation.",
    "Ihre Bewertung ist einseitig und beruecksichtigt nicht...",
    "Ich widerspreche Ihrer Darstellung in allen Punkten.",
    "Ihre Argumentation ist widerspruechlich. Sie sagen X, aber..."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Wenn du Dokumente anforderst (5 Saetze):</b>", body_style))
for i, f in enumerate([
    "Ich bitte um Einsicht in die Akte gemaess &sect; 62 SGB VIII.",
    "Ich fordere Sie auf, mir alle relevanten Unterlagen zur Verfuegung zu stellen.",
    "Bitte senden Sie mir Kopien aller Schreiben und Berichte.",
    "Ich beantrage Akteneinsicht innerhalb von 14 Tagen.",
    "Ich bitte um vollstaendige Offenlegung der Entscheidungsgrundlagen."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(PageBreak())

story.append(Paragraph("<b>Wenn du einen Termin verschieben musst (5 Saetze):</b>", body_style))
for i, f in enumerate([
    "Der vorgeschlagene Termin passt mir nicht. Ich schlage vor...",
    "Ich muss den Termin leider absagen. Bitte um neuen Vorschlag.",
    "Aufgrund eines wichtigen Termins kann ich nicht kommen. Alternative:",
    "Ich bitte um Verlegung des Termins auf einen spaeteren Zeitpunkt.",
    "Der Termin ist fuer mich nicht machbar. Ich schlage folgende Alternativen vor..."
], 1):
    story.append(Paragraph(f"{i}. &quot;{f}&quot;", body_style))
story.append(Spacer(1, 0.5*cm))

# MODUL 3: DOKUMENTATION
story.append(Paragraph("MODUL 3: DOKUMENTATIONS-SYSTEM", heading_style))
story.append(Paragraph("Erfasse jeden Kontakt, jede Frist, jedes Dokument. So behaeltst du die Kontrolle.", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Gespraechs-Logbuch:</b>", body_style))
story.append(Paragraph("Datum: ___ | Wer: ___ | Was wurde gesagt: ___ | Was wurde vereinbart: ___ | Fristen: ___", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Timeline-Template:</b>", body_style))
story.append(Paragraph("Chronologie aufbauen: Wer hat wann was gemacht? Luecken dokumentieren.", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Beweis-Checkliste:</b>", body_style))
story.append(Paragraph("&bull; Screenshots von E-Mails und Nachrichten<br/>&bull; Zeugen benennen (Name, Kontakt)<br/>&bull; Dokumente sichern (Kopien, keine Originale)<br/>&bull; Telefonate protokollieren (Datum, Dauer, Inhalt)", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Ordnerstruktur:</b>", body_style))
story.append(Paragraph("1. Korrespondenz (alle Schreiben)<br/>2. Dokumente (Urkunden, Berichte)<br/>3. Beweise (Screenshots, Fotos)<br/>4. Notizen (eigene Beobachtungen)<br/>5. Rechtliches (Anwalt, Gericht)", body_style))
story.append(PageBreak())

# MODUL 4: RECHT
story.append(Paragraph("MODUL 4: RECHTLICHES WISSEN", heading_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Was das Jugendamt darf (und was nicht):</b>", body_style))
story.append(Paragraph("&bull; Das Jugendamt darf sich melden und Informationen anfordern.<br/>&bull; Das Jugendamt darf NICHT unangemeldet vorbeikommen (Hausrecht!).<br/>&bull; Das Jugendamt darf NICHT einfach das Kind wegnehmen (nur bei akuter Gefahr, &sect; 42 SGB VIII).<br/>&bull; Das Jugendamt darf NICHT einseitig entscheiden (Eltern muessen angehoert werden!).", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Deine Rechte:</b>", body_style))
story.append(Paragraph("&bull; Recht auf Anhoerung (&sect; 62 SGB VIII)<br/>&bull; Recht auf Akteneinsicht (&sect; 62 SGB VIII)<br/>&bull; Recht auf Beistand (Anwalt, Vertrauensperson)<br/>&bull; Recht auf schriftliche Bescheide<br/>&bull; Recht auf Widerspruch und Klage", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>5 Mythen entlarvt:</b>", body_style))
story.append(Paragraph("1. &quot;Das Jugendamt kann mein Kind einfach wegnehmen&quot; &rarr; Falsch. Nur bei akuter Gefahr und nur voruebergehend.<br/>2. &quot;Ich muss allem zustimmen&quot; &rarr; Falsch. Du hast ein Widerspruchsrecht.<br/>3. &quot;Ich muss unangemeldete Besuche akzeptieren&quot; &rarr; Falsch. Du hast Hausrecht.<br/>4. &quot;Das Jugendamt entscheidet ueber mein Kind&quot; &rarr; Falsch. Eltern haben das Sorgerecht.<br/>5. &quot;Ich brauche keinen Anwalt&quot; &rarr; Falsch. Bei ernsthaften Konflikten ist anwaltliche Beratung essenziell.", body_style))
story.append(PageBreak())

# MODUL 5: BONUS
story.append(Paragraph("MODUL 5: BONUS-MATERIAL", heading_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Checkliste &quot;Erste 24 Stunden&quot;:</b>", body_style))
story.append(Paragraph("1. Ruhe bewahren. Nicht emotional reagieren.<br/>2. Schreiben genau lesen. Was wird gefordert? Welche Frist?<br/>3. Dokumente sichern. Kopien machen, Originale aufbewahren.<br/>4. Notizen machen. Was ist passiert? Wer war beteiligt?<br/>5. Anwalt kontaktieren. Bevor du antwortest, rechtliche Beratung holen.<br/>6. Antwort vorbereiten. Mit Vorlage aus diesem Kurs.<br/>7. Antwort senden. Fristgerecht, sachlich, dokumentiert.", body_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>10 Fragen die du IMMER stellen solltest:</b>", body_style))
fragen = [
    "Worauf stuetzt sich Ihre Einschaetzung?",
    "Welche konkreten Schritte schlagen Sie vor?",
    "Welche Fristen gelten?",
    "Kann ich einen Beistand mitbringen?",
    "Bekomme ich ein Protokoll des Gespraechs?",
    "Welche Unterlagen benoetigen Sie von mir?",
    "Koennen wir einen alternativen Termin vereinbaren?",
    "Wer ist mein Ansprechpartner fuer weitere Fragen?",
    "Wie kann ich mich beschweren wenn ich nicht einverstanden bin?",
    "Welche rechtlichen Grundlagen hat Ihre Entscheidung?"
]
for i, f in enumerate(fragen, 1):
    story.append(Paragraph(f"{i}. {f}", body_style))
story.append(Spacer(1, 0.5*cm))

# ABSCHLUSS
story.append(Paragraph("Abschlusshinweis", heading_style))
story.append(Paragraph("Dieses Paket gibt dir Werkzeuge an die Hand, um selbstbewusst und sachlich mit dem Jugendamt zu kommunizieren. Es ersetzt keine anwaltliche Beratung. Bei ernsthaften Konflikten, laufenden Gerichtsverfahren oder akuten Krisen: Sofort einen Fachanwalt fuer Familienrecht konsultieren.", body_style))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Rebell mit Herz &middot; www.rebellsystem.com", disclaimer_style))
story.append(Paragraph("Keine Rechtsberatung und keine Pruefung deines Einzelfalls.", disclaimer_style))

doc.build(story)
print(f"PDF erstellt: {pdf_path}")
