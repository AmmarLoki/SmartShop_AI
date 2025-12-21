"""
SmartShop AI Backend - Search Route

POST /api/v1/search endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.search import SearchRequest, SearchResponse
from app.services.search_service import SearchService
from app.core.dependencies import get_search_service

router = APIRouter()


@router.post("/search", response_model=SearchResponse, tags=["search"])
async def search_products(
    request: SearchRequest,
    search_service: SearchService = Depends(get_search_service)
):
    """
    Search for products using natural language query.
    
    Args:
        request: Search request with query and limit
        search_service: Injected search service
        
    Returns:
        SearchResponse with parsed query and products
    """
    try:
        return await search_service.search_products(request)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Search failed: {str(e)}"
        )
