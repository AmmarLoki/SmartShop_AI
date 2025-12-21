"""
SmartShop AI Backend - API v1 Router

Central router aggregating all v1 routes
"""

from fastapi import APIRouter
from app.api.v1.routes import search, compare, recommendations, health

router = APIRouter()

# Include all route modules
router.include_router(search.router)
router.include_router(compare.router)
router.include_router(recommendations.router)
router.include_router(health.router)
