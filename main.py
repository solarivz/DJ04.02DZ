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
# Хэндлер для команды /weather
@dp.message(Command("weather"))
async def weather_command(message: Message):
    # Формируем запрос к API OpenWeatherMap
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    )
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            await message.answer("Не удалось получить данные о погоде. Попробуйте позже.")
            return

        # Извлекаем данные о погоде
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        # Формируем ответ для пользователя
        weather_message = (
            f"Погода в крае {city_name}:\n"
            f"Температура: {temperature}°C\n"
            f"Условия: {description.capitalize()}"
        )
        await message.answer(weather_message)
    except Exception as e:
        logging.error(f"Ошибка при получении погоды: {e}")
        await message.answer("Произошла ошибка при получении прогноза погоды.")


# Основная функция запуска
async def main():
    logging.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())