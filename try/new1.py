from PyPDF2 import PdfReader
pdfreader = PdfReader("demo.pdf")
first_page = pdfreader.pages[0]
count = 0
for image_file in first_page.images:
    with open(str(count) + image_file.name,"wb") as fp:
        fp.write(image_file.data)
        count = count + 1