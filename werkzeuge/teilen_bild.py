"""Erzeugt bilder/teilen.jpg (1200 × 630): das Vorschaubild, das beim Teilen des Links erscheint.
Aufruf im Projektordner: uv run --no-project --with pillow python webseite/werkzeuge/teilen_bild.py
Das Zeichen kommt aus ../imagicosmos/marke/png, die Schrift ist die Systemschrift von Windows (Segoe UI)."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WEBSEITE = Path(__file__).resolve().parent.parent
ZEICHEN = WEBSEITE.parent.parent / "imagicosmos" / "marke" / "png" / "imagicoll-512.png"
B, H = 1200, 630
GRUND, TEXT, AKZENT, LEISE = (238, 244, 245), (15, 20, 22), (14, 116, 144), (63, 74, 77)


def schrift(datei: str, groesse: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(Path(r"C:\Windows\Fonts") / datei), groesse)


bild = Image.new("RGB", (B, H), GRUND)
z = ImageDraw.Draw(bild)
for x in range(0, B, 64):                                    # feines Raster wie auf der Seite
    z.line([(x, 0), (x, H)], fill=(228, 235, 237))
for y in range(0, H, 64):
    z.line([(0, y), (B, y)], fill=(228, 235, 237))
z.rectangle([0, 0, B, 10], fill=AKZENT)

zeichen = Image.open(ZEICHEN).convert("RGBA").resize((330, 330), Image.LANCZOS)
bild.paste(zeichen, (B - 330 - 80, (H - 330) // 2), zeichen)

gross, klein, marke = schrift("segoeuib.ttf", 84), schrift("segoeui.ttf", 34), schrift("segoeuib.ttf", 40)
z.text((80, 70), "Imagi", font=marke, fill=TEXT)
z.text((80 + z.textlength("Imagi", font=marke), 70), "coll", font=marke, fill=AKZENT)
y = 170
for zeile, farbe in (("Handy-Fotos.", TEXT), ("Von selbst", AKZENT), ("auf deinem PC.", TEXT)):
    z.text((80, y), zeile, font=gross, fill=farbe)
    y += 100
z.text((80, y + 30), "Über das WLAN zu Hause. Ohne Cloud, ohne Konto.", font=klein, fill=LEISE)

bild.save(WEBSEITE / "bilder" / "teilen.jpg", quality=88, optimize=True)
print("ok", WEBSEITE / "bilder" / "teilen.jpg")
