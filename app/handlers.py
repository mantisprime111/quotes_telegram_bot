from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.quotes import *
import random


router = Router()


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(f'Привет, я бот-цитатник. Отправляю одну случайную цитату. Отправь мне /quote')

@router.message(Command('quote'))
async def cmd_quote(message:Message):
    await message.answer(f'{random.choice(quotes)}')