# Code snippet is using the ConvertAPI Python Client: https://github.com/ConvertAPI/convertapi-python

import convertapi
from apikey import key

#Specify the doc path here
doc = 'documents/TranslatedDemo1'

key('docx', {
    'File': f'{doc}.pdf' 
}, from_format = 'pdf').save_files('documents')

key('pdf', {
    'File': f'{doc}.docx' 
}, from_format = 'docx').save_files('documents')