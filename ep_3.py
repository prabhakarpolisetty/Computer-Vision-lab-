import cv2

# Read the image
image = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale (required for Canny)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Image (Canny)", edges)

    # Save output
    cv2.imwrite("canny_output.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()