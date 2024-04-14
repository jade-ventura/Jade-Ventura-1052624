print ("Semana 12. Ejercicio menú")
print ()
opcion=int(input("¿Qué quieres calcular? \n 1- Sumatoria \n 2- Factorial \n 3- Tablas de multiplicar \n 4- Número perfecto"))
match opcion:
    case 1:
        print("1). PROGRAMA PARA CALCULAR UNA SUMATORIA")
        num=int(input("Ingrese un número entero: "))
        i=0
        suma=0
        for i in range(1, num+1):
            suma=suma+i
            i=i+1
        print(f"La sumatoria de {num} es igual a {suma}")

    case 2:
        print(" 2). PROGRAMA PARA CALCULAR EL FACTORIAL DE UN NÚMERO")
        f=int(input("Ingresa un número entero: "))
        i=1
        factorial=1
        for i in range (1, f+1):
            factorial*=i
            i=i+1
        print(f"El factorial de {f} es igual a {f}!={factorial}")

    case 3:
        print("3). PROGRAMA PARA VER LAS TABLAS DE MULTIPLICAR")
        columna="\t"
        for i in range(1,11):
            columna=columna+str(i)+"\t"
        print(columna+"\n")

        for f in range(1,11):
            fila=str(f)+"\t"
            for p in range(1,11):
                fila=fila+str(f*p)+"\t"
            print(fila+"\n")

    case 4:
        print("1). PROGRAMA PARA SABER SI UN NÚMERO ES PERFECTO")
        n=int(input("Ingresa un número entero "))
        i=1
        sum=0
        for i in range (1, n):
            m=n%i
            if m==0:
                sum=sum+i
                i+=i
        if sum==n:
            print("El número es perfecto")
        else:
            print("El número no es perfecto")
    case _:
        print("Esta no es una opción del menú")