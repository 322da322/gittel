import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types


# ----------------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token="6105269350:AAFdfI9vMQ77TUuv2sJXewfDg82SbPml5po")

dp = Dispatcher(bot)

# ---------------------------------------------

#КОНПКИ????
button1 = types.KeyboardButton(text='ВЫБРАТЬ ПРЕДМЕТ?')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(button1)


ALO = types.InlineKeyboardMarkup()
ALO.add(types.InlineKeyboardButton(text="МАТЕМАТИКА??", callback_data="math"))



ALO1 = types.InlineKeyboardMarkup()
ALO1.add(types.InlineKeyboardButton(text="1", callback_data="1"))


# стартовая функция????????
@dp.message_handler(commands=['start'], commands_prefix='/')
async def process_start_command(message: types.Message):
    await message.answer("qweqwewq", reply_markup=keyboard)



@dp.message_handler(text=['Выбрать предмет'])
async def predmet(message: types.Message):
    await message.answer("К КАКОМУ ПРЕДМЕТУ????????????", reply_markup=ALO)


@dp.callback_query_handler(text='math')
async def yes(callback: types.CallbackQuery):
    await callback.message.answer("ВЫБЕРИТЕ ТИП", reply_markup=ALO1)



@dp.callback_query_handler(text='1')
async def yes(callback: types.CallbackQuery):
    await callback.message.answer("ura")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)