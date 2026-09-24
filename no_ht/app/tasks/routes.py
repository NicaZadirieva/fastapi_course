import logging
from fastapi import APIRouter, Depends, HTTPException

from app.users.current_user import CurrentUserDeps


from .service import TaskServiceDeps

from .schema import (
    GetTaskResponse,
    TaskCreateRequest,
    TaskCreateResponse,
    TaskSearchParams,
    TaskSearchResponse,
)


router = APIRouter(prefix="/v2/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


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


@router.get(
    "/",
    response_model=TaskSearchResponse,
    status_code=200,
    summary="Ищет задачи",
    description="""
    Ищет задачу. Если ошибка, то возвращает 500
    """,
)
async def search_task(
    service: TaskServiceDeps,
    current_user: CurrentUserDeps,
    params: TaskSearchParams = Depends(),
):
    logger.info(current_user)
    tasks, total = await service.search(params)
    return TaskSearchResponse(
        items=[
            GetTaskResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                is_completed=task.is_completed,
                project_id=task.project_id,
            )
            for task in tasks
        ],
        total=total,
        offset=params.offset,
        limit=params.limit,
    )


@router.get("/{task_id}", response_model=GetTaskResponse | None, status_code=200)
async def get_task(
    task_id: int,
    service: TaskServiceDeps,
):
    task = await service.get_task(task_id)
    if task is None:
        return None
    return GetTaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        project_id=task.project_id,
    )
