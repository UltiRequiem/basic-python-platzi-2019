def protected(func):
    
    def wrapper(password):

        if password == '123456789':
            return func()
        else:
            print("That's not the correct password.")

    return wrapper

def protected_fun():
    print('Your Password is correct.')

if __name__ == '__main__':
    password = str(input('Write your password: '))

    wrapper = protected(protected_fun)
    wrapper(password)

