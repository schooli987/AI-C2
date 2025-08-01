
import cv2

video_path = 'Jet Dog Fight1.mp4'
cap = cv2.VideoCapture(video_path)
tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()
if not ret:
    print("Cannot read video.")
    exit()

# Re-initialize with bounding box
ret, frame = cap.read()
bbox = cv2.selectROI("Select Object", frame, False)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, box = tracker.update(frame)

    if success:
        x, y, w, h = [int(i) for i in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost Track", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Combat Jet Tracker", frame)
    if cv2.waitKey(10) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
