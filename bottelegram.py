import telebot
from datetime import datetime, timedelta

CHAV_API = "6581266371:AAHb_wLY10rLLXJwyq78lM_yUIg4CVW2IIU"

bot = telebot.TeleBot(CHAV_API)
ano= 2023       #formato AAAA
mes=  11        #usar numero
dia= 19

@bot.message_handler(commands=["contagem"])
def contagem(mensagem):
    datapadrao = datetime(ano, mes, dia)
    hoje = datetime.today() - timedelta(hours=3)

    if datapadrao > hoje:
        delta = datapadrao - hoje

    elif datapadrao <= hoje:    
        delta = hoje - datapadrao

    #bot.send_message(mensagem.chat.id, "Olá, " + mensagem.from_user.first_name + "\nhoje é dia " + str(hoje.day) + "/" + str(hoje.month)  + "\nfaltam: " + str(delta.days) + " dias pro TRI !!!")
    bot.send_message(mensagem.chat.id, "Olá, " + mensagem.from_user.first_name + "\nhoje " + str(hoje.day) + "/" + str(hoje.month)  + "é um belo dia para a Operação Emproguetes\n" + "obs: não se esqueça, Somos Tri Alto Impacto!!!!!!!!!!!!!")
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = "Clique para ver a /contagem"
    bot.reply_to(mensagem, texto)

bot.polling()

