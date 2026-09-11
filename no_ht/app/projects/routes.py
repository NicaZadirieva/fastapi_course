from fastapi import APIRouter, Body, Depends, HTTPException

from .repository import ProjectRepoDeps

from .service import ProjectServiceDeps

from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectGetResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
)

router = APIRouter(prefix="/v1/projects", tags=["Projects"])


@router.post(
    "/",
    response_model=ProjectCreateResponse,
    status_code=201,
    summary="Создает проект",
    description="""
    Создает проект. Если ошибка, то возвращает 500
    """,
)
async def create_project(data: ProjectCreateRequest, service: ProjectServiceDeps):
    res = await service.create(data)
    return ProjectCreateResponse(id=res.id, name=res.name)


@router.get("/{project_id}", response_model=ProjectGetResponse, status_code=200)
async def get_project(
    service: ProjectServiceDeps,
    repo: ProjectRepoDeps,
    path: ProjectPath = Depends(),
):
    project = await service.get_project(path.project_id)
    if project is None:
        raise HTTPException(404, "Project not found")
    return ProjectGetResponse(
        id=project.id,
        key=project.key,
        name=project.name,
        description=project.description,
    )


@router.patch("/{project_id}", response_model=ProjectUpdateResponse)
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
