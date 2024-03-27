print ("Semana No. 10. Ejercicio 1")
mesEntrada = int(input("Ingrese un número del 1 al 12 "))

match mesEntrada:
    case 1:
        mesSalida="Enero"
    case 2:
        mesSalida="Febrero"
    case 3:
        mesSalida="Marzo"
    case 4:
        mesSalida="Abril"
    case 5:
        mesSalida="Mayo"
    case 6:
        mesSalida="Junio"
    case 7:
        mesSalida="Julio"
    case 8:
        mesSalida="Agosto"
    case 9:
        mesSalida="Septiembre"
    case 10:
        mesSalida="Octubre"
    case 11:
        mesSalida="Noviembre"
    case 12:
        mesSalida="Diciembre"
    case _:
        print ("Error: El número a ingresar debe estar contenido entre 1 y 12")
print (f"Mes: {mesSalida}")

#Ejercicio 2
print ("Semana No. 10. Ejercicio 2")

#entradas
a = int(input("Ingrese el primer número mayor a cero "))
b = int(input("Ingrese el segundo número mayor a cero "))
c = int(input("Ingrese el tercer número mayor a cero "))

#validación
if a <= 0 or b <= 0 or c <= 0:
    print("Error: El númro ingresado debe ser mayor a cero")

#diagrama
print ("El número mayor es: ")
if a > b:
    if a > c:
        print(a)
    elif a == c:
        print (a or c)
    else:
        print (c)
elif a==b:
    if a > c:
        print (a or b)
    elif a ==c:
        print ("Los números son iguales")
    else:
        print(c)
else:
    if c > b:
        print (c)
    elif b>c:
        print (b)
        
print ("Semana No. 10. Ejercicio 3")
print ("¿Cuál es tu signo zodiacal?")
dia=int(input("Ingrese su día de nacimiento "))
mes=int(input("Ingrese su mes de nacimiento "))
if dia>31 or mes>12:
    print ("Esa fecha no existe")
elif dia >= 21 and mes ==3 or dia<=19 and mes ==4:
    print ("Tu signo zodiacal es: Aries")
elif dia >= 20 and mes ==4 or dia <=20 and mes==5:
    print ("Tu signo zodiacal es: Tauro")
elif dia >= 21 and mes==5 or dia <=20 and mes==6:
    print ("Tu signo zodiacal es: Géminis")
elif dia >=21 and mes ==6 or dia <=22 and mes==7:
    print ("Tu signo zodiacal es: Cáncer")
elif dia >=23 and mes==7 or dia <=22 and mes==8:
    print ("Tu signo zodiacal es: Leo")
elif dia >=23 and mes==8 or dia<=22 and mes==9:
    print ("Tu signo zodiacal es: Virgo")
elif dia >=23 and mes==9 or dia <=22 and mes==10:
    print ("Tu signo zodiacal es: Libra")
elif dia>=23 and mes==10 or dia<=21 and mes==11:
    print ("Tu signo zodiacal es: Escorpio")
elif dia >= 22 and mes==11 or dia <= 21 and mes== 12:
    print ("Tu signo zodiacal es: Sagitario")
elif dia >=22 and mes==12 or dia <= 19 and mes==1:
    print ("Tu signo zodiacal es: Capricornio")
elif dia >= 20 and mes ==1 or dia <= 18 and mes==2:
    print ("Tu signo zodiacal es: Acuario")
elif dia >= 19 and mes==2 or dia<=18 and mes==3:
    print ("Tu signo zodiacal es: Piscis")