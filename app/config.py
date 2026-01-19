import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "fyp-secretkey"
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///tester_db.db"
    SECRET_KEY = os.getenv("SECRET_KEY")
    OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")