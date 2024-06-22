import fitz
file = 'demo.pdf'
pdf = fitz.open(file)
page = pdf.load_page(0)
image_list = page.get_images(full=True)
for image in image_list:
    xref = image[0]
    pix = fitz.Pixmap(pdf, xref)
    if pix.n < 5:
        pix.save(f"images/{xref}.jpg")
    else:
        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        pix1.save(f"images/{xref}.jpg")
        pix1 = None
    pix = None
print(len(image_list), 'detected')