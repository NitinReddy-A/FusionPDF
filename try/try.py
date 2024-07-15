import fitz  # PyMuPDF
import os

# Define the path to the Noto Sans Kannada TTF file
noto_sans_kannada_path = r"NotoSansKannada-VariableFont_wdth,wght.ttf"

# Load the font into a buffer
with open(noto_sans_kannada_path, "rb") as font_file:
    font_buffer = font_file.read()

def add_spaces_to_text(text, space_width):
    words = text.split()
    spaced_text = f"{' ' * space_width}".join(words)
    return spaced_text

def calculate_text_width(page, text, fontsize, fontname):
    temp_page = page.parent.new_page()
    temp_page.insert_text((0, 0), text, fontsize=fontsize, fontname=fontname)
    text_width = temp_page.get_text("widths")[0][4]  # Get the width of the inserted text
    temp_page.parent.delete_page(-1)
    return text_width

def insert_text_without_overlap(page, rect, spaced_text, fontsize, space_width, fontname):
    # Split the text into words
    words = spaced_text.split(' ' * space_width)
    line_height = fontsize * 1.2  # Adjust the line height as necessary
    max_width = rect.width
    x, y = rect.x0, rect.y0
    current_line = ""
    
    for word in words:
        # Calculate the width of the current line with the new word
        test_line = f"{current_line} {word}".strip()
        word_width = calculate_text_width(page, test_line, fontsize, fontname)
        
        # Check if adding the word exceeds the max width
        if word_width <= max_width:
            # If it fits, add the word to the current line
            if current_line:
                current_line += f"{' ' * space_width}{word}"
            else:
                current_line = word
        else:
            # If it doesn't fit, insert the current line and start a new one
            if current_line:
                page.insert_text((x, y), current_line, fontsize=fontsize, fontname=fontname, color=(0, 0, 0))
                y += line_height
                current_line = word
            else:
                current_line = word
        
        # Check if y exceeds the bottom of the page
        if y + line_height > page.rect.y1:
            x = rect.x0
            y = rect.y0
            current_line = word
        
    # Insert the last line
    if current_line:
        page.insert_text((x, y), current_line, fontsize=fontsize, fontname=fontname, color=(0, 0, 0))

def clean_and_reformat_pdf(input_pdf_path, output_pdf_path, space_width=2):
    # Check if the input file exists
    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' does not exist.")
        return

    # Open the input PDF
    try:
        document = fitz.open(input_pdf_path)
    except Exception as e:
        print(f"Error opening the file: {e}")
        return

    # Register the custom font
    fontname = "NotoSansKannada"
    fontfile = document._insert_font(fontbuffer=font_buffer)

    if not fontfile:
        print(f"Error: Could not insert font '{fontname}' from '{noto_sans_kannada_path}'.")
        return

    # Iterate through each page and clean it
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        
        # Wrap contents if not already wrapped
        if not page.is_wrapped:
            page.wrap_contents()
        
        # Clean the page contents
        page.clean_contents(sanitize=True)
        
        # Get text blocks
        text_blocks = page.get_text("blocks")
        
        # Iterate through text blocks
        for block in text_blocks:
            # Extract the original text
            text = block[4]
            if not text.strip():
                continue  # Skip empty text blocks
            
            # Add spaces to text
            spaced_text = add_spaces_to_text(text, space_width)
            
            # Get the coordinates of the text block
            rect = fitz.Rect(block[:4])
            
            # Insert the modified text without overlapping
            insert_text_without_overlap(page, rect, spaced_text, block[3], space_width, fontname)

    # Save the cleaned and modified PDF to a new file
    try:
        document.save(output_pdf_path, deflate=True, garbage=3)
        print(f"Successfully cleaned, reformatted, and saved the PDF as '{output_pdf_path}'.")
    except Exception as e:
        print(f"Error saving the file: {e}")

# Specify the input and output file paths
input_pdf_path = 'translated_document.pdf'  # Replace with your translated PDF file path
output_pdf_path = 'cleaned_reformatted_translated_document.pdf'  # Replace with your desired output file path

# Clean and reformat the PDF
clean_and_reformat_pdf(input_pdf_path, output_pdf_path, space_width=2)
