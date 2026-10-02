#imprimir conceptos excelente, aprobado, reprobado
#Nota superior o igual a 90 = Excelente. 60 para abajo = Reprobado. El resto probado
#Developer: isabel

def Concepto(nota):
    if nota >= 90:
        return "\n Usted a aprobado, excelente trabajo!!!"
    elif nota <= 60:
        return "\n Usted a reprobado, mejora tu desempeño!!"
    else:
        return "\n Usted aprobo, vamos por más!!"

nota = int(input("\n Ingrese su nota: "))
print(Concepto(nota))