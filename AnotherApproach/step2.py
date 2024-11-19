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
json_path = r"extracted_text_with_coordinates.json"

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    extracted_data = json.load(json_file)

# Iterate through the extracted data and translate the text
for page_num, page_data in extracted_data.items():
    for block in page_data:
        original_text = block.get("text", "")
        c1 = block.get("Character_count", len(original_text)) 
        f = block.get("IniFontsize")
        translated_text = translate_text(original_text, dest_language='kn')  # Change 'kn' to your desired language code
        block["translated_text"] = translated_text
        block["translated_character_count"] = len(translated_text)
        #block["Translated_text"] = insert_newlines(block["text"], translated_text)
        if c1 < len(translated_text):
            block["Font_Size"] = len(translated_text) * f / c1
        else:
            block["Font_Size"] = f

# Save the translated data back to the same JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
