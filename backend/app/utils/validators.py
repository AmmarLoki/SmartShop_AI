"""
SmartShop AI Backend - Validators

Custom validation functions
"""

from typing import Any, Optional
import re


def validate_price(price: Any) -> bool:
    """
    Validate price value.
    
    Args:
        price: Price value to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        price_float = float(price)
        return price_float >= 0
    except (ValueError, TypeError):
        return False


def validate_product_id(product_id: str) -> bool:
    """
    Validate product ID format.
    
    Args:
        product_id: Product ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Simple validation: non-empty string
    return isinstance(product_id, str) and len(product_id) > 0


def validate_url(url: str) -> bool:
    """
    Validate URL format.
    
    Args:
        url: URL to validate
        
    Returns:
        True if valid, False otherwise
    """
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return url_pattern.match(url) is not None


def sanitize_query(query: str, max_length: int = 512) -> str:
    """
    Sanitize user query input.
    
    Args:
        query: User query
        max_length: Maximum allowed length
        
    Returns:
        Sanitized query
    """
    # Remove control characters
    query = re.sub(r'[\x00-\x1f\x7f]', '', query)
    # Trim to max length
    query = query[:max_length]
    # Remove extra whitespace
    query = ' '.join(query.split())
    return query
