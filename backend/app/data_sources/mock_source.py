"""
SmartShop AI Backend - Mock Data Source

Mock data source for development and testing (boilerplate structure)
"""

from typing import List, Dict, Any
from app.data_sources.base import DataSource
import uuid


class MockDataSource(DataSource):
    """
    Mock data source returning fake product data for development.
    """
    
    def __init__(self):
        """Initialize mock data source"""
        super().__init__("Mock")
        self.products = self._generate_mock_products()
    
    async def fetch_products(
        self, 
        query: str, 
        filters: Dict[str, Any],
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Return mock products"""
        # Simple filtering simulation
        results = self.products[:limit]
        
        # Apply price filter if present
        if "price_max" in filters:
            results = [p for p in results if p["price"] <= filters["price_max"]]
        
        return results[:limit]
    
    async def get_product_by_id(self, product_id: str) -> Dict[str, Any]:
        """Get mock product by ID"""
        for product in self.products:
            if product["product_id"] == product_id:
                return product
        return {}
    
    def _generate_mock_products(self) -> List[Dict[str, Any]]:
        """Generate some mock product data"""
        return [
            {
                "product_id": str(uuid.uuid4()),
                "name": "Wireless Headphones Pro",
                "price": 199.99,
                "rating": 4.7,
                "category": "headphones",
                "brand": "TechBrand",
                "source": "Mock",
                "url": "https://example.com/product1",
                "summary": "Premium wireless headphones with noise cancellation",
                "in_stock": True
            },
            {
                "product_id": str(uuid.uuid4()),
                "name": "Budget Earbuds",
                "price": 49.99,
                "rating": 4.2,
                "category": "headphones",
                "brand": "ValueBrand",
                "source": "Mock",
                "url": "https://example.com/product2",
                "summary": "Affordable wireless earbuds with good sound quality",
                "in_stock": True
            }
        ]
