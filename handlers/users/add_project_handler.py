from pprint import pprint
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,db 
from states.state_for_add_project import Project
from data.config import ADMINS
from keyboards.inline.main_inline_keys import services
from keyboards.default.main_keyboard import start


@dp.message_handler(chat_id=ADMINS, commands="addproject")
async def addpr(ms:Message, state:FSMContext):
    await ms.answer(f"<b>{ms.from_user.first_name}</b> Proyekt yuklash comandasi ishga tushdi.\n\n Proyekt uchun <b>\"Kategoriya\"</b>ni tanlang.\n\nBekor qilish uchun /cancel buyrug'ini bering",reply_markup=services)
    await Project.categ.set()

    
@dp.callback_query_handler(state=Project.categ , text='bekor_qilish')
async def bekor_qilish(call : CallbackQuery, state:FSMContext):
    await state.finish()
    await call.message.answer("Proyekt qo'shish bekor qilindi ☑️",reply_markup=start)

@dp.callback_query_handler(state=Project.categ)
async def inline_categ(call:CallbackQuery, state:FSMContext):
    ca = call.get_current()
    categ = ca.data
    await state.update_data(category=categ)
    await call.message.answer("Kategoriya tanlandi endi proyekt uchun rasm yoki video yuboring. \n\nBekor qilish uchun /cancel buyrug'ini bering")
    await call.message.delete()
    await Project.media.set()

@dp.message_handler(state=Project.categ)
async def javob(ms:Message):
    await ms.answer("Iltimos chatdagi tugma orqali Proyekt Kategoriyasini tanlang ⁉️ \n\nBekor qilish uchun /cancel buyrug'ini bering")

@dp.message_handler(state=Project.media, content_types='photo')
@dp.message_handler(state=Project.media, content_types='video')
async def mediaa(ms:Message, state:FSMContext):
    if ms.content_type == 'photo':
        rasm = ms.photo[-1].file_id
        await state.update_data(photo=rasm)
    elif ms.content_type == 'video':
        video = ms.video.file_id
        await state.update_data(video=video)

    await ms.answer("✅ Media saqlandi. \nendi proyekt matni uchun text yuboring. \n\n📝<b>Ishlov berish</b> uchun <u>HTML</u> kodlaridan foydalanishingiz mumkin.\n\nBekor qilish uchun /cancel buyrug'ini bering")
    await Project.text.set()

@dp.message_handler(state=Project.text)
async def texxt(ms:Message, state:FSMContext):
    matn = ms.text
    await state.update_data(text=matn)
    data = await state.get_data()
    malumot = []
    for ii in data.keys():
        malumot.append(ii)
    matnn = data['text']
    categ = data['category']
    if "photo" in malumot:
        photo = data['photo']
        await db.add_project(text=matn, category=categ, photo=photo)
    if "video" in malumot:
        video = data['video']
        await db.add_project(text=matnn, category=categ, video=video)
    await ms.answer("✅ Proyekt saqlandi")
    await state.finish()

    

    


