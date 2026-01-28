from ultralytics import YOLO
import cv2

class CrowdDetector:
    def __init__(self, model_path: str = "yolov8s.pt"):
        self.model = YOLO(model_path)

    def count_people_in_image(self, image_path: str):
        results = self.model(image_path,conf=0.3)
        people_count = 0
        for result in results:
            for box in result.boxes:
                if int(box.cls[0]) == 0:

                    confidence = float(box.conf[0])

                    # 🔹 Step 2: confidence check
                    if confidence < 0.3:
                        continue

                    # 🔹 Step 3: box size filter
                    x1, y1, x2, y2 = box.xyxy[0]
                    width = x2 - x1
                    height = y2 - y1
                    area = width * height

                    if area < 500:
                        continue

                    # 🔹 Valid person
                    people_count += 1

        return people_count
