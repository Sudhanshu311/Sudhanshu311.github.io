"""Generate the 1200x630 Open Graph share image for the resume.

Rendered with Pillow using system Arial (Bold/Regular) — no external deps.
Output: resume/assets/og-image.png
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets" / "og-image.png"
AVATAR = Path(__file__).resolve().parent.parent / "assets" / "images" / "Sudhanshu.jpeg"

W, H = 1200, 630

# Terminal-theme palette matching the site
BG           = (13, 17, 23)         # #0d1117
PANEL        = (22, 27, 34)         # #161b22
PANEL_HI     = (31, 38, 48)         # #1f2630
LINE         = (48, 54, 61)         # #30363d
INK          = (230, 237, 243)      # #e6edf3
INK_MUTED    = (155, 167, 180)      # #9ba7b4
INK_SUBTLE   = (110, 118, 129)      # #6e7681
GREEN        = (126, 231, 135)      # #7ee787
BLUE         = (121, 192, 255)      # #79c0ff
NIKE_ORANGE  = (255, 133, 51)       # a warm accent for the Nike pill


def font(size: int, weight: str = "regular"):
    # Prefer Arial Bold / regular on macOS
    candidates = {
        "bold":    ["/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
        "black":   ["/System/Library/Fonts/Supplemental/Arial Black.ttf"],
        "regular": ["/System/Library/Fonts/Supplemental/Arial.ttf",
                    "/System/Library/Fonts/Helvetica.ttc"],
    }.get(weight, [])
    for p in candidates:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                pass
    return ImageFont.load_default()


def circular_avatar(size: int) -> Image.Image | None:
    if not AVATAR.exists():
        return None
    img = Image.open(AVATAR).convert("RGB")
    # Cover-crop to square
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    dm = ImageDraw.Draw(mask)
    dm.ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGB", (size, size), BG)
    out.paste(img, (0, 0), mask=mask)
    # Wrap into RGBA with a mask so we can paste it cleanly
    rgba = out.convert("RGBA")
    rgba.putalpha(mask)
    return rgba


def rounded_rect(dr: ImageDraw.ImageDraw, xy, r, fill=None, outline=None, width=1):
    dr.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)

    # Subtle radial "glow" — two soft ellipses painted with alpha
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -260, 720, 640), fill=(*GREEN, 22))
    gd.ellipse((720, 200, 1560, 900),  fill=(*BLUE,  18))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    dr = ImageDraw.Draw(img)

    # Outer 12px border with terminal chrome
    rounded_rect(dr, (24, 24, W-24, H-24), r=18, outline=LINE, width=1)
    # Terminal chrome dots + title
    for i, c in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        dr.ellipse((60 + i*22, 60, 74 + i*22, 74), fill=c)
    dr.text((150, 55), "bash — ~/sudhanshu", fill=INK_SUBTLE, font=font(18, "regular"))

    # Prompt line
    dr.text((60, 115), "$", fill=GREEN, font=font(22, "bold"))
    dr.text((88, 115), "whoami", fill=INK, font=font(22, "bold"))

    # Avatar (circular) — left side
    av = circular_avatar(180)
    if av is not None:
        # Nice accent ring behind
        dr.ellipse((50-6, 175-6, 50+180+6, 175+180+6), outline=GREEN, width=3)
        img.paste(av, (50, 175), av)
    dr = ImageDraw.Draw(img)

    # Name
    dr.text((260, 180), "Sudhanshu Bhatnagar", fill=INK, font=font(56, "black"))
    # Title
    dr.text((260, 254), "Principal Technical Program Manager", fill=GREEN, font=font(28, "bold"))

    # "Currently @ Nike" pill
    pill_x, pill_y = 260, 306
    pill_text = "Currently @ Nike · Global Merchandising · Beaverton, OR"
    tw = dr.textlength(pill_text, font=font(20, "bold"))
    rounded_rect(dr, (pill_x, pill_y, pill_x + tw + 40, pill_y + 42),
                 r=999, fill=(20, 40, 30), outline=GREEN, width=1)
    dr.ellipse((pill_x + 14, pill_y + 15, pill_x + 26, pill_y + 27), fill=GREEN)
    dr.text((pill_x + 34, pill_y + 8), pill_text, fill=INK, font=font(20, "bold"))

    # Metric strip — 4 large numbers across the bottom
    metrics = [
        ("22+",    "years"),
        ("1000+",  "global stores"),
        ("8",      "countries"),
        ("$40M",   "saved · Amazon B2B"),
        ("99.99%", "availability"),
    ]
    strip_top = 420
    strip_h = 130
    cell_w = (W - 100) // len(metrics)
    for i, (num, lbl) in enumerate(metrics):
        cx = 50 + i * cell_w + cell_w // 2
        # Number
        f_num = font(56, "black")
        num_w = dr.textlength(num, font=f_num)
        dr.text((cx - num_w / 2, strip_top), num, fill=GREEN, font=f_num)
        # Label
        f_lbl = font(18, "regular")
        lbl_w = dr.textlength(lbl, font=f_lbl)
        dr.text((cx - lbl_w / 2, strip_top + 74), lbl, fill=INK_MUTED, font=f_lbl)
        # Divider (except last)
        if i < len(metrics) - 1:
            dr.line((50 + (i + 1) * cell_w, strip_top + 6, 50 + (i + 1) * cell_w, strip_top + strip_h - 6),
                    fill=LINE, width=1)

    # Footer URL + prompt caret
    dr.text((60, H - 76), "→", fill=GREEN, font=font(22, "bold"))
    dr.text((90, H - 76), "sudhanshu311.github.io/resume", fill=BLUE, font=font(22, "bold"))

    dr.text((W - 340, H - 76), "22+ yrs · Nike · Lululemon · Amazon", fill=INK_SUBTLE, font=font(16, "regular"))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
