import streamlit as st
import subprocess

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Styling the title */
        .title {
            font-size: 100px;  /* Extremely large font size for the title */
            font-weight: bold;
            color:  #FF4500;  /* Darker Tomato color */
            text-align: center;
            padding-bottom: 50px;
        }
        
        /* Styling the buttons container */
        .stmarkdown div{
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
        }

        /* Styling individual buttons */
        .stButton button {
            background-color: #FF4500;  /* Darker Tomato color */
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #FF6347;  /* Tomato color on hover*/
            color: white;
            font-weight: bolder;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the landing page with custom font and color
st.markdown('<p class="title">PDFLinguist</p>', unsafe_allow_html=True)

# Function to run the ScannedPDF script
def run_scanned_pdf():
    subprocess.run(["streamlit", "run", "ScannedPDF.py"])

# Function to run the DigitalPDF script
def run_digital_pdf():
    subprocess.run(["streamlit", "run", "DigitalPDF.py"])

# Function to run the DigitalPDF script
def run_KannadaOCR_pdf():
    subprocess.run(["streamlit", "run", "KannadaOCR.py"])

# Create a container for the buttons and make them side by side
with st.container():
    st.markdown('<div class="buttons-container">', unsafe_allow_html=True)

    # Button for Scanned PDF
    if st.button("Upload Scanned ENG PDF", key="scanned", help="Run Scanned PDF processing"):
        run_scanned_pdf()

    # Button for Digital PDF
    if st.button("Upload Digital ENG PDF", key="digital", help="Run Digital PDF processing"):
        run_digital_pdf()

    # Button for Digital PDF
    if st.button("Upload Scanned KANNADA PDF", key="KannadaOCR", help="Run Kannada PDF processing"):
        run_KannadaOCR_pdf()

    st.markdown('</div>', unsafe_allow_html=True)
