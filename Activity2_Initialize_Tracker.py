
import cv2

video_path = 'Jet Dog Fight1.mp4'
cap = cv2.VideoCapture(video_path)
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Cannot read video.")
    exit()

# Manually re-select the object (or use bbox from Activity 1 if saved)
bbox = cv2.selectROI("Select Object", frame, False)

# Initialize tracker
tracker.init(frame, bbox)

# First frame with the object selected
cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])),
              (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])),
              (0, 255, 0), 2)
cv2.imshow("Tracker Initialized", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
