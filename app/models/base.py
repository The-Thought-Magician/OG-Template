"""
Base model for common fields.
"""

from datetime import datetime
from typing import Optional


class BaseModel:
    """Base model with common fields."""
    
    def __init__(self):
        self.id: Optional[int] = None
        self.created_at: Optional[datetime] = None
        self.updated_at: Optional[datetime] = None
    
    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
