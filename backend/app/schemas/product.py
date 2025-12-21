"""
SmartShop AI Backend - Product Schemas

Pydantic models for product request/response validation
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductSpecs(BaseModel):
    """Product specifications schema"""
    battery_life: Optional[str] = None
    noise_cancellation: Optional[bool] = None
    # Add more specs as needed
    
    class Config:
        extra = "allow"  # Allow additional fields


class ProductBase(BaseModel):
    """Base product schema with common fields"""
    product_id: str
    name: str
    price: float
    rating: Optional[float] = None
    source: str
    url: str
    specs: Optional[ProductSpecs] = None


class ProductResponse(ProductBase):
    """Product response schema for API responses"""
    summary: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    features: Optional[List[str]] = None
    review_count: Optional[int] = 0
    in_stock: bool = True
    
    class Config:
        from_attributes = True  #  For Pydantic V2 (orm_mode in V1)


class ProductDetail(ProductResponse):
    """Detailed product schema with all fields"""
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
