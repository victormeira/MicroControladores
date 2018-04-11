from flask import Flask, render_template, redirect
from py_irsend.irsend import*
from time import sleep
from threading import Timer
app=Flask(__name__)



@app.route("/")
def mostrar_pagina_inicial():
    return render_template("home.html")

@app.route("/power")
def power():
    send_once('tomate',["KEY_POWER"])
    return redirect("/")

@app.route("/volup")
def volup():
    send_once('tomate',["KEY_VOLUMEUP"])
    return redirect("/")

@app.route("/voldown")
def voldown():
    send_once('tomate',["KEY_VOLUMEDOWN"])
    return redirect("/")

@app.route("/proxcanal")
def proxcanal():
    send_once('tomate',["KEY_LIST"])
    sleep(0.5)
    send_once('tomate',["KEY_DOWN"])
    sleep(0.5)
    send_once('tomate',["KEY_ENTER"])
    sleep(0.5)
    send_once('tomate',["KEY_EXIT"])
    return redirect("/")

@app.route("/antcanal")
def antcanal():
    send_once('tomate',["KEY_LIST"])
    sleep(0.5)
    send_once('tomate',["KEY_UP"])
    sleep(0.5)
    send_once('tomate',["KEY_ENTER"])
    sleep(0.5)
    send_once('tomate',["KEY_EXIT"])
    return redirect("/")

@app.route("/mute")
def mute():
    send_once('tomate',["KEY_MUTE"])
    return redirect("/")

@app.route("/timer/<int:segundos>")
def timer(segundos):
    t=Timer(segundos,power)
    t.start()
    return redirect("/")

@app.route("/canal/<int:numero>")
def canal(numero):
    send_once('tomate',["KEY_3","KEY_3"])
    send_once('tomate',["KEY_ENTER"])
    sleep(2)
    send_once('tomate',["KEY_LIST"])
    sleep(1)
    for i in range(numero-1):
        send_once('tomate',["KEY_DOWN"])
        sleep(0.5)
    send_once('tomate',["KEY_ENTER"])
    sleep(0.5)
    send_once('tomate',["KEY_EXIT"])
    return redirect("/")

app.run(port=5000, debug=True)