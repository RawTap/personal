def promedio(lista):
    suma = 0
    if len(lista) == 0:
        return 0
    for i in lista:
        suma += i
    return suma / len(lista)


# assert promedio([2, 4, 6]) == 4
# assert promedio([]) == 0
# assert promedio([10]) == 5


def contar_vocales(texto):
    vocales = "AEIOUaeiou"
    suma = 0
    for i in texto:
        if i in vocales:
            suma += 1
    return suma


# assert contar_vocales("Hola") == 2
# assert contar_vocales("Claude") == 3
