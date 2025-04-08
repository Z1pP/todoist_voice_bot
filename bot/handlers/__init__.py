from aiogram import Dispatcher

from .command_handler import router as command_router

routers = (command_router,)


def include_routers(dp: Dispatcher):
    for router in routers:
        dp.include_router(router)
