from ultralytics import YOLO
import cv2

# Load YOLO model once
model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break

        # Resize frame
        frame = cv2.resize(frame, (640, 480))
        

        # Run YOLO
        results = model(
            frame,
            imgsz=320,
            verbose=False
        )

        # Draw boxes
        annotated_frame = results[0].plot()

        # Encode frame
        ret, buffer = cv2.imencode(
            '.jpg',
            annotated_frame
        )

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame_bytes +
            b'\r\n'
        )