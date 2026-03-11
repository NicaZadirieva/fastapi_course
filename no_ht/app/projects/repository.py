from typing import Annotated

from fastapi import Depends

from .db import DbSessionDeps


class ProjectRepository:
    def get_by_id(self, project_id: int):
        return project_id


def get_project_repository(db: DbSessionDeps):
    return ProjectRepository()


ProjectRepoDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
