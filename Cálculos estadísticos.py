import math
def media(vec):
    suma=0
    tmedia=0
    for elemento in vec:
        suma=suma+elemento
    tmedia=suma/len(vec)
    return tmedia
def varianza(tmedia,vec):
    tvarianza=0
    for elemento in vec:
        tvarianza=tvarianza+math.pow(elemento-tmedia,2)
    total_varianza=tvarianza/len(vec)
    return total_varianza
    
def desviacion(media,vec):
    suma=0
    for elemento in vec:
        suma=suma+math.pow(elemento-media,2)
    total=math.sqrt(suma/len(vec))
    return total
def main():
    tam=int(input("Ingrese el valor de n: "))
    vector=[0]*tam
    print("ingrese la lista de numeros ")
    for i in range(0,len(vector)):
        vector[i]=float(input("elemento [{}]:  ".format(i+1)))
    tmedia=media(vector)
    tvarianza=varianza(tmedia,vector)
    tdesviacion=desviacion(tmedia,vector)
    print("Media= ",tmedia)
    print("Varianza= ",round(tvarianza,2))
    print("Desviacion estandar: ",round(tdesviacion,2))
main()
