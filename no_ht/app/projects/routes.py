from fastapi import APIRouter, Body, Depends, Request

from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
)

router = APIRouter(prefix="/projects")


@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)


@router.get("/{project_id}")
async def get_project(path: ProjectPath = Depends()):
    return {"id": path.project_id}


@router.patch("/{project_id}")
async def update_project_desc_name(
    path: ProjectPath = Depends(), data: ProjectUpdateRequest = Body()
):
    # получение project

    return ProjectUpdateResponse(
        id=path.project_id,
        key="smth",
        name="smth" if data.name is None else data.name,
        description="smth" if data.description is None else data.description,
    )
