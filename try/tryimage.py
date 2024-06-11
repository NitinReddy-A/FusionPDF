import fitz

doc = fitz.open(r"C:\Users\len\OneDrive\Desktop\Repo\Incident Analyzer\Document\TransitionProbabilityApproach.pdf")

for i in range(doc.page_count):
    page = doc.load_page(i)

    imageList = page.get_images()

    for index,image in enumerate(imageList):
        xref = image[0]
        base_image = doc.extract_image(xref)

        image_file = f"page{i}-image{index}.jpg"

        with open (image_file,"wb") as img_file:
            img_file.write(base_image["image"])