import cv2

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Get text from user
text = input("Enter the text to display on image: ")

# Put text on image
# Parameters: image, text, position, font, font scale, color, thickness
cv2.putText(img, text, (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2, (0, 0, 255), 3)

# Display image
cv2.imshow("Image with Text", img)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\text_output.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()