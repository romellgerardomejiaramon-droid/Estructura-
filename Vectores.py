import time 

def mostrar_vector(datos):
    for elemento in datos:
        print(elemento)

def media(datos):
    suma = sum(datos)
    return suma / len(datos)

def main():
    
    inicio = time.time() # ← empieza a contar
    pares = [2, 4, 6, 8, 10]
    impares = [1, 3, 5, 7, 9]

    mostrar_vector(pares)
    print("Media = " + str(media(pares)))

    mostrar_vector(impares)
    print("Media = " + str(media(impares)))
    
    fin = time.time() # ← termina de contar 
    print("Tiempo de ejecución: " + str(fin - inicio) + " segundos")
    
if __name__ == "__main__":
    main()  
