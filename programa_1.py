import sys

# Encabezado visual
print("╔══════════════════════════════════════════════╗")
print("║         🏦 BANCO CENTRAL DE RESERVA          ║")
print("║         Dispensador de Billetes S/           ║")
print("╚══════════════════════════════════════════════╝")

monto_input = input("\n👉 Ingrese el monto en soles (S/): ").strip()

# Validación preliminar de texto
if not monto_input.isdigit():
    print("\n┌──────────────────────────────────────────────┐")
    print("│ ❌ ERROR: Debe ingresar solo números enteros. │")
    print("└──────────────────────────────────────────────┘")
    sys.exit()

monto = int(monto_input)

# Validación de múltiplo de 10 y positivo
if monto <= 0 or monto % 10 != 0:
    print("\n┌──────────────────────────────────────────────┐")
    print("│ ❌ ERROR DE TRANSACCIÓN                      │")
    print("├──────────────────────────────────────────────┤")
    print("│ El monto debe ser mayor a 0 y múltiplo de 10.│")
    print("│ Ejemplos válidos: 50, 120, 280, 400.         │")
    print("└──────────────────────────────────────────────┘")
else:
    # Cálculo de billetes mediante división entera y residuo
    b100 = monto // 100
    resto = monto % 100

    b50 = resto // 50
    resto = resto % 50

    b20 = resto // 20
    resto = resto % 20

    b10 = resto // 10

    # Imprimir resultado en un marco estructurado
    print("\n┌──────────────────────────────────────────────┐")
    print(f"│ 📊 RESUMEN DE RETIRO        Monto: S/ {monto:<6} │")
    print("├──────────────────────────────────────────────┤")
    print(f"│  💵 Billetes de S/ 100 : {b100:>3} unidades        │")
    print(f"│  💵 Billetes de S/  50 : {b50:>3} unidades        │")
    print(f"│  💵 Billetes de S/  20 : {b20:>3} unidades        │")
    print(f"│  💵 Billetes de S/  10 : {b10:>3} unidades        │")
    print("└──────────────────────────────────────────────┘")
    print("      ✨ ¡Gracias por usar el servicio! ✨\n")