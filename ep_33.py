import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get image dimensions
height, width, channels = img.shape

# Create a white image
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw a rectangle
# Parameters: image, start point, end point, color(BGR), thickness
cv2.rectangle(white_img, (100, 100), (400, 300), (0, 0, 255), 3)

# Display image
cv2.imshow("Rectangle Shape", white_img)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\rectangle_output.jpg', white_img)

cv2.waitKey(0)
cv2.destroyAllWindows()