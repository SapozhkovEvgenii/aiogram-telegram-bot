from aiogram import Router, F
from aiogram.filters import CommandStart, Command, Filter, BaseFilter
from aiogram.types import Message

from keyboards.text_keyboard import main_keyboard

start_router = Router()


# Custom filter for commands without prefix
class CommandWithoutPrefix(BaseFilter):
    def __init__(self, command: str):
        self.command = command.lower()

    async def __call__(self, message: Message) -> bool:
        # Check if the message text matches the command (case-insensitive)
        return message.text.strip().lower() == self.command  # type: ignore


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        (f"HELLO! Your id = {message.from_user.id}, your username {message.from_user.username}. \
        I am using CommandStart() filter."),
        reply_markup=main_keyboard(message.from_user.id)  # type: ignore
    )


@start_router.message(CommandWithoutPrefix("SignUp"))
async def cmd_signup(message: Message):
    await message.answer("Process of registration!!!")


@start_router.message(Command("start_2"))
async def cmd_start_2(message: Message):
    await message.answer("I am using Command() filter.")


@start_router.message(F.text == "/start_3")
async def cmd_start_3(message: Message):
    await message.answer("Using F.text filter.")


@start_router.message()
async def cmd_start_any(message: Message):
    print(message.text)  # For debugging purposes
    if message.text.strip().lower() == "signup":  # type: ignore
        await message.answer("Process of registration!!!")


class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


@start_router.message(MyFilter("hello"))
async def my_handler(message: Message): ...
