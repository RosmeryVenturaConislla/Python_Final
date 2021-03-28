#MODULO 3 N° 2
import os
import val as v
aprobadas=0
desaprobadas=0
suma=0
sumapro=0
for i in range(0,v.alumnos):
    print("Ingrese nota del estudiante "+str(i+1)+": ")
    
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        suma=suma +notas
        promedio=suma/3
    pass
    if promedio>=4:
        aprobadas+=1
    else:
        desaprobadas+=1
print("la suma de notas es: ", suma)
print("cantidad de aprobados ", aprobadas)
print("cantidad de desaprobados ", desaprobadas)



