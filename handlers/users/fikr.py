from loader import dp
from loader import bot
from data.config import ADMINS
from keyboards.default.menu_button import menu_kb
    

@dp.message_handler(text= "Hammasi yoqdi ♥️")
async def send_admin(message: types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i, text="Sizga bitta <b>Hammasi yoqdi ♥️</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!", reply_markup=menu_kb)

