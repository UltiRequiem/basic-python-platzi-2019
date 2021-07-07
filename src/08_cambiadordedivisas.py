def foreign_exchange_calculator(ammount):
    soles = 0.28

    return soles * ammount

def main():
    print('CALCULADORA DE DIVISAS')
    print('Convierte tus dolares a soles.')
    print(' ')

    ammount = float(input('Ingresa la cantidad de dolares a soles que quieras convertir: '))

    result = foreign_exchange_calculator(ammount)

    result = round(result) 

    print('Tus ${} son {} soles'.format(ammount, result))
    print(' ')

if __name__=='__main__':
    main()
