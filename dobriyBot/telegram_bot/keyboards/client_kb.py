from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from variables.variable import FIRST_ITEM, SECOND_ITEM, THIRD_ITEM, FOURTH_ITEM, FIFTH_ITEM,TENTH_ITEM, NINTH_ITEM, NAMEBOT

b1 = KeyboardButton(f'/{THIRD_ITEM}')
b2 = KeyboardButton(f'/{FOURTH_ITEM}')
b3 = KeyboardButton(f'/{FIFTH_ITEM}')
b4 = KeyboardButton('Поделиться контактом', request_contact=True)
b5 = KeyboardButton('Отправить местоположение', request_location=True)


# one_time_keyboard=True при нажатии клавиатура сворачивается
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add - с новой строки; insert - добавляет в строку если есть место; row - в строку
kb_client.add(b1).add(b2).insert(b3).row(b4, b5)
# kb_client.row(b1, b2, b3)
