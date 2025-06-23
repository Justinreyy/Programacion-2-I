# EJERCICIO
def computepay(horas, tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else:
        horas_normales = 40
        horas_extras = horas - 40
        salario = (horas_normales * tarifa) + (horas_extras * tarifa * 1.5)
    return salario

# Entrada de datos
horas = float(input("Ingresar Horas: "))
tarifa = float(input("Ingresar Tarifa: "))

# Cálculo y salida
salario_total = computepay(horas, tarifa)
print("Salario:", salario_total)