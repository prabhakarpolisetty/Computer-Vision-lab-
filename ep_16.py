import cv2

img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg', 0)

# Sobel X
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# Sobel Y
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Original", img)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()