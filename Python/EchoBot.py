import telebot
import Tokens
import pyowm
from pyowm.utils.config import get_default_config
from telebot import types

bot = telebot.TeleBot(Tokens.EchoBotToken)
owm = pyowm.OWM(Tokens.PyowmToken)
mgr = owm.weather_manager()

@bot.message_handler( commands=['start'])
def welcome(message):
    #Запуск кнопки(кнопок)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #Сами кнопки
    items1 = types.KeyboardButton("Баланс")

    #Отображение кнопки в чате.
    marcup.add(items1)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n Я - <b> {1.first_name}</b>, бот созданный для вычисления ИМТ(Индекса массы тела).".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=marcup)

@bot.message_handler( content_types =['text'])
def wllpjdgd(message):
    if message.chat.type == 'private':
        if message.text == 'Баланс':
            bot.send_message(message.chat.id, "ваш город: ")
        else:
            bot.send_message(message.chat.id,"ты издеваешься? Кнопки тебе зачем нужны?")
bot.polling( none_stop = True) 
