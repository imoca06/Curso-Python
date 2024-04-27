# Programa serie de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' , ')
        a, b = b, a+b
    print()
fibonacci(1000)
# devuelve: 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987
fibonacci(10000)
# devuelve: 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584  4181  6765

# Programa para ver los numeros primos
def primos(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' , ')
    print()
primos(100)
# devuelve: 2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97

