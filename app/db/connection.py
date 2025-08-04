"""
Database connection management.
"""

from typing import Optional
from ..config.settings import settings


class DatabaseConnection:
    """Database connection manager."""
    
    def __init__(self, database_url: Optional[str] = None):
        self.database_url = database_url or settings.DATABASE_URL
        self.connection = None
    
    def connect(self):
        """Establish database connection."""
        print(f"Connecting to database: {self.database_url or 'In-memory'}")
        # Placeholder for actual database connection
        self.connection = {"status": "connected", "url": self.database_url}
        return self.connection
    
    def disconnect(self):
        """Close database connection."""
        print("Disconnecting from database")
        self.connection = None
    
    def is_connected(self) -> bool:
        """Check if database is connected."""
        return self.connection is not None


# Global database connection instance
db_connection = DatabaseConnection()


def get_database_connection() -> DatabaseConnection:
    """Get the global database connection."""
    return db_connection
