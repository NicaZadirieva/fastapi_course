from pydantic import BaseModel, Field


class GetTaskPath(BaseModel):
    task_id: int = Field(gt=0)


class GetTaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool = False
    project_id: int


class TaskCreateRequest(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False
    project_id: int


class TaskCreateResponse(BaseModel):
    id: int
    project_id: int
    title: str
    description: str | None = None
    is_completed: bool = False


class TaskSearchParams(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(20, ge=1, le=100)


class TaskSearchResponse(BaseModel):
    items: list[GetTaskResponse]
    total: int
    offset: int
    limit: int
