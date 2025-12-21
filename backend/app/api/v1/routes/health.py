"""
SmartShop AI Backend - Health Check Route

GET /api/v1/health endpoint
"""

from fastapi import APIRouter
from typing import Dict

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        Status dictionary
    """
    return {"status": "ok"}
