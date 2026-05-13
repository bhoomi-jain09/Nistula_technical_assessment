import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Nistula AI Backend"
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
settings = Settings()