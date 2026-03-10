from pydantic import BaseModel


class PostPath(BaseModel):
    """
    Путь к посту для выборки
    """

    post_id: int


class PostResponse(BaseModel):
    id: int
    content: str


class CreatePostRequest(BaseModel):
    content: str


class UpdatePostRequest(BaseModel):
    content: str
    id: int
