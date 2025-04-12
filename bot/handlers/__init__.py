from aiogram import Dispatcher

from .command_handler import router as command_router
from .task_handler import router as task_router
from .voice_handler import router as voice_router

routers = (command_router, voice_router, task_router)


def include_routers(dp: Dispatcher):
    for router in routers:
        dp.include_router(router)
