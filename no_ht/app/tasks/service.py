from typing import Annotated

from fastapi import Depends

from app.projects.repository import ProjectRepoDeps, ProjectRepository
from app.tasks.model import Task
from app.tasks.schema import TaskCreateRequest

from .repository import TaskRepoDeps, TaskRepository


class TaskService:
    def __init__(self, task_repo: TaskRepository, project_repo: ProjectRepository):
        self.task_repo = task_repo
        self.project_repo = project_repo

    async def get_task(self, task_id: int):
        return await self.task_repo.get_by_id(task_id)

    async def create(self, data: TaskCreateRequest):
        project = await self.project_repo.get_by_id(data.project_id)
        if project is None:
            return None
        task = Task(
            title=data.title,
            description=data.description,
            is_completed=data.is_completed,
            project_id=data.project_id,
        )
        return await self.task_repo.save(task)


def get_task_service(task_repo: TaskRepoDeps, project_repo: ProjectRepoDeps):
    return TaskService(task_repo, project_repo)


TaskServiceDeps = Annotated[TaskService, Depends(get_task_service)]
