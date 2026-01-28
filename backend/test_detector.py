from app.services.crowd_detector import CrowdDetector

def main():
    detector = CrowdDetector()
    image_path = "image.jpeg"   # 👈 apni image ka naam

    count = detector.count_people_in_image(image_path)
    print("Detected people count:", count)

if __name__ == "__main__":
    main()
