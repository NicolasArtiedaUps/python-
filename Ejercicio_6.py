#venta de rollos

def main():
    longitud=int(input("ingrese la longitud del alambre: "))
    #numero de rollos 500
    rollo_500=int(longitud/500)
    #el resto de la division
    aux=longitud%500
    #numero de rollos 300
    rollo_300=int(aux/300)
    #el resto de la division
    aux2=aux%500
    #numero de rollos 75
    rollo_75=int(aux2/75)
    #el resto de la division
    aux3=aux2%75

    print(rollo_500," rollos de 500 metros ",rollo_300," rollos de 300 metros ",rollo_75," rollos de 75 metros y ",aux3," metros")
    
#end
    
main()
