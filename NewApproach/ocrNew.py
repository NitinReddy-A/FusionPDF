import requests
import os

def convert_pdf_to_word(api_key, pdf_file_path):
    # Define the API endpoint
    url = "https://api.ocr.space/parse/image"
    
    # Prepare the files and parameters for the request
    with open(pdf_file_path, 'rb') as pdf_file:
        files = {
            'file': pdf_file
        }
        data = {
            'apikey': api_key,
            'language': 'eng',  # You can change this to other supported languages
            'isOverlayRequired': False,
            'filetype': 'PDF'  # Specify the file type
        }

        # Make the API request
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            if result['IsErroredOnProcessing']:
                print("Error:", result['ErrorMessage'])
                return None
            
            # Extract the text and save it to a Word document
            text = result['ParsedResults'][0]['ParsedText']
            output_file_path = os.path.splitext(pdf_file_path)[0] + '.docx'
            
            with open(output_file_path, 'w', encoding='utf-8') as word_file:
                word_file.write(text)
            
            print(f"Converted '{pdf_file_path}' to '{output_file_path}'")
        else:
            print("Error:", response.status_code)

# Example usage
api_key = "K86228425088957"  # Your API key
pdf_file_path = r"C:\Users\Lenovo\Desktop\repo\FusionPDF\documents\scan1.pdf"  # Replace with your PDF file path
convert_pdf_to_word(api_key, pdf_file_path)