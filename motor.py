voltaje = 12
corriente = 2

potencia = voltaje * corriente
resistencia = voltaje / corriente

print("Potencia:", potencia, "W")
print("Resistencia:", resistencia, "Ohm")

if potencia > 20:
    print("ALERTA: Potencia elevada")
else:
    print("Funcionamiento normal")