from abc import ABC, abstractmethod
from typing import Optional

from .entities import User


class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_tgid(self, tg_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, tg_id: int) -> None:
        pass
