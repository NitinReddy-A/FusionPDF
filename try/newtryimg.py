from PyPdf2 import PdfReader

def extract_img (pdf):
    with open(pdf,"rb") as f:
        reader = PdfReader(f)
        for page_num in range(0,len(reader.pages)):
            selected_page = reader.pages[page_num]
            for img_file_obj in selected_page.images:
                with open (img_file_obj.name, "wb") as out:
                    out.write(img_file_obj.data)

extract_img("demo.pdf") 