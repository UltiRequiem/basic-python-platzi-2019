def calificaciones():
    notas = {'matematica': 9,'CyT':9,'lenguaje':8,'WEB':8,'Bases_de_datos':10}

    suma_de_calificaciones = 0

    for notas in notas.values():
        suma_de_calificaciones += notas
    
    print(suma_de_calificaciones)


if __name__=='__main__':
    calificaciones()
