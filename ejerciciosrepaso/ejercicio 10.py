def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Ejemplo:
numero = 5
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
