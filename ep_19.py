import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded_img = cv2.erode(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)

# Save output image
cv2.imwrite("eroded_output.jpg", eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()