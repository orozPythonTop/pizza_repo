from config import TOKEN

import telebot
from telebot.types import (

    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    print(message)
    data_text = "Приветствую тебя"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    weather = InlineKeyboardButton("Погрода", callback_data="weather")
    markup.add(weather)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)