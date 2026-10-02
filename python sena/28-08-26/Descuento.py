# ================================
# Elaborar un programa que de descuento con base al precio de la compra
# Precio = 100.000 entonces 10% de descuento
# Precio = 200.000 entonces 20% de descuento
# Precio es menor a 100.000 entonces no hay descuento
# =================================

print("="*50)
print("------- FACTURA -------")
print("="*50)

Total_compra = float(input("Ingrese el valor total de la compra: "))

if Total_compra >= 200.000:
    total_descuento = Total_compra*0.20
elif Total_compra >= 100.000:
    total_descuento = Total_compra*0.1
else:
    total_descuento = 0

total_pagar = Total_compra - total_descuento

print(f"El descuento aplicado es de: ${total_descuento }")
print(f"El total a pagar con descuento es de: ${total_pagar}")
print("="*50)
print("------- GRACIAS POR VISITARNOS -------")
print("="*50)