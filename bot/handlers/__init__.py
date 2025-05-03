from aiogram import Dispatcher

# from .command_handler import router as command_router
from .menu_handlers import router as menu_router

# from .settings_handler import router as settings_router
# from .task_handler import router as task_router

# from .voice_handler import router as voice_router

routers = (
    # command_router,
    menu_router,
    # voice_router,
    # task_router,
)


def include_routers(dp: Dispatcher):
    for router in routers:
        dp.include_router(router)
