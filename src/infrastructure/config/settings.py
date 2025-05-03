from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    # БД
    DATABSE_URL: str = Field(..., description="Url подключения в БД")
    # Логгирование
    LOGS_DIR: str = "logs/"
    # Todoist
    API_TOKEN: str = Field(..., description="API токен для Todoist")
    # OpenAI
    OPENAI_API_KEY: str = Field(..., description="API токен для OpenAI")
    # Телеграм
    BOT_TOKEN: str = Field(..., description="Токен для бота")
    # Модели
    MODEL_NAME: str = "base"
    MODELS_PATH: str = "models/"
    # Войс
    VOICE_DIR: str = "voices/"

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
