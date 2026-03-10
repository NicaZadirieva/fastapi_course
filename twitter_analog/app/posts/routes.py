from fastapi import APIRouter, Body, Depends

from .schema import CreatePostRequest, PostPath, PostResponse, UpdatePostRequest

router = APIRouter(prefix="/posts")


@router.get("/{post_id}", response_model=PostResponse, status_code=200)
def get_post(post: PostPath = Depends()):
    """
    Получение поста по его уникальному идентификатору.

    Параметры пути:
    - **post_id** (int): Целочисленный идентификатор поста, например `42`.

    Возвращаемое значение:
    - При успешном выполнении возвращает объект поста (модель Post).
    - В случае, если пост с указанным ID не найден, возвращается ошибка 404 Not Found.

    Возможные статус-коды ответа:
    - **200 OK**: Пост успешно получен.
    - **404 Not Found**: Пост с таким ID отсутствует в базе данных.
    """
    # реализация функции...
    return PostResponse(content="new post", id=post.post_id)


@router.post("/", response_model=PostResponse, status_code=201)
async def create_post(
    data: CreatePostRequest = Body(),
):
    """
    Создание нового поста.

    **Тело запроса (JSON):**
    - **content** (str, обязательное): Содержимое поста.

    Возвращаемое значение:
    - Объект созданного поста с присвоенным `id` и временными метками.

    Возможные статус-коды ответа:
    - **201 Created**: Пост успешно создан.
    - **422 Unprocessable Entity**: Ошибка валидации входных данных (например, отсутствуют обязательные поля или неверный формат).
    """
    # реализация...
    return PostResponse(content=data.content, id=1)


@router.put("/", response_model=PostResponse, status_code=200)
async def update_post(
    data: UpdatePostRequest,
):
    """
    Обновление существующего поста.

    **Тело запроса (JSON):**
    - **id** (int, обязательное): Идентификатор обновляемого поста.
    - **content** (str, необязательное): Новое содержимое (если требуется изменить).

    Возвращаемое значение:
    - Обновлённый объект поста.

    Возможные статус-коды ответа:
    - **200 OK**: Пост успешно обновлён.
    - **404 Not Found**: Пост с указанным `id` не найден.
    - **422 Unprocessable Entity**: Ошибка валидации входных данных.
    """
    # реализация...
    # TODO: добавить получение по id
    return PostResponse(id=data.id, content=data.content)


@router.delete("/{post_id}", status_code=204)
def delete_post(post: PostPath = Depends()):
    """
    Удаление поста по его идентификатору.

    Параметры пути:
    - **post_id** (int): Идентификатор поста, который требуется удалить.

    Возвращаемое значение:
    - При успешном удалении тело ответа отсутствует.

    Возможные статус-коды ответа:
    - **204 No Content**: Пост успешно удалён.
    - **404 Not Found**: Пост с указанным `id` не найден.
    """
    # реализация...
    return None  # или просто return (без значения)
