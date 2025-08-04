"""
Validation utility functions.
"""

import re


def validate_email(email: str) -> bool:
    """Validate email format."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None


def validate_username(username: str) -> bool:
    """Validate username format."""
    # Username should be 3-30 characters, alphanumeric and underscores only
    if not username or len(username) < 3 or len(username) > 30:
        return False
    
    username_pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(username_pattern, username) is not None


def validate_password(password: str) -> bool:
    """Validate password strength."""
    # Password should be at least 8 characters long
    if not password or len(password) < 8:
        return False
    
    # Should contain at least one uppercase, one lowercase, and one digit
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_upper and has_lower and has_digit
