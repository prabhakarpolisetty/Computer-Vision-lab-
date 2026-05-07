import cv2

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get height and width
height, width = img.shape[:2]

# Print image size
print("Height of image =", height)
print("Width of image =", width)

# Display image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()