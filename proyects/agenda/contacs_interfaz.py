class Contact:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        print("name: {}, phone: {}, email: {}".format(name, phone, email))


def run():

    contact_book = ContactBook()

    while True:
        command = str(
            input(
                """
            ¿Qué deseas hacer?

            [A]ñadir contacto
            [AC]tualizar contacto
            [B]uscar contacto
            [E]liminar contacto
            [L]istar contactos
            [S]alir
        """
            )
        )

        if command == "a" or "A":
            name = str(input("Escribe el nombre del contacto: "))
            phone = str(input("Escribe el tel del contacto: "))
            email = str(input("Escribe el email del contacto: "))

            contact_book.add(name, phone, email)

        elif command == "ac" or "AC":
            print("actualizar contacto")

        elif command == "b" or "B":
            print("buscar contacto")

        elif command == "e" or "E":
            print("eliminar contacto")

        elif command == "l" or "L":
            print("listar contactos")

        elif command == "s" or "S":
            break
        else:
            print("Comando no encontrado.")


if __name__ == "__main__":
    print("B I E N V E N I D O  A  L A  A G E N D A")
    run()
