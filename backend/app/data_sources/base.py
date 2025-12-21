"""
SmartShop AI Backend - Base Data Source

Abstract base class for data sources (boilerplate structure)
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class DataSource(ABC):
    """
    Abstract base class for data sources.
    All data source implementations must inherit from this class.
    """
    
    def __init__(self, source_name: str):
        """
        Initialize data source.
        
        Args:
            source_name: Name of the data source (e.g., "Amazon", "Mock")
        """
        self.source_name = source_name
    
    @abstractmethod
    async def fetch_products(
        self, 
        query: str, 
        filters: Dict[str, Any],
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Fetch products from the data source.
        
        Args:
            query: Search query
            filters: Query filters (category price, etc.)
            limit: Maximum number of products to return
            
        Returns:
            List of product dictionaries
        """
        pass
    
    @abstractmethod
    async def get_product_by_id(self, product_id: str) -> Dict[str, Any]:
        """
        Get a single product by ID.
        
        Args:
            product_id: Product identifier
            
        Returns:
            Product dictionary
        """
        pass
