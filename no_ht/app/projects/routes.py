from fastapi import APIRouter, Body, Depends

from .service import ProjectService, ProjectServiceDeps, get_project_service

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
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)


@router.get("/{project_id}", response_model=ProjectGetResponse, status_code=200)
async def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    print(service.get_project(path.project_id))
    return ProjectGetResponse(
        id=path.project_id, key="key", name="name", description="smth"
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
