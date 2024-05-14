#LABORATORIO SEMANA 15
import math
print("EJERCICIO #1. ÁREAS DE FIGURAS")
def triangulo():
    base=int(input("Ingrese en tamaño de la base "))
    altura=int(input("Ingrese el tamaño de la altura "))
    A1=base*altura/2
    print("\nEl área de el triángulo es: ", A1,"\n")
def cuadrado():
    lado=int(input("Ingrese el tamaño del lado del cuadrado "))
    A2=lado**2
    print("\nEl área del cuadrado es: ", A2,"\n")
def rectangulo():
    base=int(input("Ingrese la medida de la base "))
    altura=int(input("ingrese la medida de la altura "))
    A3=base*altura
    print("\nEl área del rectángulo es: ", A3,"\n")
def circulo():
    radio=int(input("Ingrese el radio del círculo "))
    A4=math.pi*(radio**2)
    print("\nEl área del cículo es ",A4,"\n")


n=True
while n:
    n=int(input("Elige una de las siguientes opciones: \n1. Calcular el área de un triángulo\n2. Calcular el área de un cuadrado\n3. área de un rectángulo\n4. Área de un círculo\n5. Presiona '0' para salir del menú "))
    match n:
        case 1:
            triangulo()
        case 2:
            cuadrado()
        case 3:
            rectangulo()
        case 4:
            circulo()
        case 0:
            n=False
        case _:
            print("ERROR. ELIGE UNA OPCIÓN VÁLIDA")

print("\nEJERCICIO #2. COORDENADAS DE UN OBJETO\n")

c=True
y=0
x=0
while c:
    menu=int(input("¿Hacia dónde va tu personaje?:\n1. Subir\n2. Bajar\n3. Izquierda\n4. Derecha\n0. Salir del programa\n"))
    match menu:
        case 1:
            y+=1
        case 2:
            y-=1
        case 3:
            x-=1
        case 4:
            x+=1
        case 0:
            print("Las coordenadas finales de tu personaje son: (",x,",",y,")")
            c=False
        case _:
            print("ELIGE UNA OPCIÓN VÁLIDA")