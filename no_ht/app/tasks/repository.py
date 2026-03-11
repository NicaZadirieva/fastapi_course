from typing import Annotated

from fastapi import Depends


class TaskRepository:
    def get_by_id(self, id: int):
        return id


def get_task_repository():
    return TaskRepository()


TaskRepoDeps = Annotated[TaskRepository, Depends(get_task_repository)]
