#Llamadas telefónicas

def main():
    telefono=[]
    l_cadena=1
    cambio_base=100000000
    numero_telef=int(input("ingrese el numero de telefono sin colocar el cero al inicio "))
    #numero de telefono 
    x=numero_telef
    a=len(str(x))
    if a==9:
        for i in range(9):
            div=x/cambio_base
            x=x-int(div)*cambio_base
            cambio_base=cambio_base/10
            telefono.append(int(div))
        hora=int(input("Ingrese la hora [0-23]: "))
        minutos=int(input("Ingrese los minutos [0-59]: "))
        if hora>=0 and hora <=23:
            if hora==8 and (minutos>=0 and minutos<=20):
                print("CONTESTAR PODRIA SER EMERGENCIA ")
            elif (hora>=0 and hora<=7) and (minutos>=0 and minutos<=59):
                print("CONTESTAR PODRIA SER EMERGENCIA ")
            
            if (hora==8) and (minutos>=21 and minutos<=59):
                if (telefono[6]==9 and telefono[7]==0 and telefono[8]==9):
                    print("CONTESTAR")
                else:
                    print("NO CONTEESTAR")
            if (hora>8 and hora<=12) and (minutos>=0 and minutos<=59):
                if (telefono[6]==9 and telefono[7]==0 and telefono[8]==9):
                    print("CONTESTAR")
                else:
                    print("NO CONTEESTAR")
        
            if hora==19 and (minutos>=0 and minutos<=50):
                if (telefono[0]==8 and telefono[1]==7 and telefono[2]==7):
                    print("NO CONTESTAR")
                else:
                    print("CONTESTAR")

            if (hora>=13 and hora<=18) and (minutos>=0 and minutos<=59):
                if (telefono[0]==8 and telefono[1]==7 and telefono[2]==7):
                    print("NO CONTESTAR")
                else:
                    print("CONTESTAR")
                
            if hora==19 and (minutos>50 and minutos<=59):
                print("NO CONTESTAR")
                
            if hora>19 and hora<=23 and (minutos>=0 and minutos<=59):
                print("NO CONTESTAR")        
    else:
        print("la lingitud del numero de telefono debe ser de 9 digitos")
          
#end

main()
