"""
Health check routes.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "OG-Template API is running"
    }


@router.get("/ping")
def ping():
    """Simple ping endpoint."""
    return {"message": "pong"}
