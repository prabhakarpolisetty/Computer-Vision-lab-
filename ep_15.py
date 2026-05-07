import cv2
import numpy as np

img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark corners
img[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow("Harris Corners", img)

cv2.waitKey(0)
cv2.destroyAllWindows()