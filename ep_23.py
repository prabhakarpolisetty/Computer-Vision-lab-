import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Top Hat operation
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat Operation", top_hat)

# Save output image
cv2.imwrite("tophat_output.jpg", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()