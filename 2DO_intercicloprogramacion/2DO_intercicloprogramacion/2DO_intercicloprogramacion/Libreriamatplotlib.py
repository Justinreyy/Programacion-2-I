import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 8, 7]

plt.plot(x, y, marker='o', color='red')  #DIBUJA LA GRAFICA DE LINEA Añade un marcador en forma de círculo en cada punto.
plt.title('Gráfica de Línea Simple') #AGG UN TITULO AL GRAFICO
plt.xlabel('Eje X') #NOMBRE PARA EL EJE VERTICAL
plt.ylabel('Eje Y')#NOMBRE HORIZONTAL
plt.grid(True) #Activa la cuadrícula para facilitar la lectura de los datos.
plt.show()

