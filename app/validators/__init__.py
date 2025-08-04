"""
Custom validators for the application.
"""

from typing import Any, Callable, Dict, List


class ValidationError(Exception):
    """Custom validation error."""
    pass


class Validator:
    """Base validator class."""
    
    def __init__(self, rules: Dict[str, List[Callable]]):
        self.rules = rules
    
    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate data against rules."""
        errors = {}
        
        for field, validators in self.rules.items():
            if field in data:
                for validator in validators:
                    try:
                        validator(data[field])
                    except ValidationError as e:
                        if field not in errors:
                            errors[field] = []
                        errors[field].append(str(e))
        
        return errors


def required(value: Any) -> None:
    """Check if value is required."""
    if value is None or value == "":
        raise ValidationError("This field is required")


def min_length(min_len: int) -> Callable:
    """Check minimum length."""
    def validator(value: str) -> None:
        if len(value) < min_len:
            raise ValidationError(f"Minimum length is {min_len}")
    return validator


def max_length(max_len: int) -> Callable:
    """Check maximum length."""
    def validator(value: str) -> None:
        if len(value) > max_len:
            raise ValidationError(f"Maximum length is {max_len}")
    return validator


def email_format(value: str) -> None:
    """Validate email format."""
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, value):
        raise ValidationError("Invalid email format")
