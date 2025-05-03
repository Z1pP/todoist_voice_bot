import json
import logging
from datetime import datetime
from typing import Optional

from core.domain.entities import TaskData, TaskPriority


class TaskParser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    # Обработка текста полсе llm
    async def parse(self, json_string: str) -> list[TaskData]:
        try:
            data = json.loads(json_string)

            if not isinstance(data, list):
                data = [data]

            tasks = []
            for item in data:
                task = await self._validate_and_transform(item)
                tasks.append(task)

            return tasks
        except json.JSONDecodeError as e:
            self.logger.error(f"Ошибка при парсинге JSON: {e}")
            raise e
        except Exception as e:
            self.logger.error(f"Неожиданная ошибка: {e}")
            raise e

    async def _validate_and_transform(self, data: dict) -> TaskData:
        try:
            deadline = await self._parse_deadline(data.get("deadline"))
            priority = await self._parse_priority(data.get("priority"))

            task_data = TaskData(
                title=data.get("title", "").strip(),
                deadline=deadline,
                priority=priority,
                corrected_text=data.get("corrected_text", "").strip(),
            )

            if not task_data.is_valid:
                raise

            return task_data
        except (ValueError, KeyError) as e:
            self.logger.error(f"Ошибка при валидации данных: {e}")
            raise e

    async def _parse_deadline(self, deadline_str: str) -> Optional[datetime]:
        if not deadline_str:
            return None
        try:
            return datetime.fromisoformat(deadline_str)
        except ValueError:
            return None

    async def _parse_priority(self, priority_str: str) -> TaskPriority:
        try:
            return TaskPriority(priority_str.lower())
        except ValueError:
            return TaskPriority.LOW
