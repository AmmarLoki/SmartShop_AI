"""
SmartShop AI Backend - CORS Middleware

CORS configuration
"""

from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings


def setup_cors(app):
    """
    Configure CORS middleware for the application.
    
    Args:
        app: FastAPI application instance
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )
