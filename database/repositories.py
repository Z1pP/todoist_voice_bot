from typing import Optional

from sqlalchemy import insert, select

from database import get_session
from database.models import TgProfile


class TgProfileRepository:
    """
    Репозиторий для работы с БД
    """

    def get_by_tgid(self, tgid: int) -> Optional[TgProfile]:
        query = select(TgProfile).where(tgid == tgid)
        with get_session() as session:
            result = session.execute(query)
            return result.scalar_one_or_none()

    def add_new_profile(self, tgid: int) -> TgProfile:
        query = insert(TgProfile).values(tgid=tgid).returning(TgProfile)
        with get_session() as session:
            result = session.execute(query)
            return result.scalar_one()
