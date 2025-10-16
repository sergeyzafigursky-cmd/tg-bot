import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Увімкнемо логування
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Хендлер команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Перейти до каналу", url="https://t.me/praca_polska_europa")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = "🇵🇱 Робота в Польщі для українців\nДізнайся більше про роботу 👇"
    await update.message.reply_text(text, reply_markup=reply_markup)

def main():
    # Токен беремо зі змінної середовища
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("Не вказано токен у змінній BOT_TOKEN")
        return

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("Бот запущений...")
    application.run_polling()

if __name__ == "__main__":
    main()
