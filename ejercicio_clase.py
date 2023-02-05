import random
import time
def ordenamiento1(vec):
    for i in range(0,len(vec)):
        for j in range(i+1,len(vec)):
            if vec[i]>vec[j]:
                aux=vec[i]
                vec[i]=vec[j]
                vec[j]=aux
    return vec        
def ordenamiento2(vec):
    for i in range(0,len(vec)):
        for j in range(i+1,len(vec)):
            if vec[i]<vec[j]:
                aux=vec[i]
                vec[i]=vec[j]
                vec[j]=aux
    return vec
def imprimir(vec):
    for i in range(0,len(vec)):
        time.sleep(1)
        print("el valor en la posicion {} es ".format(i+1),vec[i])
#end
tam=int(input("ingrese el tamaño del vector "))
vec=[0 for i in range(0,tam)]
#rellenamos 
for i in range(0,tam):
    vec[i]=random.randint(50,100)
imprimir(vec)
op=0
while op!=3:
    print("\n1. ordenar A-Z")
    print("2. ordenar z-A")
    print("3. salir")
    op=int(input("elija la opcion "))
    if(op==1):
        
        vector1=ordenamiento1(vec)
        imprimir(vector1)
        
    elif(op==2):
     
        vector2=ordenamiento2(vec)
        imprimir(vector2)

    

    

