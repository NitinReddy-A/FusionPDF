bbox = page.get_image_rects(xref)[0]  # delivers list, because one image maybe displayed multiple times
pix = page.get_pixmap(dpi=150, clip=bbox)
pix.save("interesting.png")