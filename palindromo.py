def invertir(numero):
    respuesta=0
    rem=0

    while numero>0:
        rem=int(numero%10)
        respuesta=respuesta*10+rem
        numero=int(numero/10)
    return respuesta

def comparacion(numero,salida):
    if numero==salida:
        return True
    else:
        return False
def main():
    numero=int(input("ingrese el numero "))
    salida=invertir(numero)
    booleano=comparacion(numero,salida)
    if booleano==True:
        print(numero,"palindromo")
    else:
        print(numero,"no palindromo")
main()
