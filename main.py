from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from database import Database

from handlers import start, help_command, handle_language_change
from admin import admin_panel
from message_handler import message_handler


def main():
    # Ma'lumotlar bazasini ishga tushirish
    db = Database()

    # Bot yaratish
    app = Application.builder().token(TOKEN).build()

    # Komanda handlerlari
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("language", handle_language_change))
    app.add_handler(CommandHandler("admin", admin_panel))

    # Buttonlar va textlar uchun
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    print("Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
