from aiogram import types
from misc import dp, bot

@dp.message_handler(content_types=['contact'])
async def contact_handler(message):
    await bot.send_message(message.chat.id, "💎")
    await bot.send_message(message.chat.id, "<b>Регистрация успешно пройдена ✅</b>", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(-1001425283269, 
        "<b>🥤 Регистрация 🥤</b>" + 
        "\n<b>Номер:</b> " + message.contact.phone_number + 
        "\n<b>Имя:</b> " + message.contact.first_name + 
        "\n<b>Ник:</b> " + "@" + message.chat.username, 
        parse_mode='html')