import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

def imageDimensions(img_path):
    """
    Opens an image, calculates its dimensions, and generates a plot
    with pixel-scale axes and grid for visualization.

    Args:
        img_path (str): Path to the image file.

    Returns:
        BytesIO: A BytesIO object containing the plot as a PNG image.
    """
    # Use with statement to ensure the image is properly closed after use
    with Image.open(img_path) as image:
        # Get the dimensions of the image
        width, height = image.size
        print(f"Width: {width} pixels, Height: {height} pixels")
        
        # Create a plot with pixel scale
        plt.figure(figsize=(10, 6))  # Adjust the figure size for better visibility
        plt.imshow(image, cmap='gray')  # Display the image
        
        # Add axes with pixel scale
        plt.xticks(range(0, width + 1, width // 10), fontsize=8)  # X-axis scale with smaller font size
        plt.yticks(range(0, height + 1, height // 10), fontsize=8)  # Y-axis scale with smaller font size
        
        # Add grid lines for better visualization
        plt.grid(color='blue', linestyle='--', linewidth=0.15)
        
        # Add labels
        plt.xlabel("Width (pixels)")
        plt.ylabel("Height (pixels)")
        plt.title("Image with Pixel Scale")
        
        # Save the plot to a BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format="png")  # Save as PNG format
        buf.seek(0)  # Move to the beginning of the buffer
        plt.close()  # Close the plot to free memory
    
    return buf
