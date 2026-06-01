import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Black Hat operation
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Operation", black_hat)

# Save output image
cv2.imwrite("blackhat_output.jpg", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()