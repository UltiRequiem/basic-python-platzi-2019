def say_hello():
    age = int(input("Escribe tu edad: "))

    if age > 18:
        print("Hey Bro")

    else:
        print("Hey kiddo")


if __name__ == "__main__":
    say_hello()
