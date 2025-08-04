"""
Helper utility functions.
"""

from datetime import datetime
from typing import Any, Dict


def format_response(success: bool, message: str, data: Any = None) -> Dict[str, Any]:
    """Format a standard API response."""
    response = {
        "success": success,
        "message": message,
        "timestamp": get_current_timestamp()
    }
    
    if data is not None:
        response["data"] = data
    
    return response


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()


def sanitize_string(input_string: str) -> str:
    """Sanitize input string by removing potentially harmful characters."""
    if not input_string:
        return ""
    
    # Remove HTML tags and suspicious characters
    import re
    sanitized = re.sub(r'<[^>]*>', '', input_string)
    sanitized = re.sub(r'[<>"\']', '', sanitized)
    
    return sanitized.strip()


def generate_id() -> str:
    """Generate a unique ID."""
    import uuid
    return str(uuid.uuid4())


def truncate_string(text: str, max_length: int = 100) -> str:
    """Truncate string to specified length."""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."
