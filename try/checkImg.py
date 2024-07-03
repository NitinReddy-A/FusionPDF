import fitz

def remove_images(input_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        page.clean_contents()
        img_list = page.get_images()
        for img in img_list:
            print(img)


remove_images("documents/demo2.pdf")