from typing import Annotated

from fastapi import Depends

from .repository import ProjectRepoDeps, ProjectRepository


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def get_project(self, project_id: int):
        return self.repo.get_by_id(project_id)


def get_project_service(repo: ProjectRepoDeps):
    return ProjectService(repo)


ProjectServiceDeps = Annotated[ProjectService, Depends(get_project_service)]
