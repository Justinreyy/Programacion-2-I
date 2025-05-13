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
contraseña = "patito123"
entrada = input("Ingresa la contraseña: ")
while entrada != contraseña:
    print("Contraseña incorrecta. Intenta de nuevo.")
    entrada = input("Ingresa la contraseña: ")
print("¡Contraseña correcta! Acceso concedido.")

#Simular un cajero automático (menú: retirar, depositar, salir).
opcion = ""
while opcion != "3":
    print(" Bienvenido a Nuestro cajero ")
    print(" Ingrese 1 para retirar dinero")
    print(" Ingrese 2 para depositar dinero")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        monto = float(input("¿Cuánto deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas depositar? "))
        print("Has depositado $",monto)
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")


# Raíz cuadrada por el método babilónico

n = 20
tol = 1e-4
error_cuadrado = tol ** 2
estimacion = n / 2

while True:
    nueva_estimacion = 0.5 * (estimacion + n / estimacion)
    if (nueva_estimacion - estimacion) ** 2 < error_cuadrado:
        break
    estimacion = nueva_estimacion

print(f"Raíz cuadrada aproximada de {n}: {nueva_estimacion:.5f}")

# Contar cifras de un número entero

numero = 2358
contador = 0
valor = abs(numero)  # Para considerar también números negativos

while valor:
    valor //= 10
    contador += 1

print(f"{numero} tiene {contador} cifras.")

# Sucesión de Fibonacci hasta un límite

limite = int(input("Límite superior para Fibonacci: "))
a, b = 0, 1
fibo = []

while a <= limite:
    fibo.append(a)
    a, b = b, a + b

print(f"Fibonacci hasta {limite}: {fibo}")

# Números primos en un intervalo

inicio, fin = 10, 50

for num in range(inicio, fin + 1):
    if num > 1:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            print(f"Primo: {num}")

# Cuenta regresiva

inicio_cuenta = int(input("Inicio de la cuenta regresiva: "))

for t in range(inicio_cuenta, 0, -1):
    print(f"Tiempo restante: {t} segundos")

print("¡Cuenta regresiva completada!")

#Leer archivos línea por línea hasta fin de archivo.
f = open("archivo.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, end="")
    linea = f.readline()
f.close()
print("fin del programa")
