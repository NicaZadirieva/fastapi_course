import logging
from fastapi import APIRouter, Depends, HTTPException

from app.core.settings import SettingsDeps

from .service import TaskServiceDeps

from .schema import TaskPath, TaskResponse


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get("/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(
    service: TaskServiceDeps,
    settings: SettingsDeps,
    path: TaskPath = Depends(),
):
    logger.info("ID: %s", path.task_id, extra={"user_id": 1})
    try:
        if path.task_id > 100:
            raise ValueError(">100")
    except ValueError as e:
        logger.error("Ошибка %s", e, exc_info=True)
        raise HTTPException(404, "Не найдено")

    return TaskResponse(id=path.task_id)
