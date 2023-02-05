def pedirCol(tabla,valor):
    b=[]
    for f in range(len(tabla)):
        b.append(tabla[f][valor])
    print("Columna ",valor,": ",b)
    
def matriz(tabla,filas,columnas):
    for f in tabla:
        print(f)
    c=int(input("ingrese la columna: "))
    while c>=3:
        print("el valor del parámetro c= ",c," es incorrecto ")
        c=int(input("ingrese la columna: "))
    pedirCol(tabla,c)
    
def main():
    tabla=[["a","b","c"],["d","e","f"],["g","h","i"]]
    fila=3
    columna=3
    matriz(tabla,fila,columna)
main()
 
