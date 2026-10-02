# ===================================
# Registros de Empleados
# Tecnico en programacion de software
# ===================================

print("=" * 50)
print("REGISTRO DE EMPLEADOS")
print("=" * 50)

nombre = input("Nombre del empleado: ").upper()
edad = int(input("Edad: "))
cargo = input("Cargo: ")
SalarioMensual = int(input("Salario Mensual: "))
activo = input("¿El empleado está activo? (true / false): ")

#Conversion a dato booleano
#activo = activo == "True"

if activo == "True":
    activo = "Empleado activo"
else:
    activo = "Empleado no activo"

print("=" * 50)
print("INFORMACION REGISTRADA")
print("=" * 50)
print(F"Nombre: {nombre}")
print(F"edad: {edad}")
print(f"Cargo: {cargo}")
print(f"Salario mensual: {SalarioMensual}")
print(f"Empleado activo: ", activo)

print("\n Tipos de datos ----------")
print("Nombre", type(nombre))
print("edad", type(edad))
