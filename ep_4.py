import cv2

# Read the image
image = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale (required)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Show images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Equalized Image", equalized)

    # Save output
    cv2.imwrite("equalized_output.jpg", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()