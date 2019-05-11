#!/usr/bin/env python

import random
import requests

import telebot
import pickle
from telebot import types
from telebot.types import Message

token = '898402690:AAGghYepUWBlRdPBplWVbXTgYZ7PyXxLz2Y'
sticker_id = 'CAADAgADVBMAAp7OCwABdgcEfkxwFGcC'

bot = telebot.TeleBot(token)
users = set()


@bot.message_handler(commands = ['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Это не ответ =(')


@bot.message_handler(content_types = ['text'])
@bot.edited_message_handler(content_types = ['text'])
def echo_digits(message: Message):
    hi = ['привет', 'Привет', 'hi', 'Hi', 'hello', 'Hello']
    if message.text in hi:
        bot.send_message(message.chat.id, 'И тебе ' + str(message.text + ' ') + str(message.from_user.first_name))
        return
    reply = str(random.random())
    if message.from_user in users:
        reply += f"  {message.from_user}, hello again"
    bot.reply_to(message, reply)
    users.add(message.from_user)
    # else:
    #     bot.send_message(message.chat.id, 'Пока не понимаю, о чем ты')


@bot.message_handler(content_types = ['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, sticker_id)


@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling(none_stop = True)
