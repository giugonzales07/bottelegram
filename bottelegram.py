import telebot
from datetime import datetime, timedelta

CHAV_API = "6581266371:AAHb_wLY10rLLXJwyq78lM_yUIg4CVW2IIU"

bot = telebot.TeleBot(CHAV_API)
ano= 2024       #formato AAAA
mes=  1         #usar numero
dia= 30

@bot.message_handler(commands=["contagem"])
def contagem(mensagem):
    datapadrao = datetime(ano, mes, dia)
    hoje = datetime.today() - timedelta(hours=3)

    if datapadrao > hoje:
        delta = datapadrao - hoje

    elif datapadrao <= hoje:    
        delta = hoje - datapadrao

    bot.send_message(mensagem.chat.id, "Olá, " + mensagem.from_user.first_name + "\nhoje é dia " + str(hoje.day) + "/" + str(hoje.month) + "\nfaltam: 83.333 para o VERDE !!!" + "\nfaltam: " + str(delta.days) + " dias pras auditorias do EDL !!!")
    #bot.send_message(mensagem.chat.id, "Olá, " + mensagem.from_user.first_name + "\nhoje (" + str(hoje.day) + "/" + str(hoje.month)  + ") é um belo dia para a Operação Emproguetes\n\n" + "obs: não se esqueça, Somos Tri Alto Impacto!!!!!!!!!!!!!")
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = "Clique para ver a /contagem"
    bot.reply_to(mensagem, texto)

bot.polling()

