from os import system
from gpiozero import LED, Button
from Adafruit_CharLCD import Adafruit_CharLCD
from mplayer import Player
from time import sleep
from requests import post

lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
led1 = LED(21)
but1 = Button(11)
but2 = Button(12)
but3 = Button(13)


# Mata todos os aplicativos "mplayer" e "arecord"
system("killall mplayer")
system("killall arecord")

# parâmetros iniciais do Telegram
chave = "569417588:AAG35HDZVu01D44wiR_847xr2EXX1n_QjzM"
id_da_conversa = "547111519"
endereco_base = "https://api.telegram.org/bot" + chave

def gravaAudio():
    lcd.clear()
    lcd.message("Gravando...")
    system("arecord --duration 5 audio.wav")
    lcd.clear()

def tiraFotos():
    for i in range(0,5):
        nome = "foto-" + str(i) + ".jpeg"
        comando = "fswebcam --skip 10 " + nome
        system(comando)
        led1.blink(n=1,on_time = 0.5, off_time = 0.5)
        sleep(2)
        
def enviaMensagem():
    endereco = endereco_base + "/sendMessage"
    dados = {"chat_id": id_da_conversa, "text": "Botao 3 pressionado!"}
    resposta = post(endereco, json=dados)


but1.when_pressed = gravaAudio
but2.when_pressed = tiraFotos
but3.when_pressed = enviaMensagem