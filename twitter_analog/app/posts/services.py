from typing import Annotated

from fastapi import Depends

from .repositories import PostRepoDeps, PostRepository


class PostService:
    def __init__(self, repo: PostRepository):
        self.repo = repo


def get_post_service(repo: PostRepoDeps):
    return PostService(repo)


PostServiceDeps = Annotated[PostService, Depends(get_post_service)]
