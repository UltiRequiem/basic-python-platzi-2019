def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += temp

    return sum_of_temps / len(temps)
    
if __name__=='__main__':
    temps = [34,33,35,36,37,38,39,33,35]

    average_temps(temps)

    average = average_temps(temps)

    average = round(average)

    print('La temperatura promedio es: {}'.format(average))
