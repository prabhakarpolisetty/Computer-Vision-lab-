import cv2

# Open video file
video = cv2.VideoCapture(r"C:\Users\pbr22\OneDrive\Desktop\cv_lab\Comedy.mp4")

# Get total number of frames
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Read all frames and store them in a list
frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

# Play video in reverse slow motion
for i in range(total_frames - 1, -1, -1):

    cv2.imshow("Reverse Slow Motion Video", frames[i])

    # Slow motion delay (increase value for more slow motion)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()