# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

import convertapi

convertapi.api_credentials = 'secret_KWmzJQRIOe8M5ueS'  

# Specify the file path here
doc = 'documents/tem'
convertapi.convert('docx', {
    'File': f'{doc}.pdf' 
}, from_format = 'pdf').save_files('documents')

# try:
#     doc = 'documents/tem'
#     convertapi.convert('pdf', {
#         'File': 'finOp.docx'
#     }, from_format='docx').save_files('documents')
# except Exception as e:
#     print("Conversion failed:", e)