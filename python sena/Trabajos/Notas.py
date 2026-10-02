# Developer: Pastrana
print()
print("="*50)
print("--PROMOCION SOCIAL---")
print("="*50)

Nombre = input("Digite su Nombre: ").upper()
nota = int(input("Digite su nota: "))

print(f"Hola {Nombre}")
if nota > 100 or nota < 0:
    print("Nota Incorrecta")
elif nota >= 90:
    print("☑️Excelente nivel")
elif nota <=70:
    print("Aprobado. Buen desmpeño😂")
elif nota <=50:
    print("Debes repasar los conceptos, Tu puedes¡👌")


