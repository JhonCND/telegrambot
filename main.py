import telebot
import requests
import emoji
from web import webscraping
#token
texto = webscraping()
TOKEN = ("1694856172:AAHe3ibvW85P1fUge2v2n4ES3DnJq3mkRuk")
bot = telebot.TeleBot(TOKEN)
#commands
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
     bot.reply_to(message, texto)
#loop
bot.polling()
'''
#web scraping
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "opa, bot teste!") ''' 
