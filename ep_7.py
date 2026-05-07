import cv2

# Read captured video
cap = cv2.VideoCapture(r"C:\Users\pbr22\OneDrive\Desktop\cv_lab\Vaaram.mp4")   

print("Press 's' for Slow Motion")
print("Press 'f' for Fast Motion")
print("Press 'q' to Quit")

speed = 30   # Normal speed delay

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display video
    cv2.imshow("Video Processing", frame)

    key = cv2.waitKey(speed) & 0xFF

    # Slow motion
    if key == ord('s'):
        speed = 100

    # Fast motion
    elif key == ord('f'):
        speed = 10

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()