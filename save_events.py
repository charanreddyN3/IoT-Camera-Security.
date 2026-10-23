from ultralytics import YOLO
import cv2
import sqlite3
from datetime import datetime
import os
import time

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open camera
cap = cv2.VideoCapture(0)

# Database connection
conn = sqlite3.connect("events.db")
cursor = conn.cursor()

# Cooldown settings
last_saved_time = 0
cooldown = 10

# Create evidence folder if missing
os.makedirs("evidence", exist_ok=True)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    names = results[0].names

    person_found = False

    for box in results[0].boxes:

        cls = int(box.cls[0])

        object_name = names[cls]

        if object_name == "person":

            person_found = True
            break

    if person_found:

        current_timestamp = time.time()

        if current_timestamp - last_saved_time > cooldown:

            current_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            image_name = f"event_{int(current_timestamp)}.jpg"

            image_path = f"static/evidence/{image_name}"

            # Save image
            cv2.imwrite(image_path, frame)

            # Save database record
            cursor.execute(
                """
                INSERT INTO events(event,time,image_path)
                VALUES(?,?,?)
                """,
                (
                    "Person Detected",
                    current_time,
                    image_path
                )
            )

            conn.commit()

            last_saved_time = current_timestamp

            print(
                f"Event Saved | Image: {image_name}"
            )

    annotated_frame = results[0].plot()

    cv2.imshow(
        "Smart Surveillance System",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
conn.close()
cv2.destroyAllWindows()