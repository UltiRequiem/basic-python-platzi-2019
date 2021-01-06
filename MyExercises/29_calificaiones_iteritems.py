def calificaciones():
    notas = {'matematica': 9,'CyT':9,'lenguaje':8,'WEB':8,'Bases_de_datos':10}

    for key, value in notas.items():
        print('llave: {}, valor: {}'.format(key, value)) 

if __name__=='__main__':
    calificaciones()
