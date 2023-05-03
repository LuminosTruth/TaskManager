from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    task_name: str
    task_description: str
    task_start: datetime
    task_end: datetime
    task_create: datetime
    task_progress: int
    task_author: int
