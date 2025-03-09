import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "REST API with FastAPI, Yagmail and MongoDB"
    PROJECT_VERSION = "0.0.1"
    MONGO_URI = os.getenv("MONGO_URI")
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

settings = Settings()
