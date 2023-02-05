#funcion de comparacion
def comparacion(vec1,vec2):
    cont=0
    for i in range(0,len(vec1)):
        for j in range(0,len(vec2)):
            if vec1[i]==vec2[j] and i==j:
                cont+=1
    return cont
def porcentaje(valor_comparacion,tam):
    valor_porcentual=(valor_comparacion*100)/tam
    return valor_porcentual

def impresion(vec1,vec2,valor):
    print("vector 1: ",vec1)
    print("vector 2: ",vec2)
    print("Similitud: ",round(valor,2)," % ")
    
def main():
    tam=int(input("Ingrese el tamaño de los vectores: "))
    vector1=[0]*tam
    vector2=[0]*tam
    print("Datos vector 1 ")
    for i in range(0,len(vector1)):
        vector1[i]=int(input("ingrese elemento [{}]: ".format(i+1)))
    print("Datos vector 2 ")
    for i in range(0,len(vector2)):
        vector2[i]=int(input("ingrese elemento [{}]: ".format(i+1)))
    
    valor_comparacion=comparacion(vector1,vector2)

    porcentajeTotal=porcentaje(valor_comparacion,tam)

    impresion(vector1,vector2,porcentajeTotal)

#end
main()
