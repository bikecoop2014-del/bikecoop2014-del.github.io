from PIL import Image, ImageDraw, ImageFont
S = 4
W = 512 * S
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)
c = W // 2
R = int(W * 0.492)
grad = Image.new("RGB", (W, W))
gd = ImageDraw.Draw(grad)
for i in range(W):
    t = i / (W - 1)
    if t < 0.55:
        u = t / 0.55
        col = tuple(int(a + (b - a) * u) for a, b in zip((0x34, 0xd3, 0x99), (0x05, 0x96, 0x69)))
    else:
        u = (t - 0.55) / 0.45
        col = tuple(int(a + (b - a) * u) for a, b in zip((0x05, 0x96, 0x69), (0x0f, 0x76, 0x6e)))
    gd.line([(0, i), (W, i)], fill=col)
mask = Image.new("L", (W, W), 0)
ImageDraw.Draw(mask).ellipse([c - R, c - R, c + R, c + R], fill=255)
img.paste(grad, (0, 0), mask)
Ri = int(W * 0.433)
d.ellipse([c - Ri, c - Ri, c + Ri, c + Ri], fill=(255, 255, 255))
d.ellipse([c - Ri, c - Ri, c + Ri, c + Ri], outline=(0xd1, 0xfa, 0xe5), width=int(2 * S))

em = (0x05, 0x96, 0x69)
em_dark = (0x04, 0x78, 0x57)
lw = int(7 * W / 240)
def P(x, y):
    return (x * W / 240, y * W / 240)
def circle(x, y, r, width):
    x0, y0 = P(x - r, y - r); x1, y1 = P(x + r, y + r)
    d.ellipse([x0, y0, x1, y1], outline=em, width=width)
def line(x1, y1, x2, y2):
    d.line([P(x1, y1), P(x2, y2)], fill=em, width=lw, joint="curve")
def arc(pts):
    d.line([P(x, y) for x, y in pts], fill=em, width=lw, joint="curve")

# bike
circle(80, 116, 24, lw)
circle(160, 116, 24, lw)
line(80, 116, 96, 72)     # seat stay
line(96, 72, 120, 116)    # seat tube
line(120, 116, 146, 72)   # down tube
line(146, 72, 160, 116)   # fork
line(80, 116, 120, 116)   # chain stay
line(96, 72, 146, 72)     # top tube
arc([(146, 72), (141, 66), (135, 64), (127, 64)])  # handlebar
line(82, 64, 106, 64)     # saddle
line(96, 72, 97, 64)      # seat post
bx, by = P(120, 116); r5 = 5 * W / 240
d.ellipse([bx - r5, by - r5, bx + r5, by + r5], fill=em_dark)

font_path = "/usr/share/fonts/pickle-hwp/NotoSansCJKkr-Regular.otf"
f1 = ImageFont.truetype(font_path, int(31 * W / 240))
f2 = ImageFont.truetype(font_path, int(11 * W / 240))

def center_text(baseline_y, txt, font, fill, ls=0.0):
    widths = [d.textlength(ch, font=font) for ch in txt]
    total = sum(widths) + ls * (len(txt) - 1) * W / 240
    x = c - total / 2
    for ch, w in zip(txt, widths):
        d.text((x, baseline_y * W / 240), ch, font=font, fill=fill, anchor="ls")
        x += w + ls * W / 240

center_text(188, "바이쿱", f1, em_dark)
center_text(203, "BIKE COOP", f2, (0x10, 0xb9, 0x81), ls=2.0)

out = img.resize((512, 512), Image.LANCZOS)
out.save("work_homepage/logo.png", "PNG")
print("saved")
