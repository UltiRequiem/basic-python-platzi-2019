import turtle

def main():
    window = turtle.Screen()
    eliaz = turtle.Turtle()

    make_square(eliaz)
 
    turtle.mainloop()

def make_square(eliaz):
    lenght = int(input('Biggest of the Square: '))

    for i in range(4):
        make_line_and_turn(eliaz, 100)

def make_line_and_turn(eliaz, length):
    eliaz.forward(length)
    eliaz.left(90)


if __name__=='__main__': 
    main()
