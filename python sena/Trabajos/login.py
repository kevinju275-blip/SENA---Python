# 4 de septiembre de 2026
# Devoloper: Sam y Johan

pin = "12345"
intentos = 0
bloqueado = False
intentos_Incorrectos = 3

while  intentos < 3:
    ingreso = input("Ingrese su PIN: ")
    if ingreso == pin:
        print("Accediste, que lindo!!")
        break #rompe el Condicionla
    else:
        intentos = intentos + 1
        intentos_Incorrectos -= 1
        # Intentos += 1
        print(f"PIN incorrecto. 😂 Te quedan {intentos_Incorrectos} intentos")

if intentos == 3:
    print("Cuenta bloqueada por seguridad")
