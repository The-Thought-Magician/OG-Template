"""
Base schema for common validation.
"""

from typing import Optional
from datetime import datetime


class BaseSchema:
    """Base schema with common fields."""
    
    def __init__(self):
        self.id: Optional[int] = None
        self.created_at: Optional[datetime] = None
        self.updated_at: Optional[datetime] = None
