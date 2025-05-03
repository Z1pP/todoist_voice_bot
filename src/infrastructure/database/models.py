from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class UserModel(BaseModel):
    __tablename__ = "user"

    tgid: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)

    todoists: Mapped["TodoistModel"] = relationship(
        "TodoistModel", back_populates="user"
    )


class TodoistModel(BaseModel):
    __tablename__ = "todoist"

    api_key: Mapped[str] = mapped_column(String(255), nullable=True)
    active_project: Mapped[str] = mapped_column(String(30), nullable=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="todoists")
