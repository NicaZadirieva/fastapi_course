from fastapi import APIRouter, Depends

from .schema import ProjectCreateRequest, ProjectCreateResponse, ProjectPath

router = APIRouter(prefix="/projects")


@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)


@router.get("/{project_id}")
async def get_project(path: ProjectPath = Depends()):
    return {"id": path.project_id}
