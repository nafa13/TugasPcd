import cv2
import numpy as np
import matplotlib.pyplot as plt

def basic_image_processing(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert BGR to RGB (for matplotlib display)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # Apply edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Display results
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(img_rgb)
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('Grayscale')
    plt.imshow(gray, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.title('Blurred')
    plt.imshow(blurred, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.title('Edge Detection')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Replace with your image path
    image_path = "path_to_your_image.jpg"
    basic_image_processing(image_path)