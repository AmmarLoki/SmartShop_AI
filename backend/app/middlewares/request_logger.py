"""
SmartShop AI Backend - Request Logger Middleware

Request/response logging middleware
"""

from fastapi import Request
import time
import logging

logger = logging.getLogger(__name__)


async def request_logger_middleware(request: Request, call_next):
    """
    Log all incoming requests and responses.
    Includes timing information and request details.
    """
    start_time = time.time()
    
    # Log request
    logger.info(
        f"Request started: {request.method} {request.url.path}",
        extra={
            "method": request.method,
            "path": request.url.path,
            "client_host": request.client.host if request.client else "unknown"
        }
    )
    
    # Process request
    response = await call_next(request)
    
    # Calculate duration
    duration = time.time() - start_time
    
    # Log response
    logger.info(
        f"Request completed: {request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration:.3f}s",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_seconds": duration
        }
    )
    
    # Add custom header with response time
    response.headers["X-Process-Time"] = str(duration)
    
    return response
