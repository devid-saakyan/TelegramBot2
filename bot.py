import telebot
from telebot import types
from telebot.types import Message
import pars as p
TOKEN = '824645728:AAE6uCGHJGXgx9zdRVkPyUzOHI15oEvTCtE'
bot = telebot.TeleBot(TOKEN)

ans_h = p.get_hockey()
ans_b = p.get_basketball()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '✅✅ВЫ ЗАПУСТИЛИ БОТ, НАЖМИТЕ НА НУЖНУЮ КНОПКУ ЧТОБЫ ПОЛУЧИТЬ СПИСОК МАТЧЕЙ✅✅', reply_markup = keyboard())
    bot.register_next_step_handler(message, send_anything)
#bot.message_handler(content_types=["text"])
def send_anything(message):
    chat_id = message.chat.id
    if message.text == '🏒🥅 Hockey (USA NXL 2019 - 2020)  🏒🥅':
        bot.send_message(chat_id, '👇👇Введи числом количество матчей для показа (ИХ ОКОЛО 500) 👇👇')
        bot.register_next_step_handler(message, obrabotka, ans_h)
    elif message.text == '🏀🏀 Basketball (VTB - United - League 2019-2020) 🏀🏀':
        bot.send_message(chat_id, '👇👇Введи числом количество матчей для показа (ИХ ОКОЛО 500) 👇👇')
        bot.register_next_step_handler(message, obrabotka2, ans_h)
    elif message.text == '❌STOP❌':
        bot.send_message(chat_id, '❌❌Бот остановлен❌❌')
        bot.stop_polling()
        bot.register_next_step_handler(message, send_anything)

def obrabotka(message, data):
    chat_id = message.chat.id
    text1 = 'Лови список матчей по хоккею'
    if message.text.isdigit():
        bot.send_message(chat_id, text1)
        for i in range(int(message.text)):
            bot.send_message(chat_id, ' 😱😱   🥅{}🥅 🆚🆚 🥅{}🥅  😱😱  ⏰ {} ⏰'.format(ans_h[i][0],ans_h[i][1], ans_h[i][2]), reply_markup = keyboard())
    bot.register_next_step_handler(message, send_anything)

def obrabotka2(message, data):
    chat_id = message.chat.id
    text2 = 'Лови список мачтей по баскетболу'
    if message.text.isdigit():
        bot.send_message(chat_id, text2)
        for i in range(int(message.text)):
            bot.send_message(chat_id, ' 🧐🧐   🏀{}🏀   🆚🆚  🏀{}🏀   🧐🧐   ⏰ {} ⏰'.format(ans_b[i][0], ans_b[i][1], ans_b[i][2]))
    bot.register_next_step_handler(message, send_anything)
                         
def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    btn1 = types.KeyboardButton('🏒🥅 Hockey (USA NXL 2019 - 2020)  🏒🥅')
    btn2 = types.KeyboardButton('🏀🏀 Basketball (VTB - United - League 2019-2020) 🏀🏀')
    btn3 = types.KeyboardButton('❌STOP❌')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup

bot.polling()
