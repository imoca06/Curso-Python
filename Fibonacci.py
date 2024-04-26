# Programa serie de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' , ')
        a, b = b, a+b
    print()
fibonacci(1000)
# devuelve: 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987
