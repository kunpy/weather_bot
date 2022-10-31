from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import telebot

owm = OWM('e73464495e7acb3bfda36c756dd158f0')
bot = telebot.TeleBot("5061811891:AAE_NJOu3sX4Ni72oc_QsbgcWc6d7DaRkuM")
config_dict = get_default_config()
config_dict['language'] = 'ru'

@bot.message_handler(func=lambda message: True)
def owm1(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	humidity = w.humidity 
	temperature = w.temperature('celsius')['temp']
	answ = "В городе " + message.text  + " сейчас " + str(w. detailed_status) + "\n" + "температура: " + str(round(temperature))  + " по Цельсию" + "\n" + "влажность воздуха  " + str(humidity) + "%" + "\n" 
	bot.reply_to(message, answ)

bot.infinity_polling()