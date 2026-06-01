import cv2

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# Read image
img = cv2.imread(
    r'C:\Users\pbr22\OneDrive\Desktop\cv_lab\prabhakar.jpg'
)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Detect smiles inside face region
for (x, y, w, h) in faces:

    # Draw rectangle around face
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Detect smile
    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.8,
        minNeighbors=20
    )

    # Draw rectangle around smile
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            roi_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

# Display output
cv2.imshow("Smile Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()