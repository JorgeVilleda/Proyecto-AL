import numpy as np

def obtener_matriz(rows, cols):
    print(f"Ingrese filas {rows} e inserte columnas {cols} para la matriz: ")
    matriz = []
    for mat in range(rows):
        fila = list(map(float, input().split()))
        matriz.append(fila)
    return(np.array(matriz))

def menu_operaciones():
    print("Seleccione el tamaño de matriz:")
    print("1. Matriz 2x2")
    print("2. Matriz 2x3")
    print("3. Matriz 3x2")
    print("4. Matriz 3x3")
    opcion = int(input("Ingrese su eleccion: "))
    if opcion == 1:
        print("Ha seleccionado la opcion 2x2:")
        matriz_a = obtener_matriz(2, 2)
        matriz_b = obtener_matriz(2, 2)
    elif opcion == 2:
        print("Ha seleccionado la opcion 2x3:")
        matriz_a = obtener_matriz(2, 3)
        matriz_b = obtener_matriz(2, 3)
    elif opcion == 3:
        print("Ha seleccionado la opcion 3x2:")
        matriz_a = obtener_matriz(3, 2)
        matriz_b = obtener_matriz(3, 2)
    elif opcion == 4:
        print("Ha seleccionado la opcion 3x3:")
        matriz_a = obtener_matriz(3, 3)
        matriz_b = obtener_matriz(3, 3)
    else:
        print("Opcion invalida")
        return

    print("Listado de operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Determinante")  
    print("4. Transponer")
    print("5. Matriz Inversa")
    print("6. Sistema de ecuaciones")
    operacion = int(input("Que operacion desea realizar: "))
    
    if operacion == 1:
        print("Suma de las matrices")
        print(matriz_a + matriz_b)
    elif operacion == 2:
        print("Resta de las matrices")
        print(matriz_a - matriz_b)
    elif operacion == 3:
        print("Determinante de la matriz A")
        print(np.linalg.det(matriz_a))
    elif operacion == 4:
        print("Matriz A transpuesta")
        print(np.transpose(matriz_a))
    elif operacion == 5:
        print("Matriz A inversa")
        print(np.linalg.inv(matriz_a))
    elif operacion == 6:
        print("Resolviendo sistema de ecuaciones Ax= B")
        matriz_b = obtener_matriz(matriz_a.shape[0], 1)
        try:
            print("Solucion")
            print(np.linalg.solve(matriz_a, matriz_b))
        except np.linalg.LinAlgError:
            print("Matriz A no es invertible por lo cual no puede ser resulta")
    else:
        print("Opcion invalida")
        
menu_operaciones()