import Tokens
import pyowm
from pyowm.utils.config import get_default_config

class Weather():
    def __init__(self, place):
        self.place = place
    def FoundWeather(self):
        owm = pyowm.OWM(Tokens.PyowmToken)
        mgr = owm.weather_manager()

        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        observation = mgr.weather_at_place(self.place)
        w = observation.weather

        s = w.detailed_status
        d = w.temperature('celsius')['temp_max']
        f = w.temperature('celsius')['temp_min']
        qwerty = "в городе сейчас " + s + "\n"
        qwerty += "температура будет менятся с "+ str(f) + " до " + str(d) + " градусов, на протяжение всего дня."
        print(qwerty)
#Объекты
Moscow = Weather('moscow')
StPeterburg = Weather('санкт-петербург')
Voronezh = Weather('воронеж')
Saratov = Weather('саратов')
Ufa = Weather('уфа')
NizhniyNovgorod = Weather('нижний новгород')
Derbent = Weather('дербент')


StPeterburg.FoundWeather()