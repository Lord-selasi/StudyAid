from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    
    # App Info
    APP_NAME: str = "Study Aid API"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    
    # Database
    DATABASE_URL: str
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",  
        "http://localhost:5173",  
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()