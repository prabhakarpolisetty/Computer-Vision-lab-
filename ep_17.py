import cv2

img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Add watermark text
watermarked = cv2.putText(
    img.copy(),
    'WATERMARK',
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()