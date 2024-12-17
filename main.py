import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Ваш токен Telegram-бота
TELEGRAM_TOKEN = "7596610244:AAHGlSlZrLyoFe7fwSXcaVPB20ihRMYDzfw"
# Ваш API-ключ OpenWeatherMap
WEATHER_API_KEY = "f681d195455500f873c3bafc05704c29"
# Город для прогноза погоды
CITY = "Kamchatka"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


# Хэндлер для команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Привет! Я погодный бот.\n"
        "Чтобы узнать прогноз погоды, используй команду /weather.\n"
        "Для справки введи /help."
    )

# Хэндлер для команды /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Этот бот предоставляет прогноз погоды для Камчатки.\n"
        "Доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/help - справка\n"
        "/weather - получить прогноз погоды"
    )


# Основная функция запуска
async def main():
    logging.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())