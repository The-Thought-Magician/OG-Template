"""
Workflow definitions and management.
"""

from typing import Any, Dict, List, Callable
from enum import Enum


class WorkflowStatus(Enum):
    """Workflow execution status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class WorkflowStep:
    """Individual workflow step."""
    
    def __init__(self, name: str, action: Callable, **kwargs):
        self.name = name
        self.action = action
        self.kwargs = kwargs
        self.status = WorkflowStatus.PENDING
        self.result = None
        self.error = None
    
    def execute(self, context: Dict[str, Any]) -> Any:
        """Execute the workflow step."""
        try:
            self.status = WorkflowStatus.RUNNING
            self.result = self.action(context, **self.kwargs)
            self.status = WorkflowStatus.COMPLETED
            return self.result
        except Exception as e:
            self.status = WorkflowStatus.FAILED
            self.error = str(e)
            raise


class Workflow:
    """Workflow management class."""
    
    def __init__(self, name: str):
        self.name = name
        self.steps: List[WorkflowStep] = []
        self.status = WorkflowStatus.PENDING
        self.context: Dict[str, Any] = {}
    
    def add_step(self, step: WorkflowStep) -> None:
        """Add a step to the workflow."""
        self.steps.append(step)
    
    def execute(self, initial_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute the entire workflow."""
        if initial_context is None:
            initial_context = {}
        
        self.context.update(initial_context)
        
        self.status = WorkflowStatus.RUNNING
        
        try:
            for step in self.steps:
                result = step.execute(self.context)
                self.context[f"{step.name}_result"] = result
            
            self.status = WorkflowStatus.COMPLETED
            return {"status": "success", "context": self.context}
        
        except Exception as e:
            self.status = WorkflowStatus.FAILED
            return {"status": "failed", "error": str(e), "context": self.context}


# Example workflow functions
def log_message(context: Dict[str, Any], message: str) -> str:
    """Log a message."""
    print(f"Workflow Log: {message}")
    return message


def process_data(context: Dict[str, Any], data_key: str) -> Any:
    """Process data from context."""
    data = context.get(data_key)
    if data:
        print(f"Processing data: {data}")
        return f"processed_{data}"
    return None
