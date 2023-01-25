import logging
from keyboards.default.main_keyboard import start
from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "♻️ <b>UITC bot</b> qayta ishga tushdi",reply_markup=start)

        except Exception as err:
            logging.exception(err)
