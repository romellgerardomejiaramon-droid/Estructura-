import time 
import random
import statistics


def mostrar_vector(datos):
    for elemento in datos:
        print(elemento)


def media(datos):
    suma = sum(datos)
    return suma / len(datos)


def main():
    inicio = time.time() # ← empieza a contar
    
    datos = [random.randint(150, 250) for _ in range(50)]

    mostrar_vector(datos)

    print("Media = " + str(media(datos)))
    print("Mediana = " + str(statistics.median(datos)))
    print("Moda = " + str(statistics.mode(datos)))
    print("Varianza = " + str(statistics.pvariance(datos)))
    print("Desviación estandar = " + str(statistics.pstdev(datos)))

    fin = time.time() # ← termina de contar 
    print("Tiempo de ejecución: " + str(fin - inicio) + " segundos")
        
if __name__ == "__main__":
    main()
