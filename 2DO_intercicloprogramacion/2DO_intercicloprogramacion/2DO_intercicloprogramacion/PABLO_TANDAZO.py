import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
sns.barplot(x="class", y="fare", data=titanic)

plt.title("Gráfico de barras")
plt.show()
