def main():
    numero=int(input("ingrese el numero "))
    ran=numero
    beta=1
    for i in range(0,numero):
        for j in range(i,ran):
            print(ran-i,end=" ")
        print()
    for a in range(1,numero):
        for b in range(0,a+1):
            print(a+1,end=" ")
        print()
#end
main()
