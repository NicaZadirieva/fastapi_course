from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None
