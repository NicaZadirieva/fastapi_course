from datetime import datetime
from sqlalchemy import Boolean, DateTime, Integer, String, Text
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # текст поста
    content: Mapped[str] = mapped_column(String(280), nullable=False)
    # дата создания
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    # дата редактирования
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime, default=datetime.now, nullable=True
    )
    # количество лайков
    likes_count: Mapped[int] = mapped_column(Integer, default=0)
    # мягкое удаление (soft delete)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
