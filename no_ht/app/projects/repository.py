from typing import Annotated

from fastapi import Depends


class ProjectRepository:
    def get_by_id(self, project_id: int):
        return project_id


def get_project_repository():
    return ProjectRepository()


ProjectRepoDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
