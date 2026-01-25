from fastapi import APIRouter
from app.api.v1 import auth
api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])


@api_router.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    Returns basic info about the API.
    """
    return {
        "status": "healthy",
        "message": "Study Aid API is running",
        "version": "1.0.0"
    }

@api_router.get("/")
async def root():
   
    return {
        "message": "Welcome to Study Aid API",
        "docs": "/api/docs",
        "health": "/api/v1/health"
    }

@api_router.get("/info")
async def get_info():
    return {
        "app_name": "Study Aid",
        "environment": "development",
        "features": ["upload", "summarize", "questions", "resources"]
    }

@api_router.get("/yes")
async def get_info():
    return {
        "app_name": "Study Aid",
        "environment": "development",
        "features": ["upload", "summarize", "questions", "resources"]
    }