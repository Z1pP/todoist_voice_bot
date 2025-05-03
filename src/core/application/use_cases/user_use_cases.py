from typing import Optional

from core.domain.entities import User
from core.domain.repositories import IUserRepository


class GetUserUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    async def execute(self, tg_id: int) -> Optional[User]:
        return await self.user_repo.get_user_by_tgid(tg_id=tg_id)


class GetOrCreateUserUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    async def execute(self, tg_id: int, username: str) -> User:
        db_user = await self.user_repo.get_user_by_tgid(tg_id=tg_id)

        if not db_user:
            user = User(
                tgid=tg_id,
                username=username,
            )
            return await self.user_repo.create_user(user)

        return db_user
