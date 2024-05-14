import random
print("SEMANA 16. EJERCICIO #1")
lista=[]
for x in range(10):
    lista.append(random.randint(0,10))

opcion=True
while opcion:
    print("Menú")
    print("a. Mostrar los números ingresados b. promedio c. Tamaño del arreglo d. Suma de posiciones pares e impares. \n PRESIONA CUALQUIER OTRA TECLA PARA SALIR")
    opcion=input("Ingrese su opción: ")

    match opcion:
        case "a":
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")
        case "b":
            print("PROMEDIO")
            sumatoria=0
            for x in range(len(lista)):
                sumatoria+=lista[x]
            promedio=sumatoria/10
            print(f"-----Promedio: {promedio}")
        case "c":
            print(f"La longitud del arreglo es :{len(lista)}")
        case "d":
            sumatoriapar=0
            sumaimpar=0
            print("Suma de posiciones pares e impares")
            for x in range(len(lista)):
                if x%2==0:
                    sumatoriapar+=lista[x]
                if x%2!=0:
                    sumaimpar+=lista[x]
            print(f"\nLa sumatoria de los números en posiciones pares es: {sumatoriapar} y la sumatoria de las posiciones impares es: {sumaimpar}")
        case _:
            opcion=False


#EJERCICIO 2
cantfilas=int(input("Ingrese el número de filas"))
cantcolm=int(input("Ingrese el número de columnas"))
matriz=[[0 for x in range(cantcolm)] for y in range(0,cantfilas)]
mayor=0
menor=1000
for xFilas in range(cantfilas):
    for xCol in range(cantcolm):
        matriz[xFilas][xCol]=random.randint(0,1000)
        if matriz [xFilas][xCol]<menor:
            menor=matriz[xFilas][xCol]
    #comparar mayor
    if matriz[xFilas][xCol]>mayor:
        mayor=matriz[xFilas][xCol]
    #comparar menor
    
print(matriz)
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")