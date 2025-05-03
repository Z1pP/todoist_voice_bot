from abc import ABC, abstractmethod
from pathlib import Path


class ITranscribeService(ABC):
    @abstractmethod
    async def transcribe(self, file_path: Path) -> str:
        pass


class IllmParserService(ABC):
    @abstractmethod
    async def parse(self, text: str) -> str:
        pass
