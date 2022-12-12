import telebot
import random
from telebot import types
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +"! Нажми 'обновить'.")

# @bot.message_handler(content_types=['button'])
# def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Обновить')
    markup.add(item1)
    bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +"! Нажми 'обновить'.", reply_markup=markup)

    # @bot.message_handler(commands=['button'])
    # def button_message(message):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #
    # item1 = types.KeyboardButton("Кнопка")
    # markup.add(item1)
    # bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Обновить":
        f = open("all_films.txt")
        lines = f.readlines()
        rand_line = random.randint(1, 15000)
        bot.send_message(message.chat.id, lines[rand_line])


bot.infinity_polling()

#в плане доделать предложение фильмов по жанрам, и добавить возможность юзерам предлагать фильмы в список.
# Решил сдать на начальном этапе, позже добавлю функционал.