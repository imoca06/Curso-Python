# comprobar si un numero es capicua

numero = 13431545
def es_capicua(numero):
    numero = str(numero)
    return numero == numero[::-1]
print(es_capicua(numero))
