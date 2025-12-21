"""
SmartShop AI Backend - Text Utilities

Text processing utility functions
"""

import re
from typing import List


def clean_text(text: str) -> str:
    """
    Clean and normalize text.
    
    Args:
        text: Input text
        
    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to maximum length.
    
    Args:
        text: Input text
        max_length: Maximum length
        suffix: Suffix to add when truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def extract_keywords(text: str, max_keywords: int = 5) -> List[str]:
    """
    Extract keywords from text (simple implementation).
    
    Args:
        text: Input text
        max_keywords: Maximum number of keywords
        
    Returns:
        List of keywords
    """
    # Simple keyword extraction: split and filter
    words = text.lower().split()
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
    keywords = [w for w in words if w not in stop_words and len(w) > 3]
    return keywords[:max_keywords]
