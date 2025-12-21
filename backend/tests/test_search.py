"""
Tests for search endpoint
"""

import pytest
from fastapi import status


class TestSearchEndpoint:
    """Test suite for /api/v1/search endpoint"""
    
    def test_search_endpoint_exists(self, client):
        """Test that search endpoint exists and accepts POST requests"""
        response = client.post(
            "/api/v1/search",
            json={"query": "test query", "limit": 10}
        )
        # Should not return 404
        assert response.status_code != status.HTTP_404_NOT_FOUND
    
    def test_search_with_valid_query(self, client):
        """Test search with valid query returns expected structure"""
        response = client.post(
            "/api/v1/search",
            json={"query": "wireless headphones under $200", "limit": 10}
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Verify response structure
        assert "parsed_query" in data
        assert "products" in data
        assert "total_results" in data
    
    def test_search_validation_error(self, client):
        """Test search with invalid request returns validation error"""
        response = client.post(
            "/api/v1/search",
            json={"limit": 10}  # Missing required 'query' field
        )
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_search_limit_validation(self, client):
        """Test search limit is validated"""
        response = client.post(
            "/api/v1/search",
            json={"query": "test", "limit": 100}  # Exceeds max limit of 50
        )
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestParsedQuery:
    """Test suite for query parsing"""
    
    def test_query_parsing(self, client):
        """Test that queries are parsed correctly"""
        response = client.post(
            "/api/v1/search",
            json={"query": "wireless headphones under $200", "limit": 5}
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Check parsed query structure
        parsed = data["parsed_query"]
        assert "keywords" in parsed
        assert isinstance(parsed["keywords"], list)
