import os

from dotenv import load_dotenv

load_dotenv()


class Setting:
    def __init__(self):
        self.bot_token: str = os.getenv("BOT_TOKEN")
        self.todoist_token: str = os.getenv("TODOIST_TOKEN")
        self.voice_dir: str = "voices/"
        self.create_folder()

    def create_folder(self):
        if not os.path.exists(self.voice_dir):
            os.makedirs(self.voice_dir)


settings = Setting()
