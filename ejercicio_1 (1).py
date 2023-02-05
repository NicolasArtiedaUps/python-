def tipo_ACL(numero):
    if numero>=1 and numero<=99:
        print("El dato ingresado corresponde a una ACL de tipo Estándar")
    elif numero>=1300 and numero<=1999:
        print("El dato ingresado corresponde a una ACL de tipo Estándar en rango expandido")
    elif numero>=100 and numero<=199:
        print("El dato ingresado corresponde a una ACL de tipo Extendidas")
    elif numero>=2000 and numero<=2699:
        print("El dato ingresado corresponde a una ACL de tipo Extendida en rango expandido")
    elif numero<=0 or numero>=2700:
        print("El dato ingresado, no corresponde a una ACL")
        
#end
def main():
    numero=int(input("ingrese el # de ACL: "))
    tipo_ACL(numero)
#end

main()
