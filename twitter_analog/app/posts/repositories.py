from fastapi import Depends
from typing_extensions import Annotated


class TaskRepository:
    pass


def get_task_repository():
    return TaskRepository()


TaskRepoDeps = Annotated[TaskRepository, Depends(get_task_repository)]
