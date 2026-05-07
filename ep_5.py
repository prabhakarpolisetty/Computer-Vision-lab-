import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Split into BGR channels
    channels = ('b', 'g', 'r')

    # Calculate and plot histogram for each channel
    for i, color in enumerate(channels):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    # Labels and title
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.show()

# Function call
analyze_histogram(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')