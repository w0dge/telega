import telebot
import Session

token = '2002203224:AAHUFWxdxwELFZRaOnv1Sj5i-J2Tu2XU5Sw'
bot = telebot.TeleBot(token)
print("bot has been started")


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, 'Hello, user')
  if Session.first_user:
    Session.actual_user_id = message.chat.id
    Session.first_user = False
  else:
    bot.send_message(message.chat.id, 'I`m busy now')


@bot.message_handler(commands=['id'])
def return_id(message):
  if message.chat.id == Session.actual_user_id:
    bot.send_message(message.chat.id, message.from_user.id)
  else:
    bot.send_message(message.chat.id, "i'm busy now")


@bot.message_handler(commands=['stop'])
def stop(message):
  if message.chat.id == Session.actual_user_id:
    Session.actual_user_id = 0
    Session.first_user = True
    bot.send_message(message.chat.id, "Now you aren't the host")
  else:
    bot.send_message(message.chat.id, "You aren't the host, w8 for unlock")


bot.infinity_polling()
