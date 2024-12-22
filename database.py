import sqlite3
from config import DB_PATH

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._create_users_table()

    def _connect(self):
        """Ma'lumotlar bazasiga ulanishni."""
        return sqlite3.connect(self.db_path)

    def _create_users_table(self):
        """Foydalanuvchilar jadvalini yaratish."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id INTEGER UNIQUE,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    language TEXT
                )
            """)
            conn.commit()

    def create_user(self, chat_id, username, first_name, last_name, language="en"):
        """Foydalanuvchini qo'shish yoki yangilash."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (chat_id, username, first_name, last_name, language)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(chat_id) DO UPDATE SET
                    username = excluded.username,
                    first_name = excluded.first_name,
                    last_name = excluded.last_name,
                    language = excluded.language
            """, (chat_id, username, first_name, last_name, language))
            conn.commit()

    def get_user(self, chat_id):
        """Berilgan chat_id bo'yicha foydalanuvchini qaytarish."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,))
            return cursor.fetchone()

    def get_all_users(self):
        """Barcha foydalanuvchilarni olish."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def update_user_language(self, chat_id, new_language):
        """Foydalanuvchining tilini yangilash."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET language = ? WHERE chat_id = ?", (new_language, chat_id))
            conn.commit()
