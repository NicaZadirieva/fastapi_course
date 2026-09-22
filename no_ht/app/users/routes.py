import logging
from fastapi import APIRouter


from .service import UserServiceDeps

from .schema import UserCreateRequest, UserCreateResponse


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
