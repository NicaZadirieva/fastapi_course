from typing import Annotated

from fastapi import Depends

from .repository import TaskRepoDeps, TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)


def get_task_service(repo: TaskRepoDeps):
    return TaskService(repo)


TaskServiceDeps = Annotated[TaskService, Depends(get_task_service)]
