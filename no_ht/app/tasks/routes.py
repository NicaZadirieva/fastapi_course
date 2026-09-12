import logging
from fastapi import APIRouter, Depends, HTTPException

from app.core.db import DbSessionDeps, check_db
from app.core.settings import SettingsDeps
from app.projects.schema import ProjectCreateResponse

from .service import TaskServiceDeps

from .schema import TaskCreateRequest, TaskCreateResponse, TaskPath, TaskResponse


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get("/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(
    service: TaskServiceDeps,
    settings: SettingsDeps,
    db_session: DbSessionDeps,
    path: TaskPath = Depends(),
):
    data = await check_db(db_session)
    logger.info("db check: %s", data)
    logger.info("ID: %s", path.task_id, extra={"user_id": 1})
    try:
        if path.task_id > 100:
            raise ValueError(">100")
    except ValueError as e:
        logger.error("Ошибка %s", e, exc_info=True)
        raise HTTPException(404, "Не найдено")

    return TaskResponse(id=path.task_id)


@router.post(
    "/",
    response_model=TaskCreateResponse,
    status_code=201,
    summary="Создает задачу",
    description="""
    Создает задачу. Если ошибка, то возвращает 500
    """,
)
async def create_task(data: TaskCreateRequest, service: TaskServiceDeps):
    task = await service.create(data)
    if task is None:
        raise HTTPException(404, "Проекта с таким id нет")
    return TaskCreateResponse(
        id=task.id,
        project_id=task.project_id,
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
    )
