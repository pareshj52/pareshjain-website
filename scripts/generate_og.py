#!/usr/bin/env python3
"""Generate deterministic social-sharing artwork for the editorial portfolio."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT=Path(__file__).resolve().parents[1]/"og-image.png"
W,H=1200,630
image=Image.new("RGB",(W,H),"#f45636")
d=ImageDraw.Draw(image)
def font(size,bold=True):
    name="DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/"+name,size)
ink="#151515"; paper="#efebe3"; acid="#f4ff65"
for r in (175,225,275):
    d.ellipse((940-r,305-r,940+r,305+r),outline="#cb432b",width=3)
d.ellipse((885,252,996,363),fill=ink)
d.text((910,291),"PJ",font=font(32),fill=acid)
d.line((0,0,1200,0),fill=ink,width=9)
d.text((74,42),"P/J    INDEPENDENT STRATEGY & DELIVERY",font=font(18),fill=ink)
d.text((79,128),"THE WORK",font=font(116),fill=ink,stroke_width=0)
d.text((79,262),"IS THE",font=font(125),fill=paper)
d.text((76,400),"POINT.",font=font(135),fill=ink)
d.rectangle((72,580,1127,582),fill=ink)
d.text((73,595),"PARESH JAIN   /   MARKETING, DIGITAL & DELIVERY",font=font(15),fill=ink)
image.save(OUT,optimize=True)
print("Generated",OUT)
