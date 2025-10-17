from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("7203533541:AAFs7CuSO-t1YQ4MKcN2nk8WeXgWmx1vrf07203533541:AAFs7CuSO-t1YQ4MKcN2nk8WeXgWmx1vrf0")
CHANNEL_LINK = "https://t.me/praca_polska_europa"
WELCOME_TEXT = "🇵🇱 Робота в Польщі для українців\nДізнайся більше про роботу 👇"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Перейти до каналу", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # If user clicked via deep-link with param, Telegram still sends /start; we respond the same
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # Use polling (works on Render as a worker or web service)
    app.run_polling()

if __name__ == "__main__":
    main()
