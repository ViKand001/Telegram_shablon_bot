from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes

from database import Database
from utils import get_translation, get_user_language

db = Database()

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    # Foydalanuvchining tilini bazadan olish
    user_language = get_user_language(user.id)

    state = context.user_data.get('state', "")
    if state == "LANGUAGE_CHANGE":
        # Foydalanuvchi tilni tanlasa
        language_map = {
            "🇺🇿 Uzbek": "uz",
            "🇷🇺 Russian": "ru",
            "🇬🇧 English": "en"
        }

        if text in language_map:
            new_language = language_map[text]
            db.update_user_language(user.id, new_language)  # Tilni ma'lumotlar bazasida yangilash
            message = get_translation("language_changed", new_language)
            await update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
        else:
            await update.message.reply_text("Tugmalardan birini tanlang yoki /language komandasini yuboring.")
    elif state == "ADMIN_PANEL":
        print(text)
        #Foydalanuvchi tilinin bazadan olish

        if text == get_translation("manage_users",user_language):
            print("Foydalanuvchilar")
        elif text == get_translation("send_advertisement", user_language):
            print("Reklama")
        elif text == get_translation("manage_channels", user_language):
            print("Kanallar boshqaruvi")
        elif text==get_translation("show_statistics", user_language):
            print("Statistika")
        elif text == get_translation("exit", user_language):
            print("Admin panelidan chiqish")

            #statistikani o'chirish
            context._user_id["state"] = None

            message = get_translation("welcome_message", user_language)
            await update.message.reply_text(text=message, reply_markup=ReplyKeyboardRemove())
