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
async def update_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
    data: ProjectUpdateRequest = Body(),
):
    # получение project
    project = await service.update(path.project_id, data)
    if project is None:
        raise HTTPException(404, "Project not found")

    return ProjectUpdateResponse(
        id=project.id,
        key=project.key,
        name=project.name,
        description=project.description,
    )


@router.delete(
    "/{project_id}",
    description="Удаляет проект по id. Если проекта нет, возвращает ошибку",
)
async def delete_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    success = await service.delete(path.project_id)
    if not success:
        raise HTTPException(404, "Project not found")
