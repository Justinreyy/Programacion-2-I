numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)
