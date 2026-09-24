import logging
from typing import Annotated

from fastapi import Depends

from app.core.db import DbSessionDeps
from app.projects.model import Project, ProjectMembers

logger = logging.getLogger(__name__)


class ProjectRepository:
    def __init__(self, db_session: DbSessionDeps):
        self.db_session = db_session

    async def get_by_id(self, project_id: int):
        return await self.db_session.get(Project, project_id)

    async def get_member(self, project_id: int, user_id: int):
        return await self.db_session.get(
            ProjectMembers,
            (
                user_id,
                project_id,
            ),
        )

    async def save(self, project: Project, user_id: int):
        self.db_session.add(project)
        await self.db_session.flush()

        member = ProjectMembers(user_id=user_id, project_id=project.id, role="owner")
        self.db_session.add(member)

        await self.db_session.commit()
        await self.db_session.refresh(project)
        return project

    async def delete(self, project: Project):
        await self.db_session.delete(project)
        await self.db_session.commit()


def get_project_repository(db_session: DbSessionDeps):
    return ProjectRepository(db_session)


ProjectRepoDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
