#costo de pasaje
def main():
    nombre=input("ingrese el nombre del pasajero: ")
    valor=float(input("ingrese el valor del pasaje: "))
    edad=int(input("ingrese la edad: "))
    nacionalidad=(input("ingrese la nacionalidad: "))

    pasaje(nombre,valor,edad,nacionalidad)
#end
def pasaje(nombre,valor,edad,nacionalidad):
    descuento=0
    total=0
    if (edad>=0 and edad<=12) or edad>65:
        if nacionalidad=="ECUATORIANA " or nacionalidad=="ecuatoriana":
            descuento=valor*0.40
    else:
        descuento=0
    total=valor-descuento
    print("el descuento aplicado es de: ",descuento)
    print("El total a pagar de ",nombre," es de: ",total)

#end

main()
