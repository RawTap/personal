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


def encontrar_maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


assert encontrar_maximo([3, 9, 1, 7, 5, 12, 4, 4]) == 12
assert encontrar_maximo([-5, 8, -2, 10, 16, 7, 100, 5]) == 100
assert encontrar_maximo([-5, -2, -9]) == -2


def es_palindromo(texto):
    texto = texto.lower()
    return texto == texto[::-1]


def es_palindromo2(texto):
    texto = texto.lower()
    palindromo = ""
    for i in texto:
        palindromo = i + palindromo
    return texto == palindromo


assert es_palindromo2("Hola") == False
assert es_palindromo("Oso") == True
