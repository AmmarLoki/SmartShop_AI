"""
Tests for recommendations endpoint
"""

import pytest
from fastapi import status


class TestRecommendationsEndpoint:
    """Test suite for /api/v1/products/{product_id}/recommendations endpoint"""
    
    def test_recommendations_endpoint_exists(self, client):
        """Test that recommendations endpoint exists"""
        response = client.get("/api/v1/products/test-id/recommendations")
        # Should not return 404
        assert response.status_code != status.HTTP_404_NOT_FOUND
    
    def test_recommendations_with_valid_id(self, client):
        """Test recommendations with valid product ID"""
        response = client.get("/api/v1/products/test-product-123/recommendations?limit=5")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Should return a list
        assert isinstance(data, list)
    
    def test_recommendations_limit_parameter(self, client):
        """Test recommendations limit query parameter"""
        response = client.get("/api/v1/products/test-id/recommendations?limit=3")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Should respect limit
        assert len(data) <= 3
    
    def test_recommendations_limit_validation(self, client):
        """Test recommendations limit validation"""
        # Test exceeding max limit
        response = client.get("/api/v1/products/test-id/recommendations?limit=100")
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestHealthEndpoint:
    """Test suite for health check endpoint"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get("/api/v1/health")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "ok"
