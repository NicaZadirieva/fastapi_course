from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    email: str
    is_active: bool
    password: str


class UserCreateResponse(BaseModel):
    id: int
    email: str


class UserLoginRequest(BaseModel):
    email: str
    password: str
    model_config = {"extra": "forbid"}


class UserLoginResponse(BaseModel):
    is_logined: bool
