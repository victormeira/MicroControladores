from json import load
from turtle import *

# Copie as funções da Implementação aqui

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
    goto(lista_pontos[0]['x'],lista_pontos[0]['y'])
    end_fill()
    return
    
    

# Implemente a função abaixo
def desenha_bandeira(lista_de_elementos):
    for i in lista_de_elementos:
        if i['tipo'] == 'retangulo':
            desenha_retangulo(i['x'],i['y'],i['comprimento'],i['altura'],i['cor'])
        elif i['tipo'] == 'circulo':
            desenha_circulo(i['x'],i['y'],i['raio'],i['cor'])
        else:
            desenha_poligono(i['pontos'],i['cor'])
    return

dicionario = load(open('pais_misterioso.json'))
desenha_bandeira(dicionario)

# Crie um arquivo "nova_bandeira.json" com dados de uma nova bandeira e desenhe-a