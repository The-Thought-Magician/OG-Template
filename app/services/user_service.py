"""
User service for managing user operations.
"""

from typing import List, Optional
from app.models.user import User
from app.schema.user import UserCreate, UserUpdate


class UserService:
    """Service for managing user operations."""
    
    def __init__(self):
        # In-memory storage for demo purposes
        self.users: List[User] = []
        self.next_id = 1
    
    def create_user(self, user_data: UserCreate) -> User:
        """Create a new user."""
        user = User(
            username=user_data.username,
            email=user_data.email,
            full_name=user_data.full_name
        )
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return next((user for user in self.users if user.id == user_id), None)
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return next((user for user in self.users if user.username == username), None)
    
    def get_all_users(self) -> List[User]:
        """Get all users."""
        return self.users
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update a user."""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        if user_data.email:
            user.email = user_data.email
        if user_data.full_name:
            user.full_name = user_data.full_name
            
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """Delete a user."""
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
