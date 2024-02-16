import random
def encontrar (lista):
    num_min = float('inf')
    num_max = float('-inf')

    for numero in lista:
        if numero < num_min:
            num_min = numero
        if numero > num_max :
            num_max = numero
    return num_max,num_min

if __name__ == "__main__" :

    lista_dada= [random.randint (0,100)for _ in range (10)]
    num_max,num_min = encontrar(lista_dada)
    print("el valor minimo es: ", num_min)
    print("el valor maximo es: ", num_max)
    print(lista_dada)




