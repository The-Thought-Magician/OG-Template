"""
User schemas for validation.
"""

from typing import Optional


class UserCreate:
    """Schema for creating a user."""
    
    def __init__(self, username: str, email: str, full_name: Optional[str] = None):
        self.username = username
        self.email = email
        self.full_name = full_name


class UserUpdate:
    """Schema for updating a user."""
    
    def __init__(self, email: Optional[str] = None, full_name: Optional[str] = None):
        self.email = email
        self.full_name = full_name


class UserResponse:
    """Schema for user response."""
    
    def __init__(self, id: int, username: str, email: str, full_name: Optional[str] = None):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.is_active = True
