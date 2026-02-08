import telebot
TOKEN = '8363932836:AAE9pPoNeTBod3-BYHscry6EZ6Z97fZ400k'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🦾 Мой репозиторий GIT")
    item2 = types.KeyboardButton("✍️ Написать мне в личку Telegram")
    item3 = types.KeyboardButton("🔄 Перезапуск")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, f"Приветствую, рад познакомиться, {message.from_user.first_name}!", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🦾 Мой репозиторий GIT':
            bot.send_message(message.chat.id, 'https://github.com/Aleksandr-Khramchenkov')
        elif message.text == '✍️ Написать мне в личку Telegram':
            bot.send_message(message.chat.id, 'https://t.me/Alex_Khramchenkov')
        elif message.text == '🔄 Перезапуск':  
            welcome(message)  
        else:
            bot.send_message(message.chat.id, 'Не знаю что ответить😢')

bot.polling(none_stop=True)