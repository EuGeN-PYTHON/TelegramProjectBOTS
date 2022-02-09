from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from variables.variable import FIRST_ITEM, SECOND_ITEM, THIRD_ITEM, FOURTH_ITEM, FIFTH_ITEM, NAMEBOT
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет! Рад тебе помочь!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(f'Общение со мной через личные сообщение, напиши мне: \nhttps://t.me/{NAMEBOT}')


# @dp.message_handler(commands=['Режим работы'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВС-ЧТ с 9:00 до 20:00, ПТ-СБ с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Тверская 1')#, reply_markup=ReplyKeyboardRemove)

# @dp.message_handler(commands=['Услуги'])
async def list_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=[FIRST_ITEM, SECOND_ITEM])
    dp.register_message_handler(open_command, commands=[THIRD_ITEM])
    dp.register_message_handler(place_command, commands=[FOURTH_ITEM])
    dp.register_message_handler(list_command, commands=[FIFTH_ITEM])