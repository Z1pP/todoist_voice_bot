import logging
from dataclasses import dataclass
from typing import Optional

from requests import Session
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.models import Project, Task

from bot.parser.task_parser import TaskData
from config import settings
from todoist.exceptions import ApiInitializationException, ProjectCreationException

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
        self.async_api = None
        self._initialize_async_api()

    def _initialize_async_api(self):
        try:
            self.async_api = TodoistAPIAsync(self._token, self._session)
        except Exception as e:
            logger.error(f"Ошибка при инициализации TodoistAPIAsync: {e}")
            raise ApiInitializationException()

    @property
    def api(self) -> TodoistAPIAsync:
        if self.async_api is None:
            self._initialize_async_api()
        return self.async_api

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

    async def get_project_id(self, project_name: str) -> str:
        projects = await self.async_api.get_projects()
        project = next(
            (
                project
                for project in projects
                if project.name.lower() == project_name.lower()
            ),
            None,
        )
        if project:
            return project.id

        return self.create_new_project(project_name=project_name)

    async def create_new_project(self, project_name: str) -> Project:
        if not project_name:
            raise ValueError("project_name является обязательным параметром")

        try:
            return await self.async_api.add_project(name=project_name)
        except Exception as e:
            logger.error(f"Ошибка при создании проекта: {str(e)}")
            raise ProjectCreationException()

    async def add_task(
        self, task_data: TaskData, project_id: str = None
    ) -> Optional[Task]:
        if not project_id:
            raise ValueError("project_id это обязательный параметр")

        try:
            return await self.async_api.add_task(
                content=task_data.corrected_text, project_id=project_id
            )
        except Exception as e:
            logger.error(f"Ошибка при добавлении задания в todoist: {str(e)}")
            return None
