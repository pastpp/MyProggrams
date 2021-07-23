import telebot
import Tokens
import pyowm
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot(Tokens.WetManagerToken)
owm = pyowm.OWM(Tokens.PyowmToken)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place( message.text )
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    w = observation.weather
    s = w.detailed_status
    d = w.temperature('celsius')['temp_max']
    f = w.temperature('celsius')['temp_min']
    answer = "в городе сейчас " + s + "\n\n"
    answer += "температура будет менятся с "+ str(f) + " до " + str(d) + " градусов, на протяжение всего дня."

#                           !! РАБОТАЕТ ТОЛЬКО С ГОРОДАМИ(из-за pyowm) !!


#Ответ собщением на сообщение(Forward)
    #bot.reply_to(message, message.text)


#Отвечает на запрошенный город, погодой(weather)
    bot.send_message(message.chat.id, answer)


#Дублирует сообщение.
    #bot.send_message(message.chat.id, message.text)

bot.polling() 