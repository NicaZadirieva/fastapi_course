from sqlalchemy import String, Text
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(
        String(64), unique=True, nullable=False, index=True
    )
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __init__(
        self, key: str, name: str | None = None, description: str | None = None
    ):
        self.key = key
        self.name = name
        self.description = description
