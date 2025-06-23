import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos simulados de consumo mensual por sector
datos = {
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    "Residencial": [120, 115, 130, 140, 150, 160, 170, 165, 155, 145, 135, 125],
    "Comercial": [200, 210, 220, 230, 240, 250, 260, 255, 245, 235, 225, 215],
    "Industrial": [300, 310, 320, 330, 340, 350, 360, 355, 345, 335, 325, 315]
}

df = pd.DataFrame(datos)
df_melted = df.melt(id_vars="Mes", var_name="Sector", value_name="Consumo_kWh")
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x="Mes", y="Consumo_kWh", hue="Sector", marker="o")

plt.title("Consumo mensual de energía eléctrica por sector")
plt.xlabel("Mes")
plt.ylabel("Consumo (kWh)")
plt.legend(title="Sector")
plt.tight_layout()
plt.show()

