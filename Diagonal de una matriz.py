import random
def rellenar_matriz(matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            matriz[i][j]=random.randint(100,199)
    return matriz

def impresion(tabla,fila,columna):
    for i in range(fila):
        for j in range(columna):
            print(tabla[i][j],end=" ")
        print()
    
def diagonal(matriz,fila,columna):
    vector=[0 for i in range(fila)]
    acum=0
    for i in range(fila):
        for j in range(columna):
            if i==j:
                vector[acum]=matriz[i][j]
                acum=acum+1
    return vector
def main():
    fila=columna=3
    matriz=[[0 for j in range(columna)] for i in range(fila)]
    tabla=rellenar_matriz(matriz,fila,columna)
    impresion(tabla,fila,columna)
    print("Diagonal principal: ")
    print(diagonal(tabla,fila,columna))
main()
