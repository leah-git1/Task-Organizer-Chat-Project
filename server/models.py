from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import date


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskType(str, Enum):
    personal = "personal"
    work = "work"
    other = "other"


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    type: TaskType
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: TaskStatus = TaskStatus.pending