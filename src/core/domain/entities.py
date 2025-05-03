from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


@dataclass
class User:
    def __init__(
        self,
        tgid: int,
        username: str | None,
        id: int | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.id = id
        self.tgid = tgid
        self.username = username
        self.created_at = created_at
        self.updated_at = updated_at


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
