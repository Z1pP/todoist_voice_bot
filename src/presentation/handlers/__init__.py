from aiogram import Dispatcher

from .add_task_handlers import router as add_task_router
from .menu_handlers import router as menu_router
from .start_command_handlers import router as start_router


async def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(add_task_router)
