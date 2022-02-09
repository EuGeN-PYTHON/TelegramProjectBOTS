from aiogram import types, Dispatcher
from create_bot import dp
import string
import json


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('stopwords/cenz.json')))) != set():
        await message.reply('Мат запрещен!')
        await message.delete()

    # if message.text == 'Привет':
    # Отвечаем на сообщение(тоже что и написали)
    #     await message.answer('И тебе привет!')

    # Отвечаем на сообщение упоминая сообщения (тоже что и написал)
    # await message.reply(message.text)
    # Только при уже начатом диалоге (сообщение в личные сообщения):
    # await bot.send_message(message.from_user.id, message.text)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)