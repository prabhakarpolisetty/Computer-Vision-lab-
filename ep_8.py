import cv2
import numpy as np

# Read the image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Dilate the image
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Display original and dilated images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_img)

# Save output image
cv2.imwrite("dilated_output.jpg", dilated_img)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()