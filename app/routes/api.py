"""
Main API router that combines all route modules.
"""

from fastapi import APIRouter
from .health import router as health_router
from .core import router as core_router
from .users import router as users_router

# Create main API router
api_router = APIRouter()

# Include all route modules
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(core_router, prefix="", tags=["core"])
api_router.include_router(users_router, prefix="", tags=["users"])
