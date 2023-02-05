def rellenar_matriz(tabla,fila,columna):
    for i in range(fila):
        for j in range(columna):
            tabla[i][j]=int(input("ingrese el valor para la posicion [{},{}]: ".format(i+1,j+1)))
    return tabla

def imprimir(matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            print(matriz[i][j],end=" ")
        print()
def linealizar(matriz,fila,columna):
    vector=[0for i in range(fila*columna)]
    aux=0
    for j in range(columna):
        for i in range(fila):
            vector[aux]=matriz[i][j]
            aux=aux+1
    print(vector)
    
def main():
    fila=int(input("ingrese el numero de filas: "))
    columna=int(input("ingrese el numero de columnas: "))
    tabla=[[0 for j in range(columna)]for i in range(fila)]
    matriz=rellenar_matriz(tabla,fila,columna)
    imprimir(matriz,fila,columna)
    linealizar(matriz,fila,columna)
main()
    
