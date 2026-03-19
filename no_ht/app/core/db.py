from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy import select, text
from app.core.settings import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

settings = Settings()  # type: ignore[call-arg]

engine = create_async_engine(
    settings.db.url,
    echo=False,  # вывод sql-команд отключена
    pool_pre_ping=True,
)

async_session_local = async_sessionmaker(
    engine,
    expire_on_commit=False,  # создание новой сессии после каждого коммита в БД отключена
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_local() as session:
        yield session


async def check_db(session: AsyncSession) -> int:
    result = await session.execute(select(1))
    return result.scalar_one()


DbSessionDeps = Annotated[AsyncSession, Depends(get_session)]
