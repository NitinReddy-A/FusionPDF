import fitz

def remove_images(input_pdf):
    doc = fitz.open(input_pdf)
    #doc.extract_image()
    for page in doc:
        page.clean_contents()
        img_list = page.get_images()
        for img in img_list:
            print(img)
            xref = img[0]
            doc.extract_image(xref=xref)


remove_images("documents/demo2.pdf")