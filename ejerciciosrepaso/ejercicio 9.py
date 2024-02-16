import random

def generar_matriz(filas, columnas):
    matriz = [[random.randint(1,10) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


filas = int(input("ingrese el número de filas de la matriz: "))
columnas = int(input("ingrese el número de columnas de la matriz: "))


matriz = generar_matriz(filas, columnas)
imprimir_matriz(matriz)
