#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
import aleatorio

secreto = aleatorio(1, 100)
intentos = 0

print("Adivina el número entre 1 y 100")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < secreto:
        print("El número secreto es mayor.")
    elif intento > secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Correcto! Adivinaste en {intentos} intento(s).")
        break



#Validar contraseña (repetir hasta que coincida con una guardada).

#Simular un cajero automático (menú: retirar, depositar, salir).

#Calcular la raíz cuadrada por aproximación (método babilónico).

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.

#mientras - while
#visualizar los 5 primeros numeros con mientras = while

contador= 0
while contador <=10:
     print("numero: ", contador)
     contador += 1
