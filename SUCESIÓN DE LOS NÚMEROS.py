import math
def fsucesion(n):
    suma=0
    for i in range(1,n+1):
        suma=suma+math.pow(2,i)
    return suma
#end
def main():
    n=int(input("ingrese el numero "))
    print(fsucesion(n))
#end
main()
