import logging, json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import get_token

# Установка уровня логгирования (необязательно)
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6985481048:AAFKrlWkGRnv6H7uaBX94CuzvPzyBqkdrXs'

# Создание объектов бота и диспетчера
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

# Функция, которая будет вызываться при получении сообщения
async def greet(message: types.Message):
    # Отправляем ответное сообщение

    if message.text == "/start":
        await message.answer("ало")
    else:
        answer1 = get_token.get_chat_completion(get_token.get_token1(get_token.auth), message.text).json()['choices'][0]['message']['content']
        print(f"Сообщение от {message.from_user.full_name}: {message.text}")
        print(f"Ответ: {answer1}")
        await message.answer(answer1)

# Регистрация обработчика сообщений
dp.register_message_handler(greet)

# Запуск бота
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()