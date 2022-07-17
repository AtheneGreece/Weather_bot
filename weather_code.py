import requests
import json
from configparser import ConfigParser
country = 'RU'
def weather(city):
    req = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={appid}'
    res = requests.get(req)
    perevod_str_json=json.loads(res.text)
    return(perevod_str_json)
print('Welcome to Weather!!')
config = ConfigParser()
config.read("config.ini")
appid=config['WEATHERCODE']['APPID']
city='Moscow'
temp_c=weather(city)['main']['temp']-273.15
real_city=weather(city)['name']
print(f'Temperature in {real_city} is {round(temp_c)}')
