import telebot
import json

# Завантаження конфігу
with open("config.json", "r") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["TOKEN"])

welcome_message = f"""🔥 Вітаємо у каналі 🔥
Робота в Польщі 🇵🇱 | Вакансії для українців
📲 Контакти для зв’язку:
Viber / Telegram / WhatsApp: {config["CONTACT"]}
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, welcome_message)

bot.polling()