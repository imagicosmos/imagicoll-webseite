# Webseite für Imagicoll (Download-Seite der App „Fotos sichern“)

Die öffentliche Seite, die die Android-App **„Fotos sichern“** vorstellt und **zum Laden anbietet**. Aufbau,
Gestaltung und Regeln sind von `../../imagiclique/webseite` übernommen (und damit von imagichron.de); die Farben
sind das Petrol der Marke aus `../../imagicosmos/marke/`. Erstellt am 17.11.2026.

Online seit 17.11.2026, seit 18.11.2026 unter der eigenen Adresse **https://imagicoll.de/** (Datei `CNAME`; die alte Adresse https://imagicosmos.github.io/imagicoll-webseite/ leitet weiter). Erste Fassung der App dort: 0.1.29

Grundsätze wie bei den Schwesterseiten: einfaches HTML/CSS/JavaScript, **nichts von fremden Servern** (keine
Google-Schriften, keine Statistik, keine Cookies), Skripte nur aus eigenen Dateien (Content-Security-Policy im
Seitenkopf).

**Ehrlich bleiben:** Die App nützt nur mit dem Imagicoll-Katalog am PC, und der ist noch nicht öffentlich zu haben.
Das steht deutlich auf der Seite (Kasten „Wichtig“ bei „App laden“, erste Frage). Erst ändern, wenn es den Katalog
für andere gibt.

## Dateien

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Einstieg, Warum, So geht’s, Datenschutz, App laden, Fragen. Platzhalter `@@FASSUNG@@` und `@@GROESSE@@` setzt das Veröffentlichen ein |
| `impressum.html`, `datenschutz.html`, `404.html` | **erzeugt** von `werkzeuge/rechtsseiten.py`. Die Datenschutzseite hat den Abschnitt „Die App ‚Fotos sichern‘“ (`#app`): ändert sich, was die App überträgt oder speichert, dort nachziehen |
| `style.css` | gesamtes Aussehen; Farben für hell und dunkel oben als Variablen, Eigenes von Imagicoll im Abschnitt 15 |
| `app.js`, `modus.js` | Hell/Dunkel, Laufband, Einblenden |
| `bausteine/zauberstab.js` | Logo-Animation, gemeinsamer Baustein „zauberstab“ aus `../bausteine` (seit 18.11.2026; nicht von Hand ändern, neu einbauen mit `node ../bausteine/werkzeuge/einbauen.js zauberstab webseite/bausteine`). Wort und Farben liest er aus dem Logo und `style.css`, die Leuchtfarben stehen als `data-stern`/`data-band` in der Einbindung |
| `bilder/` | `favicon.svg` und `apple-touch-icon.png` aus `imagicosmos/marke/`; `teilen.jpg` (Vorschaubild beim Teilen des Links, 1200 × 630) |
| `schriften/` | Josefin Sans für den Schriftzug (SIL Open Font License, Lizenztext liegt bei) |
| `robots.txt`, `sitemap.xml`, `llms.txt`, `_config.yml` | **erzeugt** von `werkzeuge/rechtsseiten.py`; bei neuen Funktionen `llms.txt` dort mitpflegen |
| `werkzeuge/rechtsseiten.py` | erzeugt die oben genannten Dateien. Texte **im Werkzeug ändern**, nicht in den erzeugten Dateien. Aufruf im Projektordner: `python webseite/werkzeuge/rechtsseiten.py` |
| `werkzeuge/teilen_bild.py` | erzeugt `bilder/teilen.jpg` |
| `imagicoll.apk` | liegt **nicht** hier: Die App kommt erst beim Veröffentlichen aus `ausgabe/android/` dazu |

**Menü auf allen Seiten gleich:** Kopf und Fuß der Unterseiten sind Kopien aus `index.html`. Nach Änderungen am
Menü `rechtsseiten.py` ausführen.

**Fragen:** Die sichtbaren Fragen und die strukturierten Daten (JSON-LD im `<head>` von `index.html`) müssen
übereinstimmen.

## Ansehen auf dem eigenen Rechner

`webseite-veroeffentlichen.cmd --vorschau` legt die fertige Seite (mit App, Fassung und Größe) nach
`ausgabe\webseite\`, ohne etwas hochzuladen. Dort `python -m http.server 8798` starten und
http://127.0.0.1:8798/ öffnen.

## Veröffentlichen

Dieses Repository (`imagicosmos/imagicoll`) ist privat. Die Seite liegt im öffentlichen Repository
`imagicosmos/imagicoll-webseite`; GitHub Pages liefert dessen Zweig `main` aus.

1. Bei Änderungen an der App: committen, dann **`android-bauen.cmd`** (die Fassung zählt die Commits).
2. Änderungen an der Seite committen.
3. **`webseite-veroeffentlichen.cmd`** doppelklicken.

Das Skript (`tools/webseite_veroeffentlichen.py`) nimmt den committeten Stand von `webseite/`, setzt Fassung und
Größe ein, legt die zuletzt gebaute App als `imagicoll.apk` dazu und lädt alles als **einen** Commit mit neutralem
Autor hoch (Force-Push). Nichts außerhalb von `webseite/` und keine private E-Mail-Adresse gelangt dorthin. Nach
1–2 Minuten ist der neue Stand online.

Nichts direkt im öffentlichen Repository ändern: Der nächste Lauf des Skripts überschreibt es.

Das öffentliche Repository und GitHub Pages (Zweig `main`) sind seit 17.11.2026 eingerichtet.

## Wichtig zur Signatur

Angeboten wird die zuletzt gebaute Datei aus `ausgabe/android/`. **Seit 18.11.2026 (Fassung 0.1.39) ist das die
Freigabe-Fassung** mit eigenem Schlüssel: vor dem Veröffentlichen also `android-bauen.cmd --freigabe` ausführen.
Eine neue Fassung lässt sich nur über die alte installieren, wenn sie mit **demselben Schlüssel** signiert ist.
Deshalb nie wieder eine Test-Fassung hochladen (das Werkzeug warnt) und den Schlüssel gut sichern. Wer noch eine
Test-Fassung bis 0.1.38 hat, löscht die App einmal und installiert neu (danach neu koppeln; am PC geht nichts
verloren). Der Katalog bietet über den QR-Code dieselbe Freigabe-Fassung an.

**version.json** schreibt das Werkzeug passend zur hochgeladenen App. Die App sieht dort einmal am Tag nach und
meldet eine neue Fassung (Baustein `aktualisieren`).

## Noch offen

1. **Rechtstexte prüfen:** Impressum und Datenschutz sind nach dem Muster der Schwesterseiten geschrieben und nicht
   juristisch geprüft.
2. **Eigene Domain:** erledigt am 18.11.2026 (imagicoll.de, DNS bei IONOS von Mario, für die Organisation bestätigt). Die Datei `CNAME`
   muss in `webseite/` bleiben, sonst ist die Adresse nach dem nächsten Veröffentlichen weg.
3. **Bilder der App** fehlen (nur eine Zeichnung). Bildschirmfotos aus dem Emulator mit künstlichen Fotos wären gut.
4. **Dachseite:** Auf der Seite von Imagicosmos steht Imagicoll noch als „in Arbeit“ ohne Verweis hierher.
