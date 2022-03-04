# -*- coding: utf-8 -*-


def protected(func):
    def wrapper(password):

        if password == "platzi":
            return func()
        else:
            print("La contraseÃ±a es incorrecta")

    return wrapper


@protected
def protected_func():
    print("Tu contraseÃ±a es correcta.")


if __name__ == "__main__":
    password = str(raw_input("Ingresa tu contraseÃ±a: "))

    protected_func(password)
