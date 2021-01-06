def calificaciones():
    notas = {'matematica': 9,'CyT':9,'lenguaje':8,'WEB':8,'Bases_de_datos':10}

    for key in notas.values():
        print('La nota del curso es ' + str(key))

if __name__=='__main__':
    calificaciones()
