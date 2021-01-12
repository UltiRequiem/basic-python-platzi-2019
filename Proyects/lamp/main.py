from lamp import Lamp

def run():
    lamp = Lamp(_is_turned_on = False)

    while True:
        command = str.lower(input('''
        
        ¿What you want to Do?
        
        [P]render
        [A]pagar
        [S]alir
        
        
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == "__main__":
    run()