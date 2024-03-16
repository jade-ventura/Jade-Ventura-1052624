print ("Ejercicio 1: Operaciones aritméticas")

#ingreso de variables
n1=int(input("Ingrese el primer número "));
n2=int(input("Ingrese el segundo número "));

#operaciones
divReal = n1/n2
divEentera = n1//n2
divMod = n1%n2
sum = n1+n2
resta = n1-n2
mul = n1*n2

#mostrar en pantalla
print (n1, "/", n2, "=", divReal)
print (n1, "//", n2, "=", divEentera)
print (n1, "%", n2, "=", divMod)
print (n1, "+", n2, "=", sum)
print (n1, "-", n2, "=", resta)
print (n1, "*", n2, "=", mul)


print("Ejercicio 2: Operaciones booleanas")

#operaciones
igualdad= n1==n2
diferentes= n1!=n2
mayorque= n1>n2
menorque= n1<n2

#mostrar en pantalla
print (n1, "==", n2, "=", igualdad)
print (n1, "!=", n2, "=", diferentes)
print (n1, ">", n2, "=", mayorque)
print (n1, "<", n2, "=", menorque)


print("Ejercicio 3: Jerarquía de operaciones")

#ingreso de datos
a=int(input("Ingrese el primer número "));
b=int(input("Ingrese el segundo número "));
c=int(input("Ingrese el tercer número "));

#operaciones
print("i. ", a*b+c)
print("ii. ", a*(b+c))
print("iii. ", a/(b+c))
print("iv. ", (3*a +2*b)/(c**2))

print("Actividad 3, Ejercicio 1")

metros1= int(input("Ingrese metros "))
km= metros1/1000
print (km, "km")

print("Actividad 3, ejercicio 2")

metros2= int(input("Ingrese metros "))
yd=metros2//0.9144
modyarda = metros2%0.9144
pies = modyarda//0.33333
modpies = pies%0.0833
pulgadas = modpies//12
print(yd, "yardas", pies, "pies", pulgadas, "pulgadas")