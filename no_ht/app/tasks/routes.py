import logging
from fastapi import APIRouter, Depends, HTTPException

from app.core.db import DbSessionDeps
from app.core.settings import SettingsDeps


from .service import TaskServiceDeps

from .schema import (
    GetTaskPath,
    GetTaskResponse,
    TaskCreateRequest,
    TaskCreateResponse,
)


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get("/{task_id}", response_model=GetTaskResponse | None, status_code=200)
async def get_task(
    service: TaskServiceDeps,
    settings: SettingsDeps,
    db_session: DbSessionDeps,
    path: GetTaskPath = Depends(),
):
    task = await service.get_task(path.task_id)
    if task is None:
        return None
    return GetTaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        project_id=task.project_id,
    )


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
