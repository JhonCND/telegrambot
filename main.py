import telebot
import requests
from web import webscra

#token
texto = webscra()
TOKEN = ("CHAVE_KEY")
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
