from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo


start = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
start.insert(KeyboardButton("📄 Biz haqimizda"))
start.insert(KeyboardButton("📍 Joylashuvlarimiz"))
start.insert(KeyboardButton("📊 Bajarilgan loyihalar"))
start.insert(KeyboardButton("📞 Bog’lanish"))


ulanish_uchun = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
ulanish_uchun.insert(KeyboardButton("📨 Fikr qoldirish"))
ulanish_uchun.insert(KeyboardButton("👨🏻‍💻 Kursga yozilish"))
ulanish_uchun.insert(KeyboardButton("⬅️ Bosh menuga"))


kurs_list = ["🖥 Kompyuter savodxonligi", "🧑‍💻 FrontEnd dasturlash", "🌐 BackEnd Dasturlash", "👨‍🎨 Grafik dizayn", "🛋 3D Modeling", "🇺🇸 IT English", "📱 SMM"]
kurslar_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
for i in kurs_list:
    kurslar_markup.insert(KeyboardButton(i))


contact = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
contact.insert(KeyboardButton("📞 Telefon raqam yuborish", request_contact=True))