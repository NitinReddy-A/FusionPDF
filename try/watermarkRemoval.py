import fitz

def remove_images(input_pdf,output_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_images()
        for img in img_list:
            print(img)
            if img[5] == 'DeviceGray':
                page.delete_image(img[0])

    doc.save(output_pdf)

remove_images("demo.pdf","output.pdf")