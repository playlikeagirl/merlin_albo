from PIL import Image, ImageDraw

BG = (10, 14, 12, 255)      # --bg
AMBER = (242, 180, 65, 255) # --amber

def draw_icon(size, padding_ratio, filename, maskable=False):
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)

    pad = int(size * padding_ratio)
    inner = size - 2 * pad

    # rounded square outline (glyph container)
    sq_w = inner
    sq_x0 = pad
    sq_y0 = pad
    sq_x1 = sq_x0 + sq_w
    sq_y1 = sq_y0 + sq_w
    radius = int(sq_w * 0.16)
    stroke = max(3, int(size * 0.018))
    draw.rounded_rectangle(
        [sq_x0, sq_y0, sq_x1, sq_y1],
        radius=radius,
        outline=AMBER,
        width=stroke,
    )

    # inner circle (matches the nav glyph's dot)
    cx, cy = size / 2, size / 2
    r = inner * 0.17
    draw.ellipse(
        [cx - r, cy - r, cx + r, cy + r],
        outline=AMBER,
        width=stroke,
    )

    img.save(filename, "PNG")

if __name__ == "__main__":
    import os
    os.makedirs("icons", exist_ok=True)
    draw_icon(192, 0.22, "icons/icon-192.png")
    draw_icon(512, 0.22, "icons/icon-512.png")
    draw_icon(180, 0.22, "icons/icon-180.png")
    # maskable icons need more safe-area padding (~ up to 40% total, so content sits in inner 80% safe circle)
    draw_icon(192, 0.30, "icons/icon-maskable-192.png", maskable=True)
    draw_icon(512, 0.30, "icons/icon-maskable-512.png", maskable=True)
    print("done")
