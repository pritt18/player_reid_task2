import cv2
import os

class Tracker:
    def __init__(self):
        self.next_id = 0
        self.tracks = []

    def update(self, detections, frame):
        results = []
        for det in detections:
            x1, y1, x2, y2 = det
            results.append((x1, y1, x2, y2, self.next_id))
            self.next_id += 1
        return results

def detect_players(model, frame):
    height, width, _ = frame.shape
    return [
        (int(width * 0.3), int(height * 0.3), int(width * 0.4), int(height * 0.5)),
        (int(width * 0.6), int(height * 0.4), int(width * 0.7), int(height * 0.6))
    ]

video_path = 'data/15sec_input_720p.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"❌ Error: Could not open video file at '{video_path}'")
    exit()

ret, frame = cap.read()
if not ret:
    print("❌ Error: Could not read the first frame of the video.")
    cap.release()
    exit()

frame_height, frame_width = frame.shape[:2]

os.makedirs('output', exist_ok=True)

tracker = Tracker()
model = None

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output/reid_output.mp4', fourcc, 30.0, (frame_width, frame_height))

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    detections = detect_players(model, frame)
    tracks = tracker.update(detections, frame)

    print(f"📹 Frame {frame_count}:")
    for track in tracks:
        x1, y1, x2, y2, track_id = track
        print(f"    🧍 Player ID: {track_id}, Box: ({x1}, {y1}), ({x2}, {y2})")
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print("\n Output video saved successfully at: output folder")
