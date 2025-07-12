#Conteo regresivo con while
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

print("¡Despegue!")

#Adivina la palabra secreta
palabra_secreta = "Futbol"

while True:
    intento = input("Adivina la palabra secreta: ")
    
    if intento == palabra_secreta:
        print("¡Has adivinado la palabra!")
        break
    else:
        print("Inténtalo de nuevo.")

#procesador de entradas con continue
while True:
    entrada = input("Ingresa un texto: ")
    
    if entrada == "#":
        continue
    elif entrada == "listo":
        print("¡Procesamiento terminado!")
        break
    else:
        print(entrada.upper())
    
#Lista de invitados con for
invitados = ['Ana', 'Luis', 'Carla', 'Pedro']

for nombre in invitados:
    nombre = input("Ingresa El nombre del invitado")
    print("Hola " + nombre + ", ¡bienvenida a la fiesta!")

#Encontrados el numero mayor (for)
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = -1

for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero

print("El número más grande es:", mayor_hasta_ahora)

#Conteo de elemtos pares pares (for y codicional)
numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)

#Suma todos los numeros (FOR)
numeros = [10, 20, 30, 40, 50]
suma_total = 0

for numero in numeros:
    suma_total += numero

print("La suma total es:", suma_total)

#Calculo del Promedio (for)
numeros = [10, 15, 20, 25, 30]
suma_total = 0
cantidad = 0

for numero in numeros:
    suma_total += numero
    cantidad += 1

promedio = suma_total / cantidad
print("El promedio es:", promedio)

#Filtrando numeros mayores que un valor (For)
numeros = [5, 25, 12, 33, 18, 45, 7]

umbral = int(input("Ingresa un número umbral: "))

for numero in numeros:
    if numero > umbral:
        print(numero)

#Busqueda de un valor especifico (for,booleano)
numeros = [9, 41, 12, 3, 74, 15]
encontrado = False

for numero in numeros:
    if numero == 3:
        encontrado = True
        break

print("El valor 3 fue encontrado:", encontrado)

#Encontrando el umero menor (for y none)
numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None

for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero

print("El número más pequeño es:", menor_hasta_ahora)   