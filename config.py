import os
from dotenv import load_dotenv

load_dotenv()


class Setting:
    def __init__(self):
        self.bot_token: str = os.getenv("BOT_TOKEN")
        self.todoist_token: str = os.getenv("TODOIST_TOKEN")


settings = Setting()
