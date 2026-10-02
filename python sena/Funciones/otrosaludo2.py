#funcion con argumento
def saludar_persona(nombre):
    print(f"hola{nombre}")

#Llamamos la funcion
saludar_persona("carlos")
saludar_persona("Matias")

#otro ejempplo------
#utilizamos return
def suma(a,b):
    resultado= a+b
    return resultado

print (suma(5,8))

#otro ejemplo 
def despedida(nombre):
    print(f"Adios{nombre}")

despedida("Luis")
despedida("Mario")

