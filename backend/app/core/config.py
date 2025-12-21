"""
SmartShop AI Backend - Core Configuration Module

This module provides centralized configuration management using Pydantic BaseSettings.
All environment variables and application settings are defined here.
"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Configuration
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "SmartShop AI"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # CORS Settings
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    
    # Database Configuration
    DATABASE_URL: str = "sqlite:///./smartshop.db"
    DB_ECHO: bool = False
    
    # Redis/Cache Configuration
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    CACHE_TTL: int = 3600  # 1 hour in seconds
    
    # ML Model Configuration
    ML_MODELS_PATH: str = "./models"
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"
    MAX_QUERY_LENGTH: int = 512
    
    # API Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"  # or "text"
    
    # Application Limits
    MAX_SEARCH_RESULTS: int = 50
    DEFAULT_SEARCH_LIMIT: int = 10
    MAX_COMPARISON_PRODUCTS: int = 5
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    This ensures settings are loaded only once.
    """
    return Settings()


# Export settings instance
settings = get_settings()
