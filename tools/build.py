#!/usr/bin/env python3
"""Erzeugt alle HTML-Seiten (gemeinsame Navigation/Fußzeile an einer Stelle).

Aufruf im Repo-Hauptordner:  python3 tools/build.py
Optional: Die erzeugten .html-Dateien sind eingecheckt, GitHub Pages braucht
diesen Schritt NICHT. Entscheidung siehe CHANGELOG.md.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAND = "November 2026"
PH_NAME, PH_ADR, PH_MAIL, PH_TEL = "[NAME]", "[ADRESSE]", "[E-MAIL]", "[TELEFONNUMMER]"

NAV = [
    ("index.html", "Start"),
    ("fachkraft.html", "Fachkraft gesucht"),
    ("mitmachen.html", "Mitmachen"),
    ("angebot.html", "Angebot"),
    ("blog/index.html", "Blog"),
    ("partner.html", "Partner"),
    ("kontakt.html", "Kontakt"),
]


def page(path, title, desc, body, current=None):
    depth = path.count("/")
    pre = "../" * depth
    nav = "".join(
        '<li><a href="%s%s"%s>%s</a></li>'
        % (pre, href, ' aria-current="page"' if href == (current or path) else "", label)
        for href, label in NAV
    )
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} – Nachbarschaftshilfe Preungesheim</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{pre}css/style.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<header class="site-header">
<div class="wrap">
<a class="brand" href="{pre}index.html">Nachbarschaftshilfe<br><span>Preungesheim · in Gründung</span></a>
<nav aria-label="Hauptmenü"><ul>{nav}</ul></nav>
</div>
</header>
<main id="inhalt" class="wrap">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<p>Initiative in Gründung – noch kein eingetragener Verein. Stand der Angaben: {STAND}.</p>
<p><a href="{pre}impressum.html">Impressum</a> · <a href="{pre}datenschutz.html">Datenschutz</a> · <a href="{pre}kontakt.html">Kontakt</a></p>
<p class="small">Parteipolitisch neutral. Keine Rechtsberatung, keine Steuerberatung.</p>
</div>
</footer>
</body>
</html>
"""
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)


# ---------------------------------------------------------------- Seiten
page("index.html", "Start",
     "Initiative in Gründung für ehrenamtliche Nachbarschaftshilfe für ältere Menschen in Frankfurt-Preungesheim.",
     f"""
<section class="hero">
<h1>Praktische Hilfe zu Hause – für ältere Menschen in Preungesheim</h1>
<p class="lead">Wir ersetzen niemanden. Wir übernehmen die praktische Hilfe zu Hause, die es in Preungesheim noch nicht gibt.</p>
<p><span class="badge">Initiative in Gründung</span></p>
<div class="buttons">
<a class="btn btn-primary" href="fachkraft.html">Fachkraft gesucht</a>
<a class="btn" href="mitmachen.html">Mitmachen</a>
<a class="btn" href="kontakt.html">Kontakt</a>
</div>
</section>

<section>
<h2>Wer wir sind</h2>
<p>Wir sind Menschen aus dem Stadtteil. Wir bauen gerade eine ehrenamtliche Nachbarschaftshilfe auf. Wir sind noch kein Verein. Die Gründung bereiten wir vor.</p>
<h2>Was wir vorhaben</h2>
<p>Ältere Menschen sollen im Alltag Hilfe bekommen, ohne ihre Wohnung zu verlassen. Zum Beispiel:</p>
<ul>
<li>Einkaufen</li>
<li>Begleitung zum Arzt und zu Ämtern</li>
<li>Spaziergang und Gesellschaft</li>
<li>Hilfe mit Post und Handy</li>
<li>kleine Handwerksarbeiten (zum Beispiel Streichen)</li>
</ul>
<p>Mehr dazu auf der Seite <a href="angebot.html">Angebot</a>.</p>
<h2>Warum eine neue Initiative?</h2>
<p>Es gibt schon gute Angebote im Stadtteil, zum Beispiel Beratung und Begegnung. Praktische Alltagshilfe zu Hause fehlt bisher. Diese Lücke wollen wir füllen. Die bestehenden Angebote finden Sie auf der Seite <a href="partner.html">Partner</a>.</p>
</section>

<section class="callout">
<h2>Wir suchen eine Fachkraft</h2>
<p>Für die Anleitung der Helfenden suchen wir eine Fachkraft, zum Beispiel aus Sozialarbeit, Pflege oder Hauswirtschaft. Der Umfang sind wenige Stunden im Monat. Auch der Ruhestand ist willkommen.</p>
<p><a class="btn btn-primary" href="fachkraft.html">Mehr zur Fachkraft-Stelle</a></p>
</section>

<section>
<h2>Brauchen Sie Hilfe?</h2>
<p>Wir sind noch im Aufbau und können noch keine Hilfe vermitteln. Sobald es so weit ist, erreichen Sie uns nur per Telefon. Diese Seite ist kein Buchungsportal. Die Nummer steht auf der Seite <a href="kontakt.html">Kontakt</a>.</p>
</section>
""")

page("fachkraft.html", "Fachkraft gesucht",
     "Die Nachbarschaftshilfe Preungesheim sucht eine Fachkraft zur Anleitung der Helfenden – wenige Stunden im Monat.",
     f"""
<h1>Fachkraft gesucht</h1>
<p class="lead">Für eine gute Nachbarschaftshilfe brauchen Helfende eine fachliche Begleitung. Dafür suchen wir Sie.</p>

<h2>Ihre Aufgaben</h2>
<ul>
<li>Sie leiten die ehrenamtlich Helfenden an.</li>
<li>Sie führen Teambesprechungen durch, ungefähr alle 6 Wochen.</li>
<li>Sie sind verantwortlich für die Schulungen.</li>
</ul>

<h2>Wie viel Zeit?</h2>
<p>Wenige Stunden im Monat. Die Tätigkeit ist ehrenamtlich oder als Minijob möglich. Die genaue Form klären wir gemeinsam mit Ihnen.</p>

<h2>Welche Berufe passen?</h2>
<p>Das Land Hessen nennt für die Anerkennung von Angeboten zur Unterstützung im Alltag unter anderem diese Berufe:</p>
<ul>
<li>Altenpfleger/in</li>
<li>Gesundheits- und Krankenpfleger/in</li>
<li>Heilerziehungspfleger/in</li>
<li>Erzieher/in</li>
<li>Sozialarbeiter/in</li>
<li>Sozialpädagoge/-pädagogin</li>
<li>Gerontologe/-in</li>
<li>Heilpädagoge/-pädagogin</li>
</ul>
<p>Für reine Alltagshilfe gelten zusätzlich: Familienpfleger/in, Sozialassistent/in und Hauswirtschafter/in.</p>
<p><strong>Der Ruhestand ist ausdrücklich willkommen.</strong> Ihre Erfahrung zählt.</p>

<h2>Wofür brauchen wir Sie genau?</h2>
<p>Für die Gründung des Vereins ist keine Fachkraft nötig. Wir brauchen Sie für die spätere Anerkennung als Angebot zur Unterstützung im Alltag (§ 45a SGB XI). Erst mit dieser Anerkennung können Pflegebedürftige die Hilfe über den Entlastungsbetrag bezahlen. Die Anforderungen im Einzelnen legt das Land Hessen fest. Das ist keine Rechtsberatung. Bitte prüfen Sie die Quellen unten.</p>

<div class="callout">
<h2>Interesse?</h2>
<p>Schreiben Sie uns kurz oder rufen Sie an. Ein erstes Gespräch ist unverbindlich.</p>
<p><a class="btn btn-primary" href="kontakt.html">Zum Kontakt</a></p>
</div>

<h2>Quellen</h2>
<ul class="sources">
<li><a href="https://www.pflege-in-hessen.de">pflege-in-hessen.de</a> – Fragen und Antworten für Anbieter</li>
<li><a href="https://frankfurt.de">frankfurt.de</a> – Anerkennung nach § 45a SGB XI</li>
</ul>
<p class="small">Stand: {STAND}. Die Berufsliste ist hier mit eigenen Worten zusammengefasst. Maßgeblich ist die Hessische Pflegeunterstützungsverordnung.</p>
""")

page("mitmachen.html", "Mitmachen",
     "Gründungsmitglieder und Helfende gesucht: So können Sie bei der Nachbarschaftshilfe Preungesheim mitmachen.",
     f"""
<h1>Mitmachen</h1>
<p class="lead">Wir suchen Menschen, die Zeit schenken möchten. Jede Stunde hilft.</p>

<h2>Gründungsmitglieder</h2>
<p>Für einen Verein braucht es mindestens <strong>7 Gründungsmitglieder</strong>. Sie entscheiden mit, wie die Nachbarschaftshilfe aufgebaut wird. Dafür brauchen Sie keinen besonderen Beruf.</p>

<h2>Helfende</h2>
<p>Sie möchten ab und zu einem älteren Menschen im Stadtteil helfen? Das geht zum Beispiel mit Einkaufen, einem Spaziergang oder Hilfe am Handy.</p>

<h2>Was Sie mitbringen sollten</h2>
<ul>
<li><strong>Einfaches Führungszeugnis.</strong> Es kostet 13 €. Eine Befreiung von der Gebühr ist möglich, wenn sie gleichzeitig beantragt wird. Das erweiterte Führungszeugnis ist bei der Hilfe für Ältere nicht nötig.</li>
<li><strong>Basisqualifikation</strong> im Umfang von 30 Unterrichtseinheiten, auch online möglich, <strong>oder</strong> ein Erste-Hilfe-Kurs. Welche Variante gilt, klären wir mit Ihnen.</li>
<li><strong>Schweigepflicht.</strong> Was Sie bei der Hilfe erfahren, bleibt privat.</li>
</ul>
<p class="small">Stand: {STAND}. Das ist keine Rechtsberatung. Die Voraussetzungen können sich ändern.</p>

<div class="callout">
<h2>So melden Sie sich</h2>
<p>Schreiben Sie uns eine kurze E-Mail oder rufen Sie an. Bitte schicken Sie uns keine Gesundheitsangaben.</p>
<p><a class="btn btn-primary" href="kontakt.html">Zum Kontakt</a></p>
</div>
""")

page("angebot.html", "Angebot",
     "Geplante Tätigkeiten der Nachbarschaftshilfe Preungesheim und ihre Grenzen.",
     f"""
<h1>Unser geplantes Angebot</h1>
<p class="lead">Wir sind noch in Gründung. Alles hier ist <strong>geplant</strong> und noch nicht als Leistung buchbar.</p>

<h2>Das wollen wir anbieten</h2>
<ul>
<li>Einkaufen</li>
<li>Begleitung zu Ärzten und Behörden</li>
<li>Spaziergang</li>
<li>Gesellschaft, zum Beispiel Gespräche oder Vorlesen</li>
<li>Hilfe mit Post und Handy</li>
<li>kleine Handwerksarbeiten: Streichen und kleine Reparaturen</li>
</ul>

<h2>Das machen wir nicht</h2>
<ul>
<li><strong>Keine Pflege.</strong> Pflege übernehmen Pflegedienste.</li>
<li><strong>Kein großes Handwerk.</strong> Strom-, Gas- und Wasserinstallationen machen Fachbetriebe.</li>
</ul>

<h2>Wer bezahlt?</h2>
<p>Unser Ziel ist die Anerkennung als Angebot zur Unterstützung im Alltag (§ 45a SGB XI). Erst <strong>nach dieser Anerkennung</strong> können Pflegebedürftige mit Pflegegrad die Hilfe über den Entlastungsbetrag bezahlen. Er beträgt 131 € im Monat. Handwerksarbeiten sind davon ausgenommen. Mehr dazu im Blog: <a href="blog/entlastungsbetrag.html">Was ist der Entlastungsbetrag?</a></p>
<p class="small">Das ist keine Rechtsberatung. Stand: {STAND}.</p>

<h2>Hilfe anfragen</h2>
<p>Nur per Telefon, sobald wir starten. Siehe <a href="kontakt.html">Kontakt</a>.</p>
""")

page("partner.html", "Partner",
     "Bestehende Angebote für ältere Menschen in Frankfurt-Preungesheim – wir verlinken auf Organisationen.",
     f"""
<h1>Partner und bestehende Angebote</h1>
<p class="lead">Wir ersetzen niemanden. Wir wollen mit den Angeboten im Stadtteil zusammenarbeiten.</p>
<p>Wir nennen hier nur Organisationen, keine Privatpersonen. Die Einträge sind Stand {STAND}. Die Organisationen wissen von dieser Seite nicht unbedingt: Es ist kein Zeichen einer Zusammenarbeit, solange wir das nicht ausdrücklich schreiben.</p>

<div class="cards">
<article class="card">
<h2>Quartiersmanagement der Diakonie</h2>
<p>Beratung, Hilfe bei Formularen und der StadtRaum.</p>
<p><a href="https://www.diakonie-frankfurt-offenbach.de">diakonie-frankfurt-offenbach.de</a></p>
</article>
<article class="card">
<h2>Preungesheimer Nachbarschaftsverein</h2>
<p>Infos zum Stadtteil und Feste.</p>
<p><a href="https://www.preungesheim.net">preungesheim.net</a></p>
</article>
<article class="card">
<h2>Frankfurter Verband</h2>
<p>Begegnung und Angebote für Ältere.</p>
<p><a href="https://www.frankfurter-verband.de">frankfurter-verband.de</a></p>
</article>
</div>

<h2>Unsere Lücke</h2>
<p>Praktische Alltagshilfe zu Hause für Ältere fehlt in Preungesheim bisher. Genau dafür gründen wir die Nachbarschaftshilfe.</p>
""")

page("kontakt.html", "Kontakt",
     "Kontakt zur Initiative Nachbarschaftshilfe Preungesheim per E-Mail und Telefon.",
     f"""
<h1>Kontakt</h1>
<p class="lead">Sie erreichen uns per E-Mail und Telefon.</p>

<div class="card">
<p><strong>E-Mail:</strong> {PH_MAIL}</p>
<p><strong>Telefon:</strong> {PH_TEL}</p>
</div>

<h2>Wofür?</h2>
<ul>
<li>Sie sind Fachkraft und möchten mehr wissen.</li>
<li>Sie möchten Gründungsmitglied oder Helfer/in werden.</li>
<li>Sie sind Organisation oder Förderer.</li>
<li>Sie suchen Hilfe: Bitte rufen Sie an. Wir sind noch im Aufbau.</li>
</ul>

<p><strong>Wichtig:</strong> Wir haben bewusst kein Formular. Bitte schicken Sie uns keine Angaben zur Gesundheit per E-Mail. Die Angaben besprechen wir, wenn nötig, am Telefon.</p>
<p class="small">Hinweis für die Betreiber: Die Platzhalter in eckigen Klammern müssen vor der Veröffentlichung ersetzt werden.</p>
""")

page("impressum.html", "Impressum",
     "Impressum der Initiative Nachbarschaftshilfe Preungesheim.",
     f"""
<h1>Impressum</h1>
<p class="small">Platzhalter bis zur Gründung – vor der Veröffentlichung ersetzen.</p>
<h2>Angaben nach § 5 DDG</h2>
<p>{PH_NAME}<br>{PH_ADR}</p>
<h2>Kontakt</h2>
<p>E-Mail: {PH_MAIL}<br>Telefon: {PH_TEL}</p>
<h2>Verantwortlich für den Inhalt</h2>
<p>{PH_NAME}, Anschrift wie oben.</p>
<h2>Haftung für Links</h2>
<p>Wir verlinken auf Seiten anderer Anbieter. Auf deren Inhalte haben wir keinen Einfluss. Verantwortlich ist jeweils der Anbieter.</p>
<h2>Hinweis</h2>
<p>Die Initiative ist in Gründung und noch kein eingetragener Verein. Inhalte zu Recht, Steuern und Förderung sind allgemeine Informationen, keine Rechts- oder Steuerberatung.</p>
""")

page("datenschutz.html", "Datenschutz",
     "Datenschutzerklärung der Website der Nachbarschaftshilfe Preungesheim.",
     f"""
<h1>Datenschutz</h1>
<p class="small">Platzhalter bis zur Gründung – vor der Veröffentlichung von einer fachkundigen Stelle prüfen lassen. Keine Rechtsberatung.</p>
<h2>Verantwortlich</h2>
<p>{PH_NAME}, {PH_ADR}, {PH_MAIL}</p>
<h2>Was diese Website nicht tut</h2>
<ul>
<li>Keine Tracker, keine Statistik-Dienste, kein Google Analytics, kein Facebook-Pixel.</li>
<li>Keine eingebetteten Inhalte von Facebook oder anderen Diensten.</li>
<li>Keine Cookies. Schriften und Dateien kommen von dieser Website selbst.</li>
<li>Kein Kontaktformular.</li>
</ul>
<h2>Hosting</h2>
<p>Die Seite wird über GitHub Pages ausgeliefert (GitHub Inc., USA). Dabei kann der Anbieter technisch notwendige Daten verarbeiten, zum Beispiel die IP-Adresse beim Aufruf. Wir haben darauf nur begrenzten Einfluss. Die Datenschutzhinweise von GitHub gelten ergänzend.</p>
<h2>Kontakt per E-Mail oder Telefon</h2>
<p>Wenn Sie uns schreiben oder anrufen, verarbeiten wir Ihre Angaben nur, um Ihre Anfrage zu beantworten. Bitte senden Sie keine Gesundheitsdaten per E-Mail.</p>
<h2>Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Außerdem können Sie sich bei einer Datenschutz-Aufsichtsbehörde beschweren. Für Hessen ist das der Hessische Beauftragte für Datenschutz und Informationsfreiheit.</p>
<h2>Links</h2>
<p>Links zu anderen Seiten sind einfache Verweise. Erst wenn Sie sie anklicken, werden Daten an den anderen Anbieter übertragen.</p>
""")

# ---------------------------------------------------------------- Blog
SRC = {
    "pih": ("pflege-in-hessen.de", "https://www.pflege-in-hessen.de"),
    "ffm": ("frankfurt.de", "https://frankfurt.de"),
    "kem": ("hs-kempten.de", "https://www.hs-kempten.de"),
    "iwak": ("iwak-frankfurt.de", "https://www.iwak-frankfurt.de"),
    "pre": ("preungesheim.net", "https://www.preungesheim.net"),
    "dia": ("diakonie-frankfurt-offenbach.de", "https://www.diakonie-frankfurt-offenbach.de"),
}

POSTS = []


def post(slug, title, teaser, body, sources, extra=""):
    POSTS.append((slug, title, teaser))
    src = "".join(
        '<li><a href="%s">%s</a>%s</li>' % (SRC[k][1], SRC[k][0], (" – " + n) if n else "")
        for k, n in sources
    )
    b = f"""
<p><a href="index.html">← Alle Beiträge</a></p>
<article>
<h1>{title}</h1>
<p class="small">Stand: {STAND}</p>
{body}
<h2>Quellen</h2>
<ul class="sources">{src}</ul>
<p class="small">Die Quellen sind verlinkt, nicht abgeschrieben. Die Texte hier sind eigene Zusammenfassungen. Bitte prüfen Sie wichtige Angaben direkt bei der Quelle. Keine Rechts- oder Steuerberatung.{extra}</p>
</article>
"""
    page("blog/%s.html" % slug, title, teaser, b, current="blog/index.html")


post("warum-preungesheim", "Warum Preungesheim eine Nachbarschaftshilfe braucht",
     "Ein wachsender Stadtteil mit älteren Menschen, denen praktische Hilfe zu Hause fehlt.",
     """
<p>Preungesheim ist ein Stadtteil im Norden von Frankfurt. Ende 2024 lebten dort etwa 15.770 Menschen. Der Stadtteil wächst, vor allem durch das Neubaugebiet Frankfurter Bogen.</p>
<h2>Was es schon gibt</h2>
<p>Im Stadtteil gibt es gute Angebote. Das Quartiersmanagement der Diakonie berät und hilft bei Formularen. Es gibt dort auch den StadtRaum als Treffpunkt. Der Preungesheimer Nachbarschaftsverein informiert über den Stadtteil und organisiert Feste. Der Frankfurter Verband bietet Begegnung.</p>
<h2>Was fehlt</h2>
<p>Nach unserem Kenntnisstand fehlt bisher ein Angebot für praktische Hilfe zu Hause. Das sind Dinge wie Einkaufen, eine Begleitung zum Arzt oder Hilfe mit der Post. Wer wenig Familie in der Nähe hat, findet dafür nicht leicht Unterstützung. Wir haben dieses Angebot nicht flächendeckend geprüft. Wenn Sie ein passendes Angebot kennen, schreiben Sie uns bitte.</p>
<h2>Wie groß ist der Bedarf?</h2>
<p><strong>Schätzung:</strong> In einem Stadtteil dieser Größe leben vermutlich einige Hundert Menschen, die im Alltag regelmäßig Unterstützung gebrauchen könnten. Das ist eine grobe Annahme von uns und keine gezählte Zahl. Wir wollen den Bedarf mit den Partnern im Stadtteil genauer erfassen.</p>
<h2>Unser Ansatz</h2>
<p>Wir wollen niemanden ersetzen. Wir wollen die vorhandenen Angebote ergänzen und mit ihnen zusammenarbeiten. Dafür brauchen wir Helfende, Gründungsmitglieder und eine Fachkraft.</p>
<p><a href="../mitmachen.html">So können Sie mitmachen</a></p>
""", [("pre", "Stadtteil-Infos"), ("dia", "Quartiersmanagement"), ("ffm", "Statistik der Stadt Frankfurt, Einwohnerzahlen")])

post("entlastungsbetrag", "Was ist der Entlastungsbetrag?",
     "131 Euro im Monat für Menschen mit Pflegegrad – und warum er nur für anerkannte Angebote gilt.",
     """
<p>Menschen mit Pflegegrad bekommen von der Pflegeversicherung einen Entlastungsbetrag. Er liegt bei <strong>131 € im Monat</strong> und gilt ab Pflegegrad 1.</p>
<h2>Wofür darf man ihn nutzen?</h2>
<p>Für Angebote, die dafür anerkannt sind. Das können zum Beispiel Betreuung und Alltagshilfe sein. Die Grundlage ist § 45a im Sozialgesetzbuch XI. In Hessen regelt die Hessische Pflegeunterstützungsverordnung die Anerkennung.</p>
<h2>Was heißt „anerkannt“?</h2>
<p>Ein Angebot muss bestimmte Bedingungen erfüllen und anerkannt werden. Dazu gehören zum Beispiel geschulte Helfende und eine fachliche Anleitung. Genau dafür suchen wir eine <a href="../fachkraft.html">Fachkraft</a>.</p>
<h2>Wie viel darf Hilfe kosten?</h2>
<p>Nach unseren Quellen gelten in Hessen Höchstsätze: bis zu 25 € pro Stunde für Alltagshilfe und bis zu 30 € pro Stunde für Betreuung. Bitte prüfen Sie die aktuellen Werte bei den Quellen, sie können sich ändern.</p>
<h2>Was gilt für uns?</h2>
<p>Wir sind noch nicht anerkannt. Deshalb können wir den Entlastungsbetrag heute noch nicht nutzen. Handwerksarbeiten sind vom Entlastungsbetrag grundsätzlich ausgenommen. Die Anerkennung ist unser Ziel.</p>
""", [("pih", "Fragen und Antworten für Anbieter"), ("ffm", "Anerkennung nach § 45a")])

post("andere-staedte", "Wie machen es andere Städte?",
     "Nachbarschaftshilfen in Hessen, Hamburg, Österreich und der Schweiz als Anregung.",
     """
<p>Nachbarschaftshilfe ist keine neue Idee. In vielen Orten gibt es sie schon. Wir schauen uns an, was dort gut funktioniert.</p>
<h2>Beispiele aus Hessen</h2>
<p>Im Oberen Rheingau (Eltville) und in Taunusstein gibt es Nachbarschaftshilfen, die Hilfe im Alltag vermitteln. In Bad Nauheim sitzt der Landesverband der Nachbarschaftshilfen Hessen. Dort können Initiativen Rat und Austausch finden.</p>
<h2>Andere Regionen</h2>
<p>In Hamburg-Wandsbek gibt es eine Nachbarschaftshilfe im Stadtteil. Das Modell Zeitpolster in Österreich und die Zeitvorsorge in St. Gallen (Schweiz) arbeiten mit einem anderen Gedanken: Helfende sammeln Zeit, die ihnen später selbst zugutekommt.</p>
<h2>Was wir daraus mitnehmen</h2>
<ul>
<li>Der Stadtteil ist die richtige Größe: Man kennt sich.</li>
<li>Eine feste Ansprechperson am Telefon schafft Vertrauen.</li>
<li>Helfende brauchen Schulung und Austausch.</li>
<li>Der Landesverband kann beim Aufbau helfen.</li>
</ul>
<p class="small">Wir nennen die Beispiele hier als Anregung. Wir haben sie nicht im Einzelnen geprüft. Details finden Sie auf den Seiten der jeweiligen Träger. Wir können nicht beurteilen, ob sich die Modelle auf Preungesheim übertragen lassen.</p>
<p>Auch ein Blick in die Forschung lohnt sich: <a href="forschung.html">Was lernen wir aus der Forschung?</a></p>
""", [("pih", "Hinweise zu Angeboten in Hessen")], extra=" Weitere Träger-Links ergänzen wir nach Prüfung.")

post("forschung", "Was lernen wir aus der Forschung?",
     "Die IPot-Studie der Hochschule Kempten und das Projekt „NAH sein“ geben Hinweise für gute Nachbarschaftshilfe.",
     """
<p>Zur Frage, wie Hilfe für Ältere gelingt, gibt es Forschung. Zwei Projekte sind für uns wichtig.</p>
<h2>Die IPot-Studie</h2>
<p>Die Studie <strong>IPot</strong> kommt von der Hochschule Kempten und wurde 2025 abgeschlossen. Sie zeigt nach unserem Verständnis zwei Dinge:</p>
<ul>
<li>Ältere Menschen bleiben beim Telefon. Der Erstkontakt per Telefon passt besser als Apps oder Online-Formulare.</li>
<li>Die Gemeinschaft der Helfenden ist entscheidend. Wo Helfende sich verbunden fühlen, bleiben sie länger dabei.</li>
</ul>
<h2>Das Projekt „NAH sein“</h2>
<p>„NAH sein“ wird vom IWAK an der Goethe-Universität Frankfurt begleitet. Es beschäftigt sich mit Nachbarschaftshilfe. Genaue Ergebnisse haben wir hier nicht zusammengefasst. Bitte lesen Sie sie bei der Quelle nach.</p>
<h2>Was wir daraus machen</h2>
<ul>
<li>Hilfesuchende erreichen uns per Telefon, nicht über ein Portal.</li>
<li>Wir planen regelmäßige Teambesprechungen, ungefähr alle 6 Wochen.</li>
<li>Wir wollen, dass sich Helfende kennenlernen.</li>
</ul>
<p class="small">Das ist unsere eigene Zusammenfassung. Für genaue Aussagen lesen Sie bitte die Berichte bei den Quellen.</p>
""", [("kem", "IPot-Abschlussbericht"), ("iwak", "Projekt „NAH sein“")])

post("foerderung", "Welche Förderung gibt es?",
     "Mögliche Geldquellen für eine neue Nachbarschaftshilfe: Pflegekasse, Ortsbeirat, Stadt und Stiftungen.",
     """
<p>Eine Initiative braucht auch Geld, zum Beispiel für Schulungen, Versicherung und Auslagen. Wir haben mögliche Quellen gesammelt. Ob wir sie bekommen, ist offen.</p>
<h2>Förderung nach § 45c SGB XI</h2>
<p>Die Pflegeversicherung kann den Aufbau von Angeboten zur Unterstützung im Alltag fördern. Die Bedingungen und Antragswege regelt das Land. Wir klären das nach der Vereinsgründung.</p>
<h2>Ortsbeiratsbudget</h2>
<p>Der Ortsbeirat in Frankfurt hat ein Budget von 0,50 € je Einwohner. Projekte werden über die Fraktionen im Ortsbeirat eingebracht. Wir sprechen alle Fraktionen gleichermaßen an. Wir sind parteipolitisch neutral.</p>
<h2>Frankfurter Programm „Aktive Nachbarschaft“</h2>
<p>Die Stadt Frankfurt unterstützt Nachbarschaftsprojekte. Wir prüfen, ob unser Vorhaben passt.</p>
<h2>DSEE und Stiftungen</h2>
<p>Die Deutsche Stiftung für Engagement und Ehrenamt (DSEE) hat Programme wie 100xDigital. Auch Stiftungen fördern Ehrenamt. Wir sammeln passende Angebote.</p>
<p class="small">Alle Angaben sind Stand der Recherche und können sich ändern. Förderprogramme haben Fristen und Bedingungen. Wir geben keine Zusage und keine Rechtsberatung.</p>
""", [("pih", "Angebote zur Unterstützung im Alltag"), ("ffm", "Stadt Frankfurt")])

post("fachkraft-werden", "Wer kann Fachkraft werden – und was macht sie?",
     "Welche Berufe passen und welche Aufgaben die Fachkraft in der Nachbarschaftshilfe hat.",
     """
<p>Die Fachkraft ist wichtig für die spätere Anerkennung. Für die Gründung des Vereins ist sie <strong>nicht</strong> nötig.</p>
<h2>Aufgaben</h2>
<p>Die Fachkraft leitet die Helfenden an, führt etwa alle 6 Wochen Teambesprechungen durch und verantwortet die Schulungen. Das sind wenige Stunden im Monat. Sie ist ehrenamtlich oder als Minijob möglich.</p>
<h2>Passende Berufe</h2>
<p>Laut Land Hessen zum Beispiel Altenpflege, Gesundheits- und Krankenpflege, Heilerziehungspflege, Erziehung, Sozialarbeit, Sozialpädagogik, Gerontologie und Heilpädagogik. Für reine Alltagshilfe zusätzlich Familienpflege, Sozialassistenz und Hauswirtschaft.</p>
<h2>Auch im Ruhestand</h2>
<p>Wir freuen uns besonders über Menschen im Ruhestand. Ihre Erfahrung hilft den Helfenden.</p>
<p>Alle Details finden Sie auf der Seite <a href="../fachkraft.html">Fachkraft gesucht</a>.</p>
""", [("pih", "Fragen und Antworten für Anbieter"), ("ffm", "Anerkennung nach § 45a")])

post("ehrenamt-steuern", "Ehrenamt und Steuern",
     "Ehrenamtspauschale und Übungsleiterpauschale kurz erklärt – ohne Steuerberatung.",
     """
<p>Wer sich ehrenamtlich engagiert, bekommt manchmal eine kleine Aufwandsentschädigung. Dafür gibt es steuerliche Freibeträge.</p>
<h2>Zwei Pauschalen</h2>
<ul>
<li><strong>Ehrenamtspauschale:</strong> 960 € im Jahr.</li>
<li><strong>Übungsleiterpauschale:</strong> 3.300 € im Jahr.</li>
</ul>
<p>Diese Werte nennen Fachportale für 2026. Wir haben sie nicht amtlich geprüft.</p>
<h2>Wer bekommt welche?</h2>
<p>Die Übungsleiterpauschale gilt für bestimmte Tätigkeiten, zum Beispiel Ausbilden, Betreuen und Pflegen. Ob eine Tätigkeit dazu zählt, hängt vom Einzelfall ab. Beide Pauschalen können nicht für dieselbe Tätigkeit genutzt werden. Auch müssen Verein und Satzung bestimmte Bedingungen erfüllen.</p>
<h2>Was bedeutet das für unsere Fachkraft?</h2>
<p>Eine Vergütung ist als Ehrenamt oder Minijob möglich. Wie das steuerlich und bei Sozialversicherungen aussieht, hängt von Ihrer persönlichen Lage ab. Bitte lassen Sie sich beraten, zum Beispiel von einer Steuerberatung oder einem Lohnsteuerhilfeverein.</p>
<p><strong>Das ist keine Steuerberatung.</strong></p>
""", [("ffm", "Stadt Frankfurt, Ehrenamt")], extra=" Prüfen Sie die Beträge bitte bei einer amtlichen Quelle (Bundesfinanzministerium).")

cards = "".join(
    '<article class="card"><h2><a href="%s.html">%s</a></h2><p>%s</p></article>' % (s, t, d)
    for s, t, d in POSTS
)
page("blog/index.html", "Blog",
     "Beiträge zur Nachbarschaftshilfe in Preungesheim: Bedarf, Entlastungsbetrag, Förderung, Forschung.",
     f"""
<h1>Blog</h1>
<p class="lead">Hintergründe in einfacher Sprache, mit Quellen.</p>
<div class="cards">{cards}</div>
""")

print(len(POSTS) + 8 + 1, "Seiten erzeugt")
