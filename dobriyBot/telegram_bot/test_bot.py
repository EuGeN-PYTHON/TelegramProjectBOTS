from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Привет! Рад тебе помочь!')

@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
    await message.answer(message.text)

#хендлер на проверку содержания в сообщение Такси
@dp.message_handler(lambda message: 'такси' in message.text)
async def check_taxi(message: types.Message):
    await message.answer('такси')

#хендлер на проверку содержания в сообщение Нло
@dp.message_handler(lambda message: 'нло' in message.text)
async def check_nlo(message: types.Message):
    await message.answer('нло')

#хендлер на проверку начала сообщения со слова такси
@dp.message_handler(lambda message: message.text.startswith('такси'))
async def check_start_taxi(message: types.Message):
    await message.answer(message.text[6:])


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды!')
    await message.delete()

executor.start_polling(dp, skip_updates=True)
