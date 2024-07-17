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

# Sample input JSON
data = {
    "1": [
        {
            "coordinates": [
                445.9200134277344,
                711.7718505859375,
                465.41241455078125,
                724.6261596679688
            ],
            "IniFontsize": 11.0,
            "text": "1 n\n",
            "Character_count": 4,
            "Translated_text": "1 ಎನ್",
            "translated_character_count": 5,
            "Font_Size": 13.75
        },
        {
            "coordinates": [
                101.5199966430664,
                188.42947387695312,
                247.6913299560547,
                204.42945861816406
            ],
            "IniFontsize": 16.0,
            "text": "Rasheeda’s question\n",
            "Character_count": 20,
            "Translated_text": "ರಾಧಾಕೃಷ್ಣನ್ ಪ್ರಶ್ನೆ",
            "translated_character_count": 19
        },
        {
            "coordinates": [
                101.5199966430664,
                211.74618530273438,
                424.8001708984375,
                266.9452819824219
            ],
            "IniFontsize": 12.0,
            "text": "Rasheeda sat reading the newspaper. Suddenly, her eyes\nfell on a small headline: “One Hundred Years Ago.” How,\nshe wondered, could anyone know what had happened\nso many years ago?\n",
            "Character_count": 180,
            "Translated_text": "ರಶೀದಾ ಪತ್ರಿಕೆ ಓದುತ್ತಾ ಕುಳಿತಿದ್ದಳು. ಇದ್ದಕ್ಕಿದ್ದಂತೆ, ಅವಳ ಕಣ್ಣುಗಳು ಒಂದು ಸಣ್ಣ ಶೀರ್ಷಿಕೆಯ ಮೇಲೆ ಬಂದವುಃ ನೂರು ವರ್ಷಗಳ ಹಿಂದೆ. “ ಇಷ್ಟು ವರ್ಷಗಳ ಹಿಂದೆ ಏನಾಯಿತು ಎಂದು ಯಾರಿಗಾದರೂ ಹೇಗೆ ಗೊತ್ತು? ”",
            "translated_character_count": 173
        }
    ]
}

# Apply the function to each text entry in the JSON
for entry in data["1"]:
    entry["Translated_text"] = insert_newlines(entry["text"], entry["Translated_text"])

# Output the modified JSON
import json
print(json.dumps(data, ensure_ascii=False, indent=4))
