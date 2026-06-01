import cv2

# Read image in grayscale
img = cv2.imread(
    r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg',
    0
)

# Apply threshold segmentation
# Threshold value = 127
ret, segmented = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)

# Save output image
cv2.imwrite("segmented_output.jpg", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()