from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
from keyboards.default.main_keyboard import start
import asyncpg


@dp.message_handler(CommandStart())
async def bot_start(ms: types.Message):
    try:
        user = await db.add_user(
            telegram_id=ms.from_user.id,
            full_name=ms.from_user.full_name,
            username=ms.from_user.username
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=ms.from_user.id)
    introduction = f"Assalomu alaykum, <b>{ms.from_user.first_name}</b> !\n<b>United IT Clubs</b> Kompaniyasining \nrasmiy telegram botiga xush kelibsiz!\n🤖 Ushbu bot orqali kompaniya haqida \nto’liq ma’lumot olishingiz mumkin \n\nBiz bilan bo’g’lanish uchun\npastdagi <b>\"📞 Bog’lanish\"</b> tugmasini \nbosib ro’yxatdan o’ting \nHodimlarimiz siz bilan tez \norada bog’lanishadi."
    await ms.answer(introduction, reply_markup=start)
