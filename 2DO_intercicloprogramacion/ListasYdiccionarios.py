# FRECUENCIA DE PALABRAS
linea = input("Escribe una línea de texto: ")
palabras = linea.lower().split()

frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, cuenta in frecuencia.items():
    print(f"{palabra}: {cuenta}")

#LISTA CON INDICES 
elementos = ["motor", "resistor", "transformador", "cable", "fusible"]

for i, elemento in enumerate(elementos):
    print(f"Índice {i}: {elemento}")

#PALABRA MAS LARGA
palabras = input("Ingresa varias palabras separadas por espacio: ").split()
palabra_larga = max(palabras, key=len)
print(f"La palabra más larga es: {palabra_larga}")

#PALABRAS MAS REPETIDA EN UN ARCHIVO
with open("datos.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read().lower().split()

frecuencia = {}
for palabra in texto:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Ordenar por frecuencia
top_3 = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

print("Las 3 palabras más repetidas son:")
for palabra, cuenta in top_3:
    print(f"{palabra}: {cuenta}")

 #SIMULACION DE TIENDA
tienda = {
    "cable": 1.5,
    "bombillo": 0.75,
    "interruptor": 2.0,
    "toma corriente": 1.25,
    "fusible": 0.50
}

print("Productos disponibles:")
for producto, precio in tienda.items():
    print(f"{producto} - ${precio:.2f}")

busqueda = input("¿Qué producto deseas buscar? ").lower()
if busqueda in tienda:
    print(f"{busqueda} cuesta ${tienda[busqueda]:.2f}")
else:
    print("Producto no encontrado.")



