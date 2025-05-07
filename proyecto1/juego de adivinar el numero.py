numero_secreto = 7  # Número fijo
intentos = 3

print("Adivina el número del 1 al 10. Tienes 3 intentos.")

for i in range(intentos):
    intento = int(input(f"Intento {i + 1}: Ingresa un número: "))
    
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print(f"Lo siento, no adivinaste el número. Era el {numero_secreto}.")
    