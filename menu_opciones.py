import random


def impresion(vector):
    for i in range(0,len(vector)):
        print(round(vector[i],2), end=" ")
#end
def sumar(vector1,vector2,dimension):
    vector3=[0 for i in range(dimension)]
    for i in range(0,dimension):
        vector3[i]=vector1[i]+vector2[i]
    return vector3
    
#end
def restar(vector1,vector2,dimension):
    vector3=[0 for i in range(dimension)]
    for i in range(0,dimension):
        vector3[i]=vector1[i]-vector2[i]
    return vector3
    
#end
def multiplicar(vector1,vector2,dimension):
    vector3=[0 for i in range(dimension)]
    for i in range(0,dimension):
        vector3[i]=vector1[i]*vector2[i]
    return vector3
    
#end

def dividir(vector1,vector2,dimension):
    vector3=[0 for i in range(dimension)]
    for i in range(0,dimension):
        vector3[i]=vector1[i]/vector2[i]
    return vector3
    
#end
    
def menu(vector1,vector2,dimension):
    resp='s'
    op=1
    while op!=5:
        vec3=[0 for i in range(dimension)]
        
        print("\n1. suma")
        print("2. resta")
        print("3. miltiplicacion")
        print("4. division")
        print("5. salir")
        op=int(input("elija la opcion "))
        if op==1:
            vec3=sumar(vector1,vector2,dimension)
            print("la suma de ",vector1," + ",vector2," es ")
            impresion(vec3)
        elif op==2:
            vec3=restar(vector1,vector2,dimension)
            print("la resta de ",vector1," - ",vector2," es ")
            impresion(vec3)
        elif op==3:
            vec3=multiplicar(vector1,vector2,dimension)
            print("la multiplicacion de ",vector1," * ",vector2," es ")
            impresion(vec3)
        elif op==4:
            vec3=dividir(vector1,vector2,dimension)
            print("la division de ",vector1," / ",vector2," es ")
            impresion(vec3)
        else:
            print("!!!!!GRACIAS!!!!")   
#end
def main():
    dimension=int(input("ingrese la dimension del vector "))
    while dimension<5 or dimension>30:
        dimension=int(input("ingrese la dimension del vector "))
    else:
        vector1=[0 for i in range(dimension)]
        vector2=[0 for i in range(dimension)]
        vector3=[0 for i in range(dimension)]
        
        
        #rellenar vector con valores aleatorios
        for i in range(0,len(vector1)):
            vector1[i]=(random.randint(1,100))
            vector2[i]=(random.randint(1,100))

        print("vector 1 ")
        impresion(vector1)
        print("\nvector 2")
        impresion(vector2)

        menu(vector1,vector2,dimension)
       
        
#end

main()

    
