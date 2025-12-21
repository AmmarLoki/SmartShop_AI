"""Middlewares module initialization"""

from app.middlewares.error_handler import (
    error_handler_middleware,
    validation_exception_handler,
    http_exception_handler
)
from app.middlewares.request_logger import request_logger_middleware
from app.middlewares.rate_limiter import rate_limiter_middleware
from app.middlewares.cors import setup_cors

__all__ = [
    "error_handler_middleware",
    "validation_exception_handler",
    "http_exception_handler",
    "request_logger_middleware",
    "rate_limiter_middleware",
    "setup_cors",
]
