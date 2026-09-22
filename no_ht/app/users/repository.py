import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select

from app.core.db import DbSessionDeps
from app.users.model import User

logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, db_session: DbSessionDeps):
        self.db_session = db_session

    async def get_by_id(self, id: int):
        user = await self.db_session.get(User, id)
        return user

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        user = await self.db_session.execute(query)
        return user.scalar_one_or_none()

    async def save(self, user: User):
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        logger.info(user)
        return user


def get_user_repository(db_session: DbSessionDeps):
    return UserRepository(db_session)


UserRepoDeps = Annotated[UserRepository, Depends(get_user_repository)]
