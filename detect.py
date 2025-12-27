from ultralytics import YOLO
import cv2
import sqlite3
from datetime import datetime
from gps import get_gps_location

model = YOLO("yolov8n.pt")  

conn = sqlite3.connect("road.db")
cursor = conn.cursor()

cap = cv2.VideoCapture("road_video.mp4")

print("🚀 Object detection started. Press 'Q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            object_name = model.names[cls]
            confidence = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{object_name} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            if confidence > 0.5:
                latitude, longitude = get_gps_location()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                cursor.execute("""
                INSERT INTO detections
                (object_type, confidence, timestamp, latitude, longitude)
                VALUES (?, ?, ?, ?, ?)
                """, (object_name, confidence, timestamp, latitude, longitude))

                conn.commit()

    cv2.imshow("AI-Based Road Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
conn.close()
cv2.destroyAllWindows()

print("🛑 Detection stopped. Database updated successfully.")
