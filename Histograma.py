import random
def histograma(maximo,minimo,vec):
    cont=0
    for i in range(minimo,maximo+1):
        cont=0
        for j in range(0,len(vec)):
            if i==vec[j]:
                cont=cont+1
        print("[{}]: ".format(i),end="")
        for k in range(0,cont):
            print(" * ",end="")
        print("")                  
def main():
    minimo=-1
    maximo=-1
    tam=-1
    while (minimo<0 or maximo<0) or (maximo<minimo):
        
        minimo=int(input("ingrese el minimo: "))
        maximo=int(input("ingrese el maximo: "))
        
    while tam<0:
        tam=int(input("ingrese el tamaño de la lista: "))

    vector=[0]*tam
    for i in range(0,tam):
        vector[i]=random.randint(minimo,maximo)
        
    print("Vector: ",vector)
    histograma(maximo,minimo,vector)
#end
main()
