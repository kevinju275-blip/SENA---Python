# ================================
# Elaborar un programa que diga si el zorro cruza con base a la energia y a las monedas
# =================================

Energia = int(input("Ingrese la cantidad de energia: "))
Monedas = int(input("Ingrese la cantidad de monedas: "))

if Energia >= 50:
    print("Puede cruzar el puente sin pagar nada")
elif Energia < 50 and Monedas >= 5:
    print("Tiene que pagar peaje en la barca magica")
else:
    print("Deberas quedarte en la posada del bosque")