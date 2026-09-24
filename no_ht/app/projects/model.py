from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, Text
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.tasks.model import Task
    from app.projects.model import Project
    from app.users.model import User


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(
        String(64), unique=True, nullable=False, index=True
    )
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    tasks: Mapped[list["Task"]] = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    project_members: Mapped[list["ProjectMembers"]] = relationship(
        "ProjectMembers", back_populates="projects"
    )

    def __init__(
        self, key: str, name: str | None = None, description: str | None = None
    ):
        self.key = key
        self.name = name
        self.description = description


class ProjectMembers(Base):
    __tablename__ = "project_members"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True
    )
    role: Mapped[str] = mapped_column(String(50), default="member")
    user: Mapped["User"] = relationship("User", back_populates="project_members")
    project: Mapped["Project"] = relationship(
        "Project", back_populates="project_members"
    )
