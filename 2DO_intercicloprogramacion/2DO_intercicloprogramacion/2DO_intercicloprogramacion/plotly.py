import matplotlib.pyplot as plit
import plotly.express as px

tipos = ["H10", "H20", "H30", "H40"]
resistencia = [150, 220, 280, 340]

fig = px.bar(x=tipos, y=resistencia,
             labels={"x": "Tipo de Hormigón", "y": "Resistencia (kg/cm²)"},
             title="Resistencia de Diferentes Tipos de Hormigón")
fig.show()



