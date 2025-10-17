# Telegram Bot - Візитка (Praca Polska)

Цей репозиторій містить простий Telegram-бот — візитку, яка відправляє користувачу повідомлення з кнопкою на канал.

## Файли
- `bot.py` — основний код бота
- `requirements.txt` — залежності
- `Procfile` — запуск для Render (`web: python bot.py`)
- `runtime.txt` — вказує Python 3.11 для сумісності
- `start.sh` — скрипт для локального запуску

## Налаштування
1. Створи бота в @BotFather і отримай токен.
2. Додай секретний токен у середовище Render (Dashboard → Environment):
   - `BOT_TOKEN = <твій_токен_тут>`
3. Або локально створіть змінну середовища перед запуском:
   ```bash
   export BOT_TOKEN="your_token_here"
   ./start.sh
   ```

## Deep link
Щоб користувач бачив вітальне повідомлення майже одразу після переходу — використовуй deep link:
```
https://t.me/YourBotUsername?start=job
```
Після переходу Telegram відкриє чат і користувач натисне **Start** — бот відповість автоматично.

## Деплой на Render.com
1. Завантаж код в GitHub (корінь репозиторію повинен містити `bot.py` та інші файли).
2. На Render → Create → Web Service → підключи репозиторій.
3. Build command: `pip install -r requirements.txt`
4. Start command: `python bot.py` (Render автоматично використовує Procfile при потребі)
5. Додай змінну оточення `BOT_TOKEN` у Render Dashboard.

## Безпека
**Ніколи** не зберігай реальний токен у публічному репозиторії. Використовуй змінні середовища.
