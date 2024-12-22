import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Telegram bot konfiguratsiyasi
TOKEN = os.getenv("TOKEN")
DB_PATH = os.getenv("DB_PATH", "bot.db")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
LANGUAGES = ['uz', 'ru', 'en']

