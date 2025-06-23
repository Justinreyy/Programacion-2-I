# Calculadora básica
def calculadora():
    print("\nCalculadora Básica")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("¿Qué operación quieres hacer?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Resultado de la suma es:", a + b)
    elif opcion == "2":
        print("Resultado de la resta es:", a - b)
    elif opcion == "3":
        print("Resultado de la multiplicación es:", a * b)
    elif opcion == "4":
        if b != 0:
            print("Resultado de la división es:", a / b)
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opción inválida.")

# Promedio de notas
def promedio():
    print("\nPromedio de Notas")
    notas = []
    cantidad = int(input("¿Cuántas notas quieres ingresar? "))
    for i in range(cantidad):
        nota = float(input("Ingresa la nota: "))
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    print("El promedio es:", promedio)

# Juego de adivinanza
def juego_numero():
    print("\nJuego del Número Secreto")
    import random
    numero_secreto = random.randint(1, 10)
    adivina = 0
    while adivina != numero_secreto:
        adivina = int(input("Adivina el número (1-10): "))
        if adivina < numero_secreto:
            print("Muy bajo. Intenta otra vez.")
        elif adivina > numero_secreto:
            print("Muy alto. Intenta otra vez.")
        else:
            print("¡Adivinaste!")
# Conversor de temperatura
def conversor_temp():
    print("\nConversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción (1-2): ")

    if opcion == "1":
        celsius = float(input("Ingresa los grados Celsius: "))
        f = (celsius * 9/5) + 32
        print("La temperatura en Fahrenheit es:", f)
    elif opcion == "2":
        f = float(input("Ingresa los grados Fahrenheit: "))
        celsius = (f - 32) * 5/9
        print("La temperatura en Celsius es:", celsius)
    else:
        print("Opción inválida.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Calculadora")
        print("2. Promedio de notas")
        print("3. Juego del número secreto")
        print("4. Conversor de temperatura")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            calculadora()
        elif opcion == "2":
            promedio()
        elif opcion == "3":
            juego_numero()
        elif opcion == "4":
            conversor_temp()
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción Incorrecta. Intenta de nuevo.")

# Ejecutar el menú
menu()
