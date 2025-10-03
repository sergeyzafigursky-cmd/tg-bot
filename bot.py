import telebot
import json

with open("config.json", "r") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["TOKEN"])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Привіт! Ви можете зв'язатися зі мною:\n\n"
        f"Viber: {config['VIBER']}\n"
        f"Telegram: {config['TELEGRAM']}\n"
        f"WhatsApp: {config['WHATSAPP']}"
    )
    bot.send_message(message.chat.id, welcome_text)

bot.polling()
