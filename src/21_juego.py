import random


def main():
    frase_juego = frases_para_jugar()
    print("LA FRASE CON LA QUE JUGAMOS ES:")
    frase_tapada = tapando_frase(frase_juego)
    print(frase_tapada)
    contador = 0
    choose_char(frase_juego, frase_tapada, contador)


def frases_para_jugar():
    lista_frases = [
        "La vida es bella",
        "El princio del fin",
        "Por fin pude terminar el programa",
    ]
    num_frase = int(input("Escoge un número del 1 al {}: ".format(len(lista_frases))))
    frase_elegida = lista_frases[num_frase - 1]
    return frase_elegida


def choose_char(frase_juego, frase_tapada, contador):
    cond = False
    frase_juego_lista = list(frase_juego)
    frase_tapada_lista = list(frase_tapada)
    while not cond:
        cont = 0
        letra_elegida = input("Elige una letra: ")
        for char in frase_juego_lista:
            if char.upper() == letra_elegida.upper():
                frase_tapada_lista[frase_juego_lista.index(char)] = char
                frase_juego_lista[frase_juego_lista.index(char)] = "*"
                cont += 1

        if cont == 0:
            contador += 1
            print("Intendo {} fallido ".format(contador))
            print("")
        else:
            print("La letra ({}) es correcta".format(letra_elegida))
            frase_actualizada = "".join(frase_tapada_lista)
            print(frase_actualizada)
            print("")
        if frase_juego.upper() == frase_actualizada.upper():
            print("FELICIDADES... ¡¡¡FRASE COMPLETADA!!!")
            input("")
            cond = True


def tapando_frase(frase):
    frase_list = list(frase)
    lenght = len(frase)
    trescuatros = int(3 * lenght / 4)
    quinto = int(lenght / 5)
    cantidad_tapados = random.randint(quinto, trescuatros)
    for i in range(cantidad_tapados):
        index_tapados = random.randint(0, lenght - 1)
        if (
            frase_list[index_tapados] != " "
            and frase_list[index_tapados] != ","
            and frase_list[index_tapados] != "."
            and frase_list[index_tapados] != "*"
        ):
            letra = frase_list[index_tapados]
            for char in frase_list:
                if char.upper() == letra.upper():
                    frase_list[frase_list.index(char)] = "*"

    frase_tapada = "".join(frase_list)
    return frase_tapada


if __name__ == "__main__":
    main()
