from enum import Enum
from datetime import datetime
from typing import Optional
import uuid

class TaskStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Task:
    def __init__(self, id: str, title: str, description: str, priority: Priority, assignee_id: Optional[str]):
        if not title or title.strip() == "":
            raise ValueError("El título no puede estar vacío")
        
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = TaskStatus.OPEN
        self.assignee_id = assignee_id
        self.created_at = datetime.utcnow()

class TaskFactory:
    @staticmethod
    def create_task(title: str, description: str, priority: str, assignee_id: Optional[str] = None) -> Task:
        try:
            priority_enum = Priority[priority.upper()]
        except KeyError:
            raise ValueError("Prioridad inválida. Debe ser LOW, MEDIUM o HIGH")
            
        return Task(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            priority=priority_enum,
            assignee_id=assignee_id
        )