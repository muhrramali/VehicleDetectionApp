from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Make sure this weights file is in the same directory or provide full path

cap = cv2.VideoCapture("D:\python\ML\china.mp4")  # Replace with 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if model.names[cls] in ["car", "truck", "bus", "motorbike"]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, model.names[cls], (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("YOLOv8 Vehicle Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
