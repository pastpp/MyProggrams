import Tokens
import pyowm
from pyowm.utils.config import get_default_config

owm = pyowm.OWM(Tokens.PyowmToken)
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru'

q = input('ваш город: ')
observation = mgr.weather_at_place(q)
w = observation.weather

s = w.detailed_status
d = w.temperature('celsius')['temp_max']
f = w.temperature('celsius')['temp_min']
print("в городе сейчас: " + s)
print("температура будет менятся с "+ str(f) + " до " + str(d) + " градусов, на протяжение всего дня.")