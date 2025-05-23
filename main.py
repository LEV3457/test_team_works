from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())
# TOKEN = os.getenv("TOKEN")
# CHANNEL_ID = os.getenv("CHANNEL_ID")

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
logger.info("Создан бот")
dp = Dispatcher()
logger.info("Создан Диспетчер")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🔢 Калькулятор\n\n"
        "Отправь мне математическое выражение, например:\n"
        "• 2 + 2\n"
        "• 3.5 * 4\n"
        "• (10 - 3) / 2"
    )

@dp.message()
async def calculate(message: types.Message):
    try:
        expr = message.text.strip()
        if any(c not in "0123456789+-*/(). " for c in expr):
            raise ValueError("Недопустимые символы")

        result = eval(expr)  # Опасно! Лучше использовать безопасный парсер математических выражений
        await message.answer(f"✅ Результат: {result}")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}\n\nПопробуй пример: <code>2 + 2 * 2</code>", parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


