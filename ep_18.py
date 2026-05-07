import cv2

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Print image size
print(img.shape)

# Crop ROI (50x50)
roi = img[20:70, 20:70]

# Paste ROI to valid position
img[100:150, 100:150] = roi

# Display output
cv2.imshow("ROI Copy Paste", img)

cv2.waitKey(0)
cv2.destroyAllWindows()