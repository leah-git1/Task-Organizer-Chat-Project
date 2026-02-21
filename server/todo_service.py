from typing import List, Optional
from models import Task, TaskStatus, TaskType

_tasks: List[Task] = []
_next_id = 1


def get_tasks(
    status: Optional[TaskStatus] = None,
    task_type: Optional[TaskType] = None
):
    result = _tasks

    if status:
        result = [t for t in result if t.status == status]

    if task_type:
        result = [t for t in result if t.type == task_type]

    return result


def add_task(data: dict):
    global _next_id
    task = Task(id=_next_id, **data)
    _tasks.append(task)
    _next_id += 1
    return task


def update_task(task_id: int, updates: dict):
    for task in _tasks:
        if task.id == task_id:
            for key, value in updates.items():
                setattr(task, key, value)
            return task
    raise ValueError("Task not found")


def delete_task(task_id: int):
    global _tasks
    _tasks = [t for t in _tasks if t.id != task_id]
    return True