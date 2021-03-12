import telebot
#token
TOKEN = ("API_KEY")
bot = telebot.TeleBot(TOKEN)

#commands
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "opa, bot teste!")

#loop
bot.polling()
