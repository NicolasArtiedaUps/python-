
def main():
   dinero=float(input("ingrese el dinero inicial: "))
   anios=int(input("Ingrese el tiempo(años): "))
   interes=float(input("Ingrese el interés: "))
   meses=12*anios
   for i in range(1,meses+1):
       dinero=dinero+dinero*(interes*0.01)
   print("Total de la póliza: ",round(dinero,2))     
#end
main()
