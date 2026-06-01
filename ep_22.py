import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Closing operation
# Closing = Dilation + Erosion
closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Closing Operation", closing_img)

# Save output image
cv2.imwrite("closing_output.jpg", closing_img)

cv2.waitKey(0)
cv2.destroyAllWindows()