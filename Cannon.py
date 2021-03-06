"""Cannon, hitting targets with projectiles.
Exercises
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Función para detectar un click fuera del área designada para el juego.
#Responde dando a la bola una velocidad y posición que la hacen invisible
#al momento de jugar
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 400) / 25
        speed.y = (y + 400) / 25

#Función que verifica si un objeto se encuentra dentro de los límites de la pantalla
#del juego.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Función que dibuja los objetivos como puntos azules y las bolas como puntos rojos
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#Esta función sirve para actualizar el movimiento de los objetivos y de la pelota cada 50 milisegundos
#Se llama a la función draw para dibujar las nuevas posiciones de los objetivos y la pelota, y se llama 
#a la función inside para corroborar si la pelota ya fue disparada y si así lo fue, comenzar su decenso
#por la gravedad y su movimiento hacia el punto al que se disparó.
def move():
    "Move ball and targets."

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1

    if inside(ball):
        speed.y -= 0.7
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()