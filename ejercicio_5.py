#indice de masa corporal

def main():
    nombre=input("ingrese el nombre: ")
    masa=float(input("ingrese la masa corporal (kg): "))
    estatura=float(input("ingrese la estatura (m): "))
    imc=masa/((estatura)*(estatura))

    print(nombre," tiene un IMC de: ",round(imc,2)," kg/m^2 ")
    print("Observacion sobre peso: ",peso(imc))
    
#end
def peso(imc):
    if imc<18.5:
        npeso="Bajo peso"
    elif imc>=18.5 and imc<=24.9:
        npeso="Normal"
    elif imc>=25 and imc<=29.9:
        npeso="Sobrepeso"
    elif imc>=30:
        npeso="Obeso"
    return npeso
#end
main()
