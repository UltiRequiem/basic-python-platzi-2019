# -*- coding: utf-8 -*-

import random

palabras_posibles = [
    "leon",
    "tigre",
    "murcielago",
    "peyorativo",
    "misantropia",
    "hipotalamo",
    "ventriculo",
    "esclerosis",
    "necrosis",
    "isquemia",
    "filantropia",
    "epilepsia",
    "llamar",
    "mudo",
    "crema",
    "piedad",
    "recolector",
    "cometa",
    "elefante",
    "zero",
]
palabra_seleccionada = palabras_posibles[random.randint(0, len(palabras_posibles) - 1)]

IMAGES = [
    """   

    +---+
    |   |
        |
        |
        |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
        |
        |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========""",
    """   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========""",
    """   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========""",
]

FIN_DIBUJO = ["""--- * --- * --- * --- * --- * --- * --- * --- * --- * ---"""]

x = 0  # x = Cantidad de Fracasos
y = len(palabra_seleccionada)

string = "-"
largo = string * y
palabra_sustituta = list(largo)


def dibujo_inicial(x):
    print(IMAGES[x])
    print("")
    print(palabra_sustituta)
    print("")
    print(FIN_DIBUJO[0])
    print("")


def intento(x):
    letra_seleccionada = str(input("Escoge una letra: "))
    a = y

    for i in range(y):
        if letra_seleccionada == palabra_seleccionada[i]:
            palabra_sustituta[i] = letra_seleccionada
        else:
            a -= 1
    if a == 0:
        x += 1
        dibujo_inicial(x)
        if x >= (len(IMAGES) - 1):
            print("Vuelve a intentarlo B(")
            print(" ")
        else:
            intento(x)
    else:
        if palabra_sustituta == list(palabra_seleccionada):
            dibujo_inicial(x)
            print("Ganaste B)")
            pass
        else:
            dibujo_inicial(x)
            intento(x)
        pass


if __name__ == "__main__":
    dibujo_inicial(0)

    intento(x)
