import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types


# курс доллара

# Настойка бота
# ----------------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token="6105269350:AAFdfI9vMQ77TUuv2sJXewfDg82SbPml5po")

dp = Dispatcher(bot)

# ---------------------------------------------



# стартовая функция
@dp.message_handler(commands=['start'], commands_prefix='/')
async def process_start_command(message: types.Message):
    await message.answer("qweqwewq")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)