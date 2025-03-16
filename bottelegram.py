import telebot
from datetime import datetime, timedelta

CHAV_API = "your-api-key"

bot = telebot.TeleBot(CHAV_API)
ano= 2025       #formato AAAA
mes= 12         #usar numero
dia= 31

@bot.message_handler(commands=["contagem"])
def contagem(mensagem):
    datapadrao = datetime(ano, mes, dia)
    hoje = datetime.today() - timedelta(hours=3)

    if datapadrao > hoje:
        delta = datapadrao - hoje

    elif datapadrao <= hoje:    
        delta = hoje - datapadrao

    bot.send_message(mensagem.chat.id, "Olá, " + mensagem.from_user.first_name + "\nhoje é dia " + str(hoje.day) + "/" + str(hoje.month) + "\nfaltam: 10.000 para o VERDE !!!" + "\nfaltam: " + str(delta.days) + " dias pras auditorias do EDL !!!")
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = "Clique para ver a /contagem"
    bot.reply_to(mensagem, texto)

bot.polling()

