import val as v

Promedios=[]
for i in range(0,v.alumnos):
    print("Ingrese nota del estudiante "+str(i+1)+": ")
    sum=0
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        sum=sum+notas  
        prom=sum/3
    pass
    Promedios.append(prom)
    
print("El promedio es: ",Promedios)
maximo=max(Promedios)
minimo=min(Promedios)
if maximo>minimo:
    print("El promedio mayor es: ", maximo)
    print("El promedio menor es: ", minimo)