from gpiozero import LED, Button, LightSensor, MotionSensor, PWMLED
from threading import Timer
from time import sleep
from requests import post
from Adafruit_CharLCD import Adafruit_CharLCD
from flask import Flask, send_from_directory
from os import system
from datetime import datetime

##system("fswebcam --resolution 640x480 foto.jpeg")

app = Flask(__name__)

lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)
lcd.clear()
timer=None
led1=LED(21)
led2=LED(22)
led3=LED(23)
led4=LED(24)
led5=PWMLED(25)
but1=Button(11)
but2 = Button(12)
but3 = Button(13)
but4 = Button(14)
sensor_de_luz=LightSensor(8)
sensor_de_movimento=MotionSensor(27)
chave = "cB2Z3ma0b6FHUsDl0AVF_vm7mCMmg0ftj9ohwbwDsBH"
evento="Sendemail"
endereco = "https://maker.ifttt.com/trigger/" + evento + "/with/key/" + chave

@app.route("/<string:nome_foto>")
def foto(nome_foto):
    return send_from_directory("fotos",nome_foto)   

def tirar_foto():
    agora = datetime.now()
    hora = agora.strftime("%H:%M:%S")
    endereco_foto = "./fotos/foto-" + hora + ".jpeg"
    foto = "fswebcam " + endereco_foto
    #print(foto)
    system(foto)
    print("tirei foto")
    global timer
    timer = Timer(3.0,tirar_foto)
    timer.start()

def movimento_detectado():
    print("mov")
    global timer
    timer = Timer(3.0,tirar_foto)
    timer.start()
        
        
def movimento_inerte():
    print("iner")
    global timer
    if(timer!=None):
        timer.cancel()
        
sensor_de_movimento.when_motion=movimento_detectado
sensor_de_movimento.when_no_motion=movimento_inerte     

app.run(port=5000, debug=False) 
