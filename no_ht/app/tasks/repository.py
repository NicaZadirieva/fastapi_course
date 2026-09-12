import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemy import func, select

from app.core.db import DbSessionDeps
from app.tasks.model import Task

logger = logging.getLogger(__name__)


class TaskRepository:
    def __init__(self, db_session: DbSessionDeps):
        self.db_session = db_session

    async def get_by_id(self, id: int):
        task = await self.db_session.get(Task, id)
        return task

    async def save(self, task: Task):
        self.db_session.add(task)
        await self.db_session.commit()
        await self.db_session.refresh(task)
        logger.info(task)
        return task

    async def search(self, offset: int = 0, limit: int = 20):
        count_query = select(func.count()).select_from(Task)
        total_result = await self.db_session.execute(count_query)
        total = total_result.scalar_one()

        query = select(Task).order_by(Task.id).offset(offset).limit(limit)
        result = await self.db_session.execute(query)
        tasks = list(result.scalars().all())

        return tasks, total


def get_task_repository(db_session: DbSessionDeps):
    return TaskRepository(db_session)


TaskRepoDeps = Annotated[TaskRepository, Depends(get_task_repository)]
