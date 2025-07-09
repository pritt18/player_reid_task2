from ultralytics import YOLO

def detect_players(model_path, frame):
    model = YOLO(model_path)
    results = model(frame, verbose=False)[0]

    detections = []
    for box in results.boxes:
        cls = int(box.cls[0])
        if cls != 0:  
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'person'))

    return detections
