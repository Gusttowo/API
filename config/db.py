from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

try:
    MONGO_URI = os.getenv("MONGO_URI")
    if not MONGO_URI:
        raise ValueError("MONGO_URI no está definido en el entorno")

    client = MongoClient(MONGO_URI)
    db = client["API"]
    collection = db["emails"]
    print("Conexión a MongoDB establecida correctamente")
except Exception as e:
    print(f"Error conectando a MongoDB: {e}")
    db = None  # Evitar que la API crashee