"""
SmartShop AI Backend - Main Application

FastAPI application entry point with middleware and router configuration
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.logging import setup_logging
from app.core.database import init_db
from app.api.v1.router import router as api_v1_router
from app.middlewares import (
    setup_cors,
    validation_exception_handler,
    http_exception_handler,
    request_logger_middleware,
    rate_limiter_middleware,
)

# Setup logging
setup_logging()

# Create FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered shopping assistant API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

# Setup CORS
setup_cors(app)

# Register middleware
app.middleware("http")(request_logger_middleware)
if not settings.DEBUG:
    # Only enable rate limiting in production
    app.middleware("http")(rate_limiter_middleware)

# Register exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)

# Include API routers
app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)


@app.on_event("startup")
async def startup_event():
    """
    Application startup event handler.
    Initialize database and other resources.
    """
    # Initialize database tables
    init_db()
    print(f"✅ {settings.PROJECT_NAME} v{settings.VERSION} started successfully!")
    print(f"📚 API Documentation: http://localhost:8000{settings.API_V1_PREFIX}/docs")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Application shutdown event handler.
    Clean up resources.
    """
    print(f"👋 {settings.PROJECT_NAME} shutting down...")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running",
        "docs": f"{settings.API_V1_PREFIX}/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
