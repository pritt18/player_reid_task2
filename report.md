# Project Report: Player Re-Identification in a Single Feed

**Company**: Liat.ai  
**Role**: AI Intern  
**Task**: Re-identify players in a 15-second video clip and assign consistent IDs even when they leave and re-enter the frame.

---

## Objective

To build a computer vision pipeline that can:
- Detect players using an object detection model (YOLOv8)
- Track and consistently identify players using a tracking algorithm (e.g., DeepSORT or ByteTrack)
- Ensure ID consistency throughout the clip, especially when players leave and reappear

---

## Approach

1. **Object Detection**:
   - Used YOLOv8 (fine-tuned) to detect players in each frame.
   - Detection results included bounding boxes and class labels.

2. **Tracking & Re-Identification**:
   - Integrated DeepSORT (or mock tracker in constrained environments) to track players based on visual appearance and motion cues.
   - Each player was assigned an ID in early frames and re-identified when they reappeared after going out of view.

3. **Visualization**:
   - Used OpenCV to draw bounding boxes and label player IDs.
   - Output was saved to an `.mp4` file with overlaid annotations.

---

## Techniques Tried

- **Mock detection/tracking** for local testing in restricted environments.
- **Custom YOLO model** trained on player-and-ball-specific datasets.
- **DeepSORT tracker** for ID assignment based on Kalman filters and deep feature embeddings.
- Explored dynamic resolution handling and error-robust file loading.

---

##  Challenges Faced

- In low-resource systems or environments without GPU, YOLO or torch-based models can’t be loaded.
- ID switches occurred briefly in cases of:
  - Occlusion
  - Re-entry from the same position as another player
- Without team colors or jersey number detection, tracking by appearance alone could sometimes fail.

---

## Future Work

- Incorporate **jersey number OCR** to improve re-ID robustness.
- Add **team color embedding** to assist in differentiating players with similar movements.
- Use **ByteTrack** for more stable multi-object tracking in crowded scenes.
- Support real-time tracking in live sports analysis dashboards.

---



