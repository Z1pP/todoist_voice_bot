import json
import logging
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from bot.exceptions import ParsingError, ValidationError


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class TaskData:
    title: str
    deadline: Optional[datetime]
    priority: TaskPriority
    corrected_text: str

    @property
    def is_valid(self) -> bool:
        return bool(self.title) and bool(self.corrected_text)


class TaskParser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def parse_llm_response(self, json_string: str) -> TaskData:
        try:
            data = json.loads(json_string)
            return await self._validate_and_transform(data)
        except json.JSONDecodeError as e:
            self.logger.error(f"Ошибка при парсинге JSON: {e}")
            raise ParsingError("Не верный JSON формат.") from e
        except Exception as e:
            self.logger.error(f"Неожиданная ошибка: {e}")
            raise ParsingError(f"Ошибка при парсинге данных: {str(e)}") from e

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
                raise ValidationError("Неверный формат данных.")

            return task_data
        except (ValueError, KeyError) as e:
            self.logger.error(f"Ошибка при валидации данных: {e}")
            raise ValidationError("Неверный формат данных.") from e

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
