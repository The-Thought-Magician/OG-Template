"""
CORS middleware setup.
"""

from fastapi import FastAPI


def setup_cors_middleware(app: FastAPI) -> None:
    """Set up CORS middleware for the application."""
    # Note: In production, you should specify exact origins instead of "*"
    
    # For now, we'll add a simple middleware function
    # In a real implementation, you'd use fastapi.middleware.cors.CORSMiddleware
    
    @app.middleware("http")
    async def cors_middleware(request, call_next):
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
