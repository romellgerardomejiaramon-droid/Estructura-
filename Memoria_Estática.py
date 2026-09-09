
def main():
    
    TAMANO_FIJO = 5
    calificaciones = [None] * TAMANO_FIJO
    
    print("--- PROGRAMA: MEMORIA ESTÁTICA ---")
    print(f"Espacios reservados en memoria: {len(calificaciones)}\n")
    
    for i in range(TAMANO_FIJO):
        entrada = input(f"Ingrese la calificación [{i}]: ")
        calificaciones[i] = int(entrada)
        
    print("\nCalificaciones almacenadas en la memoria estática:")
    print(calificaciones)

if __name__ == "__main__":
    main()
