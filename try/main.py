#Working ---> Able to sort out noisy images

import fitz  # PyMuPDF
import os
# Create the images directory if it doesn't exist
if not os.path.exists('image/'):
    os.mkdir('image/')

def get_pixmaps_in_pdf(pdf_filename):
    doc = fitz.open(pdf_filename)
    xrefs = list()
    for page_index in range(doc.page_count):
        for image in doc.get_page_images(page_index):
            #print(image[7])
            if image[7].startswith("Im"):
                xrefs.append(image[0])
            #xrefs.add(image[0])  # Add XREFs to set so duplicates are ignored
    pixmaps = [fitz.Pixmap(doc, xref) for xref in xrefs]
    doc.close()
    return pixmaps


def save_pixmaps(pixmaps):
    for i, pixmap in enumerate(pixmaps):
        pixmap.save(f'image/{i}.jpg')  # Might want to come up with a better name


pixmaps = get_pixmaps_in_pdf(r"demo.pdf")
save_pixmaps(pixmaps)