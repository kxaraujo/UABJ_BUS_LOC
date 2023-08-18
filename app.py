from flask import Flask, request, render_template
import telebot
import os
from buffer import MessageBuffer
import time


# Cria uma instância da classe MessageBuffer
message_buffer = MessageBuffer()

# Token de acesso do bot do Telegram
token = '6103231923:AAH1sxXKyQMZrwbrjT9VsL5coUK7OD24qT4'

# Cria uma nova instância do bot
bot = telebot.TeleBot(token)

# Cria uma instância do servidor web Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/script.js')
def script():
    return app.send_static_file('script.js')


# Rota para o comando /start
@bot.message_handler(commands=['start'])
def comando_start(message):
    chat_id = message.chat.id
    print(chat_id)
    bot.send_message(chat_id, 'Olá! Digite o comando /enviar_distancia para obter a distância.')

@app.route('/enviar_distancia', methods=['POST'])
def enviar_distancia():
    localizacoes = request.json['localizacoes']
    chat_id = request.json['chat_id']  # Obtém o chat ID do JSON recebido
    mensagem = "Buscando...\n"
    
    for localizacao in localizacoes:
        nome = localizacao['name']
        mensagem = f"Sua localização atual é: {nome}\n"
        message_buffer.add_message((chat_id, mensagem))  # Adiciona a mensagem ao buffer
    
    return "OK"

def enviar_mensagens_buffer():
    while True:
        time.sleep(30)  # Espera por 30 segundos
        messages = message_buffer.get_messages()
        for chat_id, mensagem in messages:
            bot.send_message(chat_id, mensagem)

# Inicia uma thread para enviar as mensagens do buffer
import threading
threading.Thread(target=enviar_mensagens_buffer).start()


if __name__ == '__main__':
    app.run()
    

