

#asinamos variables a (a) y (x) para obtener los valores de y y compararlas con la (y) original 
a=3;
x=7;
y=a*pow(x,3)+3;
y1=a*x*x*x+3;
y2=a*x*x*(x+3);
y3=(a*x)*x*(x+3);
y4=a*(x*x*x)+3;

print("original Y= ",y);
print("A....Y1= ",y1);
print("B....Y2= ",y2);
print("C....Y3= ",y3);
print("D....Y4= ",y4);

if(y==y1):
    print("respuesta A correcta");
if(y==y2):
    print("respuesta B correcta");
if(y==y3):
    print("respuesta C correcta");
if(y==y4):
    print("respuesta D correcta");


