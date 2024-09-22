import turtle

# Configurar la ventana de dibujo
window = turtle.Screen()
window.bgcolor("sky blue")

# Crear un objeto Turtle para dibujar
girasol = turtle.Turtle()
girasol.shape("circle")
girasol.color("yellow")
girasol.speed(0)  # Velocidad máxima

# Función para dibujar un pétalo
def dibujar_petalo():
    girasol.begin_fill()
    for _ in range(2):
        girasol.circle(50, 60)
        girasol.left(120)
    girasol.end_fill()

# Función para dibujar el girasol completo
def dibujar_girasol():
    girasol.fillcolor("yellow")  # Rellenar pétalos de amarillo
    for _ in range(6):
        dibujar_petalo()
        girasol.left(60)

# Función para dibujar el tallo
def dibujar_tallo():
    girasol.right(90)
    girasol.pensize(5)
    girasol.forward(150)
    girasol.pensize(1)  # Volver a grosor normal
    girasol.left(90)

# Función para mover la tortuga a una posición específica
def mover_a_posicion(x, y):
    girasol.penup()
    girasol.goto(x, y)
    girasol.pendown()

# Dibujar varias flores en una fila
posiciones = [(-250, 0), (-100, 0), (50, 0), (200, 0)]
for pos in posiciones:
    mover_a_posicion(pos[0], pos[1])
    dibujar_girasol()
    dibujar_tallo()

# Ocultar la tortuga después de dibujar las flores
girasol.hideturtle()

# Crear un objeto Turtle para el título
titulo = turtle.Turtle()
titulo.penup()
titulo.goto(0, 100)  # Posición del título
titulo.hideturtle()
titulo.color("dark red")

# Escribir el título "Feliz Día"
titulo.write("Feliz Día, mi amor", align="center", font=("Arial", 24, "bold"))

# Crear otro objeto Turtle para el resto del texto
texto = turtle.Turtle()
texto.penup()
texto.goto(0, -250)  # Posición del texto
texto.hideturtle()
texto.color("black")

# Escribir el mensaje
mensaje = (
    "Te amo muchísimo y eres una persona muy especial para mí.\n"
    "Quiero ser mejor cada día por ti, porque eres lo más importante en mi vida.\n"
    "Me comprometo, tanto conmigo como con nuestra relación, a mejorar y aprender\n"
    "de los errores que he cometido. Eres mi luz, mi vida, y mi inspiración.\n"
    "Te amo, mi Wiwowi."
)

# Escribir el texto debajo del título
texto.write(mensaje, align="center", font=("Courier", 16, "normal"))

# Cerrar la ventana al hacer clic en ella
window.exitonclick()