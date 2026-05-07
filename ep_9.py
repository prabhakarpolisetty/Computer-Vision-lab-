import cv2

# Read the image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get original image size
height, width = img.shape[:2]

# Scale image to bigger size
bigger_img = cv2.resize(img, (width * 2, height * 2))

# Scale image to smaller size
smaller_img = cv2.resize(img, (width // 2, height // 2))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger_img)
cv2.imshow("Smaller Image", smaller_img)

# Save output images
cv2.imwrite("bigger_output.jpg", bigger_img)
cv2.imwrite("smaller_output.jpg", smaller_img)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()