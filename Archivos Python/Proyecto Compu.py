import turtle #inicia turtle
turtle.screensize(300,300) #indica dimensiones
def margen(): #division de recuadros para titulo, panel y narrativa
    turtle.clearscreen() #reinicia el dibujo anterior
    margen=turtle.Turtle()
    margen.hideturtle()
    margen.speed(300)
    margen.penup()
    margen.teleport(-300, 210)
    margen.pendown()
    margen.pencolor("black")
    margen.fillcolor("white") #color de recuadros 
    margen.begin_fill()
    for i in range (0,2):
        margen.forward(600)
        margen.left(90)
        margen.forward(40)
        margen.left(90)
    margen.end_fill()
    margen.fillcolor("white")
    margen.penup()
    margen.teleport(-300, 190)
    margen.pendown()
    margen.fillcolor("lightblue")
    margen.begin_fill()
    for i in range(0,2):
        margen.forward(600)
        margen.right(90)
        margen.forward(340)
        margen.right(90)
    margen.end_fill()
    margen.penup()
    margen.teleport(-300, -170)
    margen.pendown()
    margen.fillcolor("white")
    margen.begin_fill()
    for i in range(0,2):
        margen.forward(600)
        margen.right(90)
        margen.forward(100)
        margen.right(90)
    margen.end_fill()
def fondo():
    screen =turtle.Screen()
    screen.bgcolor("light pink") #color del fondo
    fondo=turtle.Turtle()
    fondo.speed(0)
    fondo.hideturtle()
    fondo.begin_fill()
    fondo.color("lightgoldenrod3")
    fondo.teleport(-300,-150)
    for _ in range(2): #arena
        fondo.pencolor("Black")
        fondo.forward(600)
        fondo.left(90)
        fondo.forward(100)
        fondo.left(90)
    fondo.end_fill()
    fondo.penup()
    fondo.teleport(-200,120)
    fondo.color("light sky blue")
    fondo.begin_fill() #burbujas
    fondo.circle(30)
    fondo.teleport(-225,95)
    fondo.circle(30)
    fondo.teleport(-180,95)
    fondo.circle(30)
    fondo.teleport(180,95)
    fondo.circle(30)
    fondo.teleport(225,95)
    fondo.circle(30)
    fondo.teleport(200,120)
    fondo.circle(30)
    fondo.teleport(0,20)
    fondo.circle(30)
    fondo.teleport(-30,-10)
    fondo.circle(30)
    fondo.teleport(15,-10)
    fondo.circle(30)
    fondo.end_fill()
    fondo.color("darkgreen") #algas de mar
    fondo.begin_fill()
    g=1
    j=-149
    while g<5:
        d=1
        i=-290
        while d<22:
            fondo.teleport(i,j)
            for _ in range(3):
                fondo.forward(10)  
                fondo.left(120) 
            i=i+30
            d=d+1
        j=j+25
        g=g+1
def pez():
    pez=turtle.Turtle()
    pez.speed(300)
    pez.color(a)
    pez.hideturtle()
    pez.penup()
    pez.teleport(x,y)
    pez.pendown()
    pez.begin_fill() #hace circulo o cuerpo del pez
    pez.circle(50)
    pez.end_fill()
    pez.penup()
    pez.teleport(x+100,y)
    pez.pendown()
    pez.setheading(0)
    pez.begin_fill() #hace tringulo de cola del pez
    pez.left(150)
    pez.forward(100)
    pez.right(120)
    pez.forward(100)
    pez.right(120)
    pez.forward(100)
    pez.end_fill()
    pez.penup()
    pez.teleport(x-25,y+50)
    pez.pendown()
    pez.color("black")
    pez.begin_fill() #hace ojo del pez
    pez.circle(10)
    pez.end_fill()
def titulo(): #titulo
    texto=turtle.Turtle()
    texto.hideturtle()
    texto.penup()
    texto.teleport(-110,215)
    texto.pendown()
    texto.write(f"{t}", font=("Arial",16))
def contexto(): #narrativa
    texto=turtle.Turtle()
    texto.hideturtle()
    texto.penup()
    texto.teleport(h,-200-k)
    texto.pendown()
    texto.write(f"{m}", font=("Arial",12))
def cofre(): 
    cofre=turtle.Turtle()
    cofre.hideturtle()
    cofre.speed(300)
    cofre.penup()
    cofre.teleport(x-400,y-90) 
    cofre.pendown()
    cofre.fillcolor("saddlebrown")
    cofre.begin_fill()
    for _ in range(2): #rectangulo del cofre
        cofre.forward(200)
        cofre.right(90)
        cofre.forward(100)
        cofre.right(90)
    cofre.end_fill()
    cofre.penup
    cofre.color("black")
    cofre.teleport(x-400,y-120)
    cofre.pendown #linea divisora de la tapadera
    cofre.forward(200)
    cofre.penup
    cofre.color("yellow") #entrada de la llave
    cofre.teleport(x-308,y-125)
    cofre.pendown
    cofre.begin_fill()
    for _ in range(3):
        cofre.forward(15)
        cofre.left(120)
    cofre.end_fill()
def estrella():
    star=turtle.Turtle()
    star.hideturtle()
    star.speed(300)
    star.teleport(x-300, y-10)
    star.color(a)
    star.begin_fill()
    for _ in range(5):
        star.forward(100)
        star.right(144)
    star.end_fill()
    star.penup
    star.teleport(x-262,y-10)
    star.begin_fill()
    for _ in range(5): #relleno de la estrella 
        star.forward(24)
        star.right(72)
    star.end_fill()
def habla():
    bubble = turtle.Turtle()
    bubble.hideturtle()
    bubble.speed(0)
    bubble.penup()
    bubble.teleport(x - 200, y+130)
    bubble.pendown()
    bubble.color("white")
    bubble.pencolor("black")
    bubble.begin_fill()
    for _ in range(6): #dibuja hexagono de burbuja de texto
        bubble.forward(60)
        bubble.right(60)
    bubble.end_fill()
    bubble.penup()
    bubble.teleport(x -210, y +80) #se posiciona para escribir
    bubble.pendown()
    bubble.color("black")
    bubble.write(b, font=("Arial", 12))
z=1
print("Hola, bienvenido a nuestro cuenta cuentos")
#preguntar datos del niño
n=input("Ingresa tu nombre: ")
e=int(input("ingresa tu edad en numeros: "))
print("1) rojo", "2) azul", "3) amarillo", "4) morado", "5) rosado", sep="\n")
c=int(input("ingresa tu color preferido entre los mencionados"))
while z==1: #ciclo para pasar de escena
    s=int(input("ingrese la escena a la que desea ir (o presiona 0 para salir): "))
    match s:
        case 1:
            margen()
            fondo()
            #definicion de variables
            t=f"{n}, un Pez Curioso"
            titulo()
            x=-50
            y=0
            #estructura anhidada para definir el color 
            if c==1:
                a="red"
                m=f'Había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color rojo.'
            elif c==2:
                a="blue"
                m=f'Había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color azul.'
            elif c==3:
                a="yellow"
                m=f'Había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color amarillo.'
            elif c==4:
                a="purple"
                m=f'Había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color morado.'
            elif c==5:
                a="pink"
                m=f'Había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color rosado.'
            else:
                print("Por favor ingrese un color válido")
                z=1
            pez()
            h=-290
            k=0
            contexto()
            z=1
            
        case 2:
            margen()
            fondo()
            t='El Tesoro'
            titulo()
            x=125
            y=50
            if c==1:
               a="red"
            elif c==2:
               a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            cofre()
            m= f"{n} salió a jugar al arrecife cuando se encontró un cofre del tesoro, que nunca "
            h=-290
            k=0
            contexto()
            m= f"antes había visto. Aún asi, {n}, a sus {e} años tenía mucha curiosidad de ver que "
            k=20 #cambio de línea en la narrativa
            contexto()
            m= f"sorpresas contendría ese cofre misterioso. "
            k=40
            contexto()
            z=1

        case 3:      
            margen()
            fondo()
            t='La Estrella del Cofre'
            titulo()
            x=150
            y=70
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            m=f"Del cofre salió una desconocida estrella que casualmente era del color favorito "
            cofre()
            estrella()
            h=-290
            k=0
            contexto()
            k=20
            m=f"de {n}. {n} amaba las estrellas y su color, por lo que decició acercarse "
            contexto()
            k=40
            m=f" sin pensar en las concecuencias."
            contexto()
            z=1

        case 4:
            margen()
            fondo()
            t='Una Lección de Vida'
            titulo()
            x=80
            y=20
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            estrella()
            h=-290
            b='Ten cuidado'
            habla()
            k=0
            m=f"La estrella le dijo a {n} que tuviera cuidado porque, a pesar de que esta vez se"
            contexto()
            k=20
            m='encontró con una estrella amistosa, no siempre tendría la misma suerte y eso podría'
            contexto()
            k=40
            m='hacerle daño.'
            contexto()
        case 5:
            margen()
            fondo()
            t="Un Aprendizaje Valioso"
            titulo()
            x=0
            y=0
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            h=-290
            k=0
            m=f"Entonces, {n} aprendió que debe ser cuidadoso con los lugares a donde va"
            contexto()
            k=20
            m='porque podría ser peligroso para él y los que lo rodean.'
            contexto()
            b='Seré más'
            habla()
            #lineas 384-378 hacen la 2da linea de texto para la burbuja 
            h=-210
            k=-250
            m='cuidadoso'
            contexto()
            z=1
        case 0: #rompe el ciclo 
            print("Gracias por visitarnos")
            break

        case _: #no se ingresó una escena valida
            print("ERROR. Elige una escena entre 1 y 5")
#finaliza turtle
turtle.done
