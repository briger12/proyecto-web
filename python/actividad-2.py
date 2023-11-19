
# 3 numeros positivos elegir el mayor
numeros=[]
cont=0

def mayor(lista):
    mayor=lista[0]
   
    i=0
    for i in range(0,3,1):
        
        if lista[i]>mayor:
            mayor=lista[i]

    print("el mayor es {}".format(mayor))


while cont < 3:
    
    num= float(input("introdusca un numero"))
    if num < 0:
        print("el numero debe ser positivo")
        
    else:
        numeros.append(num)
        cont+=1
    print(cont)
    
mayor(numeros)

