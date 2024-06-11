import PyPDF2 
from PyPDF2 import PdfReader 
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
    def process_fonts(page_resource):
        fonts = {}
        # Check if '/Resources' exists in page_resource
        if '/Resources' in page_resource:
            # Check if '/Font' exists within '/Resources'
            if '/Font' in page_resource['/Resources']:
                font_dict = page_resource['/Resources']['/Font']
                for font_name, font_obj_ref in font_dict.items():
                    # Try to resolve the font object reference
                    font_obj = font_obj_ref.getObject()
                    if font_obj is not None:
                        # Extract the BaseFont information
                        base_font = font_obj.get('/BaseFont', 'Unknown')
                        fonts[font_name] = base_font
        return fonts


    def extract_fonts(pdf_file): 
        pdf_reader = PdfReader(open(pdf_file, 'rb')) 
        font_data = {} 

        with warnings.catch_warnings(): 
            warnings.filterwarnings("ignore", category=UserWarning)
            for page_num in range(len(pdf_reader.pages)): 
                page = pdf_reader.pages[page_num]
                page_resource = page['/Resources'] 
                if '/Font' in page_resource: 
                    font_data[page_num] = process_fonts(page_resource) 

        return font_data 

    file_path = 'try/demo.pdf' 
    font_data = extract_fonts(file_path) 

    for page_num, fonts in font_data.items(): 
        print(f"Fonts on page {page_num}:") 
        for font_name, font_base in fonts.items(): 
            print(f"  {font_name}: {font_base}") 
        print() 
