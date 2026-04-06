from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# DTOs
class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = ""
    priority: str
    assignee_id: Optional[str] = None

class TaskResponse(BaseModel):
    id: str
    title: str
    priority: str
    status: str
    created_at: datetime

class TaskService:
    @staticmethod
    def create_task(request: TaskCreateRequest) -> TaskResponse:
        task = TaskFactory.create_task(
            title=request.title,
            description=request.description,
            priority=request.priority,
            assignee_id=request.assignee_id
        )
        return TaskResponse(
            id=task.id,
            title=task.title,
            priority=task.priority.value,
            status=task.status.value,
            created_at=task.created_at
        )

# Endpoint
@app.post("/tasks", response_model=TaskResponse)
def create_task_endpoint(request: TaskCreateRequest):
    return TaskService.create_task(request)