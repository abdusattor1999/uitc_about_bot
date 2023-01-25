from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



serr ={
        "🌐 Web saytlar":"biznes_sites",
        "🛋 3D modellar":"3d_models",
        "🎨 Grafik dizayn":"graphic_design",
        "🎞 Motion Grafika":"motion_graphic",
        "🤖 Telegram botlar":"telegram_bots",
        "◀️ Orqaga qaytish" : "bekor_qilish"
    }
services = InlineKeyboardMarkup(row_width=1)

for k,v in serr.items():
    services.insert(InlineKeyboardButton(text=k, callback_data=v))

