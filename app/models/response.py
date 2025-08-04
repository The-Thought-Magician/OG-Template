"""
API response models.
"""

from typing import Any, Optional


class ApiResponse:
    """Standard API response model."""
    
    def __init__(
        self, 
        success: bool = True, 
        message: str = "Success", 
        data: Optional[Any] = None,
        error: Optional[str] = None
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error = error
    
    def to_dict(self) -> dict:
        """Convert response to dictionary."""
        response = {
            "success": self.success,
            "message": self.message
        }
        
        if self.data is not None:
            response["data"] = self.data
            
        if self.error is not None:
            response["error"] = self.error
            
        return response


def success_response(message: str = "Success", data: Optional[Any] = None) -> dict:
    """Create a success response."""
    return ApiResponse(success=True, message=message, data=data).to_dict()


def error_response(message: str = "Error", error: Optional[str] = None) -> dict:
    """Create an error response."""
    return ApiResponse(success=False, message=message, error=error).to_dict()
