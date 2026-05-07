import cv2
import numpy as np

img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

rows, cols = img.shape[:2]

# Original points
pts1 = np.float32([[50,50], [300,50], [50,300], [300,300]])

# Destination points
pts2 = np.float32([[10,100], [300,50], [100,250], [300,300]])

# Perspective matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
output = cv2.warpPerspective(img, matrix, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transform", output)

cv2.waitKey(0)
cv2.destroyAllWindows()