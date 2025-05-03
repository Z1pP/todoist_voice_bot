from punq import Container
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.application.use_cases.user_use_cases import (
    GetOrCreateUserUseCase,
    GetUserUseCase,
)
from core.domain.repositories import IUserRepository
from infrastructure.database.repositories.user_repository import (
    SQLAlchemyUserRepository,
)
from infrastructure.database.session import session_maker


def init_container():
    container = Container()

    # Регистрации сессии
    container.register(async_sessionmaker, instance=session_maker)

    # Регистрация репозитория с внедрением сессии
    container.register(IUserRepository, SQLAlchemyUserRepository)

    # Регистрация use_case
    container.register(GetUserUseCase)
    container.register(GetOrCreateUserUseCase)

    return container


container = init_container()
