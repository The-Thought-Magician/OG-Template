"""
Configuration settings for the application.
"""

import os
from typing import Optional


class Settings:
    """Application settings."""
    
    # App information
    APP_NAME: str = "OG-Template"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "A comprehensive FastAPI backend template"
    
    # Server configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Database configuration
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # API configuration
    API_V1_PREFIX: str = "/api/v1"


# Global settings instance
settings = Settings()
