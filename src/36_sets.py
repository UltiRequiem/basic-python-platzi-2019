s = set([1,2,3])
t = set([3,4,5])

union = str(s.union(t))
print('La union de los dos sets es ' + union)

interseccion = str(s.intersection(t))
print('La interseccion de los dos sets es ' + interseccion)

diferencia_uno= str(s.difference(t))
print('La diferencia de s y t es ' + diferencia_uno)
