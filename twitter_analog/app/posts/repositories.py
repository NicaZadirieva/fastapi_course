from fastapi import Depends
from typing_extensions import Annotated


class PostRepository:
    pass


def get_post_repository():
    return PostRepository()


PostRepoDeps = Annotated[PostRepository, Depends(get_post_repository)]
