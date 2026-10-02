numero = 1
suma_pares = 0

# 1. Completa la condicion para que llegue hasta el 20 (incluido)
while numero <= 20:
    #2. Completa la logica para saber si el numero es par (residuo de 2)
    if numero % 2 == 0:
        suma_pares += numero

    numero += 1

print(f"La suma de los números pares del 1 al 20 es: {suma_pares}")