import matplotlib.pyplot as plt
from PIL import Image

# Open the image
image = Image.open(r"ScannedPDF_Final\page_1.jpg")

# Get the dimensions of the image
width, height = image.size
print(f"Width: {width} pixels, Height: {height} pixels")

# Display the image with scale as axes
plt.figure(figsize=(10, 6))  # Adjust the figure size for better visibility
plt.imshow(image, cmap='gray')  # Display the image

# Add axes with pixel scale
plt.xticks(range(0, width + 1, width // 10))  # X-axis scale
plt.yticks(range(0, height + 1, height // 10))  # Y-axis scale

# Add grid lines for better visualization
plt.grid(color='blue', linestyle='--', linewidth=0.15)

# Add labels
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.title("Image with Pixel Scale")

# Show the plot
plt.show()
