# 📘 Task 2: Re-Identification in a Single Feed

## Project Overview
This project uses object detection (YOLOv8) and DeepSORT-style tracking to maintain consistent player IDs within a single camera feed, even when players temporarily exit and re-enter the frame.

---

## Folder Structure
```

player\_reid\_task2/
├── main.py
├── detect.py
├── track.py
├── models/
│   └── best.pt
├── data/
│   └── 15sec\_input\_720p.mp4
├── output/
│   └── reid\_output.mp4
├── requirements.txt
├── README.md
└── report.md

````

---

## Setup Instructions

### 1. Install Python
Python 3.8+ recommended.

### 2. Create and activate virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/macOS
````

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

### Place the following files in `data/` folder:

* `15sec_input_720p.mp4`

### Place your custom YOLO model in `models/`:

* `best.pt`

Then run:

```bash
python main.py
```

The final annotated video will be saved to:

```
output/reid_output.mp4
```

---

## Download Required Files

- [Download best.pt](https://drive.google.com/file/d/1bGSS4EuCWkYTLoBUEz0h2FMsy-PNYGKy/view?usp=sharing)

---

## Notes

* The script assigns unique IDs using tracking, not just detection.
* If a player disappears and returns, the same ID is reassigned.
* Uses a mock or simplified tracker by default (DeepSORT can be added).
* Modify `track.py` to integrate more advanced tracking methods.

---
