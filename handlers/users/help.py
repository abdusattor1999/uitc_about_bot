from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import ADMINS
from loader import dp



@dp.message_handler(chat_id=ADMINS, commands='help')
async def bot_help(message: types.Message):
    text = ("Admin uchun komandalar",
            "/start - ♻️  Botni qayta ishga tushirish",
            "/help - 🆘 Mavjud komandalarni ko'rish",
            "/addproject - ⏬ Bazaga Proyekt qo'shish",
            )
    
    await message.answer("\n".join(text))



@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
