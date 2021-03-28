#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4%
#  de interés al año. Estos ahorros debido a intereses, que no se cobran hasta
#  finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir 
# un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#  introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la 
# cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
while(True):
    try:
        Ahorro=int(input("Ingrese cantidad de dinero a depositar : "))
    except:
        print("Error, Vuelva Ingresar dato")
    else:
        break
i=0.04 
for n in range(1,4):
    D=Ahorro*((1+i)**n)
    D=round(D,2)
    print(f"El ahorro del mes {n} es {D}")


#Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y 
# escriba la solución.
#recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos 
# soluciones o que todos los números sean solución.

import math
a=int(input("Ingrese 1er coeficiente : "))
b=int(input("Ingrese 2do coeficiente : "))
c=int(input("Ingrese 3er coeficiente : "))
Discriminante=math.pow(b,2)-4*a*c
if Discriminante>0:
    x=(-b+math.sqrt(Discriminante))/2*a
    x1=(-b-math.sqrt(Discriminante))/2*a
    print(f"La solucion Positiva es : {x}")
    print(f"La solucion Negativa es : {x1}")
elif Discriminante ==0:
    x2=-b/2*a
    print(f"La unica solucion es: {x2}")
else:
    print("No tiene solucion real ")
