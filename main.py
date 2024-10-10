import logging, random, config
import parsing
from aiogram import Bot, Dispatcher, executor, types
import get_token


# ----------------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)

dp = Dispatcher(bot)

# ---------------------------------------------

#КОНПКИ????
button1 = types.KeyboardButton(text='ВЫБРАТЬ ПРЕДМЕТ?')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(button1)


ALO = types.InlineKeyboardMarkup()
ALO.add(types.InlineKeyboardButton(text="МАТЕМАТИКА", callback_data="math"))



ALO1 = types.InlineKeyboardMarkup()
ALO1.add(types.InlineKeyboardButton(text="1", callback_data="1"))


# стартовая функция







@dp.message_handler(commands=['start'], commands_prefix='/')
async def process_start_command(message: types.Message):
    await message.answer("qweqwew", reply_markup=keyboard)



@dp.message_handler(text=['ВЫБРАТЬ ПРЕДМЕТ?'])
async def predmet(message: types.Message):
    print(1)
    await message.answer("К КАКОМУ ПРЕДМЕТУ", reply_markup=ALO)


@dp.callback_query_handler(text='math')
async def yes(callback: types.CallbackQuery):
    await callback.message.answer("ВЫБЕРИТЕ ТИП", reply_markup=ALO1)



@dp.callback_query_handler(text='1 ')
async def yes(callback: types.CallbackQuery):
    await callback.message.answer(parsing.qeustion[random.randint(1,50)])


async def greet(message: types.Message):
    
    answer1 = get_token.get_chat_completion(get_token.get_token1(get_token.auth), message.text).json()['choices'][0]['message']['content']
    print(f"Сообщение от {message.from_user.full_name}: {message.text}")
    print(f"Ответ: {answer1}")
    await message.answer(answer1)


dp.register_message_handler(greet)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)