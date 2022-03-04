import turtle, random

w = turtle.Screen()
t = turtle.Turtle()
t.color("green")
numNivel = 13
largoRama = 120
angulo = 17


def cambioColor():
    colors = ["blue", "red", "orange", "purple"]
    t.pencolor(random.choice(colors))


def dibujaArbol(largoRama, Nivel):

    cambioColor()
    width = t.width()

    t.width(width * 3.0 / 4.0)

    largoRama = 3.0 / 4.0 * largoRama

    t.left(angulo)
    t.forward(largoRama)

    if Nivel < numNivel:
        dibujaArbol(largoRama, Nivel + 1)
    t.back(largoRama)
    t.right(2 * angulo)
    t.forward(largoRama)

    if Nivel < numNivel:
        dibujaArbol(largoRama, Nivel + 1)
    t.back(largoRama)
    t.left(angulo)

    t.width(width)


def main():
    t.speed("fastest")

    t.left(90)
    t.width(numNivel)  #
    t.penup()
    t.back(largoRama)

    t.pendown()
    t.forward(largoRama)

    dibujaArbol(largoRama, 2)

    turtle.done()


if __name__ == "__main__":
    main()
