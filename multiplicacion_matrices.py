def rellenar(matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            matriz[i][j]=int(input("[{},{}]: ".format(i+1,j+1)))
            
def imprimir(matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            print(matriz[i][j],end=" ")
        print(" ")
    
def producto(matriz1,matriz2,columna2,fila1,columna1):
    matriz3=[[0 for j in range(columna2)]for i in range(fila1)]
    suma=0
    for columna3 in range(columna2):
        for i in range(fila1):
            suma=0
            for j in range(columna1):
                suma+=matriz1[i][j]*matriz2[j][columna3]
            matriz3[i][columna3]=suma
    imprimir(matriz3,fila1,columna2)
def main():
    print("MATRIZ 1 ")
    filas1=int(input("Ingrese el numero de filas: "))
    columnas1=int(input("ingrese el numero de columnas: "))
    matriz1=[[0 for j in range(columnas1)] for i in range(filas1)]
    rellenar(matriz1,filas1,columnas1)
    print("MATRIZ 2 ")
    filas2=int(input("Ingrese el numero de filas: "))
    columnas2=int(input("ingrese el numero de columnas: "))
    matriz2=[[0 for j in range(columnas2)] for i in range(filas2)]
    while columnas1!=filas2:
        print("la primera matriz debe tener el mismo número de columnas que filas la segunda matriz ")
        print("MATRIZ 1 ")
        filas1=int(input("Ingrese el numero de filas: "))
        columnas1=int(input("ingrese el numero de columnas: "))
        matriz1=[[0 for j in range(columnas1)] for i in range(filas1)]
        rellenar(matriz1,filas1,columnas1)
        print("MATRIZ 2 ")
        filas2=int(input("Ingrese el numero de filas: "))
        columnas2=int(input("ingrese el numero de columnas: "))
        matriz2=[[0 for j in range(columnas2)] for i in range(filas2)]
        
    
    rellenar(matriz2,filas2,columnas2)
    print("MATRIZ 1: ")
    imprimir(matriz1,filas1,columnas1)
    print("MATRIZ 2: ")
    imprimir(matriz2,filas2,columnas2)
    print("MATRIZ 3: ")
    producto(matriz1,matriz2,columnas2,filas1,columnas1)
    
    
main()
