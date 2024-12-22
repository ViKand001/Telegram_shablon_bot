import json

from config import LANGUAGES
from database import Database

db = Database()

def load_translations():
    """
    Mavjud tillarni olish.
    """
    translations = {}
    for lang in LANGUAGES:
        with open(f"locales/{lang}.json", "r", encoding="utf-8") as file:
            translations[lang] = json.load(file)
    return translations

TRANSLATIONS = load_translations()

def get_translation(key, language="en"):
    return TRANSLATIONS.get(language, {}).get(key, key)


def get_user_language(user_id):
    """
    Foydalanuvchining tilini ma'lumotlar bazasidan olish.
    """
    user_data = db.get_user(user_id)
    return user_data[5] if user_data else "ru"  # Default til
