import telebot

class main():
    def _init_(self):
        #token
        TOKEN = ("API_KEY")
        bot = telebot.TeleBot(TOKEN)        

        #commands
        @bot.message_handler(commands=['start','help'])
        def send_welcome(message):
            bot.reply_to(message, "opa, bot teste!")

        #loop
        bot.polling()
        
iniciar = main()
while True:
    metodo = input('o que você deseja fazer? ')
     
    if (metodo == "enviar"):
        iniciar.send_welcome()
    
    if (metodo == "sair"):
        break
    
print('Código Finalizado')
