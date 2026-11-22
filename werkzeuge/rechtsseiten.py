"""Erzeugt impressum.html, datenschutz.html, 404.html (Kopf und Fuß aus index.html) sowie robots.txt, sitemap.xml,
llms.txt und _config.yml. Aufruf im Projektordner (über webseite/): python webseite/werkzeuge/rechtsseiten.py

ADRESSE ist die Adresse der Seite: nach dem Verbinden einer eigenen Domain hier und in index.html umstellen.
Aufbau wie ../imagiclique/webseite/werkzeuge/rechtsseiten.py."""
import io

ADRESSE = 'https://imagicoll.de/'
WURZEL = '/'                             # Pfad der Seite auf dem Server (für 404.html); eigene Domain imagicoll.de seit 18.11.2026
src = io.open('webseite/index.html', encoding='utf-8').read()


def seite(titel, inhalt, wurzel=''):
    kopf = src[src.index('<header class="kopf">'):src.index('</header>') + 9]
    fuss = src[src.index('<footer class="fuss">'):src.index('</footer>') + 9]
    ix = wurzel + 'index.html'
    kopf = kopf.replace('href="#"', 'href="%s"' % ix).replace('href="#', 'href="%s#' % ix)
    fuss = (fuss.replace('href="#"', 'href="%s"' % ix)
                .replace('href="impressum.html"', 'href="%simpressum.html"' % wurzel)
                .replace('href="datenschutz.html"', 'href="%sdatenschutz.html"' % wurzel))
    return f'''<!DOCTYPE html>
<html lang="de" data-modus="hell">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'">
<title>{titel} · Imagicoll</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{wurzel}bilder/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{wurzel}bilder/apple-touch-icon.png">
<script src="{wurzel}modus.js"></script>
<link rel="stylesheet" href="{wurzel}style.css">
</head>
<body>
{kopf}
<main id="inhalt">
  <div class="leuchten" aria-hidden="true"></div>
  <article class="breite"><div class="rechtstext">
{inhalt.strip()}
  </div></article>
</main>
{fuss}
<script src="{wurzel}app.js"></script>
<script src="{wurzel}bausteine/zauberstab.js" data-stern="#06b6d4" data-band="#67e8f9" defer></script>
</body>
</html>
'''


ADR = '''<address>
Mario Glaser<br>
Gründelparkweg 5c<br>
08371 Glauchau%s
</address>'''
MAIL = '<a href="mailto:kontakt@imagicosmos.de">kontakt@imagicosmos.de</a>'
DACH = '<a href="https://imagicosmos.de/" rel="noopener">Imagicosmos</a>'

impressum = f'''
<h1>Impressum</h1>
<p><strong>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG) und § 18 Abs. 1 Medienstaatsvertrag (MStV)</strong></p>
{ADR % ''}
<h2>Kontakt</h2>
<p>E-Mail: {MAIL}</p>
<h2>Über diese Seite</h2>
<p>Imagicoll ist ein privates Software-Projekt. Diese Seite stellt die Android-App „Fotos sichern“ vor und bietet sie zum Laden an. Imagicoll ist ein Projekt von {DACH}, einer Sammlung von Programmen, die Fotos gestalten und präsentieren.</p>
<p>„Android“ und „Google Play“ sind Marken von Google LLC. Imagicoll steht in keiner Verbindung zu Google.</p>
<h2>Haftung für die App</h2>
<p>Die App befindet sich in der Testphase und wird kostenlos und ohne Zusage bestimmter Eigenschaften angeboten. Sie ersetzt keine eigene Datensicherung: Bitte prüfe am PC, ob deine Fotos angekommen sind, bevor du sie auf dem Handy löschst.</p>
<h2>Links zu anderen Seiten</h2>
<p>Diese Seite enthält Links zu anderen Webseiten. Für deren Inhalte sind die jeweiligen Anbieter verantwortlich. Bei Hinweisen auf rechtswidrige Inhalte entferne ich den Link umgehend.</p>
'''

datenschutz = f'''
<h1>Datenschutz</h1>
<p>Kurz gesagt: Diese Webseite setzt <strong>keine Cookies</strong>, nutzt <strong>keine Statistik- oder Werbedienste</strong> und lädt <strong>keine Inhalte von fremden Servern</strong> (auch keine Schriften). Es gibt kein Kontaktformular und kein Benutzerkonto.</p>
<p>Der erste Teil gilt für den Besuch dieser Webseite. Was die <strong>App</strong> „Fotos sichern“ mit Daten macht, steht im Abschnitt <a href="#app">Die App „Fotos sichern“</a>.</p>

<h2>Verantwortlich</h2>
{ADR % ('<br>' + chr(10) + 'E-Mail: ' + MAIL)}

<h2>Bereitstellung der Seite (Hosting)</h2>
<p>Diese Seite und die Datei der App werden über <strong>GitHub Pages</strong> ausgeliefert. Anbieter ist die GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite und beim Laden der App verarbeitet GitHub technisch notwendige Daten, insbesondere deine <strong>IP-Adresse</strong>, Datum und Uhrzeit, die aufgerufene Seite und Angaben zu Browser und Betriebssystem. Das ist nötig, um die Seite auszuliefern und sie gegen Angriffe zu schützen.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und funktionierenden Webseite). Dabei können Daten in die USA übermittelt werden. GitHub ist nach dem EU-US Data Privacy Framework zertifiziert; dafür besteht ein Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO). Mehr dazu in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

<h2>Hell oder dunkel</h2>
<p>Wenn du oben rechts auf ☀/☾ klickst, merkt sich dein Browser deine Wahl („hell“ oder „dunkel“) im lokalen Speicher deines Geräts. Diese Angabe wird nicht übertragen, und du kannst sie jederzeit über die Einstellungen deines Browsers löschen. Sie wird nur gespeichert, weil du die Funktion ausdrücklich nutzt (§ 25 Abs. 2 Nr. 2 TDDDG).</p>

<h2>Kontakt per E-Mail</h2>
<p>Wenn du mir eine E-Mail schreibst, verwende ich deine Angaben nur, um deine Anfrage zu beantworten (Art. 6 Abs. 1 lit. b bzw. f DSGVO). Ich lösche sie, sobald sie dafür nicht mehr nötig sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

<h2 id="app">Die App „Fotos sichern“</h2>
<p>Die App sichert die Fotos deines Android-Handys in den Imagicoll-Katalog auf deinem eigenen PC. <strong>Es gibt kein Konto und keinen Server von Imagicoll. Ich erhalte weder deine Fotos noch sonst eine Angabe von dir.</strong> Ins Internet nimmt die App nur Verbindung auf, um nach einer neuen Version zu sehen (siehe unten).</p>

<h3>Was übertragen wird, und wohin</h3>
<p>Die App überträgt Daten nur an den Katalog auf dem PC, mit dem du sie gekoppelt hast, über dein WLAN zu Hause:</p>
<ul>
  <li><strong>Deine Fotos</strong>, unverändert, also mit allem, was im Foto steht (Aufnahmedatum, Aufnahmeort, Kamera), dazu Dateiname und Änderungsdatum.</li>
  <li><strong>Beim Koppeln</strong> den Namen, den du dem Handy gibst, und den Code, den dein PC anzeigt. Der Katalog vergibt dafür eine Kennung, mit der sich die App künftig ausweist.</li>
</ul>
<p><strong>Die Übertragung im Heimnetz ist nicht verschlüsselt.</strong> Wer in deinem eigenen WLAN mitliest, könnte Fotos und Kennung sehen. Nutze die App deshalb nur in einem WLAN, dem du vertraust.</p>

<h3>Suche nach dem Katalog</h3>
<p>Damit die Sicherung von selbst läuft, fragt die App im Hintergrund in jedem WLAN bei der gespeicherten Adresse nach, ob dort dein Katalog antwortet. Dabei schickt sie nur eine Zufallszahl, keine Fotos und nicht ihre Kennung. Erst wenn sich der Katalog damit als deiner ausgewiesen hat, schickt die App ihre Kennung und Fotos. Ist der Katalog im Heimnetz unter der gespeicherten Adresse nicht mehr zu finden, fragt die App auf dieselbe Weise die übrigen Adressen dieses Netzes ab (nur im Netz, in dem gekoppelt wurde).</p>

<h3>Frage nach einer neuen Version</h3>
<p>Höchstens einmal am Tag ruft die App die kleine Datei <code>version.json</code> von dieser Webseite ab, um zu sehen, ob es eine neuere Fassung gibt, und meldet sie dir. Dabei verarbeitet GitHub dieselben technischen Daten wie beim Aufruf dieser Seite (siehe oben „Bereitstellung der Seite“), insbesondere die IP-Adresse deines Handys. Die App sendet dabei nichts weiter, keine Fotos, keine Kennung und keine Angaben zu deinem Katalog. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse, dich auf Fehlerbehebungen hinzuweisen). Du kannst das Nachsehen in der App unter ⋮ → „Über Imagicoll“ abschalten.</p>

<h3>Was auf deinem Handy gespeichert wird</h3>
<p>Im privaten Speicher der App liegen: die Adresse deines PCs, die Kennung und der Name des Handys, deine Einstellungen, das Ergebnis der letzten Sicherung und eine Liste, welche Fotos schon gesichert sind (laufende Nummer, Größe und Änderungsdatum, keine Bilder). Diese Angaben nehmen nicht an der Cloud-Sicherung des Handys teil. Du löschst sie mit „Entkoppeln“ in der App, über die Einstellungen deines Handys (Apps → Imagicoll → Speicher) oder durch Deinstallieren.</p>

<h3>Was auf deinem PC gespeichert wird</h3>
<p>Der Katalog legt die Fotos in dem Ordner ab, den du dort gewählt hast, und merkt sich den Namen des Handys und einen Fingerabdruck der Kennung. Das alles liegt auf deinem PC und wird nicht an mich übertragen.</p>

<h3>Zugriffe, um die dich dein Handy fragt</h3>
<ul>
  <li><strong>Fotos:</strong> damit die App die Fotos lesen kann. Sie liest nur; sie löscht und ändert nichts.</li>
  <li><strong>Aufnahmeort der Fotos:</strong> damit der Aufnahmeort im Foto erhalten bleibt (Android entfernt ihn sonst beim Lesen). Der Standort deines Handys wird nicht abgefragt.</li>
</ul>
<p>Ohne Nachfrage nutzt die App das Netz (für die Verbindung zu deinem PC und für die Frage nach einer neuen Version) und darf nach einem Neustart des Handys die automatische Sicherung wieder anmelden.</p>

<h2>Deine Rechte</h2>
<p>Du hast das Recht auf</p>
<ul>
  <li>Auskunft über die gespeicherten Daten (Art. 15 DSGVO),</li>
  <li>Berichtigung (Art. 16), Löschung (Art. 17) und Einschränkung der Verarbeitung (Art. 18),</li>
  <li>Datenübertragbarkeit (Art. 20) und Widerspruch gegen die Verarbeitung (Art. 21),</li>
  <li>Beschwerde bei einer Datenschutz-Aufsichtsbehörde (Art. 77), zum Beispiel der deines Wohnorts.</li>
</ul>
<p>Für Anfragen genügt eine E-Mail an die oben genannte Adresse.</p>

<p class="leise" style="margin-top:40px">Stand: November 2026</p>
'''

nf = f'''
<h1>Seite nicht gefunden</h1>
<p>Diese Seite gibt es leider nicht (mehr). Vielleicht hilft der Weg zurück zur Startseite.</p>
<p style="margin-top:28px"><a class="knopf" href="{WURZEL}">Zur Startseite</a></p>
'''


def w(p, s):
    io.open('webseite/' + p, 'w', encoding='utf-8', newline='\n').write(s)


w('impressum.html', seite('Impressum', impressum))
w('datenschutz.html', seite('Datenschutz', datenschutz))
w('404.html', seite('Seite nicht gefunden', nf, WURZEL))
w('robots.txt', f'''# Imagicoll - reine Informationsseite ohne private Inhalte.
# Alle Suchmaschinen und KI-Dienste duerfen lesen (wie bei imagichron.de, entschieden 11.11.2026).

User-agent: *
Allow: /

Sitemap: {ADRESSE}sitemap.xml
''')
w('sitemap.xml', f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Nur Seiten, die in Suchmaschinen erscheinen sollen (Rechtstexte haben „noindex“). Bei Änderungen lastmod anpassen. -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{ADRESSE}</loc><lastmod>2026-11-17</lastmod></url>
</urlset>
''')
w('llms.txt', f'''# Imagicoll – App „Fotos sichern“

> „Fotos sichern“ ist eine Android-App von Imagicoll. Sie sichert die Fotos des Handys über das WLAN zu Hause in den Imagicoll-Katalog auf dem eigenen Windows-PC, auf Wunsch von selbst. Sprache: Deutsch.

Wichtige Fakten:

- **Braucht den Imagicoll-Katalog** auf einem Windows-PC im selben WLAN. Der Katalog ist noch in Arbeit und noch nicht öffentlich zu haben; ohne ihn kann die App nichts sichern.
- **Nur im Heimnetz:** Die App spricht nur mit dem eigenen PC. Kein Server von Imagicoll, keine Cloud, kein Konto, keine Nutzungsstatistik. Ins Internet geht nur einmal am Tag die Frage nach einer neuen Version (abschaltbar).
- **Im Original:** Fotos kommen unverändert an, mit Aufnahmedatum und Aufnahmeort.
- **Von selbst:** Android startet die Sicherung etwa alle 15 Minuten im WLAN und kurz nach jedem neuen Foto; die App muss nicht offen sein.
- **Nichts doppelt:** App und Katalog merken sich, was gesichert ist.
- **Koppeln** einmal je Handy über einen QR-Code, den der Katalog am PC zeigt.
- **Nur lesen:** Die App löscht und ändert auf dem Handy nichts.
- **Noch nicht:** Videos, iPhone, Play Store. Die Übertragung im Heimnetz ist nicht verschlüsselt.
- **System:** Android 10 oder neuer. Die App wird als Datei (APK) von der Seite geladen.
- **Kosten:** derzeit kostenlos.
- **Stand:** Testphase (November 2026).

## Seiten

- [Startseite]({ADRESSE}): Wozu, Ablauf, Datenschutz, App laden, Fragen
- [Datenschutz]({ADRESSE}datenschutz.html): Webseite und App

## Verwandt

- [Imagicosmos](https://imagicosmos.de/): das Dach über Imagicoll und seinen Geschwistern
- [Imagiclique](https://imagiclique.de/): Status-Bilder für WhatsApp aus eigenen Fotos
- [Imagichron](https://imagichron.de/): persönliche Bilder-Zeitreisen (Windows-Programm) aus derselben Familie
''')
w('_config.yml', '''# GitHub Pages (Jekyll): Die Seite besteht aus fertigen Dateien, Jekyll kopiert sie nur.
# Interne Dateien werden nicht mit veröffentlicht.
exclude:
  - README.md
  - werkzeuge
''')
print('ok')
