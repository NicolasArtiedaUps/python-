def piramide(altura):
    acum1=altura+2
    for i in range(2,altura+2):
        for j in range(0,acum1):
            print(" ",end="")
        acum1=acum1-1
        for k in range(0,i):
            print(" *",end="")
        print("")
def main():
    altura=0
    while altura<1 or altura>20:
        altura=int(input("ingrese la altura: "))
    piramide(altura)
#end
main()
