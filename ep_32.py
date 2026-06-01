import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get image size
height, width, channels = img.shape

# Create white image
white_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size = 1/10th of image size
box_h = height // 10
box_w = width // 10

# Top-Left Corner -> Black
white_img[0:box_h, 0:box_w] = (0, 0, 0)

# Top-Right Corner -> Blue
white_img[0:box_h, width-box_w:width] = (255, 0, 0)

# Bottom-Left Corner -> Green
white_img[height-box_h:height, 0:box_w] = (0, 255, 0)

# Bottom-Right Corner -> Red
white_img[height-box_h:height, width-box_w:width] = (0, 0, 255)

# Display image
cv2.imshow("White Image with Colored Boxes", white_img)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\output_boxes.jpg', white_img)

cv2.waitKey(0)
cv2.destroyAllWindows()