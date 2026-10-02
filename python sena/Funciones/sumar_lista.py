#Bucle for para una lista

def sumar_lista(numeros):
    total = 0
    for num in numeros:
        total += num
        #total = total + num
    return total

#------------------------
# LLamamos la funcion

notas = [10,25,5,40] #Esto es una lista
total = sumar_lista(notas)
print(total)