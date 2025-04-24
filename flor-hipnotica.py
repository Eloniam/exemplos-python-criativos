import turtle

#configuração inicial
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("magenta")

#desenhar a flor
for i in range(72):
    t.circle(100)
    t.left(5)

# Finalizar
t.hideturtle()
turtle.done()
