import telebot
from test import Testing
from Bot import token

bot = telebot.TeleBot(token)

if Testing.test_string():
    return bot.send_message(message.chat.id, "Yuppy, info is correct")
else:
    return bot.send_message(message.chat.id, ":(), info is not correct")

if Testing.test_boolean():
    return bot.send_message(message.chat.id, "Yuppy, info 2  is correct")
else:
    return bot.send_message(message.chat.id, ":(), info 2 is not correct")    
