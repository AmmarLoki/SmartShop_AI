"""
SmartShop AI Backend - Comparison Schemas

Pydantic models for product comparison request/response validation
"""

from pydantic import BaseModel, Field, RootModel
from typing import List, Dict, Any, Optional


class ComparisonRequest(BaseModel):
    """Product comparison request schema"""
    product_ids: List[str] = Field(..., min_length=2, max_length=5, description="List of product IDs to compare")
    
    class Config:
        json_schema_extra = {
            "example": {
                "product_ids": ["uuid1", "uuid2"]
            }
        }


class ComparisonData(RootModel):
    """Comparison data for a specific attribute"""
    root: Dict[str, Any]  # Product name -> value mapping


class ComparisonResponse(BaseModel):
    """Product comparison response schema"""
    comparison: Dict[str, Dict[str, Any]]  # Attribute -> {product_name -> value}
    ai_insight: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "comparison": {
                    "price": {
                        "Sony WH-1000XM5": 199.99,
                        "Bose QC45": 189.99
                    },
                    "battery_life": {
                        "Sony WH-1000XM5": "30h",
                        "Bose QC45": "24h"
                    }
                },
                "ai_insight": "Sony offers better battery life, while Bose is slightly cheaper."
            }
        }
