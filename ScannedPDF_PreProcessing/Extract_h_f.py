from PIL import Image

# Open the image
image = Image.open(r"ScannedPDF_IMG\page_1.jpg")

# Define the coordinates for cropping (left, upper, right, lower)
left = 0
upper = 100
right = 1780
lower = 650

# Crop the image
cropped_image = image.crop((left, upper, right, lower))

left1 = 0
upper1 = 2235
right1 = 1780
lower1 = 2520

# Crop the image
cropped_image1 = image.crop((left1, upper1, right1, lower1))

# Display or save the cropped image
cropped_image1.show()
cropped_image.save("Header.jpg")

cropped_image1.save("Footer.jpg")