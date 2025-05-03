from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.domain.entities import User
from core.domain.repositories import IUserRepository
from infrastructure.database.models import UserModel


class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, session_maker: async_sessionmaker):
        self.session_maker = session_maker

    async def get_user_by_tgid(self, tg_id: int) -> Optional[User]:
        """
        Получение пользователя по tg_id
        """
        async with self.session_maker() as session:
            try:
                query = select(UserModel).where(UserModel.tgid == tg_id)
                result = await session.execute(query)
                user = result.scalars().first()

                if user:
                    return User(
                        id=user.id,
                        tgid=user.tgid,
                        username=user.username,
                        created_at=user.created_at,
                        updated_at=user.updated_at,
                    )
                else:
                    return None
            except Exception as e:
                raise e

    async def create_user(self, user: User) -> User:
        async with self.session_maker() as session:
            try:
                db_user = UserModel(
                    tgid=user.tgid,
                    username=user.username,
                )
                session.add(db_user)
                await session.commit()
                await session.refresh(db_user)

                user.id = db_user.id
                return user
            except Exception as e:
                await session.rollback()
                raise e

    async def update_user(self, user: User) -> User:
        async with self.session_maker() as session:
            try:
                db_user = await session.get(UserModel, user.tgid)

                if not db_user:
                    raise ValueError("User not found")

                for field, value in user.__dict__.items():
                    if field != "id" and value is not None:
                        setattr(db_user, field, value)

                await session.commit()
                await session.refresh(db_user)

                return User(
                    id=db_user.id,
                    tgid=db_user.tgid,
                    username=db_user.username,
                    created_at=db_user.created_at,
                    updated_at=db_user.updated_at,
                )

            except Exception as e:
                await session.rollback()
                raise e

    async def delete_user(self, tg_id: int) -> None:
        async with self.session_maker() as session:
            try:
                db_user = await session.get(UserModel, tg_id)

                if not db_user:
                    raise ValueError("User not found")

                await session.delete(db_user)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
