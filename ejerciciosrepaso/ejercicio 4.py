def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingrese un número: "))
resultado = es_par_o_impar(numero)
print("El número", numero, "es", resultado)
