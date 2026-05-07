import cv2

# Read the image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Rotate image 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_img)

# Save rotated image
cv2.imwrite("rotated_output.jpg", rotated_img)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()