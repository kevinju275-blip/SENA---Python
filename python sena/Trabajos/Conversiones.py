# Probando las conversiones de tipo (de datos)

# Definimos una variable con un tipo de dato como numerico
edad = ("12")
edad = int(edad) # covertimos el tipo de dato strig a numerico
edad = edad + 2
print("Tienes", edad, "años")
# el toque profesional para mostrar la misma info
print(f"Tienes {edad} años")