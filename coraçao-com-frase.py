import turtle

# Configuração
t = turtle.Turtle()
t.speed(1)  # velocidade devagar
t.color("red", "red")
turtle.bgcolor("black")

# desenhar o coração
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Mensagem no centro do coração
t.penup()
t.goto(0, -20)
t.color("white")
t.write("Você é incrível!" , align="center", font=("Arial", 16, "bold"))

# mostrar
t.hideturtle()
turtle.done()
