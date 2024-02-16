def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = [5, 10, 15, 20]
resultado = suma_lista(numeros)
print("La suma de los números en la lista es:", resultado)
