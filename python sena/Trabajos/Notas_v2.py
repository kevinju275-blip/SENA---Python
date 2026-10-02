#programa de notas
#de la loper Pastrana
#Date: 21-08-26

print()
print("=" *50)
print("--Promocio social---")
print("=" * 50)

nombre = input("Digite su Nombre:").upper()
nota = int(input("Digite su nota"))

if nota >= 100:
    print(f"la nota{nota} es incorrecta")
elif nota >= 90:
    print("☑️excelente nivel ")
elif nota >= 70:
    print("👌aprobado,buen desempeño" )
elif nota >= 50:
    print("👍 debes repasar los conceptos tu puedes")
