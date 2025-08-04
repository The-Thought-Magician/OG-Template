"""
Core application routes.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    """Root endpoint - returns welcome message."""
    return {
        "message": "Welcome to OG-Template",
        "version": "0.1.0",
        "docs": "/docs"
    }


@router.get("/info")
def get_app_info():
    """Get application information."""
    return {
        "name": "OG-Template",
        "version": "0.1.0",
        "description": "A comprehensive FastAPI backend template",
        "features": [
            "FastAPI Foundation",
            "Modular Architecture", 
            "Docker Support",
            "Testing Setup"
        ]
    }
