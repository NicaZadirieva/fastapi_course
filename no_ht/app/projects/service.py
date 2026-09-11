from typing import Annotated

from fastapi import Depends

from .model import Project
from app.projects.schema import ProjectCreateRequest, ProjectUpdateRequest

from .repository import ProjectRepoDeps, ProjectRepository


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    async def get_project(self, project_id: int):
        return await self.repo.get_by_id(project_id)

    async def create(self, data: ProjectCreateRequest):
        project = Project(key=data.key, name=data.name, description=data.description)
        return await self.repo.save(project)

    async def update(self, project_id: int, data: ProjectUpdateRequest):
        project = await self.repo.get_by_id(project_id)
        if project is None:
            return None
        patch = data.model_dump(exclude_unset=True)
        for field, value in patch.items():
            setattr(project, field, value)
        return await self.repo.save(project)

    async def delete(self, project_id: int):
        project = await self.repo.get_by_id(project_id)
        if project is None:
            return False
        await self.repo.delete(project)
        return True


def get_project_service(repo: ProjectRepoDeps):
    return ProjectService(repo)


ProjectServiceDeps = Annotated[ProjectService, Depends(get_project_service)]
