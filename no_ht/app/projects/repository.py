import logging
from typing import Annotated

from fastapi import Depends

from app.core.db import DbSessionDeps
from app.projects.model import Project

logger = logging.getLogger(__name__)


class ProjectRepository:
    def __init__(self, db_session: DbSessionDeps):
        self.db_session = db_session

    def get_by_id(self, project_id: int):
        return project_id

    async def create(self):
        project = Project(
            key="ps", name="purpleschool", description="Обучающая платформа"
        )
        self.db_session.add(project)
        await self.db_session.commit()
        await self.db_session.refresh(project)
        logger.info(project)


def get_project_repository(db_session: DbSessionDeps):
    return ProjectRepository(db_session)


ProjectRepoDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
