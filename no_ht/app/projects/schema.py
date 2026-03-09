from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None

    @field_validator("key")
    @classmethod
    def key_not_empty(cls, value):
        if not value.strip():
            raise HTTPException(400, "key must be valid string")
        return value


class ProjectCreateResponse(BaseModel):
    id: int
    name: str


class ProjectPath(BaseModel):
    project_id: int = Field(gt=0)
