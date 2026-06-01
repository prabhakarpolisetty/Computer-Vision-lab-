import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Opening operation
# Opening = Erosion + Dilation
opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Opening Operation", opening_img)

# Save output image
cv2.imwrite("opening_output.jpg", opening_img)

cv2.waitKey(0)
cv2.destroyAllWindows()