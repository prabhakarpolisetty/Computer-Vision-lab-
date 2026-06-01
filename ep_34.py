import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get image dimensions
height, width, channels = img.shape

# Create white image
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw a circle
# Parameters: image, center point, radius, color(BGR), thickness
cv2.circle(white_img, (width//2, height//2), 100, (255, 0, 0), 3)

# Display image
cv2.imshow("Circle Shape", white_img)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\circle_output.jpg', white_img)

cv2.waitKey(0)
cv2.destroyAllWindows()