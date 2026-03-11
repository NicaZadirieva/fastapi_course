from fastapi import APIRouter, Depends

from .service import TaskServiceDeps

from .schema import TaskPath, TaskResponse


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


@router.get("/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(
    service: TaskServiceDeps,
    path: TaskPath = Depends(),
):
    return TaskResponse(id=path.task_id)
