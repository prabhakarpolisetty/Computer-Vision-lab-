import cv2
import numpy as np

# Read the image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get image height and width
rows, cols = img.shape[:2]

# Define three points in original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define corresponding points in transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Get affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_img = cv2.warpAffine(img, matrix, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

# Save output image
cv2.imwrite("affine_output.jpg", affine_img)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()