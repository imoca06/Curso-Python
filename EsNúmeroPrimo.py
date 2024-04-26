# comprobar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = 7
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
# devuelve: 7 es primo

numero = 2568
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
# devuelve: 2568 no es p
numero = 2978
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
# devuelve: 2978 no es primo





