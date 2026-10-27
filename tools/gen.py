#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pillow"]
# ///
"""Generates every image in assets/. No network, no system fonts.

    uv run tools/gen.py

ateez.gif and mamamoo.gif are vendored, not generated here. See assets/CREDITS.md.
twice.gif and seventeen.gif are built from the logos in tools/logos/.
Do not wipe assets/ before running this.
"""

import colorsys
import math
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

import font

OUT = Path(__file__).resolve().parent.parent / "assets"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (0, 255, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 220)
YELLOW = (255, 220, 0)
ORANGE = (255, 140, 0)
VIOLET = (150, 120, 255)


def canvas(w, h, bg):
    img = Image.new("RGB", (w, h), bg)
    return img, img.load()


def save_gif(frames, name, duration):
    quantised = [f.convert("P", palette=Image.ADAPTIVE, colors=64) for f in frames]
    quantised[0].save(
        OUT / name,
        save_all=True,
        append_images=quantised[1:],
        duration=duration,
        loop=0,
        optimize=True,
    )
    print(f"  {name}  {frames[0].width}x{frames[0].height}  {len(frames)}f")


def centre(text, width, scale):
    return (width - font.measure(text, scale)[0]) // 2


def border(px, w, h, outer, inner):
    for x in range(w):
        px[x, 0] = px[x, h - 1] = outer
        px[x, 1] = px[x, h - 2] = inner
    for y in range(h):
        px[0, y] = px[w - 1, y] = outer
        px[1, y] = px[w - 2, y] = inner


def sparkle(px, w, h, seed, frame, colour, count=7):
    """Deterministic twinkles that hop between frames."""
    for i in range(count):
        n = (seed * 7919 + i * 104729 + frame * 31337) % 100003
        x, y = n % w, (n // w) % h
        if (n // 3) % 3 == frame % 3:
            px[x, y] = colour


def blinkie(text, name, bg, ink_a, ink_b, trim_a, trim_b):
    scale = 2
    tw, th = font.measure(text, scale)
    w, h = tw + 16, th + 6
    frames = []
    for f in range(2):
        img, px = canvas(w, h, bg)
        border(px, w, h, trim_a if f == 0 else trim_b, bg)
        sparkle(px, w, h, len(text), f, trim_b if f == 0 else trim_a)
        font.draw(px, text, 8, 3, ink_a if f == 0 else ink_b, scale)
        frames.append(img)
    save_gif(frames, name, 420)


def button(top, bot, name, tag, block, bg, ink):
    w, h = 88, 31
    frames = []
    for f in range(2):
        img, px = canvas(w, h, bg)
        for x in range(w):
            px[x, 0] = px[x, h - 1] = WHITE
        for y in range(h):
            px[0, y] = px[w - 1, y] = WHITE
        for x in range(1, 30):
            for y in range(1, h - 1):
                shade = 1 - (y / h) * 0.45
                px[x, y] = tuple(int(c * shade) for c in block)
        bx = 15 - font.measure(tag, 2)[0] // 2
        font.draw(px, tag, bx, 9, WHITE if f == 0 else YELLOW, 2)
        for x in range(30, 31):
            for y in range(1, h - 1):
                px[x, y] = WHITE
        font.draw(px, top, 34, 7, ink, 1)
        font.draw(px, bot, 34, 17, ink, 1)
        frames.append(img)
    save_gif(frames, name, 700)


def banner(text, name):
    scale = 3
    tw, th = font.measure(text, scale)
    w, h = tw + 40, th + 26
    frames = []
    for f in range(14):
        img, px = canvas(w, h, BLACK)
        for i in range(len(text)):
            hue = ((i / max(1, len(text))) + f / 14.0) % 1.0
            rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue, 0.75, 1.0))
            font.draw(px, text[i], 20 + i * font.ADVANCE * scale, 13, rgb, scale)
        for x in range(w):
            wave = int(2 + 2 * math.sin((x / 9.0) + f * 0.65))
            px[x, wave] = px[x, h - 1 - wave] = CYAN if f % 2 else MAGENTA
        sparkle(px, w, h, 3, f, WHITE, count=18)
        frames.append(img)
    save_gif(frames, name, 110)


def construction(name):
    w, h = 260, 34
    band_top, band_bot = 8, 27
    frames = []
    for f in range(8):
        img, px = canvas(w, h, BLACK)
        for y in range(h):
            for x in range(w):
                if band_top <= y < band_bot:
                    continue
                stripe = (x + y * 2 + f * 4) % 16
                px[x, y] = YELLOW if stripe < 8 else BLACK
        label = "under construction"
        font.draw(px, label, centre(label, w, 2), 10, YELLOW if f % 2 else WHITE, 2)
        frames.append(img)
    save_gif(frames, name, 130)


def rule(name):
    w, h = 640, 6
    frames = []
    for f in range(12):
        img, px = canvas(w, h, BLACK)
        for x in range(w):
            hue = ((x / w) * 2 + f / 12.0) % 1.0
            rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue, 0.7, 1.0))
            for y in range(h):
                px[x, y] = rgb if 1 <= y <= h - 2 else BLACK
        frames.append(img)
    save_gif(frames, name, 90)


def runs(text, scale):
    """Lit pixels of a string, merged into horizontal runs of (x, y, len)."""
    out = []
    for i, ch in enumerate(text.upper()):
        rows = font.FONT.get(ch)
        if rows is None:
            continue
        ox = i * font.ADVANCE * scale
        for ry, row in enumerate(rows):
            x = 0
            while x < font.WIDTH:
                if row[x] != "#":
                    x += 1
                    continue
                start = x
                while x < font.WIDTH and row[x] == "#":
                    x += 1
                out.append((ox + start * scale, ry * scale, (x - start) * scale))
    return out


def marquee(text, name, seconds=18):
    scale = 2
    gap = 80
    span = len(text) * font.ADVANCE * scale + gap
    w, h = 640, 26
    rects = []
    for copy in (0, 1):
        for x, y, length in runs(text, scale):
            rects.append(
                f'<rect x="{x + copy * span}" y="{y + 6}" '
                f'width="{length}" height="{scale}"/>'
            )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"
     viewBox="0 0 {w} {h}" role="img" aria-label="{text}">
  <rect width="{w}" height="{h}" fill="#000"/>
  <g fill="#00ffff" shape-rendering="crispEdges">
    <animateTransform attributeName="transform" type="translate"
      values="{w},0; {-span},0" dur="{seconds}s" repeatCount="indefinite"/>
    {"".join(rects)}
  </g>
</svg>
"""
    (OUT / name).write_text(svg)
    print(f"  {name}  {w}x{h}  {len(rects)} rects")


LOGOS = Path(__file__).resolve().parent / "logos"


def logo_blinkie(mask, text, name, colour, dim):
    w, h = 150, 20
    mark = mask.crop(mask.getbbox())
    mh = 14
    mark = mark.resize((round(mark.width * mh / mark.height), mh), Image.LANCZOS)
    mark = mark.point(lambda v: 255 if v > 110 else 0)
    tw, th = font.measure(text, 1)
    x = (w - mark.width - 6 - tw) // 2
    frames = []
    for f in range(6):
        img, px = canvas(w, h, BLACK)
        for i in range(w):
            lit = ((i + f) // 2) % 2 == 0
            px[i, 0], px[i, h - 1] = (colour, dim) if lit else (dim, colour)
        for j in range(h):
            lit = ((j + f) // 2) % 2 == 0
            px[0, j], px[w - 1, j] = (colour, dim) if lit else (dim, colour)
        sparkle(px, w, h, len(name), f, WHITE)
        img.paste(Image.new("RGB", mark.size, colour), (x, (h - mh) // 2), mark)
        font.draw(px, text, x + mark.width + 6, (h - th) // 2, WHITE)
        frames.append(img)
    save_gif(frames, name, 120)


def twice():
    alpha = Image.open(LOGOS / "twice.png").convert("RGBA").getchannel("A")
    logo_blinkie(alpha, "twice", "twice.gif", (255, 95, 162), (110, 40, 70))


def seventeen():
    grey = Image.open(LOGOS / "seventeen.jpg").convert("L").point(lambda v: 255 if v > 128 else 0)
    rows = [y for y in range(grey.height) if grey.crop((0, y, grey.width, y + 1)).getbbox()]
    gap = next(a for a, b in zip(rows, rows[1:]) if b - a > 8)
    symbol = grey.crop((0, 0, grey.width, gap + 1))
    logo_blinkie(symbol, "seventeen", "seventeen.gif", (247, 202, 201), (146, 168, 209))


BLINKIES = [
    ("nix or die", "blinkie-nix.gif", BLACK, LIME, WHITE, LIME, MAGENTA),
    ("i use fish btw", "blinkie-fish.gif", BLACK, CYAN, WHITE, CYAN, VIOLET),
    ("wine is not an emulator", "blinkie-wine.gif", BLACK, MAGENTA, WHITE, MAGENTA, ORANGE),
    ("kubernetes survivor", "blinkie-k8s.gif", BLACK, VIOLET, WHITE, VIOLET, CYAN),
    ("terminal dweller", "blinkie-term.gif", BLACK, LIME, YELLOW, LIME, YELLOW),
]

BUTTONS = [
    ("made with", "nix", "btn-nix.gif", "N", VIOLET, BLACK, CYAN),
    ("powered", "by go", "btn-go.gif", "G", CYAN, BLACK, CYAN),
    ("best in a", "terminal", "btn-term.gif", ">", LIME, BLACK, LIME),
    ("swift on", "macos", "btn-swift.gif", "S", (255, 90, 40), BLACK, YELLOW),
    ("dappy", ".lgbt", "btn-site.gif", "@", ORANGE, BLACK, YELLOW),
]


def main():
    OUT.mkdir(exist_ok=True)
    print("banner")
    banner("~*~ millia's corner ~*~", "banner.gif")
    print("marquee")
    marquee(
        "welcome to my corner of the internet  *  "
        "devsecops engineer  *  go, swift, nix, kubernetes  *  "
        "sign my guestbook  *  ",
        "marquee.svg",
    )
    twice()
    seventeen()
    print("furniture")
    construction("construction.gif")
    rule("rule.gif")


if __name__ == "__main__":
    main()
