from aiogram import types
from misc import dp,bot


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bat_a = types.KeyboardButton(text='🥤РЕГИСТРАЦИЯ🥤', request_contact=True)
    markup.add(bat_a)
    await bot.send_message(message.chat.id, f'🥤Для начала <b>пройдите регистрацию.</b>'
                                            ,parse_mode='html',reply_markup=markup)