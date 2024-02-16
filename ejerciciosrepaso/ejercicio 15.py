def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()

    return cadena == cadena[::-1]

texto = input("Ingrese una cadena de texto: ")

if palindromo(texto):
    print("el texto es un palíndromo.")

else:
    print("el texto no es un palíndromo.")
