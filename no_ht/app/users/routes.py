import logging
from fastapi import APIRouter, HTTPException


from .service import UserServiceDeps

from .schema import (
    JWTResponse,
    UserCreateRequest,
    UserLoginRequest,
)


router = APIRouter(prefix="/v2/auth", tags=["Auth"])
logger = logging.getLogger(__name__)


@router.post(
    "/register",
    response_model=JWTResponse,
    status_code=201,
    summary="Создает пользователя",
    description="""
    Создает пользователя. Если ошибка, то возвращает 400
    """,
)
async def register(data: UserCreateRequest, service: UserServiceDeps):
    jwt = await service.create(data)
    return JWTResponse(jwt=jwt)


@router.post(
    "/login",
    response_model=JWTResponse,
    status_code=200,
    summary="Авторизовывает пользователя",
    description="""
    Авторизовывает пользователя
    """,
)
async def login(data: UserLoginRequest, service: UserServiceDeps):
    jwt = await service.authenticate(data)
    if jwt is None:
        raise HTTPException(401, "Wrong email or password")
    else:
        return JWTResponse(jwt=jwt)
