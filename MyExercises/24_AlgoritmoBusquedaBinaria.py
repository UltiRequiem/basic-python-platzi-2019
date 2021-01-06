def binary_search(number_to_find, numbers, low, high):
    
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(number_to_find, numbers, low, mid -1)
    
    else:
        return binary_search(numbers,number_to_find, mid +1, high)


if __name__=='__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,25,26,87,98,105,546]
    
    number_to_find = int(input('Ingresa tu numero: '))

    result = binary_search(numbers,number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El numero si esta en la lista')

    else:
        print('El numero no esta en la lista')
