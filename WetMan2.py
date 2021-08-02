import telebot
import Tokens
from telebot import types
import pyowm
from pyowm.utils.config import get_default_config

owm = pyowm.OWM(Tokens.PyowmToken)
mgr = owm.weather_manager()
bot = telebot.TeleBot(Tokens.WetManagerToken)

@bot.message_handler(commands=['start'])
def welcome(message):
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Button1 = types.KeyboardButton("Санкт-Петербург")
    Button2 = types.KeyboardButton("Дербент")
    Button3 = types.KeyboardButton("Москва")
    Button4 = types.KeyboardButton("Архангельск")
    markup.add(Button1,Button2,Button3,Button4)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который находит пагоду.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler( content_types =['text'])
def wllpjdgd(message):
    if message.chat.type == 'private':
        
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        observation = mgr.weather_at_place( message.text )
        w = observation.weather

        s = w.detailed_status
        d = w.temperature('celsius')['temp_max']
        f = w.temperature('celsius')['temp_min']
        qwerty = "в городе сейчас " + s + "\n"
        qwerty += "температура будет менятся с "+ str(f) + " до " + str(d) + " градусов, на протяжение всего дня."
        bot.send_message(message.chat.id, qwerty)
    else:
        bot.send_message(message.chat.id, "Ты издеваешься? Кнопки здесь для чего по-твоему?")


bot.polling( none_stop = True )

