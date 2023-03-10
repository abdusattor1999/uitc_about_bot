from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo


start = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
start.insert(KeyboardButton("π Biz haqimizda"))
start.insert(KeyboardButton("π Joylashuvlarimiz"))
start.insert(KeyboardButton("π Bajarilgan loyihalar"))
start.insert(KeyboardButton("π Bogβlanish"))


ulanish_uchun = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
ulanish_uchun.insert(KeyboardButton("π¨ Fikr qoldirish"))
ulanish_uchun.insert(KeyboardButton("π¨π»βπ» Kursga yozilish"))
ulanish_uchun.insert(KeyboardButton("β¬οΈ Bosh menuga"))


kurs_list = ["π₯ Kompyuter savodxonligi", "π§βπ» FrontEnd dasturlash", "π BackEnd Dasturlash", "π¨βπ¨ Grafik dizayn", "π 3D Modeling", "πΊπΈ IT English", "π± SMM"]
kurslar_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
for i in kurs_list:
    kurslar_markup.insert(KeyboardButton(i))


contact = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
contact.insert(KeyboardButton("π Telefon raqam yuborish", request_contact=True))