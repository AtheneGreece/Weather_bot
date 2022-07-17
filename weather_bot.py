import telebot
import weather_code
from telebot import types
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
code=config['TELEGRAMCODE']['CODE']

bot = telebot.TeleBot(f'{code}')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}! Your ID is {message.from_user.id}')
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="Moscow", callback_data="moscow")
    button2 = types.InlineKeyboardButton(text="Saint Petersburg", callback_data="saint_p")
    button3 = types.InlineKeyboardButton(text="Novosibirsk", callback_data="novosib")
    button4 = types.InlineKeyboardButton(text="Krasnodar", callback_data="krasnodar")
    button5 = types.InlineKeyboardButton(text="Another city", callback_data="an_city")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, 'Choose your city:', reply_markup=markup)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'moscow':
        bot.send_message(c.message.chat.id, 'Your city is Moscow')
        city='Moscow'
        temp_c = weather_code.weather(city)['main']['temp'] - 273.15
        real_city = weather_code.weather(city)['name']
        bot.send_message(c.message.chat.id, f'Temperature in {real_city} is {round(temp_c)}')
    elif c.data == 'saint_p':
        bot.send_message(c.message.chat.id, 'Your city is Saint Petersburg')
        city = 'Saint Petersburg'
        temp_c = weather_code.weather(city)['main']['temp'] - 273.15
        real_city = weather_code.weather(city)['name']
        bot.send_message(c.message.chat.id, f'Temperature in {real_city} is {round(temp_c)}')
    elif c.data == 'novosib':
        bot.send_message(c.message.chat.id, 'Your city is Novosibirsk')
        city = 'Novosibirsk'
        temp_c = weather_code.weather(city)['main']['temp'] - 273.15
        real_city = weather_code.weather(city)['name']
        bot.send_message(c.message.chat.id, f'Temperature in {real_city} is {round(temp_c)}')
    elif c.data == 'krasnodar':
        bot.send_message(c.message.chat.id, 'Your city is Krasnodar')
        city = 'Krasnodar'
        temp_c = weather_code.weather(city)['main']['temp'] - 273.15
        real_city = weather_code.weather(city)['name']
        bot.send_message(c.message.chat.id, f'Temperature in {real_city} is {round(temp_c)}')
    elif c.data == 'an_city':
        bot.send_message(c.message.chat.id, 'Please, enter your city')
        @bot.message_handler()
        def get_user_text(message):
            city=message.text
            bot.send_message(c.message.chat.id, f'Your city is {city}')
            temp_c = weather_code.weather(city)['main']['temp'] - 273.15
            real_city = weather_code.weather(city)['name']
            bot.send_message(c.message.chat.id, f'Temperature in {real_city} is {round(temp_c)}')


bot.polling(none_stop=True)