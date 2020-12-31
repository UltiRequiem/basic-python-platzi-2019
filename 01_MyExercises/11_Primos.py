def is_prime(number):
    if number < 2:
        return false
    elif number == 2:
        return True
    elif number < 2 and number % 2 == 0:
        return True
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
            else: 
                return True


def main():
    number = int(input('Write a numer: '))
    is_prime(number)

    result = is_prime(number) 

    if result is True:
        print('¡Your number is prime!')
    else:
        print("Your number isn't prime :(")

if __name__=='__main__':
    main()
