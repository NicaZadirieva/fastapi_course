import logging
from fastapi import APIRouter, Depends

from app.core.settings import SettingsDeps

from .service import TaskServiceDeps

from .schema import TaskPath, TaskResponse


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[TASKS] %(levelname)s:%(name)s:%(message)s"))

logger.addHandler(handler)


@router.get("/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(
    service: TaskServiceDeps,
    settings: SettingsDeps,
    path: TaskPath = Depends(),
):
    logger.info("ID: %s", path.task_id)
    return TaskResponse(id=path.task_id)
