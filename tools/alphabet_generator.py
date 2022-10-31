"""
alphabet_generator.py
Generates the pre-generated monograms found in /assets/generated.zip
Creates a manifest file at /assets/generated.zip://manifest.txt with a list of usable files in the archive.
Creates a manifest info file at /assets/generated.zip://manifest.json which includes info about the archive.
"""
import os, io, json, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageColor

FONTPATH = os.path.abspath(
    "../py_simple_ttk/assets/fonts/Open_Sans/static/OpenSans/OpenSans-Bold.ttf"
)
# fmt: off
FONT_SIZES = [8,12,14,16,18,22,24,36,48,64,128]
# fmt: on
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&~`+-.="
with zipfile.ZipFile(
    zipfile_data := io.BytesIO(),
    "w",
    compresslevel=9,
    compression=zipfile.ZIP_DEFLATED,
) as z:

    def make_char_image(c, siz, fnt, clr):
        print(c, siz, clr)
        img = Image.new("RGBA", (siz, siz), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (halfsiz := siz / 2, halfsiz - (siz / 8) * int(c == "J")),
            c,
            fill=clr,
            font=fnt,
            anchor="mm",
        )
        img.save(img_data := io.BytesIO(), format="PNG")
        z.writestr(zipfile.ZipInfo(name := f"{c}_{siz}_{clr}.png"), img_data.getvalue())
        return name

    colors, manifest = [], []
    for color, code in ImageColor.colormap.items():
        for size in FONT_SIZES:
            font = ImageFont.truetype(FONTPATH, size)
            for char in CHARACTERS:
                manifest.append(make_char_image(char, size, font, color))
        colors.append(color)

    info = {
        "file_count": len(manifest),
        "characters": list(CHARACTERS),
        "font_sizes": FONT_SIZES,
        "colors": colors,
        "manifest": manifest,
    }
    z.writestr(zipfile.ZipInfo("manifest.txt"), "\n".join(manifest))
    z.writestr(zipfile.ZipInfo("manifest.json"), json.dumps(info, indent=4))
    info.pop("manifest")
    print(json.dumps(info, indent=4))

with open("../py_simple_ttk/assets/generated.zip", "wb+") as f:
    f.write(zipfile_data.getvalue())
