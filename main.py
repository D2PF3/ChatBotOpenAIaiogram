import logging
import os
import json

from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

initial_prompt = "Вопрос:"

current_prompt = initial_prompt


def save_conversation(question, answer):
    data = {
        "question": question,
        "answer": answer
    }
    with open("chat_log.json", "a", encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
        f.write("\n")



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id

    message = (
        f"Я готов ответить на любой ваш вопрос. Просто задайте его в следующем сообщении."
    )

    await bot.send_message(user_id, message)


@dp.message_handler(content_types=[types.ContentType.TEXT], state=None)
async def handle_message(message: types.Message, state: FSMContext):
    user_input = f"Пользователь: {message.text}"
    user_id = message.from_user.id
    logging.info(f"User {user_id} input: {user_input}")

    async with state.proxy() as data:
        user_messages = data.get("user_messages", [])
        user_messages.append(user_input)

        if len(user_messages) > 3:
            user_messages = user_messages[-2:]

        data["user_messages"] = user_messages

    messages = [
        {"role": "system", "content": "Ты отвечаешь на вопросы пользователя"},
    ]

    for msg in user_messages:
        messages.append({"role": "user", "content": msg})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=messages
    )

    generated_text = response.choices[0].message.content
    logging.info(f"Neural network response: {generated_text}")

    save_conversation(message.text, generated_text)

    await message.answer(generated_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
