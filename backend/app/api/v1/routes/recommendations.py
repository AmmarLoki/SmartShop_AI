"""
SmartShop AI Backend - Recommendations Route

GET /api/v1/products/{product_id}/recommendations endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.schemas.product import ProductResponse
from app.services.recommendation_service import RecommendationService
from app.core.dependencies import get_recommendation_service

router = APIRouter()


@router.get(
    "/products/{product_id}/recommendations",
    response_model=List[ProductResponse],
    tags=["recommendations"]
)
async def get_recommendations(
    product_id: str,
    limit: int = Query(5, ge=1, le=20, description="Number of recommendations"),
    recommendation_service: RecommendationService = Depends(get_recommendation_service)
):
    """
    Get product recommendations based on similarity.
    
    Args:
        product_id: Product ID to get recommendations for
        limit: Maximum number of recommendations
        recommendation_service: Injected recommendation service
        
    Returns:
        List of recommended products
    """
    try:
        return await recommendation_service.get_recommendations(product_id, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Recommendation failed: {str(e)}"
        )
