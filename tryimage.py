import fitz
import os

# Open the PDF document
doc = fitz.open(r"demo1.pdf")
new_pdf_path = r"new_demo1.pdf"

# Create a new PDF document
new_doc = fitz.open()

# Create a new PDF document
new_doc = fitz.open()

# Define the path to the output text file
output_file_path = r"extracted_image_with_coordinates.txt"

# Create the images directory if it doesn't exist
if not os.path.exists('images/'):
    os.mkdir('images/')

# Open the output text file in write mode
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Iterate through each page in the document
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        # Get the original page
        original_page = doc.load_page(page_index)
    
        # Create a new page with the same size as the original page
        new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)
    
        # Get the list of images on the page
        image_list = page.get_images(full=True)
    
        # Iterate through each image and save it in the images folder
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            print(xref)
            bbox = page.get_image_rects(xref)[0]  # delivers list, because one image maybe displayed multiple times
            pix = page.get_pixmap(dpi=150, clip=bbox)
            pix.save(f"images/page{page_index}-image{img_index}.jpg")
            # Save the image
            #image_file = f"images/page{page_index}-image{img_index}.jpg"
            #with open(image_file, "wb") as img_file:
            #    img_file.write(base_image["image"])
    
        # Find the image coordinates and print the location of the image aswell
        for i in range (len(image_list)):
            bbox = page.get_image_bbox(image_list[i])
            # Draw text on the new page with default font style
            new_page.insert_image(bbox, stream=open(f"images/page{page_index}-image{i}.jpg", "rb").read())
            
            # Write text with coordinates to the file
            output_file.write(f"Image {i} on page {page_index}: {bbox}")
            output_file.write("\n")
            print(f"Image {i} on page {page_index}: {bbox}")


    # Save the new PDF document
    new_doc.save(new_pdf_path)
    # Close all documents
    doc.close()
    new_doc.close()