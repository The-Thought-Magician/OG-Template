"""
User API routes.
"""

from fastapi import APIRouter, HTTPException
from app.controllers.user_controller import UserController
from app.schema.user import UserCreate, UserUpdate

router = APIRouter()
user_controller = UserController()


@router.post("/users/")
def create_user(user_data: dict):
    """Create a new user."""
    try:
        user_create = UserCreate(
            username=user_data.get("username"),
            email=user_data.get("email"),
            full_name=user_data.get("full_name")
        )
        return user_controller.create_user(user_create)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/")
def get_all_users():
    """Get all users."""
    return user_controller.get_all_users()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    """Get user by ID."""
    result = user_controller.get_user(user_id)
    if not result.get("success"):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result


@router.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    """Update a user."""
    try:
        user_update = UserUpdate(
            email=user_data.get("email"),
            full_name=user_data.get("full_name")
        )
        result = user_controller.update_user(user_id, user_update)
        if not result.get("success"):
            raise HTTPException(status_code=404, detail=result.get("message"))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete a user."""
    result = user_controller.delete_user(user_id)
    if not result.get("success"):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result
