from typing import Annotated

from fastapi import Depends, HTTPException

from app.projects.repository import ProjectRepoDeps, ProjectRepository
from app.users.jwt import create_access_token
from app.users.model import User
from app.users.schema import UserCreateRequest, UserLoginRequest
from app.users.security import hash_password, verify_password

from .repository import UserRepoDeps, UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user(self, user_id: int):
        return await self.user_repo.get_by_id(user_id)

    async def create(self, data: UserCreateRequest):
        user = await self.user_repo.get_by_email(data.email)
        if user:
            raise HTTPException(400, "User already exists")
        new_user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
            is_active=data.is_active,
        )
        saved_user = await self.user_repo.save(new_user)
        jwt = create_access_token(saved_user.id)
        return jwt

    async def authenticate(self, data: UserLoginRequest):
        user = await self.user_repo.get_by_email(data.email)
        if user is None:
            return None
        if not verify_password(data.password, user.hashed_password):
            return None
        jwt = create_access_token(user.id)
        return jwt


def get_user_service(user_repo: UserRepoDeps):
    return UserService(user_repo)


UserServiceDeps = Annotated[UserService, Depends(get_user_service)]
