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