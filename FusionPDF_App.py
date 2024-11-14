import streamlit as st
from googletrans import Translator
import time
import base64

# Custom CSS for background image and font styling
def add_bg_from_local(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{"png"};base64,{image_path});
            background-size: cover;
            color: white;  /* Default text color */
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #f5f5f5;  /* Light gray headings for visibility */
        }}
        .css-1d391kg p {{
            color: white; /* Adjust text in paragraph elements */
        }}
        .stButton>button {{
            background-color: #333;  /* Darker button color for contrast */
            color: white;
            border-radius: 8px;
            font-size: 18px;
        }}
        .stButton>button:hover {{
            background-color: #555;  /* Slightly lighter button on hover */
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to encode the background image to base64
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Load the background image
# image_base64 = get_base64_of_image("Background Image.webp")

# # Add background and custom styling
# add_bg_from_local(image_base64)

# Main Streamlit application code
def main():
    st.title("PDF Content Extraction and Translation")
    st.subheader("Upload your PDF and translate it to Kannada")

    # Session state to handle stop functionality
    if "stop_translation" not in st.session_state:
        st.session_state.stop_translation = False

    # File uploader for PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Placeholder for the progress and translation
        progress_placeholder = st.empty()

        # Start Translation button
        if st.button("Translate content to Kannada"):
            st.session_state.stop_translation = False  # Reset the stop flag
            progress_placeholder.text("Translating... Please wait.")
            extracted_text = extract_text_from_pdf(uploaded_file)
            translated_text = translate_text_to_kannada(extracted_text, progress_placeholder)
            if not st.session_state.stop_translation:
                st.success("Translation Complete!")
                st.write(translated_text)

        # Stop Translation button
        if st.button("Stop Translation"):
            st.session_state.stop_translation = True

        # Option to upload another PDF
        if st.button("Upload another PDF"):
            st.experimental_rerun()

# Dummy functions for demonstration purposes
def extract_text_from_pdf(pdf_file):
    # Code to extract text from the uploaded PDF
    return "Extracted text from the PDF."

def translate_text_to_kannada(text, progress_placeholder):
    translator = Translator()
    words = text.split()
    translated_text = ""
    
    for i, word in enumerate(words):
        if st.session_state.stop_translation:
            progress_placeholder.text("Translation Stopped.")
            return translated_text  # Stop and return the translation so far

        # Simulating a slow translation process for demonstration
        time.sleep(0.1)
        translated_word = translator.translate(word, dest='kn').text
        translated_text += translated_word + " "

        # Update progress message
        progress_placeholder.text(f"Translating... {i+1}/{len(words)} words translated.")

    return translated_text

if __name__ == "__main__":
    main()
