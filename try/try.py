from PIL import Image

def convert_gray_to_cmyk(input_path, output_path):
    # Open the grayscale image
    gray_image = Image.open(input_path).convert("L")  # Ensure it is in grayscale mode

    # Prepare a new image in CMYK mode
    cmyk_image = Image.new("CMYK", gray_image.size)

    # Map grayscale to CMYK
    for y in range(gray_image.height):
        for x in range(gray_image.width):
            gray_value = gray_image.getpixel((x, y))
            cmyk_value = (0, 0, 0, 255 - gray_value)  # Map gray_value to the black channel in CMYK
            cmyk_image.putpixel((x, y), cmyk_value)

    # Save the converted CMYK image
    cmyk_image.save(output_path)



# Example usage
input_image_path = "image/1.jpg"  # Replace with your grayscale image path
output_image_path = "output_cmyk_image.jpg"  # Replace with your desired output path
convert_gray_to_cmyk(input_image_path, output_image_path)
