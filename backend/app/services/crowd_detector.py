from ultralytics import YOLO
import cv2

class CrowdDetector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)

    def count_people_in_image(self, image_path: str):
        results = self.model(image_path)
        people_count = 0
        for result in results:
            for box in result.boxes:
                if int(box.cls[0]) == 0:  # Class 0 = person in YOLO
                    people_count += 1
        return people_count
