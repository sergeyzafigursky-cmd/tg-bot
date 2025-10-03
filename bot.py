import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔗 Наш канал", url="https://t.me/praca_polska_europa"))
    keyboard.add(types.InlineKeyboardButton("📲 Зв'язатись", url="https://t.me/ТВІЙ_НІК"))

    await message.answer(
        "👋 Вітаю!\n\n"
        "Ми – твій партнер, якому можна довіряти.\n"
        "Робота в Польщі та Європі 🇵🇱🇪🇺\n\n"
        "👉 Обери дію нижче:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
