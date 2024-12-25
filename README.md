# 🔹 **PDF Linguist**: A Seamless PDF Content Extraction, Merging, and Translation Tool

## 🌐 *Overview*

**Meet PDF Linguist** – your ultimate tool for extracting, merging, and translating PDF content! 🌟 Whether it’s digital PDFs or scanned ones, this versatile app makes it a breeze to transform and translate documents while keeping the original formatting intact. Perfect for tackling all your document translation and manipulation needs! 📄✨

### 🔹 *Key Highlights:*

1. **Translation for Digital PDFs** 🔍
2. **Translation for Scanned PDFs** 🔐

All these features are wrapped up in a single app, giving you complete control over your PDF workflows. 🏠

---

## 🔧 *Features*

### ⭐ *Digital PDFs*

- **📄 Extract Text and Images**: Quickly extract searchable text and embedded images.
- **💬 Translate Content**: Convert text into your desired language effortlessly.
- **🔠 Render Complex Scripts**: Perfect for Indic languages like Devanagari, thanks to the **HarfBuzz** engine to handle intricate ligatures and unicode combinations.
- **🌈 Merge & Preserve Layout**: Combines translated content while keeping the original layout intact.
- **🔖 Multiple Output Formats**: Save your work as PDF and Word (DOCX).
- **🔄 Multi-page Handling**: Process multi-page documents seamlessly.

### 🔐 *Scanned PDFs*

- **🔍 OCR-Based Extraction**: Extract text from scanned images using **Tesseract OCR**.
- **🕒 Customizable Cropping**: Select specific dimensions to exclude unwanted sections.
- **💬 Translate Content**: High-quality translations for regional languages.
- **🎨 Merge & Preserve Layout**: Seamlessly combine translated text with the scanned PDF’s layout.
- **🔖 Multiple Output Formats**: Export translations as PDF and Word (DOCX).

---

## 🛠️ *Installation*

### *Prerequisites*

1. Python installed on your system.
2. Recommended: Virtual environment setup.

### *Steps*

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NitinReddy-A/PDF_Linguist.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd PDF_Linguist
   ```

3. **Set up a virtual environment (optional)**:

   ```bash
   python -m venv virtual-env
   source virtual-env/bin/activate  # Linux/Mac
   virtual-env\Scripts\activate    # Windows
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🎨 *Usage*

### *Step 1: Prepare Your PDF Document*

Place the PDF file you want to process in the `documents/` folder.

### *Step 2: Run the Application*

Launch the app using Streamlit:

```bash
streamlit run app.py
```

### *Step 3: Select PDF Type*

- **Digital PDF**: For PDFs with searchable text.
- **Scanned PDF**: For image-based PDFs needing OCR.

#### 🔹 *Digital PDFs*

1. Upload your PDF using the file uploader.
2. Choose the target language for translation.
3. Click the button to extract, translate, and reassemble the PDF.
4. Download your translated file in PDF or DOCX format.

#### 🔹 *Scanned PDFs*

1. Upload your scanned PDF.
2. Define crop dimensions (optional).
3. Select the target translation language.
4. Process the file to extract text via OCR, translate, and merge the layout.
5. Download your translated file in PDF or DOCX format.

---

## 📊 *Notes*

- You’ll need API keys for **ConvertAPI** and **LightPDF API**.
- Update the script with your API keys and specify the destination language code.

---

## 📝 *Dependencies*

- **Streamlit**: For the user-friendly web app.
- **PyMuPDF (fitz)**: Handles digital PDFs and converts pages to images.
- **Pillow (PIL)**: For image processing like cropping and resizing.
- **PyTesseract**: Extracts text from scanned PDFs using OCR.
- **Googletrans**: For language translation.
- **FPDF**: Generates PDF files from translations.
- **PDF2Image**: Converts PDF pages to images for OCR.

---

## 🚀 *APIs Utilized*

- **LightPDF API**: Enables OCR-based conversion of scanned PDFs.
- **ConvertAPI**: Converts between PDF and other formats seamlessly.

---

## 🗃️ *Output Files*

- Translated PDFs and DOCX files are saved in the `documents/` folder.
- Both formats preserve the layout and formatting of the original document.

---

## 🖌️ *Summary*

PDF Linguist simplifies document management with:

- High-accuracy text and image extraction.
- Smooth translations in multiple languages.
- Seamless merging while preserving original layouts.

💡 The dual-mode functionality ensures you’re ready for any type of PDF – digital or scanned. Manage and translate documents like a pro! 🔹✨

