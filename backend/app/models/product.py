"""
SmartShop AI Backend - Product Model

Database model for product entities (boilerplate structure)
"""

from sqlalchemy import Column, String, Float, Integer, JSON, Text
from app.models.base import BaseModel


class Product(BaseModel):
    """
    Product model representing aggregated product data.
    
    This is a boilerplate structure - actual implementation will include
    relationships, indexes, and business logic.
    """
    # Basic Information
    product_id = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(500), nullable=False)
    category = Column(String(100), index=True)
    brand = Column(String(100), index=True)
    
    # Pricing
    price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    
    # Rating and Reviews
    rating = Column(Float)
    review_count = Column(Integer, default=0)
    
    # Product Details
    description = Column(Text)
    summary = Column(Text)  # AI-generated summary
    features = Column(JSON)  # List of features as JSON
    specs = Column(JSON)  # Product specifications as JSON
    
    # Source Information
    source = Column(String(100))  # e.g., "Amazon", "eBay"
    url = Column(String(1000))
    image_url = Column(String(1000))
    
    # ML/AI Fields
    embedding = Column(JSON)  # Vector embedding for similarity search
    embedding_model = Column(String(100))  # Model used for embedding
    
    # Availability
    in_stock = Column(Integer, default=1)  # Boolean as integer
    
    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
