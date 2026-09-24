from typing import Annotated

from fastapi import Depends

from app.users.model import User

from .model import Project
from app.projects.schema import ProjectCreateRequest, ProjectUpdateRequest

from .repository import ProjectRepoDeps, ProjectRepository


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    async def get_project(self, project_id: int, user_id: int):
        member = await self.repo.get_member(project_id, user_id)
        if member:
            return await self.repo.get_by_id(project_id)
        return None

    async def create(
        self,
        data: ProjectCreateRequest,
        user_id: int,
    ):
        project = Project(key=data.key, name=data.name, description=data.description)
        return await self.repo.save(project, user_id)

    async def update(self, project_id: int, data: ProjectUpdateRequest, user_id: int):
        project = await self.repo.get_by_id(project_id)
        if project is None:
            return None
        patch = data.model_dump(exclude_unset=True)
        for field, value in patch.items():
            setattr(project, field, value)
        return await self.repo.save(project, user_id)

    async def delete(self, project_id: int):
        project = await self.repo.get_by_id(project_id)
        if project is None:
            return False
        await self.repo.delete(project)
        return True


def get_project_service(repo: ProjectRepoDeps):
    return ProjectService(repo)


ProjectServiceDeps = Annotated[ProjectService, Depends(get_project_service)]
