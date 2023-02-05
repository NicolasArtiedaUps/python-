def fpotencia(potencia,base):
    if potencia==0:
        return 1
    elif potencia==1:
        return base
    else:
        return base*fpotencia(potencia-1,base)
#end
def main():
    base=-1
    potencia=-1
    potencia=int(input("ingrese la potencia: "))
    base=int(input("ingrese la base: "))
    if base<0 or potencia<0:
        print("base: ",base)
        print("exponente: ",potencia)
        print("ERROR!!!")
    else:
        print("base: ",base)
        print("exponente: ",potencia)
        print("resultado es: ",fpotencia(potencia,base))
    
#end
main()
