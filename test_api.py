
from pyowm import OWM

api_key = "da093ff3980a7f4cab335019cf1e6029"

#get access to your api with your key
owm = OWM(api_key)

#call the manager to handle the data
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Tokyo')
w = observation.weather

#wind = w.wind()
#humidity = w.humidity
#temperature = w.temperature("celsius")

#print(f"Wind: {wind}\nHumidity: {humidity} \nTemperature: {temperature}")
print ( w )
