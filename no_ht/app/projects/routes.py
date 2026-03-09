from fastapi import APIRouter

from .schema import ProjectCreateRequest, ProjectCreateResponse

router = APIRouter(prefix="/projects")


@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id="1", name=data.name)
