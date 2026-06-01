import cv2

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# Read image
img = cv2.imread(
    r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\prabhakar.jpg'
)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Detect eyes inside face region
for (x, y, w, h) in faces:

    # Draw rectangle around face
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            roi_color,
            (ex, ey),
            (ex + ew, ey + eh),
            (0, 255, 0),
            2
        )

# Display output
cv2.imshow("Eye Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()