import fitz
import os

# Open the PDF document
doc = fitz.open(r"try/demo.pdf")

# Create the images directory if it doesn't exist
if not os.path.exists('images/'):
    os.mkdir('images/')

# Iterate through each page in the document
for page_index in range(doc.page_count):
    page = doc.load_page(page_index)

    # Get the list of images on the page
    image_list = page.get_images(full=True)

    # Iterate through each image and save it in the images folder
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)

        # Save the image
        image_file = f"images/page{page_index}-image{img_index}.jpg"
        with open(image_file, "wb") as img_file:
            img_file.write(base_image["image"])

    # Find the image coordinates and print the location of the image aswell
    for i in range (len(image_list)):
        bbox = page.get_image_bbox(image_list[i])
        print(f"Image {i} on page {page_index}: {bbox}")

print("Images and their coordinates have been extracted.")
