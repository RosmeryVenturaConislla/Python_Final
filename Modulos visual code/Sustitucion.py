
#Implemente un programa que implemente un 
# cifrado de sustitución, 
# como se indica a continuación.

def encriptacion(phrase):
    X=input("Ingrese llave de sustitucion :")
    a=len(X)
    if a<26:
        print("Error, Ingrese 26 caracteres")
    else: 
        abc="abcdefghijklmnopqrstuvwxyz"
        encript=""
        for i in phrase:
            for n in range(len(abc)):
                if i==abc[n]:
                    encript+=X[n]
        return encript
        
phrase=input("Ingrese texto a encriptar : ")
encript=encriptacion(phrase)
print(phrase)
print(encript)
    