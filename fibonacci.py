def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

# Imprimir la serie de Fibonacci hasta el número 21
fibonacci(21)
