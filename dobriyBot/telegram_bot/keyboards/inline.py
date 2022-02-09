from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

answ = {}

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

#Кнопки ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))

@dp.message_handler(commands=['Ссылки'])
async def url_command(message: types.Message):
    await message.answer('Ссылки: ', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми меня', callback_data='www'))


@dp.message_handler(commands=['test'])
async def url_command(message: types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inkb)

@dp.callback_query_handlers(text='www')
async def www_call(callback : types.CallbackQuery):
    #callback.answer отображатие в виде всплывающего окна
    #callback.message.answer отображатие в виде сообщения
    # callback.message.answer(show_alert=True) отображатие в виде сообщения alert
    await callback.message.answer('Произошло нажатие инлайн кнопки')
    # await callback.answer()
    await callback.answer('Произошло нажатие инлайн кнопки', show_alert=True)


inkb_like = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),
                                                  InlineKeyboardButton(text='Not Like', callback_data='like_-1'))

@dp.message_handler(commands=['test'])
async def url_command(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb_like)

@dp.callback_query_handlers(Text(startswith='like_', ignore_case=True))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали!')
    else:
        await callback.answer('Вы уже проголосовали!', show_alert=True)




executor.start_polling(dp, skip_updates=True)

