from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    email: str
    is_active: bool
    password: str


class JWTResponse(BaseModel):
    jwt: str


class UserLoginRequest(BaseModel):
    email: str
    password: str
    model_config = {"extra": "forbid"}
