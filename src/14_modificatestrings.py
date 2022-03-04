a = "platzi"
a = list(a)  # Convierto a lista, porque una lista si se puede modificar
a[0] = "c"  # Realizo el cambio que necesito
a = "".join(a)  # Concateno para obtener nuevamente el string

print(a)
