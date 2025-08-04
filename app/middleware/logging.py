"""
Logging middleware setup.
"""

import time
from fastapi import FastAPI, Request


def setup_logging_middleware(app: FastAPI) -> None:
    """Set up logging middleware for the application."""
    
    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        start_time = time.time()
        
        # Log the request
        print(f"📥 {request.method} {request.url.path} - Started")
        
        # Process the request
        response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Log the response
        print(f"📤 {request.method} {request.url.path} - "
              f"Status: {response.status_code} - "
              f"Time: {process_time:.4f}s")
        
        # Add processing time to response headers
        response.headers["X-Process-Time"] = str(process_time)
        
        return response
