import fitz

def remove_images(input_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        page.clean_contents()
        print(page)
        img_list = page.get_images()
        for img in img_list:
            if img[1] == 0:
                print(img)


remove_images("documents/demo2.pdf")