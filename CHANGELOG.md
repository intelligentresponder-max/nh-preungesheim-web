# Changelog

## 2026-11-12 – Erste Fassung
- Alle Seiten aus CLAUDE.md Abschnitt 3: Start, Fachkraft, Mitmachen, Angebot, Partner, Kontakt, Impressum, Datenschutz, Blog-Übersicht und 7 Startbeiträge.
- Design Gold-Blau mit Dark Mode, Skip-Link, Fokus-Rahmen, 18 px Basisschrift, kein JavaScript.

### Entscheidungen
- **Blog:** einzelne HTML-Seiten, erzeugt von `tools/build.py` (Python 3, nur Standardbibliothek). Grund: Navigation und Fußzeile stehen an einer Stelle statt in 16 Dateien. Die erzeugten Seiten sind eingecheckt, GitHub Pages braucht keinen Build.
- **Schriften:** nur lokal (`fonts/`), bis die Dateien dort liegen gilt die Systemschrift.
- **Gold nur als Zierfarbe** (Rahmen, Linien), nicht als Textfarbe: Gold `#B8901E` auf `#F3F6FB` erreicht nur etwa 2,9 : 1 und verfehlt WCAG AA (4,5 : 1). Navy und Blau bestehen deutlich.

### Offen
- Blogbeiträge haben aktuell etwa 150–250 Wörter statt der geforderten 400–700. Erweitern nur mit geprüften Quellen, nicht mit Vermutungen.
- Fakten gegen die Quellen prüfen (Stand Nov 2026): Höchstsätze 25/30 €/Std., Pauschalen 960/3.300 €, Beschreibung IPot und „NAH sein“, Budget Ortsbeirat. Beitrag „andere Städte“ hat noch keine Träger-Links.
- Platzhalter `[NAME]`, `[ADRESSE]`, `[E-MAIL]`, `[TELEFONNUMMER]` ersetzen; Impressum/Datenschutz rechtlich prüfen lassen.
- Lighthouse und Netzwerk-Tab-Prüfung (keine Fremdaufrufe) auf dem echten Gerät durchführen. Per Textsuche sind keine Fremdadressen im Code.
- GitHub Pages in den Repo-Einstellungen aktivieren (Branch `main`, Ordner `/`).
- Einwohnerzahl 15.770 (Ende 2024) mit Quelle der Stadt Frankfurt belegen.

## 2026-11-12 – Geräte-Prüfung, lokale Schriften, Ladeverhalten
Geprüft mit Chromium (390 px), hell und dunkel, alle 16 Seiten, plus Lighthouse 12 (mobil und Desktop). Das ist **noch keine** Prüfung auf einem echten Gerät.

- Kein seitliches Scrollen, 0 Fremdaufrufe, 0 Fehlerantworten auf allen 16 Seiten in beiden Modi.
- Schriften Fraunces und Atkinson liegen jetzt lokal unter `fonts/` (OFL, Lizenztexte beigelegt) und laden nachweislich.
- Lighthouse nach den Änderungen: Leistung, Barrierefreiheit, Best Practices, SEO je 100; CLS 0.
- Platzhalter `[NAME]` usw. stehen nur noch in Impressum, Datenschutz und Kontakt (bewusst).

### Fehler und Korrekturen
- **Layoutsprung (CLS 0,24) auf Blogseiten:** Die Schriften luden nach dem ersten Rendern (`font-display: swap`) und verschoben den Text. Behoben durch `preload` der beiden Hauptschriften in `tools/build.py`. **Regel:** Neue Webfonts immer mit `preload` und danach CLS messen.
- **Konsolenfehler 404 auf `/favicon.ico`:** kein Favicon vorhanden (Lighthouse: Best Practices 96). Behoben durch ein eingebettetes SVG-Favicon (keine zusätzliche Anfrage).
- **`local()` in `@font-face` entfernt:** Eine zufällig installierte Systemversion hätte die Darstellung je nach Gerät verändert und Fettdruck nur nachgebildet. Jetzt gibt es eine eigene Bold-Datei.
- **Fraunces als variable Datei:** Ohne `font-weight: 100 900` in `@font-face` würde der Browser Gewichte nachbilden. Eingetragen.

### Alternativen geprüft
- Google Fonts per Link: verworfen (Fremdaufruf an Google, Abmahnrisiko DSGVO, widerspricht „keine Tracker“).
- Fontsource-Pakete (npm) statt Download von Google: gewählt. Gleiche Dateien, OFL, versioniert, Quelle nachvollziehbar. Vor dem Einbinden die Lizenzdateien mitkopiert.
- `font-display: optional` gegen den Sprung: verworfen, weil die Schrift beim ersten Besuch auf langsamen Geräten ganz fehlen könnte. `preload` bringt Schrift und Stabilität.
- Sicherheit: Die Schriftdateien sind reine Binärdaten ohne Skript. Pakete wurden nur zum Kopieren der Dateien genutzt, nichts davon liegt im Repo außer den Dateien und Lizenzen.

### Weiterhin offen
- Test auf echtem Android-Gerät (Netzwerk-Tab, älteres Gerät).
- Bei Seiten mit Texten in anderen Alphabeten Schriftteilsatz erweitern.

## 2026-11-12 – Quellenprüfung (Suchergebnisse, Volltext war gesperrt)
Die Quellen selbst konnten nicht gelesen werden (Netzwerk der Session). Diese Funde stammen aus Suchtreffern und sind **nicht** im Volltext geprüft.

### Neue Korrekturen / Warnungen
- **Stundensätze 25 €/30 €:** nicht bestätigt. Gefunden wurde nur eine PfluV-Fassung von 2022 mit 30 € für Angebote nach § 45a Abs. 1 Satz 2 Nr. 1 und 2. Vor Veröffentlichung gegen die aktuelle Verordnung prüfen; die Zahlen im Beitrag „Entlastungsbetrag“ gelten bis dahin als ungeprüft.
- **IPot-Studie:** untersuchte die Einführung einer digitalen Plattform in einer ländlichen Nachbarschaftshilfe (Deisenhofer, Geiselhart, Wöhrle, 2025; Laufzeit 08/2023–10/2024). Befund laut Auszug: Plattform plus persönliche Vermittlung (hybrid) wirkt. „Ältere bleiben beim Telefon“ ist daraus nicht belegt. Beitrag „Forschung“ umformulieren.
- **Fachkraft:** Nach der PfluV braucht ein Angebot bei mehr als 3 Helfenden mindestens eine Fachkraft, wenn die Leitung keine ist. Das gilt nicht für Alltagsentlastung nach Nr. 3. `fachkraft.html` und Beitrag „Fachkraft“ präzisieren.
- **Erste-Hilfe-Kurs:** Hanau verlangt einen Nachweis von höchstens 3 Jahren. Ob Frankfurt dasselbe verlangt, ist offen.
- **Entlastungsbetrag:** 131 €/Monat (1.572 €/Jahr) bestätigt; Anerkennung nach Landesrecht.
- **Frankfurt:** Zuständige Stelle und Antragsformular nicht gefunden, auf frankfurt.de klären.

### Nächster Schritt
Blogbeiträge von 150–250 auf 400–700 Wörter erweitern, sobald diese Hosts erreichbar sind: www.hs-kempten.de, www.pflege-in-hessen.de, frankfurt.de, www.iwak-frankfurt.de, www.bundesgesundheitsministerium.de, rp-giessen.hessen.de, www.marburg-biedenkopf.de.

## Korrekturen
Übernommen aus CLAUDE.md Abschnitt 8, nicht wiederholen:
- Studie heißt **IPot**, Hochschule Kempten (nicht „IPAT, Uni Augsburg“).
- Führungszeugnis: einfaches genügt bei Älteren; 13 €; Gebührenbefreiung nur bei gleichzeitigem Antrag.
- Entlastungsbetrag 131 € (nicht 125 €).
- Für die Vereinsgründung ist keine Fachkraft nötig, nur für die Anerkennung nach § 45a.

Eigene Korrekturen dieser Sitzung:
- Die Befehle `git remote add … / git branch -M main / git push` wurden zuerst im Hotel-Repo `turmhotel` aufgerufen. Das hätte dessen Verlauf in dieses Repo geschoben. Stattdessen frisches Repo geklont. **Regel:** vor `remote add` immer `git remote -v` und `git log` prüfen.
