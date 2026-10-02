# ================================
# Elaborar un producto en donde venda ropa, etc
# Nombre del cliente en mayusculas
# Precio redondeado
# Consentir al cliente
# =================================

print("=" * 50)
print("TIENDA VIRTUAL")
print("=" * 50)


Cliente = input("Nombre del cliente: ").upper()
ProductoVenta = input("Ingrese el nombre del producto: ")
Precio = float(input("Precio Unitario del producto en USD: "))
Cantidad = int(input("Cantidad a comprar: "))

total = Precio * Cantidad
total = round(total,2)

print("=" * 50)
print("FACTURA DE COMPRA")
print("=" * 50)
print(f"Cliente: {Cliente}")
print(f"Producto: {ProductoVenta}")
print(f"Precio Unitario: {Precio}")
print(f"Cantidad: {Cantidad}")
print(f"Total a pagar: ${total} USD")

if total > 20:
    print("¡FELICIDADES! Por comprar más de $20 USD recibes un obsequio del 20% en tu proxima compra!")
else:
    print("Gracias por tu compra. ¡Vuelve pronto!")

print("\n Tipos de datos ----------")
print("Nombre", type(Cliente))
print("Cantidad", type(Cantidad))