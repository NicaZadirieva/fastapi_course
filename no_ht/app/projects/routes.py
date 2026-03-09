from fastapi import APIRouter

from .schema import ProjectCreateRequest

router = APIRouter(prefix="/projects")


@router.post("/")
async def create_project(data: ProjectCreateRequest):
    return data
