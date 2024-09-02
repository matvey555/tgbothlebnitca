from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Ваш токен и ID администратора
API_TOKEN = '7350546586:AAHjDS1QW6TluH-ptUsz7XLy96Yi8b1qoTk'
ADMIN_ID = '1038191408'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!")

# Обработчик всех остальных сообщений
@dp.message_handler()
async def forward_message(message: types.Message):
    # Перенаправляем сообщение админу
    await bot.send_message(ADMIN_ID, f"Новое сообщение от {message.from_user.full_name} (@{message.from_user.username}):\n\n{message.text}")
    # Отправляем ответное сообщение пользователю
    await message.reply("Спасибо за твою активность и вовлеченность! Ответ предоставим в течение 2 рабочих дней🥨")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
