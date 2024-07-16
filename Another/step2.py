from googletrans import Translator
import json

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_language='kn'):  # Change 'kn' to your desired language code
    try:
        translated = translator.translate(text, dest=dest_language)
        print("Translated:", translated.text)
        return (translated.text)
    except Exception as e:
        print(f"Error in translation: {e}")
        return text

# Path to the input JSON file
json_path = r"extracted_text_with_coordinates.json"

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    extracted_data = json.load(json_file)

# Iterate through the extracted data and translate the text
for page_num, page_data in extracted_data.items():
    for block in page_data:
        original_text = block["text"]
        c1 = block["Character_count"]
        f = block["IniFontsize"]
        translated_text = translate_text(original_text, dest_language='kn')  # Change 'kn' to your desired language code
        block["translated_text"] = translated_text
        block["translated_character_count"] = len(translated_text)
        if c1 < len(translated_text):
            block["Font_Size"] = len(translated_text) * f / c1

# Save the translated data back to the same JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
