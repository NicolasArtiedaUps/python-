def potencia(numero):
    vector=[2*i+1 for i in range(0,numero)]
    acum=0
    for i in range(0,numero):
        acum=acum+vector[i]
    return acum
        
#end
def main():
    numero=int(input("ingrese el numero: "))
    inicio=1
    while numero<1:
        numero=int(input("ingrese el numero: "))
    else:
        while inicio>=1 and inicio<100:
            print(inicio,"^2 = ",potencia(inicio))
            inicio=inicio+1     
#end
main()
