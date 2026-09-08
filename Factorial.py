import sys
import time

sys.set_int_max_str_digits(1000000)


def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


a = 100000

inicio = time.perf_counter()

resultado = factorial(a)

fin = time.perf_counter()

print("Factorial calculado correctamente")
print("Tiempo de ejecución:", fin - inicio, "segundos")
print("Cantidad de dígitos:", len(str(resultado)))
