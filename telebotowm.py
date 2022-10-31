from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import telebot

owm = OWM('your_api')#take from https://openweathermap.org/
bot = telebot.TeleBot("your_api")# take from https://t.me/BotFather
config_dict = get_default_config()
config_dict['language'] = 'your language'

@bot.message_handler(func=lambda message: True)
def owm1(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	humidity = w.humidity 
	temperature = w.temperature('celsius')['temp']
	answ = "the temperature: " + str(round(temperature))+"in the city " + message.text  + "is now " + str(w.detailed_status) + "\n"  + " Celsius" + "\n" + "and the humidity of the air " + str(humidity) + "%" + "\n" 
	bot.reply_to(message, answ)

bot.infinity_polling()
