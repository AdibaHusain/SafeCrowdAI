from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str = "sqlite:///./safe_crowd_ai.db"
    YOLO_MODEL: str = "yolov8s.pt"

    class Config:
        env_file = ".env"

settings = Settings()
