import logging
from fastapi import APIRouter


from .service import UserServiceDeps

from .schema import (
    UserCreateRequest,
    UserCreateResponse,
    UserLoginRequest,
    UserLoginResponse,
)


router = APIRouter(prefix="/v2/auth", tags=["Auth"])
logger = logging.getLogger(__name__)


@router.post(
    "/register",
    response_model=UserCreateResponse,
    status_code=201,
    summary="Создает пользователя",
    description="""
    Создает пользователя. Если ошибка, то возвращает 400
    """,
)
async def register(data: UserCreateRequest, service: UserServiceDeps):
    user = await service.create(data)
    return UserCreateResponse(id=user.id, email=user.email)


@router.post(
    "/login",
    response_model=UserLoginResponse,
    status_code=200,
    summary="Авторизовывает пользователя",
    description="""
    Авторизовывает пользователя
    """,
)
async def login(data: UserLoginRequest, service: UserServiceDeps):
    is_logined = await service.authenticate(data)
    return UserLoginResponse(is_logined=is_logined)
