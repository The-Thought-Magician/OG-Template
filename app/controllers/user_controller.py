"""
User controller for handling user-related HTTP requests.
"""

from typing import List
from app.models.response import success_response, error_response
from app.services.user_service import UserService
from app.schema.user import UserCreate, UserUpdate


class UserController:
    """Controller for user operations."""
    
    def __init__(self):
        self.user_service = UserService()
    
    def create_user(self, user_data: UserCreate) -> dict:
        """Create a new user."""
        try:
            # Check if username already exists
            existing_user = self.user_service.get_user_by_username(user_data.username)
            if existing_user:
                return error_response("Username already exists")
            
            user = self.user_service.create_user(user_data)
            return success_response("User created successfully", user.to_dict())
        
        except Exception as e:
            return error_response("Failed to create user", str(e))
    
    def get_user(self, user_id: int) -> dict:
        """Get user by ID."""
        try:
            user = self.user_service.get_user_by_id(user_id)
            if not user:
                return error_response("User not found")
            
            return success_response("User retrieved successfully", user.to_dict())
        
        except Exception as e:
            return error_response("Failed to retrieve user", str(e))
    
    def get_all_users(self) -> dict:
        """Get all users."""
        try:
            users = self.user_service.get_all_users()
            user_dicts = [user.to_dict() for user in users]
            return success_response("Users retrieved successfully", user_dicts)
        
        except Exception as e:
            return error_response("Failed to retrieve users", str(e))
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> dict:
        """Update a user."""
        try:
            user = self.user_service.update_user(user_id, user_data)
            if not user:
                return error_response("User not found")
            
            return success_response("User updated successfully", user.to_dict())
        
        except Exception as e:
            return error_response("Failed to update user", str(e))
    
    def delete_user(self, user_id: int) -> dict:
        """Delete a user."""
        try:
            success = self.user_service.delete_user(user_id)
            if not success:
                return error_response("User not found")
            
            return success_response("User deleted successfully")
        
        except Exception as e:
            return error_response("Failed to delete user", str(e))
