import cv2

# Read image
image = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\camera.jpg')
if image is None:
    print("Image not found! Check file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show images
    cv2.imshow("Original", image)
    cv2.imshow("Gray", gray)

    # Save output
    cv2.imwrite("gray_output.jpg", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()