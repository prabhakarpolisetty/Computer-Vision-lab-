import cv2

# Load Haar Cascade file for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Read image
img = cv2.imread(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\iphone.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Count faces
face_count = len(faces)

print("Number of faces detected:", face_count)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display image
cv2.imshow("Face Detection", img)

# Save output image
cv2.imwrite(r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\face_detected.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()