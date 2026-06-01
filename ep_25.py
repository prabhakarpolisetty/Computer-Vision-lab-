import cv2

# Load Haar Cascade classifier
watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect objects
objects = watch_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around detected objects
for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display output
cv2.imshow("Object Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()