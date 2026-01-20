from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """
    Application configuration.
    Reads from environment variables and .env file.
    """
    
    # App Info
    APP_NAME: str = "Study Aid API"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    
    # Database
    DATABASE_URL: str
    
    # CORS - which domains can access our API
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
    ]
    
    class Config:
        # Tell Pydantic to read from .env file
        env_file = ".env"
        case_sensitive = True

# Create a single settings instance
settings = Settings()