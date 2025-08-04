"""
Middleware for the application.
"""

from .cors import setup_cors_middleware
from .logging import setup_logging_middleware

__all__ = ["setup_cors_middleware", "setup_logging_middleware"]
