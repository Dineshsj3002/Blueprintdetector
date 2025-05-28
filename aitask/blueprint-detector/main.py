from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import numpy as np
import cv2
import uvicorn

app = FastAPI()

# Allow CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model (replace with your trained model if needed)
model = YOLO("yolov8n.pt")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # Read and decode image
        img_bytes = await file.read()
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            return {"error": "Invalid image format"}

        # Run prediction
        results = model.predict(source=img)

        detections = []
        for result in results:
            for box in result.boxes:
                label_id = int(box.cls[0])
                label = model.names[label_id]
                conf = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                w, h = x2 - x1, y2 - y1

                detections.append({
                    "label": label,
                    "confidence": round(conf, 2),
                    "bbox": [round(x1, 1), round(y1, 1), round(w, 1), round(h, 1)]
                })

        return {"detections": detections}
    
    except Exception as e:
        return {"error": str(e)}

# If you want to run it directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
