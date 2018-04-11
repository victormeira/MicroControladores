from os import system
from gpiozero import LED, Button, Buzzer
from Adafruit_CharLCD import Adafruit_CharLCD
from mplayer import Player
from time import sleep
from requests import post,get

lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
led1 = LED(21)
but1 = Button(11)
but2 = Button(12)
but3 = Button(13)
buzzer = Buzzer(16)

# Mata todos os aplicativos "mplayer" e "arecord"
system("killall mplayer")
system("killall arecord")


# parâmetros iniciais do Telegram
chave = "569417588:AAG35HDZVu01D44wiR_847xr2EXX1n_QjzM"
id_da_conversa = "547111519"
endereco_base = "https://api.telegram.org/bot" + chave

proximo_id_de_update = 0

def enviaAlerta():
    endereco = endereco_base + "/sendMessage"
    dados = {"chat_id": id_da_conversa, "text": "Abrir porta para esta pessoa?"}
    resposta = post(endereco, json=dados)
    
    system("fswebcam foto.jpeg")
    endereco = endereco_base + "/sendPhoto"
    dados = {"chat_id": id_da_conversa}
    
    arquivo = {"photo":open("foto.jpeg","rb")}
    resposta = post(endereco, data=dados, files=arquivo)

but1.when_pressed = enviaAlerta
but2.when_pressed = led1.off

while True:
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update}
    resposta = get(endereco,json=dados)
    dic_da_resposta = resposta.json()

    for resultado in dic_da_resposta["result"]:
        mensagem = resultado["message"]
        if "text" in mensagem:
            texto = mensagem["text"]
            if(texto == "Abrir"):
                led1.on()
            elif(texto == "Alarme"):
                buzzer.beep(n=5, on_time = 0.1, off_time = 0.1)
        proximo_id_de_update = int(resultado["update_id"]) + 1 

            
                           
        
