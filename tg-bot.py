import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiohttp import web

# --------------------------
# Логування
# --------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------
# Токен бота (змінна середовища)
# --------------------------
    raise SystemExit("API_TOKEN required!")
API_TOKEN = os.getenv"7203533541:AAFs7CuSO-t1YQ4MKcN2nk8WeXgWmx1vrf0")
if not API_TOKEN:
    logger.error("❌ Не знайдено токен! Вкажи API_TOKEN у Render → Environment.")
    raise SystemExit("API_TOKEN required!")

# --------------------------
# Ініціалізація бота
# --------------------------
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --------------------------
# Команди
# --------------------------
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    text = (
        "👋 Вітаю!\n\n"
        "Актуальні пропозиції працевлаштування\n"
        "Щоб перейти до нашої спільноти, натискай <b>/do_roboty</b>"
    )
    await message.answer(text)

@dp.message_handler(commands=["do_roboty"])
async def do_roboty_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            "🔗 Перейти до каналу Praca Polska Europa",
            url="https://t.me/praca_polska_europa"
        )
    )
    await message.answer(
        "✅ Натисни кнопку нижче, щоб перейти в наш Telegram-канал 👇",
        reply_markup=keyboard
    )

# --------------------------
# HTTP сервер для Render
# --------------------------
async def handle_root(request):
    return web.Response(text="Bot is running ✅")

async def handle_health(request):
    return web.json_response({"status": "ok"})

def run_webserver():
    port = int(os.getenv("PORT", 8000))
    app = web.Application()
    app.router.add_get("/", handle_root)
    app.router.add_get("/healthz", handle_health)
    web.run_app(app, host="0.0.0.0", port=port)

# --------------------------
# Запуск polling і сервера
# --------------------------
def run_polling():
    logger.info("🚀 Бот запущений (polling)...")
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    threading.Thread(target=run_polling, daemon=True).start()
    run_webserver()
