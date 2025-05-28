Blueprintdetector Door & Window Detector 🚪🪟
What is this?
A custom YOLOv8 model server that detects doors and windows in blueprint images. Perfect for construction analysis, smart home projects, or just showing off your AI skills.

Why?
Because your model should know the difference between a door and a window — not confuse your house for a modern art gallery.

How does it work?
You upload an image to the API endpoint /detect (POST request with an image file).

The backend runs inference using a YOLOv8 model trained on door and window blueprints.

It returns JSON with detected objects: labels, confidence scores, and bounding boxes.

Example output
json
Copy
Edit
{
  "detections": [
    {"label": "door", "confidence": 0.91, "bbox": [x, y, w, h]},
    {"label": "window", "confidence": 0.84, "bbox": [x, y, w, h]}
  ]
}
Setup
Clone the repo:

bash
Copy
Edit
git clone <your_repo_url>
cd blueprint-detector
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
# or, if you don't have requirements.txt:
pip install ultralytics fastapi uvicorn python-multipart pillow
Download your custom YOLOv8 weights (trained on doors & windows) and place them in the project folder as yolov8n.pt or best.pt.

Run the API server:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
Usage
Send a POST request to http://localhost:8000/detect with your image file.

Example with curl:

bash
Copy
Edit
curl -X POST -F "file=@path/to/your/image.jpg" http://localhost:8000/detect
You’ll get a JSON response with the detected doors and windows.

Training your own model (optional but highly recommended)
Collect and label your dataset (try LabelImg or Roboflow).

Use YOLOv8 training command, e.g.:

bash
Copy
Edit
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640
Replace the weights in your API with your trained model.

Troubleshooting
Got clocks & bikes instead of doors & windows?
You’re using the default COCO weights. Train or load your custom weights.

API returns 500 errors?
Check the logs. Make sure you’re sending the file correctly as form-data with key file.

Unicode errors on Windows paths?
Use raw strings (r"path\to\file") or forward slashes (path/to/file).

License
MIT License. Do whatever you want, just don’t mess with my cats.

