import fitz

def remove_images(input_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_image_info()
        for img in img_list:
            print(img)


remove_images("demo.pdf")