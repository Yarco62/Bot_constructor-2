import telebot
import os
from telebot import types    
token = '925344997:AAGWfYn_GkgWBd1ViHdp6KcYmhG51yKSjJQ'

bot = telebot.TeleBot(token=token)
    
    
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b0 = types.KeyboardButton("321321")

    b1 = types.KeyboardButton("312123")
    markup.add(b0, b1)

    bot.send_message(message.chat.id, " Hello, thanks for starting me".format(message.from_user, bot.get_me()),
		             parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_response(message):
    
    if message.text.upper() == '876876'.upper():
        bot.send_message(message.from_user.id, 'lkjhkhkjhjk')
    if message.text.upper() == '564456456'.upper():
        bot.send_message(message.from_user.id, 'jhjhgjghjgh')
    if message.chat.type == 'private':
        if message.text == '321321':
            bot.send_message(message.from_user.id, 'dasasddasdsa')    

        if message.text == '312123':
            bot.send_message(message.from_user.id, 'dsadasdsa')    


bot.polling(none_stop=True, interval=0)
