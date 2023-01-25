from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, MediaGroup
from loader import dp , db
from keyboards.inline.main_inline_keys import services 
from keyboards.default.main_keyboard import start, contact,ulanish_uchun, kurslar_markup
from utils.media_groups import alpomish_albom,kutubxona_albom,yoshlar_albom
from states.state_for_add_project import Done,Shikoyat,Ochered,Project
from aiogram.dispatcher import FSMContext
from haversine import haversine
from data.config import ADMINS
from utils.media_groups import formatla

@dp.message_handler(commands='cancel',state="*")
async def toxtatish(ms:Message, state:FSMContext):
    await state.finish()
    await ms.answer("Jarayon bekor qilindi 🏁", reply_markup=start)



@dp.message_handler(content_types='location')
async def locatioo(ms:Message):
    user_lat = ms.location.latitude
    user_long = ms.location.longitude 
    user = (user_lat, user_long)
    uitc = (40.99440667460731, 71.60483196648644) 
    masofa = haversine(user, uitc)
    javob = await formatla(masofa)
    if float(javob) <= 0.100:
        response = f"Assalomu aleykum <b>{ms.from_user.first_name}</b>\nSiz bizni <b>UITC</b> ning yaqinida yoki ichida turibsiz 😁"
    else:
        response = f"Assalomu aleykum <b>{ms.from_user.first_name}</b>\nSiz bizni <b>UITC</b> akademiyamizdan {javob} km masofada turibsiz"
    await ms.answer(response)

@dp.message_handler(text='⬅️ Bosh menuga')
async def glavaaa(ms:Message):
    await ms.answer("Bosh menuga qaytildi",reply_markup=start)

@dp.message_handler(text="📄 Biz haqimizda")
async def about_us(ms:Message):
    await ms.answer_video(video="BAACAgIAAxkBAAIB0GN8wFfzniq2vS3gzdfOC0kXuZCaAAJFIAACQeRwSqFq3aSu2FIYKwQ", caption="Biz haqimizda")
 

@dp.message_handler(text="📍 Joylashuvlarimiz")
async def locations(ms:Message):
    await ms.answer_media_group(media=alpomish_albom)
    await ms.answer_location(latitude=40.99443198497194,longitude=71.60484165582112, heading="sarlavha")
    await ms.answer_media_group(media=kutubxona_albom)
    await ms.answer_location(latitude=41.00119846500162,longitude=71.60533078640627)
    await ms.answer_media_group(media=yoshlar_albom)
    await ms.answer_location(latitude=40.99631161280575,longitude=71.6728745046119)

@dp.message_handler(text='📊 Bajarilgan loyihalar')
async def loyihalar(ms:Message):
    await ms.answer("Sizni qiziqtirgan yo'nalishni tanlang", reply_markup=services)
    await Done.bir.set()


@dp.callback_query_handler(state=Done.bir)
async def yonalish(call:CallbackQuery, state:FSMContext):
    data_full_call = call.get_current()
    data = data_full_call.data
    db_datas = await db.select_project(category=data)
    for db_data in db_datas:
        if db_data['photo']:
            await call.message.answer_photo(photo=db_data['photo'], caption=db_data['text'], parse_mode="HTML")
        elif db_data['video']:
            await call.message.answer_video(video=db_data['video'], caption=db_data['text'], parse_mode='HTML')
    
    await call.message.delete()
    await state.finish()


tel_reg = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
@dp.message_handler(text="📞 Bog’lanish")
async def svyazi(ms:Message):
    await ms.answer("Pastdagi opsiyalardan birini tanlang", reply_markup=ulanish_uchun)

@dp.message_handler(text="📨 Fikr qoldirish")
async def fikri(ms:Message):
    await ms.answer("Ismingizni yuboring", reply_markup=ReplyKeyboardRemove())
    await Shikoyat.bir.set()

@dp.message_handler(state=Shikoyat.bir)
async def ismi_keldi(ms:Message, state:FSMContext):
    await state.update_data(name=ms.text)
    await ms.answer("Ismingiz saqlandi endi telefon raqamingizni yoki tugma orqali kontaktingizni yuboring. \n\nBekor qilish uchun /cancel buyrug'ini bering",reply_markup=contact)
    await Shikoyat.ikki.set()
    
@dp.message_handler(state=Shikoyat.ikki, regexp=tel_reg)
@dp.message_handler(state=Shikoyat.ikki, content_types="contact")
async def tel_yubordi(ms:Message, state=FSMContext):
    if ms.content_type == "contact":
        raqam = ms.contact.phone_number
    else:
        raqam = ms.text
    await state.update_data(number=raqam)
    await ms.answer("Bizga yo'llamoqchi bo'lgan xabaringiz matnini yuboring. \n\nBekor qilish uchun /cancel buyrug'ini bering", reply_markup=ReplyKeyboardRemove())
    await Shikoyat.uch.set()

@dp.message_handler(state=Shikoyat.ikki)
async def uyin(ms:Message):
    await ms.answer("Iltimos telefon raqamni to'g'ri kiriting ⁉️\n\nBekor qilish uchun /cancel buyrug'ini bering")

@dp.message_handler(state=Shikoyat.uch)
async def xabar(ms:Message, state:FSMContext):
    await state.update_data(text=ms.text)
    data = await state.get_data()
    ismi = data['name']
    nomeri = data['number']
    xabari = data['text']
    javob = f"<b>Yangi murojaat : </b>\n\nXabar matni : <b>{xabari}</b>\n\nFoydalanuvchini ismi : <b>{ismi}</b>\nFoydalanuvchini telefoni : <b>{nomeri}</b>"
    for admin in ADMINS:
        await dp.bot.send_message(chat_id=admin,text=javob)
    await ms.answer("✔️ Habaringiz yetkazildi \n<b>UITC</b> bilan bo'ling",reply_markup=start)
    await state.finish()

@dp.message_handler(text="👨🏻‍💻 Kursga yozilish")
async def courses(ms:Message):
    await ms.answer("Ism va Familiyangizni yuboring")
    await Ochered.bir.set()

@dp.message_handler(state=Ochered.bir)
async def ism_fam_keldi(ms:Message, state:FSMContext):
    await state.update_data(name = ms.text)
    await ms.answer("Telefon raqamingizni yoki pastdagi tugma orqali kontaktingizni yuboring\n\nBekor qilish uchun /cancel buyrug'ini bering",reply_markup=contact)
    await Ochered.ikki.set()


@dp.message_handler(state=Ochered.ikki, regexp=tel_reg)
@dp.message_handler(state=Ochered.ikki, content_types="contact")
async def tel_yubordi(ms:Message, state=FSMContext):
    if ms.content_type == "contact":
        raqam = ms.contact.phone_number
    else:
        raqam = ms.text
    await state.update_data(number=raqam)
    await ms.answer("O'zingiz qiziqqan sohani tanlang \n\nBekor qilish uchun /cancel buyrug'ini bering", reply_markup=kurslar_markup)
    await Ochered.uch.set()

@dp.message_handler(state=Ochered.ikki)
async def uyin(ms:Message):
    await ms.answer("Iltimos telefon raqamni to'g'ri kiriting ⁉️\n\nBekor qilish uchun /cancel buyrug'ini bering")

@dp.message_handler(state=Ochered.uch)
async def kursga(ms:Message, state:FSMContext):
    await state.update_data(kurs=ms.text)
    data = await state.get_data()
    full_namesi = data['name']
    nomeri = data['number']
    kurs_turi = data['kurs']
    xabar_adminga = f"<b>O'quv kursi uchun yangi ariza :</b>\n\n✅ Ism Familiya : <b>{full_namesi}</b>\n✅ Telefon : <b>{nomeri}</b>\n✅ Kurs turi : <b>{kurs_turi}</b>"
    xabar_userga = f"Xurmatli <b>{ms.from_user.first_name}</b> \nSiz {kurs_turi} - nomli kursda o'qish uchun ariza berdingiz tez orada hodimlarimiz siz bilan bog'lanishadi \n\n<b>UITC</b> bilan bo'ling "
    for admin in ADMINS:
        await dp.bot.send_message(chat_id=admin, text=xabar_adminga)
    await ms.answer(xabar_userga,reply_markup=start)
    await state.finish()











