import cv2
import pytesseract

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open video file
video = cv2.VideoCapture(
    r"C:\Users\pbr22\OneDrive\Desktop\cv_lab\Comedy.mp4"
)

frame_count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    # Process every 30th frame
    if frame_count % 30 == 0:

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text using OCR
        text = pytesseract.image_to_string(gray)

        print("Frame:", frame_count)
        print("Extracted Text:")
        print(text)
        print("----------------------")

        # Display frame
        cv2.imshow("Video", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()