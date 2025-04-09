import os

from dotenv import load_dotenv

load_dotenv()


class Setting:
    def __init__(self):
        self.bot_token: str = os.getenv("BOT_TOKEN")
        self.todoist_token: str = os.getenv("TODOIST_TOKEN")
        # models
        self.model_name: str = os.getenv("MODEL_NAME", "base")
        self.models_path: str = os.getenv("MODELS_PATH", "models/")

        self.voice_dir: str = "voices/"
        self.__create_folder()

    def __create_folder(self):
        if not os.path.exists(self.voice_dir):
            os.makedirs(self.voice_dir)


settings = Setting()
