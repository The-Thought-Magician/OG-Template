"""
User model.
"""

from typing import Optional
from .base import BaseModel


class User(BaseModel):
    """User model."""
    
    def __init__(self, username: str, email: str, full_name: Optional[str] = None):
        super().__init__()
        self.username = username
        self.email = email
        self.full_name = full_name
        self.is_active = True
        self.is_superuser = False
    
    def to_dict(self) -> dict:
        """Convert user to dictionary."""
        base_dict = super().to_dict()
        base_dict.update({
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser
        })
        return base_dict
