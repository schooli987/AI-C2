
import cv2

# Step 1: Load the video
video_path = 'Jet Dog Fight1.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Step 2: Read the first frame
ret, frame = cap.read()
if not ret:
    print("Abort the mission.")
    cap.release()
    exit()

# Step 3: Select object to track
bbox = cv2.selectROI("Select the jet to track", frame, False)
cv2.destroyWindow("Select the jet to track")

print("Selected Jet location:", bbox)
cap.release()
