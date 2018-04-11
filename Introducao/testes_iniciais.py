from turtle import *

# Parte 1: desenhe o retângulo no centro
penup()
goto(-50,25)
pendown()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)

# Parte 2: desenhe o triângulo equilátero à direita
penup()
goto(270,-30)
pendown()
setheading(60)
forward(60)
right(120)
forward(60)
right(120)
forward(60)

# Parte 3: desenhe o zigue-zague à esquerda
penup()
goto(-300,50)
pendown()
setheading(270)
for i in range(1,6):
    forward(10)
    left(90)
    forward(80)
    right(90)
    forward(10)
    right(90)
    forward(80)
    left(90)

    

# Parte 4: desenhe o círculo em cima
penup()
goto(-50,250)
pendown()
circle(50)



# Parte 5: desenhe a espiral na parte debaixo
penup()
goto(0,-250)
pendown()
for i in range(1,60):
    circle(i,20)
    

