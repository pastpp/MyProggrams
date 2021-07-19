from pyowm import OWM
owm = OWM('d11d4eecace811fd43ba83c3520611fa')
mgr = owm.weather_manager()
q = input('your city: ')
observation = mgr.weather_at_place(q)
w = observation.weather
s = w.detailed_status
d = w.temperature('celsius')['temp_max']
f = w.temperature('celsius')['temp_min']
print(s)
print("temperature: "+ str(f) + " - " + str(d))