import os
from dotenv import load_dotenv
load_dotenv() 

class Settings:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB = os.getenv("MONGO_DB", "fastapi_db")
    JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

settings = Settings()