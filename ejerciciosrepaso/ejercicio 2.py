import math

def calcular_area_circulo(radio):

    area = math.pi * radio**2
    return area

# Ejemplo
radio = 5
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)
