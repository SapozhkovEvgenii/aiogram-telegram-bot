from aiogram import Router, F
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        (f"HELLO! Your id = {message.from_user.id}, your username {message.from_user.username}. \
        I am using CommandStart() filter.")
    )


@start_router.message(Command("start_2"))
async def cmd_start_2(message: Message):
    await message.answer("I am using Command() filter.")


@start_router.message(F.text == "/start_3")
async def cmd_start_3(message: Message):
    await message.answer("Using F.text filter.")


class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


@start_router.message(MyFilter("hello"))
async def my_handler(message: Message): ...
