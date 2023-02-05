def primo(numero):
    x=0
    for i in range(1,9):
        if numero%i==0:
            x=x+1
        if x>2:
            break
    if x==2:
        return True
#end
k=2
for i in range(1,7):
    for j in range(1,7):
        while k<150:
            salida=primo(k)
            if salida==True:
                print(k, end=" ")
            k=k+1
    print()
    

