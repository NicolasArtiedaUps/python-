def mostrar(vec1,vec2):
    cont1=0
    cont2=0
    for i in range(0,len(vec1)):
        cont1=2*i+1
        cont2=2*(i+1)
        print(cont1,vec1[i],cont2,vec2[i],sep=" ")
        
def reserva(vec1,vec2):
    asiento=0
    while asiento<=0 or asiento>18:
        asiento=int(input("elija su asiento: "))
    cont1=0
    cont2=0
    acum=0
    for i in range(0,len(vec1)):
        acum=0
        cont1=2*i+1
        cont2=2*(i+1)
        if asiento==cont1:
            acum=i
            vec1[acum]="[X]"
            print("Asiento: ",asiento," reservado ")
        elif asiento==cont2:
            acum=i
            vec2[acum]="[X]"
            print("Asiento: ",asiento," reservado ")
        elif vec1[i]=="X" or vec2=="X":
            print("asiento ya reservado ")
            asiento=int(input("elija su asiento: "))
            
        cont1=2*i+1
        cont2=2*(i+1)  
def menu():
    op=0
    asientosPares=['[O]']*9
    asientosImpares=['[O]']*9
    while op!=3:
        print("1) Mostrar asientos")
        print("2) Reservar un asiento")
        print("3) Salir")
        op=int(input("ingrese su opcion: "))
        if op==1:
            mostrar(asientosPares,asientosImpares)
        elif op==2:
            reserva(asientosPares,asientosImpares)
        elif op==3:
            print("** fin del programa **")
       
def main():
    menu()
main()
