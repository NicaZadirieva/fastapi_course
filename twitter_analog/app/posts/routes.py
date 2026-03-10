from fastapi import APIRouter, Body, Depends

from .schema import CreatePostRequest, PostPath, PostResponse, UpdatePostRequest

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get(
    "/{post_id}",
    response_model=PostResponse,
    status_code=200,
    summary="Получение поста по его уникальному идентификатору.",
    description="""
    Получение поста по его уникальному идентификатору.
    
    Возвращаемое значение:
    - При успешном выполнении возвращает объект поста
    - В случае, если пост с указанным ID не найден, возвращается ошибка 404 Not Found.
    """,
)
def get_post(post: PostPath = Depends()):
    # реализация функции...
    return PostResponse(content="new post", id=post.post_id)


@router.post(
    "/",
    response_model=PostResponse,
    status_code=201,
    summary="Создание нового поста.",
    description="""
    Создание нового поста.

    Возвращаемое значение:
    - Объект созданного поста с присвоенным `id` и временными метками.

    """,
)
async def create_post(
    data: CreatePostRequest = Body(),
):
    # реализация...
    return PostResponse(content=data.content, id=1)


@router.put(
    "/",
    response_model=PostResponse,
    status_code=200,
    summary="Обновление существующего поста.",
    description="""
    Обновление существующего поста.

    Возвращаемое значение:
    - Обновлённый объект поста.
    """,
)
async def update_post(
    data: UpdatePostRequest,
):
    # реализация...
    # TODO: добавить получение по id
    return PostResponse(id=data.id, content=data.content)


@router.delete(
    "/{post_id}",
    status_code=204,
    summary="Удаление поста по его идентификатору.",
    description="""
    Удаление поста по его идентификатору.

    Возвращаемое значение:
    - При успешном удалении тело ответа отсутствует.
    """,
)
def delete_post(post: PostPath = Depends()):

    # реализация...
    return None  # или просто return (без значения)
