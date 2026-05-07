import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Create kernel (structuring element)
    kernel = np.ones((5,5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded)

    # Save output
    cv2.imwrite("eroded_output.jpg", eroded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()