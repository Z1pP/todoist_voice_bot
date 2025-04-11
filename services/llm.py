import asyncio
import logging
import threading
from datetime import datetime

from openai import OpenAI

from bot.constants import LLM_PROMPT
from config import settings

logger = logging.getLogger(__name__)


class LlmClient:
    def __init__(self, base_url: str = None, api_key: str = None):
        self.client = OpenAI(
            base_url=base_url or "https://openrouter.ai/api/v1",
            api_key=api_key or settings.openai_token,
        )
        self.lock = threading.Lock()

    def _make_request_sync(self, content: str):
        # Получение текущег времени
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.lock:
            try:
                completion = self.client.chat.completions.create(
                    model="meta-llama/llama-4-maverick:free",
                    messages=[
                        {
                            "role": "system",
                            "content": f"{LLM_PROMPT}. date={current_date}",
                        },
                        {
                            "role": "user",
                            "content": content,
                        },
                    ],
                )
                return completion.choices[0].message.content
            except Exception as e:
                logger.error(f"Ошибка при запросе к LLM: {e}")
                raise

    async def make_request_async(self, content: str) -> str:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._make_request_sync, content)
