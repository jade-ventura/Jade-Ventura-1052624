print ("Semana No. 11: Ejercicio 1")

n=int(input("Ingrese un número mayor a 0 "))

#declaración de variables
a = 0
b = 1
c = 0
i = 2
resultado = ""

if (n > 0):
    resultado = str(a)

    if (n > 1):
        resultado += ", " + str(b)

    while (i<n):
        c=a+b
        resultado += "," + str(c)
        a=b
        b=c
        i=i+1

        print(resultado)
else:
    print (resultado)


print ("Semana No. 11: Ejercicio 2")

n= int(input("Ingrese un número mayor a cero "))

if n <= 0:
    print ("Error: El número debe ser mayor a cero")

#EJERCICIO A
resultadoA = 0
for x in range (1, n+1):
    resultadoA += (1/x)
print ("Inciso A", resultadoA)

#EJERCICIO B
resultadoB = 0
for x in range (1, n+1):
    resultadoB += (1/(x**2))
print ("Inciso B", resultadoB)

#EJERCICIO C
resultadoC= 0
a=int(input("Ingrese un número entero"))
n=int(input("Ingrese un número entero"))
x=int(input("Ingrese un número entero"))

for k in range (1, n+1):
    resultadoC += ((x**k)*(a**(n-k)))
print (resultadoC)