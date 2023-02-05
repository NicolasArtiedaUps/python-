import math
def fgeneral(a,b,c):
    raiz=(b*b)-4*a*c
    x1=0
    x2=0
    if a==0:
        print("División para cero")
    elif raiz<0:
        print("Raíz negativa")
    elif raiz==0:
        print("unica solucion ")
        x1=(-b+math.pow(raiz,0.5))/(2*a)
        print("X1= ",x1)
    elif raiz>0:
        print("dos soluciones ")
        x1=(-b+math.pow(raiz,0.5))/(2*a)
        x2=(-b-math.pow(raiz,0.5))/(2*a)
        print("X1= ",x1)
        print("X2= ",x2)
        
#end
def main():
    a=float(input("ingrese el valor de a: "))
    b=float(input("ingrese el valor de b: "))
    c=float(input("ingrese el valor de c: "))
    fgeneral(a,b,c)
#end
main()
