import json
import shutil

"""
    Sample project for OCRWebService.com (REST API).
    Extract text from scanned images and PDF documents and convert into editable formats.
    Please create new account with ocrwebservice.com via http://www.ocrwebservice.com/account/signup and get license code
"""

# Provide your username and license code
LicenseCode = 'XXXX-XXXX-XXXXX-XXXXX(your license code)';
UserName =  '<your user name>';

try:
	import requests
except ImportError:
	print("You need the requests library to be installed in order to use this sample.")
	print("Run 'pip install requests' to fix it.")

	exit()


"""

        You should specify OCR settings. See full description http://www.ocrwebservice.com/service/restguide
         
        Input parameters:
         
	[language]     - Specifies the recognition language. 
	   		This parameter can contain several language names separated with commas. 
                        For example "language=english,german,spanish".
			Optional parameter. By default:english
        
	[pagerange]    - Enter page numbers and/or page ranges separated by commas. 
			For example "pagerange=1,3,5-12" or "pagerange=allpages".
                        Optional parameter. By default:allpages
         
        [tobw]	      - Convert image to black and white (recommend for color image and photo). 
			For example "tobw=false"
                        Optional parameter. By default:false
         
        [zone]         - Specifies the region on the image for zonal OCR. 
			The coordinates in pixels relative to the left top corner in the following format: top:left:height:width. 
			This parameter can contain several zones separated with commas. 
		        For example "zone=0:0:100:100,50:50:50:50"
                        Optional parameter.
          
        [outputformat] - Specifies the output file format.
                        Can be specified up to two output formats, separated with commas.
			For example "outputformat=pdf,txt"
                        Optional parameter. By default:doc

        [gettext]	- Specifies that extracted text will be returned.
			For example "tobw=true"
                        Optional parameter. By default:false
        
        [description]  - Specifies your task description. Will be returned in response.
                        Optional parameter. 


	!!!!  For getting result you must specify "gettext" or "outputformat" !!!!  

"""

# Build your OCR:

# Extract text with English language by default
RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?gettext=true";

# Extract text with English and german language using zonal OCR
#RequestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=english,german&zone=0:0:600:400,500:1000:150:400';

# Convert first 5 pages of multipage document into doc and txt
# RequestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=english&pagerange=1-5&outputformat=doc,txt';

#Full path to uploaded document
FilePath = "C:\\test_image.jpg"

with open(FilePath, 'rb') as image_file:
    image_data = image_file.read()
    
r = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))

if r.status_code == 401:
    #Please provide valid username and license code
    print("Unauthorized request")
    exit()

# Decode Output response
jobj = json.loads(r.content)

ocrError = str(jobj["ErrorMessage"])

if ocrError != '':
        #Error occurs during recognition
        print ("Recognition Error: " + ocrError)
        exit()


# Task description
print("Task Description:" + str(jobj["TaskDescription"]))

# Available pages 
print("Available Pages:" + str(jobj["AvailablePages"]))

# Processed pages 
print("Processed Pages:" + str(jobj["ProcessedPages"]))

# For zonal or multipage OCR: OCRText[z][p]    z - zone, p - pages

# Extracted text from first or single page
print("Extracted Text:" + str(jobj["OCRText"][0][0]))

# Extracted text from second page (if multipage doc converted)
#print("Extracted Text:" + str(jobj["OCRText"][0][1]))

# Get extracted text from First zone for each page
print("Zone 1 Page 1 Text:" + str(jobj["OCRText"][0][0]))
print("Zone 1 Page 2 Text:" + str(jobj["OCRText"][0][1]))

# Get extracted text from Second zone for each page
#print("Zone 2 Page 1 Text:" + str(jobj["OCRText"][1][0]))
#print("Zone 2 Page 2 Text:" + str(jobj["OCRText"][1][1]))

#Download output file (if outputformat was specified)
#file_response = requests.get(jobj["OutputFileUrl"], stream=True)
#with open("outputDoc.doc", 'wb') as output_file:
#   shutil.copyfileobj(file_response.raw, output_file)



