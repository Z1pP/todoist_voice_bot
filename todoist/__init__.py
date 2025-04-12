import logging
from dataclasses import dataclass
from typing import Optional

from requests import Session
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.models import Project

from config import settings

logger = logging.getLogger(__name__)


@dataclass
class TodoistProject:
    id: str
    name: str


class TodoistManagerAsync:
    """
    Асинхронный менеджер для работы с todoist
    """

    def __init__(self, token: Optional[str] = None, session: Optional[Session] = None):
        self._token = token or settings.todoist_token
        self._session = session
        self._api = Optional[TodoistAPIAsync]
        self._initialize_async_api()

    def _initialize_async_api(self):
        try:
            self.async_api = TodoistAPIAsync(self._token, self._session)
        except Exception as e:
            logger.error(f"Ошибка при инициализации TodoistAPIAsync: {e}")
            raise

    @property
    def api(self) -> TodoistAPIAsync:
        if self._api is None:
            self._initialize_async_api()
        return self._api

    @staticmethod
    def _convert_project_to_dict(projects: list[Project]) -> dict[str, str]:
        """
        Конвертация списка проектов в словарь
        """
        return dict((project.name, project.id) for project in projects)

    async def get_todoist_projects(self) -> dict[str, str]:
        """
        Получения списка проектов пользователя
        """
        try:
            projects = await self.async_api.get_projects()
            return self._convert_project_to_dict(projects)
        except Exception as e:
            logger.error(f"Ошибка при получении проектов: {e}")
            return {}
