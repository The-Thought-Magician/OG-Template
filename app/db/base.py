"""
Base database class for common operations.
"""

from typing import Any, Dict, List, Optional


class DatabaseBase:
    """Base class for database operations."""
    
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.data: List[Dict[str, Any]] = []  # In-memory storage for demo
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new record."""
        # Generate ID if not provided
        if 'id' not in data:
            data['id'] = len(self.data) + 1
        
        self.data.append(data)
        return data
    
    def find_by_id(self, record_id: int) -> Optional[Dict[str, Any]]:
        """Find record by ID."""
        return next((item for item in self.data if item.get('id') == record_id), None)
    
    def find_by(self, **kwargs) -> List[Dict[str, Any]]:
        """Find records by criteria."""
        results = []
        for item in self.data:
            match = True
            for key, value in kwargs.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                results.append(item)
        return results
    
    def update(self, record_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update a record by ID."""
        record = self.find_by_id(record_id)
        if record:
            record.update(data)
            return record
        return None
    
    def delete(self, record_id: int) -> bool:
        """Delete a record by ID."""
        record = self.find_by_id(record_id)
        if record:
            self.data.remove(record)
            return True
        return False
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Get all records."""
        return self.data.copy()
    
    def count(self) -> int:
        """Count total records."""
        return len(self.data)
