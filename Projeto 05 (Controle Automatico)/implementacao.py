from gpiozero import LED, Button, LightSensor, MotionSensor, PWMLED
from threading import Timer
from time import sleep
from requests import post
from Adafruit_CharLCD import Adafruit_CharLCD
from flask import Flask

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
evento="Button_pressed"
endereco = "https://maker.ifttt.com/trigger/" + evento + "/with/key/" + chave
listaLeds = ["Luz 1", "Luz 2","Luz 3", "Luz 4", "Luz 5"]
listaLedsRef = [led1,led2,led3,led4]

sensor_de_luz.threshold = 0.4

def salvar_na_planilha (led , estado):
    dados = {"value1": listaLeds[led-1], "value2":estado}
    post(endereco, json=dados)

def retornaEstado(led):
    if(led.is_lit):
        return "aceso"
    
    return "apagado"

def luz_detectada():
    led5.off()
    print("luz")
    sensor_de_luz.threshold = 0.6
    salvar_na_planilha(5,"apagado")
    lcd.clear()
    lcd.message("Sensor: %.2f" % (sensor_de_luz.value))
    
def escuro_detectado():
    led5.on()
    print("escuro")
    sensor_de_luz.threshold = 0.4
    salvar_na_planilha(5,"aceso")
    lcd.clear()
    lcd.message("Sensor: %.2f" % (sensor_de_luz.value))
    
sensor_de_luz.when_light = luz_detectada
sensor_de_luz.when_dark = escuro_detectado

@app.route("/luz/<int:led>/<string:estado>")
def ledServer(led,estado):
    if(estado == "on"):
        listaLedsRef[led-1].on()
        state = "aceso"
    elif estado == "off":
        listaLedsRef[led-1].off()
        state = "apagado"
    
    salvar_na_planilha(led,state)
    

    
#render_template("home.html")

def botao1P():
    led1.toggle()
    salvar_na_planilha(1,retornaEstado(led1))
    
def botao2P():
    led2.toggle()
    salvar_na_planilha(2,retornaEstado(led2))

def botao3P():
    led3.toggle()
    salvar_na_planilha(3,retornaEstado(led3))
    
def botao4P():
    led4.toggle()
    salvar_na_planilha(4,retornaEstado(led4))

but1.when_pressed = botao1P
but2.when_pressed = botao2P
but3.when_pressed = botao3P
but4.when_pressed = botao4P
        
app.run(port=5000, debug=False)
      
        

