# 4 sep 2026
# Developer: Samuel

# Imprimiendo una serie de numeros
# Recorremos una COLLECION de elementos como un rango o lista
for numero in range(1, 6):
    print(f"Generando reporte numero {numero}")

#=========================================
print("=" * 30)
for num in range(10):
    print(num)

#=========================================
print("=" * 30)
for palabra in "hola":
    print(palabra)

#=========================================
print("=" * 30)
frutas = ["Manzana", "Pera", "Piña", "Sandia", "Fresa", "Cereza"]

for fruta in frutas:
    print(fruta)

#=========================================
print("=" * 30)
print("Ahora viene la magia")

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

#=========================================
print("=" * 30)
print("Menu de frutas".upper())
print("Bienvenidos".upper())
print("=" * 30)

for indice, fruta in enumerate(frutas):
    print(f"En la caja {indice}, tengo {fruta}")

print("=" * 30)
print("Muchas gracias por utilizar".upper())
print("Nuestro programa".upper())
print("=" * 30)