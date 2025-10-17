from fastapi import APIRouter, UploadFile, File
from app.services.crowd_detector import CrowdDetector

router = APIRouter()
detector = CrowdDetector()

@router.get("/test")
def test_crowd_detector():
    return {"message": "Crowd detector is active!"}

@router.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    image_path = f"temp_{file.filename}"
    with open(image_path, "wb") as f:
        f.write(await file.read())

    count = detector.count_people_in_image(image_path)
    return {"people_count": count}
