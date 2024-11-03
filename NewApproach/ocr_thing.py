import json
import shutil
import requests

# Provide your username and license code
LicenseCode = '7132C263-625C-4CF9-A82C-8DE8F852CB07'
UserName = 'nitin21'

# Full path to uploaded document (PDF in this case)
FilePath = r"C:\Users\Lenovo\Desktop\repo\FusionPDF\documents\scan2.pdf"

# URL to process the document using the OCRWebService
# Convert the PDF into Word (docx) format
RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?outputformat=docx"

try:
    with open(FilePath, 'rb') as image_file:
        image_data = image_file.read()
        
    # Send the request with the document for OCR processing
    r = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))

    # Check if the request is authorized
    if r.status_code == 401:
        print("Unauthorized request. Please check your username and license code.")
        exit()

    # Print the raw response for debugging
    print(f"Raw Response: {r.content}")

    # Decode output response from JSON
    jobj = json.loads(r.content)

    # Print the entire parsed JSON for inspection
    print("Parsed JSON Response: ", jobj)

    # Check for errors in the response
    ocrError = jobj.get("ErrorMessage", "")
    if ocrError:
        print("Recognition Error: " + ocrError)
        exit()

    # Handle None for TaskDescription safely
    task_description = jobj.get("TaskDescription", "")
    task_description = task_description if task_description is not None else "No task description provided"
    print("Task Description: " + task_description)

    # Safely get AvailablePages and ProcessedPages
    available_pages = jobj.get("AvailablePages", "No available pages info")
    processed_pages = jobj.get("ProcessedPages", "No processed pages info")

    print("Available Pages: " + str(available_pages))
    print("Processed Pages: " + str(processed_pages))

    # If an output file was generated, download it
    if "OutputFileUrl" in jobj:
        output_url = jobj["OutputFileUrl"]
        file_response = requests.get(output_url, stream=True)

        # Save the downloaded file as a Word document
        output_file_path = r"op1.docx"
        with open(output_file_path, 'wb') as output_file:
            shutil.copyfileobj(file_response.raw, output_file)

        print(f"File successfully downloaded: {output_file_path}")
    else:
        print("No output file URL found in the response.")

except Exception as e:
    print(f"An error occurred: {e}")
