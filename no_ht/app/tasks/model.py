from sqlalchemy import Boolean, String, Text
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)

    def __init__(
        self, title: str, description: str | None = None, is_completed: bool = False
    ):
        self.title = title
        self.description = description
        self.is_completed = is_completed
