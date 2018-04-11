from gpiozero import LED, Button, LightSensor, MotionSensor, PWMLED
from threading import Timer
from time import sleep
from requests import post


timer=None
ledPWM=PWMLED(21)
led2=LED(22)
led3=LED(23)
but1=Button(11)
sensor_de_luz=LightSensor(8)
sensor_de_movimento=MotionSensor(27)
chave = "cB2Z3ma0b6FHUsDl0AVF_vm7mCMmg0ftj9ohwbwDsBH"
evento="Button1_pressed"
endereco = "https://maker.ifttt.com/trigger/" + evento + "/with/key/" + chave

def botao_pressionado ():
    dados = {"value1": sensor_de_luz.value}
    post(endereco, json=dados)

def movimento_inerte():
    led2.off()
    print("inerte")
    global timer
    timer=Timer(8.0,desliga_led_3)
    timer.start()

def movimento_detectado():
    led2.on()
    led3.on()
    if timer != None:
        timer.cancel()
  
def desliga_led_3():
    led3.off()

sensor_de_movimento.when_motion=movimento_detectado
sensor_de_movimento.when_no_motion=movimento_inerte
but1.when_pressed=botao_pressionado

while True:
    ledPWM.value=sensor_de_luz.value
    sleep(0.2)
