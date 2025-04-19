from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TgProfile(Base):
    __tablename__ = "tgprofile"
    id: Mapped[int] = mapped_column(primary_key=True)
    tgid: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    api_key: Mapped[str] = mapped_column(String(255), nullable=True)
    active_project: Mapped[str] = mapped_column(String(30), nullable=True)
