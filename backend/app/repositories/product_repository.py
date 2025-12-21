"""
SmartShop AI Backend - Product Repository

Product-specific repository with additional query methods
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.product import Product
from app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository[Product]):
    """
    Product repository with domain-specific query methods.
    Extends BaseRepository with product-specific operations.
    """
    
    def __init__(self, db: Session):
        """Initialize product repository"""
        super().__init__(Product, db)
    
    def get_by_product_id(self, product_id: str) -> Optional[Product]:
        """Get product by external product_id"""
        return self.db.query(Product).filter(Product.product_id == product_id).first()
    
    def search_by_category(self, category: str, limit: int = 10) -> List[Product]:
        """Search products by category"""
        return (
            self.db.query(Product)
            .filter(Product.category == category)
            .limit(limit)
            .all()
        )
    
    def search_by_price_range(
        self, 
        min_price: Optional[float] = None, 
        max_price: Optional[float] = None,
        limit: int = 10
    ) -> List[Product]:
        """Search products within a price range"""
        query = self.db.query(Product)
        
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)
        
        return query.limit(limit).all()
    
    def search_by_brand(self, brand: str, limit: int = 10) -> List[Product]:
        """Search products by brand"""
        return (
            self.db.query(Product)
            .filter(Product.brand == brand)
            .limit(limit)
            .all()
        )
    
    def get_top_rated(self, limit: int = 10) -> List[Product]:
        """Get top-rated products"""
        return (
            self.db.query(Product)
            .filter(Product.rating.isnot(None))
            .order_by(Product.rating.desc())
            .limit(limit)
            .all()
        )
    
    def get_similar_products(self, product_id: str, limit: int = 5) -> List[Product]:
        """
        Get similar products (placeholder for ML-based similarity).
        In actual implementation, this would use embeddings and FAISS.
        """
        # Placeholder: For now, return products in the same category
        product = self.get_by_product_id(product_id)
        if not product or not product.category:
            return []
        
        return (
            self.db.query(Product)
            .filter(Product.category == product.category)
            .filter(Product.product_id != product_id)
            .limit(limit)
            .all()
        )
