import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range for background removal
# Example: removing green background
lower_color = np.array([35, 50, 50])
upper_color = np.array([85, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_color, upper_color)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Remove background
result = cv2.bitwise_and(img, img, mask=mask_inv)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Background Removed", result)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\background_removed.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()