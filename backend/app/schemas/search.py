"""
SmartShop AI Backend - Search Schemas

Pydantic models for search request/response validation
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from app.schemas.product import ProductResponse


class ParsedQuery(BaseModel):
    """Parsed query structure"""
    category: Optional[str] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    brands: List[str] = Field(default_factory=list)
    features: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)


class SearchRequest(BaseModel):
    """Search request schema"""
    query: str = Field(..., min_length=1, max_length=512, description="Natural language product query")
    limit: Optional[int] = Field(10, ge=1, le=50, description="Maximum number of results")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Best wireless headphones under $200",
                "limit": 10
            }
        }


class SearchResponse(BaseModel):
    """Search response schema"""
    parsed_query: ParsedQuery
    products: List[ProductResponse]
    total_results: int = 0
    query_time_ms: Optional[float] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "parsed_query": {
                    "category": "headphones",
                    "price_max": 200.0,
                    "features": ["wireless"]
                },
                "products": [],
                "total_results": 0
            }
        }
