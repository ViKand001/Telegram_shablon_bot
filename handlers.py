from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from database import Database
from utils import get_translation

db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if db.get_user(user.id):
        # Foydalanuvchini ma'lumotlar bazasiga saqlash yoki yangilash
        db.create_user(
            chat_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            language="en"  # Default til
        )
    else:
        # Foydalanuvchini ma'lumotlar bazasiga saqlash yoki yangilash
        db.create_user(
            chat_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            language="ru"  # Default til
        )

    # Foydalanuvchining tilini bazadan olish
    user_data = db.get_user(user.id)
    user_language = user_data[5] if user_data else "en"  # Default til, agar topilmasa

    message = get_translation("welcome_message", user_language)
    await update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Foydalanuvchining tilini bazadan olish
    user_data = db.get_user(user.id)
    user_language = user_data[5] if user_data else "en"  # Default til, agar topilmasa

    message = get_translation("help_message", user_language)
    await update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())


async def handle_language_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # State ni o'zgartirish
    context.user_data['state'] = "LANGUAGE_CHANGE"

    """Foydalanuvchi tilini o'zgartirish."""
    user = update.effective_user
    text = update.message.text

    # Foydalanuvchining tilini bazadan olish
    user_data = db.get_user(user.id)
    user_language = user_data[5] if user_data else "en"  # Default til, agar topilmasa

    # Agar foydalanuvchi til tanlash uchun so'rov yuborsa
    if text == "/language":
        keyboard = [
            ["🇺🇿 Uzbek", "🇷🇺 Russian"],
            ["🇬🇧 English"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        choose_language_message = get_translation("choose_language", user_language)
        await update.message.reply_text(choose_language_message, reply_markup=reply_markup)
        return
