from  telegram import Update, ReplyKeyboardMarkup
from  telegram.ext import ContextTypes

from config import ADMIN_IDS
from database import Database

from buttons import get_admin_buttons
from message_handler import message_handler
from  utils import get_translation, get_user_language

db = Database()

async  def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin panelini ko'rsatish"""
    user = update.effective_user

    #stetaeni o'zgartirish
    context.user_data['state'] = "ADMIN_PANEL"

    #Foydalanuvchi tilini bazadan olish
    user_language = get_user_language(user.id)

    #Adminni tekshirish
    if user.id not in ADMIN_IDS:
        await update.message.reply_text("Siz admin panelga kirish huquqiga ega emassiz!")
        return

    #Tugmalarni olish
    buttons = get_admin_buttons(user_language)
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    #Xabarni yuborish
    welcome_message = get_translation("welcome_admin_panel", user_language)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)
