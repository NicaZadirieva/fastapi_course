from typing import Annotated

from fastapi import Depends

from .repositories import TaskRepoDeps, TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo


def get_task_service(repo: TaskRepoDeps):
    return TaskService(repo)


TaskServiceDeps = Annotated[TaskService, Depends(get_task_service)]
