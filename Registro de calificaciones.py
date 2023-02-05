def rellenar_vector(vec1,vec2):
    for i in range(0,len(vec1)):
        vec1[i]=input("ingrese el nombre: ")
        while vec2[i]<0 or vec2[i]>100:
            vec2[i]=int(input("ingrese la calificacion: "))
def promedio(vec):
    suma=0
    for elementos in vec:
        suma=suma+elementos
    p=suma/len(vec)
    return p
def impresion(vec1,vec2,prom,vec3):
    print("CUADRO DE CALIFICACIONES ")
    print("No.",end="|||||")
    print("Nombre",end="|||||||||")
    print("Nota",end="|||||||")
    print("observacion",end="")
    print("")
    for i in range(0,len(vec1)):
        print("{}".format(i+1),end="|||||")
        print(vec1[i],end="|||||||||")
        print(vec2[i],end="|||||||||")
        print(vec3[i],end=" ")
        print("") 
    print("Promedio: ",round(prom,2))

def observacion(vec,prom):
    ob=[""]*len(vec)
    for i in range(0,len(vec)):
        if vec[i]>prom:
            ob[i]=" * "
    return ob
def main():
    estudiantes=int(input("Numero de estudiantes: "))
    nombre=["O"]*estudiantes
    calificacion=[-1]*estudiantes
    rellenar_vector(nombre,calificacion)
    tprom=promedio(calificacion)
    asterisco=observacion(calificacion,tprom)
    impresion(nombre,calificacion,tprom,asterisco)
main()
    

    
