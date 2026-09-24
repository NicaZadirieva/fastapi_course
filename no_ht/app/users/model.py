from typing import TYPE_CHECKING
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean

if TYPE_CHECKING:
    from app.projects.model import ProjectMembers


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    project_members: Mapped[list["ProjectMembers"]] = relationship(
        "ProjectMembers", back_populates="user"
    )

    def __init__(self, email: str, hashed_password: str, is_active: bool):
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
