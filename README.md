### Setup Instructions

1. Install Python 3.8+
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

### Run the Script

Make sure your input video and model are placed correctly:

```
models/best.pt
data/15sec_input_720p.mp4
```

Then run:

```bash
python main.py
```

### Project Structure

```
player_reid_task2/
├── models/
│   └── best.pt
├── data/
│   └── 15sec_input_720p.mp4
├── output/
│   └── reid_output.mp4
├── main.py
├── detect.py
├── track.py
├── requirements.txt
├── README.md
└── report.md
```
