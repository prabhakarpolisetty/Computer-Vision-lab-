import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define foreground color range
# Example: selecting red foreground
lower_color = np.array([0, 120, 70])
upper_color = np.array([10, 255, 255])

# Create mask for foreground
mask = cv2.inRange(hsv, lower_color, upper_color)

# Subtract foreground from image
result = cv2.bitwise_and(img, img, mask=mask)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Foreground Extracted", result)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\foreground_removed.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()