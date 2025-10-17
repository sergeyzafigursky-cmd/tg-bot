from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Отримуємо токен з Environment Variables (у Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Посилання на твій канал
CHANNEL_LINK = "https://t.me/praca_polska_europa"

# Текст, який побачить користувач
WELCOME_TEXT = "🇵🇱 Робота в Польщі для українців\nДізнайся більше про роботу 👇"

# Основна функція /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Перейти до каналу", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# Точка входу
def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN не знайдено! Додай його у Render → Environment → Key=BOT_TOKEN")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
