peso = 70.5
altura = 1.75

# 1. Completa la fórmula matemática del IMC (peso dividido por la altura al cuadrado
imc = peso /(altura * altura)

print("Tu IMC es:", imc)

# Encuentra los 3 errores en esta estructura:
if imc < 18.5:
    print("Diagnóstico: Bajo peso")
elif imc <= 24.9:
    print("Diagnóstico: Peso normal")
elif imc < 29.9:
    print("Diagnóstico: Sobrepeso")
else:
    print("Diagnóstico: Obesidad")