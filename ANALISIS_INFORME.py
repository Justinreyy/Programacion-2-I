import numpy as np
import matplotlib.pyplot as plt

# Datos simulados (puedes usar los reales)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([100, 120, 135, 160, 200, 250, 310, 380, 470, 580, 710, 860])  # crecimiento

# Transformación logarítmica: ln(y) = ln(a) + b*x
log_y = np.log(y)
coef = np.polyfit(x, log_y, 1)
b = coef[0]
ln_a = coef[1]
a = np.exp(ln_a)

# Ecuación: y = a * e^(b * x)
print(f"Modelo exponencial: y = {a:.2f} * e^({b:.2f}x)")

# Gráfica
x_suave = np.linspace(1, 12, 100)
y_ajuste = a * np.exp(b * x_suave)

plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x_suave, y_ajuste, color='red', label='Modelo exponencial')
plt.title('Ajuste Exponencial del Consumo')
plt.xlabel('Mes')
plt.ylabel('Consumo (kWh)')
plt.grid(True)
plt.legend()
plt.show()









