import win32com.client
import os

# INPUT/OUTPUT PATH
pdf_path = r"documents\outputdemo1.pdf"
output_path = r"documents"

word = win32com.client.Dispatch("Word.Application")
word.Visible = 0  # CHANGE TO 1 IF YOU WANT TO SEE WORD APPLICATION RUNNING AND ALL MESSAGES OR WARNINGS SHOWN BY WORD

# GET FILE NAME AND NORMALIZED PATH
filename = os.path.basename(pdf_path)
in_file = os.path.abspath(pdf_path)

# CONVERT PDF TO DOCX AND SAVE IT ON THE OUTPUT PATH WITH THE SAME INPUT FILE NAME
wb = word.Documents.Open(in_file)
out_file = os.path.abspath(os.path.join(output_path, filename[:-4] + ".docx"))
wb.SaveAs2(out_file, FileFormat=16)
wb.Close()
word.Quit()

#pywintypes.com_error: (-2147352567, 'Exception occurred.', (0, 'Microsoft Word', 'The file appears to be corrupted.', 'wdmain11.chm', 25272, -2146822496), None)