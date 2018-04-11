from turtle import *


def desenha_retangulo(x, y, comprimento, altura, cor):
    penup()
    goto(x,y)
    pendown()
    fillcolor(cor)
    begin_fill()
    setheading(0)
    forward(comprimento)
    right(90)
    forward(altura)
    right(90)
    forward(comprimento)
    right(90)
    forward(altura)
    end_fill()
    return
    
    
def desenha_circulo(x, y, raio, cor):
    penup()
    goto(x,y-raio)
    pendown()
    setheading(0)
    fillcolor(cor)
    begin_fill()
    circle(raio)
    end_fill()
    return
    
    
def desenha_poligono(lista_pontos, cor):
    penup()
    goto(lista_pontos[0]['x'],lista_pontos[0]['y'])
    pendown()
    fillcolor(cor)
    begin_fill()
    for i in lista_pontos:
        goto(i['x'],i['y'])
    end_fill()
    return
    
    
# Bandeira 1
desenha_retangulo(0, 40, 100, 20, 'blue')
desenha_retangulo(0, 20, 100, 20, 'white')
desenha_retangulo(0, 0, 100, 20, 'red')


# Bandeira 2
desenha_retangulo(0, 140, 100, 20, 'orange')
desenha_retangulo(0, 120, 100, 20, 'white')
desenha_retangulo(0, 100, 100, 20, 'green')
desenha_circulo(50, 110, 10, 'orange')

# Bandeira 3
desenha_retangulo(0, 230, 100, 30, 'white')
desenha_retangulo(0, 200, 100, 30, 'red')
desenha_poligono([{'x':0, 'y':230}, {'x':50, 'y':200}, {'x':0, 'y':170}], 'blue')