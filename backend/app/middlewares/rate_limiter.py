"""
SmartShop AI Backend - Rate Limiter Middleware

Rate limiting middleware (boilerplate structure)
"""

from fastapi import Request, HTTPException, status
from typing import Dict
import time


class RateLimiter:
    """
    Simple in-memory rate limiter.
    Boilerplate - production should use Redis-based rate limiting.
    """
    
    def __init__(self, requests_per_minute: int = 60):
        """Initialize rate limiter"""
        self.requests_per_minute = requests_per_minute
        self.requests: Dict[str, list] = {}
    
    def is_allowed(self, client_id: str) -> bool:
        """Check if request is allowed for client"""
        now = time.time()
        minute_ago = now - 60
        
        # Initialize client history
        if client_id not in self.requests:
            self.requests[client_id] = []
        
        # Remove old requests
        self.requests[client_id] = [
            req_time for req_time in self.requests[client_id]
            if req_time > minute_ago
        ]
        
        # Check limit
        if len(self.requests[client_id]) >= self.requests_per_minute:
            return False
        
        # Record this request
        self.requests[client_id].append(now)
        return True


# Global rate limiter instance
rate_limiter = RateLimiter()


async def rate_limiter_middleware(request: Request, call_next):
    """
    Rate limiting middleware.
    Limits requests per client IP address.
    """
    # Get client IP
    client_id = request.client.host if request.client else "unknown"
    
    # Check rate limit
    if not rate_limiter.is_allowed(client_id):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please try again later."
        )
    
    response = await call_next(request)
    return response
