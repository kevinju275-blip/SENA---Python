#Programa para  restar, multiplicar, dividir

def resta():
    return num1 - num2

def multiplicacion():
    return num1 * num2


def division():
    return num1 / num2

num1 = int(input("\n Ingrese el primer numero: "))
num2 = int(input("\n Ingrese el segundo numero: "))

resultado = resta()
print(f"\n el resultado de la resta es: {resultado}")

resultado = multiplicacion()
print(f"\n el resultado de la multiplicacion es: {resultado}")

if num2 == 0:
    print("\n ERROR, no se puede dividir entre 0 :3")
else:
    resultado = division()
    print(f"\n El resultado de la division es: {resultado}")
