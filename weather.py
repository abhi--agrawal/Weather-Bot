import os
import requests
from database import get_random_message as grm

default = "Thats all you're going to get. Now go away let me rest."

def get_cur_weather(city_name):
  api_key = os.getenv('API_KEY')
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  response = requests.get(complete_url) 
  x = response.json()
  if x["cod"] != "404": 
    z = x["weather"]
    message = process_weather_code(z[0]["id"])
    weather_description = 'It is ' + z[0]["description"] + ' ' + message
    return weather_description
  else:
    return "OOPS cannot find that."

def process_weather_code(code):
  if code >= 200 and code < 300:
    return get_thunderstorm()
  elif code >= 300 and code < 400:
    return get_drizzle()
  elif code >= 500 and code < 600:
    return get_rain()
  elif code >= 600 and code < 700:
    return get_snow()
  elif code >= 700 and code < 800:
    return get_mist_or_smoke()
  elif code > 800:
    return get_cloudy()
  else:
    return default

def get_thunderstorm():
  return grm('stormy')

def get_drizzle():
  return grm('drizzle')

def get_rain():
  return grm('rainy')

def get_snow():
  return grm('snowy')

def get_cloudy():
  return grm('cloudy')

def get_mist_or_smoke():
  return grm('misty')
