# Website „Nachbarschaftshilfe Preungesheim“ – Übergabe an Claude Code

Repo-Vorschlag: `nachbarschaftshilfe-preungesheim`
(Alternativen: `nh-preungesheim-web`, `nachbarschaftshilfe-ffm-nord`)
Hosting: GitHub Pages (Konto intelligentresponder-max), statische Seite.

## 1. Ziel der Website
Informationsseite einer **Initiative in Gründung** für ehrenamtliche Nachbarschaftshilfe für ältere,
hilfebedürftige Menschen in Frankfurt-Preungesheim. Die Seite soll:
1. **eine Fachkraft gewinnen** (Sozialpädagogik, Sozialarbeit, Heilpädagogik, Alten-/Krankenpflege, Hauswirtschaft) – wichtigstes Ziel,
2. Gründungsmitglieder und Helfende gewinnen,
3. mit belegten Informationen Vertrauen schaffen (Ortsbeirat, Stadt, Förderer, Partner).

Die Seite ist kein Buchungsportal. Hilfesuchende werden nur auf die Telefonnummer verwiesen.

## 2. Positionierung (Kernbotschaft)
„Wir ersetzen niemanden. Wir übernehmen die praktische Hilfe zu Hause, die es in Preungesheim noch nicht gibt.“
- Bestehende Angebote: Quartiersmanagement der Diakonie (Beratung, Formularhilfe, StadtRaum), Preungesheimer
  Nachbarschaftsverein (Stadtteilinfo, Feste), Frankfurter Verband (Begegnung). Praktische Alltagshilfe zu Hause
  für Ältere fehlt bisher → unsere Lücke.
- Angebot (geplant): Einkaufen, Arzt- und Behördenbegleitung, Spaziergang, Gesellschaft, Hilfe mit Post und Handy,
  kleine Handwerksarbeiten (Streichen, kleine Reparaturen; keine Strom-/Gas-/Wasserinstallation).
- Ziel: Anerkennung als Angebot zur Unterstützung im Alltag (§ 45a SGB XI, Hessische Pflegeunterstützungsverordnung),
  damit Pflegebedürftige über den Entlastungsbetrag (131 €/Monat) zahlen können. Handwerk ist davon ausgenommen.

## 3. Seitenstruktur
| Seite | Inhalt |
| --- | --- |
| `index.html` – Start | Wer wir sind, was wir vorhaben, Status „in Gründung“, drei Buttons: Fachkraft gesucht · Mitmachen · Kontakt |
| `fachkraft.html` – Fachkraft gesucht | **Wichtigste Seite.** Aufgabe: Anleitung der Helfenden, Teambesprechungen (ca. alle 6 Wochen), Schulungsverantwortung. Umfang: wenige Stunden/Monat, ehrenamtlich oder Minijob. Passende Berufe laut Land Hessen: Altenpfleger/in, Gesundheits- und Krankenpfleger/in, Heilerziehungspfleger/in, Erzieher/in, Sozialarbeiter/in, Sozialpädagoge/-pädagogin, Gerontologe/-in, Heilpädagoge/-pädagogin; für Alltagshilfe auch Familienpfleger/in, Sozialassistent/in, Hauswirtschafter/in. Ruhestand ausdrücklich willkommen. |
| `mitmachen.html` | Gründungsmitglieder (7 nötig) und Helfende; Voraussetzungen kurz: Führungszeugnis (13 €, Befreiung möglich), Basisqualifikation (30 UE, auch online) bzw. Erste-Hilfe-Kurs, Schweigepflicht. |
| `angebot.html` | Geplante Tätigkeiten, Grenzen (keine Pflege, kein großes Handwerk), Hinweis Entlastungsbetrag „nach Anerkennung“. |
| `blog/` | Beiträge (siehe Abschnitt 4), Übersicht `blog/index.html`. |
| `partner.html` | Bestehende Angebote im Stadtteil mit Link (nur Organisationen, keine privaten Telefonnummern Dritter). |
| `kontakt.html` | E-Mail und Telefonnummer der Initiative, **kein** Formular mit Gesundheitsangaben. |
| `impressum.html`, `datenschutz.html` | Pflicht. Platzhalter `[NAME]`, `[ADRESSE]`, `[E-MAIL]` bis zur Gründung. |

## 4. Blogbeiträge (Startpaket, je 400–700 Wörter, eigene Worte, Quellen am Ende)
1. **Warum Preungesheim eine Nachbarschaftshilfe braucht** – Stadtteil ~15.770 Einwohner (Ende 2024), wachsend
   durch den Frankfurter Bogen; Schätzung Bedarf (als Schätzung kennzeichnen).
2. **Was ist der Entlastungsbetrag?** – 131 €/Monat ab Pflegegrad 1, nur bei anerkannten Angeboten; Höchstsätze
   Hessen 25 €/Std. (Alltag) bzw. 30 €/Std. (Betreuung).
3. **Wie machen es andere Städte?** – Beispiele: Oberer Rheingau (Eltville), Taunusstein, Bad Nauheim (Sitz
   Landesverband Nachbarschaftshilfen Hessen), Hamburg-Wandsbek, Zeitpolster (Österreich), Zeitvorsorge St. Gallen.
4. **Was lernen wir aus der Forschung?** – IPot-Studie, Hochschule Kempten (2025): ältere Menschen bleiben beim
   Telefon, Gemeinschaft der Helfenden ist entscheidend; Projekt „NAH sein“ (IWAK, Goethe-Universität).
5. **Welche Förderung gibt es?** – § 45c SGB XI, Ortsbeiratsbudget (0,50 €/Einwohner, Projekte über Fraktionen),
   Frankfurter Programm „Aktive Nachbarschaft“, DSEE 100xDigital, Stiftungen.
6. **Wer kann Fachkraft werden – und was macht sie?** – Verlinkt auf `fachkraft.html`.
7. **Ehrenamt und Steuern** – Ehrenamtspauschale 960 €, Übungsleiterpauschale 3.300 € (laut Fachportalen ab 2026;
   „keine Steuerberatung“).

Quellen (verlinken, nicht abschreiben): pflege-in-hessen.de (FAQ Anbieter), frankfurt.de (Anerkennung § 45a),
hs-kempten.de (IPot-Abschlussbericht), iwak-frankfurt.de (NAH sein), preungesheim.net, diakonie-frankfurt-offenbach.de.

## 5. Inhaltsregeln
- Nur eigene Formulierungen; keine Texte oder Bilder von anderen Websites kopieren. Fakten mit Quelle und Stand.
- Schätzungen immer als „Schätzung“ markieren. Rechtliches mit Hinweis „keine Rechtsberatung“.
- Parteipolitisch neutral; keine Parteilogos.
- Keine Namen oder Telefonnummern Dritter ohne deren Einverständnis; Partner nur als Organisation verlinken.
- Sprache: Deutsch, einfach, große Schrift, kurze Sätze (Zielgruppe auch ältere Menschen).

## 6. Design
- Gold-Blau: Navy `#132A4E`, Blau `#1F4E91`, Gold `#B8901E`, Hintergrund `#F3F6FB`; Dark Mode mitliefern.
- Schriften: Fraunces (Überschriften), Atkinson Hyperlegible (Text), mit System-Fallback.
- Barrierefreiheit WCAG 2.1 AA, gut lesbar auf älteren Android-Geräten, mobil zuerst.

## 7. Technik
- Statisches HTML/CSS, wenig JavaScript, keine Build-Tools nötig (Arbeit oft in Termux/Android).
- Keine Tracker, kein Google Analytics, kein Facebook-Pixel, keine eingebetteten Facebook-Widgets
  (nur einfacher Link). Schriften möglichst lokal einbinden (DSGVO).
- Blog als einzelne HTML-Seiten oder Markdown + einfacher Generator – Entscheidung dokumentieren.
- `CHANGELOG.md` mit Abschnitt „Korrekturen“ führen.

## 8. Dokumentierte Korrekturen (nicht wiederholen)
- Studie heißt **IPot**, Hochschule Kempten (nicht „IPAT, Uni Augsburg“).
- Führungszeugnis: Für Ältere genügt das **einfache** Führungszeugnis; das erweiterte nur bei Minderjährigen/Menschen
  mit Behinderung. Kosten 13 €, Gebührenbefreiung nur bei gleichzeitigem Antrag.
- Entlastungsbetrag 131 € (nicht 125 €).
- Für die **Vereinsgründung** ist keine Fachkraft nötig – nur für die Anerkennung nach § 45a.

## 9. Abnahmekriterien
- [ ] Alle Seiten aus Abschnitt 3 vorhanden, Navigation auf allen Seiten gleich
- [ ] „Fachkraft gesucht“ von der Startseite mit einem Klick erreichbar
- [ ] Mindestens 3 Blogbeiträge mit Quellenliste
- [ ] Impressum/Datenschutz mit Platzhaltern, keine Tracker (prüfen mit Browser-Netzwerk-Tab)
- [ ] Lighthouse: Barrierefreiheit ≥ 95, mobil gut lesbar
- [ ] Deployment über GitHub Pages funktioniert
