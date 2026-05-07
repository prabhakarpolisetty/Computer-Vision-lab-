import cv2

# Read the image
image = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else: 
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred)

    # Save blurred image
    cv2.imwrite("blur_output.jpg", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()