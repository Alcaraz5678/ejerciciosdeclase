def conversor (num):
    conversion = 0
    conversion = (num - 32) * 5/9

    return conversion

if __name__ == "__main__" :
    num = int(input("Ingrese el número en grados a convertir: "))
    resultado = conversor(num)
    print(resultado)
