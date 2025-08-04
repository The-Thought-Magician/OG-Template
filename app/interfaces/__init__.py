"""
Interface definitions and contracts.
"""

# This directory will contain interface definitions
# Interfaces help define contracts between different parts of the application

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseService(ABC):
    """Base service interface."""
    
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Any:
        """Create a new resource."""
        pass
    
    @abstractmethod
    def get_by_id(self, resource_id: int) -> Optional[Any]:
        """Get resource by ID."""
        pass
    
    @abstractmethod
    def update(self, resource_id: int, data: Dict[str, Any]) -> Optional[Any]:
        """Update resource."""
        pass
    
    @abstractmethod
    def delete(self, resource_id: int) -> bool:
        """Delete resource."""
        pass


class BaseRepository(ABC):
    """Base repository interface."""
    
    @abstractmethod
    def save(self, entity: Any) -> Any:
        """Save entity to storage."""
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: int) -> Optional[Any]:
        """Find entity by ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Any]:
        """Find all entities."""
        pass
    
    @abstractmethod
    def delete_by_id(self, entity_id: int) -> bool:
        """Delete entity by ID."""
        pass
