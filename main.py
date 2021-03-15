import telebot
import requests
from web import webscra

#token
texto = webscra()
TOKEN = ("1694856172:AAHe3ibvW85P1fUge2v2n4ES3DnJq3mkRuk")
bot = telebot.TeleBot(TOKEN)
#commands
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
     bot.reply_to(message, texto)
'''
#web scraping
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "opa, bot teste!") '''
    
#loop
bot.polling()
