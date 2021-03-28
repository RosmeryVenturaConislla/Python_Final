#Implemente un programa que imprima una
# media pirámide de una altura específica, 
# como se indica a continuación.

#$ ./mario
#Height: 4
   #
  ##
 ###
####

A=int(input("Ingrese altura de la piramide: "))
if A>=1 and A<=8:
    for n in range(A+1):
        X=A-n
        
        print(" "*X+"#"*n)
else:
    print("Vuelva a ingresar valor")