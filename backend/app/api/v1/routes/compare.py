"""
SmartShop AI Backend - Compare Route

POST /api/v1/compare endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.comparison import ComparisonRequest, ComparisonResponse
from app.services.comparison_service import ComparisonService
from app.core.dependencies import get_comparison_service

router = APIRouter()


@router.post("/compare", response_model=ComparisonResponse, tags=["comparison"])
async def compare_products(
    request: ComparisonRequest,
    comparison_service: ComparisonService = Depends(get_comparison_service)
):
    """
    Compare multiple products.
    
    Args:
        request: Comparison request with product IDs
        comparison_service: Injected comparison service
        
    Returns:
        ComparisonResponse with comparison data and AI insights
    """
    try:
        return await comparison_service.compare_products(request)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Comparison failed: {str(e)}"
        )
