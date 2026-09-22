from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    email: str
    is_active: bool
    password: str


class UserCreateResponse(BaseModel):
    id: int
    email: str
