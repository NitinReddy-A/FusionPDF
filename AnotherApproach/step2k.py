from googletrans import Translator
import json

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, src_language='kn', dest_language='en'):  # Set source and destination languages
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        print("Translated:", translated.text)
        return translated.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return text
    
def insert_newlines(text, translated_text):
    # Find positions of '\n' in the original text
    newline_positions = [pos for pos, char in enumerate(text) if char == '\n']
    
    # Adjust positions for translated text
    adjusted_positions = []
    offset = 0
    for pos in newline_positions:
        while pos + offset < len(translated_text) and translated_text[pos + offset] != ' ':
            offset += 1
        adjusted_positions.append(pos + offset)
    
    # Insert '\n' at the adjusted positions
    for pos in reversed(adjusted_positions):  # reversed to avoid messing up positions
        translated_text = translated_text[:pos] + '\n' + translated_text[pos:]
    
    return translated_text

# Path to the input JSON file
json_path = r"extracted_text_with_coordinates1.json"

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    extracted_data = json.load(json_file)

# Iterate through the extracted data and translate the text
for page_num, page_data in extracted_data.items():
    for block in page_data:
        original_text = block.get("text", "")
        c1 = block.get("Character_count", len(original_text)) 
        # f = block.get("IniFontsize")
        translated_text = translate_text(original_text, src_language='kn', dest_language='en')  # Translate from Kannada to English
        block["translated_text"] = translated_text
        block["translated_character_count"] = len(translated_text)
        #block["Translated_text"] = insert_newlines(block["text"], translated_text)
        # if c1 < len(translated_text):
        #     block["Font_Size"] = len(translated_text) * f / c1
        # else:
        #     block["Font_Size"] = f

# Save the translated data back to the same JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)


ಆಡಳಿತ ಕನ್ನಡವನ್ನು ನೊಂದಣಿ ಮಾಡಿಕೊಳ್ಳಬೇಕಾದ ವಿದ್ಯಾಥ್ಥಿ೯ಗಳು: 
(೧) 
೨) 
(೩) 
(೪) 
(೫) 
(೬) 
೧ ರಿಂದ ೧೦ನೇ ತರಗತಿಯವರೆಗೆ ಕನ್ನಡ ಮಾಧ್ಯಮದಲ್ಲಿ ಅಭ್ಯಾಸಿಸಿರುವರು. 
೧೦ನೇ ತರಗತಿಯಲ್ಲಿ ಕನ್ನಡವನ್ನು ಮೊದಲನೇಯ ಅಥವಾ ಎರಡನೇಯ ಭಾಷೆಯಾಗಿ ಅಭ್ಯಾಸಿಸಿರುವರು. 
ಪ್ರೌಡಶಿಕ್ಷಣದ  ಯಾವುದೇ  ಹಂತದಲ್ಲಿ  ಕನ್ನಡವನ್ನು  ಅಭ್ಯಾಸಿದ್ದು,  ಕನ್ನಡವನ್ನು  ಬರೆಯುವುದು  ಹಾಗೂ  ಓದುವದನ್ನು 
ಕಲಿತಿರುವವರು. 
ಮಾನ್ಯತೆ ಪಡೆದ ವಿಶ್ವವಿದ್ಯಾಲಯದಿಂದ ಕನ್ನಡ ವಿಷಯದಲ್ಲಿ ಡಿಪ್ಲೊಮಾ ಅಥವಾ ಸರ್ಟಿಫಿಕೇಟ್‌ನ್ನು ಪಡೆದಿರುವವರು. 
ಕನ್ನಡ ಸಾಹಿತ್ಯ ಪರಿಷತ ನಡೆಸುವ ಕಾವ, ಜಾಣ ಅಥವಾ ಕನ್ನಡ ರತ್ನ ಪರೀಕ್ಷೆ ತೇರ್ಗಡೆಯಾಗಿರುವವರು. 
ರಾಜ್ಯ  ಸರ್ಕಾರದಿಂದ  ಎಸ್‌ಎಸ್‌ಎಲ್‌ಸಿ  ಪರೀಕ್ಷೆಗೆ  ಸಮಾನವೆಂದು ಮಾನ್ಯತೆ  ಪಡೆದ ಪರೀಕ್ಷೆಗಳಲ್ಲಿ  ಕನ್ನಡವನ್ನು ಸಮ್ಮಿಶ್ರ 
ಅಭ್ಯಾಸಮಾಡದೆ  ಹಾಗೂ  ವಿವಿಧ  ವಿಷಯಗಳ ಪ್ರಶ್ನೆ  ಪತ್ರಿಕೆಗಳಿಗೆ  ಕನ್ನಡ  ಮಾಧ್ಯಮದಲ್ಲಿ  ಉತ್ತರಿಸಿದ್ದರೆ  ಹಾಗೂ  ಆ) 
ಕನ್ನಡವನ್ನು  ಮೊದಲನೇಯ  ಅಥವಾ  ಎರಡನೇಯ  ಭಾಷೆಯಾಗಿ  ಅಭ್ಯಸಿಸಿರುವರು  ಅಥವಾ  ಐಚ್ಛಿಕ  ವಿಷಯವಾಗಿ 
ಅಭ್ಯಾಸಿಸಿರುವರು 
ವ್ಯವಹಾರಿಕ ಕನ್ನಡ ನೊಂದಣಿ ಮಾಡಿಕೊಳ್ಳಬೇಕಾದ ವಿದ್ಯಾರ್ಥಿಗಳು: 
ಪ್ರೌಡಶಿಕ್ಚಣ  (ಸಿಬಿಎಸಇ/ಐಸಿಎಸ್‌ಇ ಅಥವಾ ಅಂತರ್‌ ರಾಷ್ಟ್ರೀಯ. ಇತ್ಯಾದಿ) ದ ಯಾವುದೇ ಹಂತದಲ್ಲಿ ಕನ್ನಡವನ್ನು ಅಭ್ಯಾಸಿಸದೇ 
ಇರುವವರು ಮತ್ತು ಕನ್ನಡವನ್ನು ಮಾತನಾಡಲು,  ಬರೆಯಲು, ಓದಲು ಹಾಗೂ ಅರ್ಥವಾಗದೆ ಇರುವವರು. 
ವಿದ್ಯಾರ್ಥಿಗಳು  ಪದವಿ ಕೋರ್ಸಿಗೆ  ಪ್ರವೇಶ  ಪಡೆಯುವ ಸಮಯದಲ್ಲಿ ನೀಡಿದ ಪ್ರಮಾಣ  ಪತ್ರಗಳ  ಆಧಾರದ ಮೇಲೆ 
ಮಹಾವಿದ್ಯಾಲಯಗಳ  ಪ್ರಾಂಶುಪಾಲರು,  ವ್ಯವಹಾರಿಕ  ಕನ್ನಡ  ಮತ್ತು  ಆಡಳಿತ  ಕನ್ನಡಕ್ಕೆ  ನೊಂದಣಿ  ಮಾಡಲು ಸೂಕ್ತ  ನಿರ್ದೇಶನ 
ನೀಡಬೇಕೇಂದು ಈ ಮೂಲಕ ತಿಳಿಸಲಾಗಿದೆ. 
ಈ ಸುತ್ತೋಲೆಯನ್ನು ಕಟ್ಟುನಿಟ್ಟಾಗಿ  ಪಾಲಿಸಲು ಹಾಗೂ ಸಂಬಂಧಿಸಿದ ಎಲ್ಲರ ಗಮನಕ್ಕೆ ತರಲು  ಪ್ರಾಂಶುಪಾಲರಿಗೆ 
ನಿರ್ದೇಶಿಸಲಾಗಿದೆ.  ಆದೇಶ ಮೇರೆಗೆ 
ಸಹಿ ಇದೆ/-. 
ಕುಲಸಚಿವರು