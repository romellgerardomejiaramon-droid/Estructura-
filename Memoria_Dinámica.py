
def main():
    print("--- PROGRAMA: MEMORIA DINÁMICA ---")
    
    frutas = []
    
    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Durazno")
    
    print("Contenido inicial de la lista frutas:")
    print(frutas)
    
    print("\nEliminando el elemento en el índice 0 ('Mango')...")
    frutas.pop(0)
    
    print("Eliminando el elemento en el índice 1...")
    frutas.pop(1)
    
    print("Agregando 'Sandía' a la lista...")
    frutas.append("Sandía")
    
    print("\nContenido final de la lista tras modificar la memoria:")
    print(frutas)

if __name__ == "__main__":
    main()
