
print("ejercicio 1 ");
dia=24;
periodo=27.3;# dias 
#periodo en horas 
T=periodo*86400;
print("PERIODO:...",T);
# velocidad tangencial
milla=1609.34 #m
r=238000*milla;
print("radio millas a metros ",r);
vt=(2*3.14)*r/T;
print("la velocidad tangencial es ",vt);
a=((vt*vt))/r;
print("la aceleracion es ",a," m/seg");
