# lista=int(input("Ingrese los numeros que desea promediar separados por una coma")).
def promedio(lista):
    suma = 0
    if len(lista) == 0:
        return 0
    for i in lista:
        suma += i
    return suma / len(lista)


def promedio2(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def contar_vocales(texto):
    vocales = "AEIOUaeiou"
    suma = 0
    for i in texto:
        if i in vocales:
            suma += i
    return suma


def contar_vocales2(texto):
    return sum(1 for i in texto if i in "AEIOUaeiou")


def derivada_numerica(f, x):
    return (f(x + 0.00001) - f(x)) / 0.00001


def mi_funcion(x):
    return x**2


print(derivada_numerica(mi_funcion, 3))
