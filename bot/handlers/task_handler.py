# import logging

# from aiogram import F, Router
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message

# from bot.constants import Answers, MenuButtons, Messages
# from bot.keyboards.reply import reply_kb
# from bot.parser.task_parser import TaskParser
# from bot.states import TaskCreationStates
# from bot.utils import (
#     handle_task_creation,
#     request_content_to_llm,
#     send_message_with_keyboard,
# )
# from todoist import TodoistManagerAsync

# logger = logging.getLogger(__name__)

# router = Router(name=__name__)


# CONST_PROJECT_NAME = "Тестовый проект"


# @router.message(F.text.in_(MenuButtons.ADD_TASK))
# async def add_task_command(message: Message, state: FSMContext):
#     """
#     Обработчик начала создания задачи
#     """
#     await send_message_with_keyboard(message, Messages.State.WAITING_INPUT)
#     # Устанавливаем состояние ожидания выбора метода ввода
#     await state.set_state(TaskCreationStates.WAINTING_INPUT)


# @router.message(TaskCreationStates.WAINTING_INPUT, F.text)
# async def proccess_text_input(message: Message, state: FSMContext):
#     text = message.text
#     # Отправляем на обработку нейронке
#     await proccess_llm_processing(message, state, text)


# async def proccess_llm_processing(message: Message, state: FSMContext, text: str):
#     """
#     Процесс проверки и исправления текста LLM
#     """
#     try:
#         result_text = await request_content_to_llm(text)
#         await handle_task_creation(message, state, result_text)
#     except Exception as e:
#         logger.error(f"Ошибка при обработке создания задачи: {str(e)}")
#         await send_message_with_keyboard(
#             message, "Произошла ошибка при работе нашей LLM."
#         )


# @router.message(TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text(Answers.YES.value))
# async def proccess_confirmation_text_yes(message: Message, state: FSMContext):
#     data = await state.get_data()
#     result_text = data.get("text")

#     try:
#         task_parser = TaskParser()
#         tasks_data = await task_parser.parse_llm_response(json_string=result_text)

#         manager = TodoistManagerAsync()

#         project_id = await manager.get_project_id(project_name=CONST_PROJECT_NAME)

#         tasks_content = "\n"
#         for task in tasks_data:
#             task = await manager.add_task(task_data=task, project_id=project_id)
#             tasks_content += f"\t--{task.content}\n"

#         text = Messages.TASK_CREATED.format(task=tasks_content)
#         await send_message_with_keyboard(message, text, reply_kb.menu_btn)

#     except Exception as e:
#         await message.answer(str(e))
#     finally:
#         await state.clear()


# @router.message(TaskCreationStates.WAITING_CONFIRMATION_TEXT, F.text(Answers.NO.value))
# async def proccess_confirmation_text_no(message: Message, state: FSMContext):
#     await add_task_command(message, state)


# @router.message(F.text.in_(MenuButtons.LIST_TASKS.value))
# async def list_tasks_command(message: Message):
#     await send_message_with_keyboard(
#         message, Messages.Dialog.IN_DEVELOPMENT, reply_kb.cancel_btn
#     )
