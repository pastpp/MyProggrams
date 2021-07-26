import telebot
import Tokens
from telebot import types
import pyowm
from pyowm.utils.config import get_default_config

owm = pyowm.OWM(Tokens.PyowmToken)
mgr = owm.weather_manager()
bot = telebot.TeleBot(Tokens.WetManagerToken)


@bot.message_handler( content_types =['text'])
def wllpjdgd(message):
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

bot.polling( none_stop = True)