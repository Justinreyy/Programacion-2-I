import os

def crear_archivo():
    nombre = input("Ingrese el nombre del archivo (sin .txt): ").strip()
    with open(nombre + ".txt", "w") as archivo:
        archivo.write("")  # crea archivo vacío
    print("Archivo creado correctamente.")

def nuevo():
    print("Esta opción eliminará TODOS los archivos listados por el usuario.")
    archivos = input("Ingrese los nombres de los archivos separados por coma: ")
    lista = archivos.split(",")
    for nombre in lista:
        nombre = nombre.strip()
        try:
            os.remove(nombre + ".txt")
            print(f"Archivo '{nombre}.txt' eliminado.")
        except FileNotFoundError:
            print(f"El archivo '{nombre}.txt' no existe.")

def escribir():
    nombre = input("Nombre del archivo donde escribir (sin .txt): ").strip()
    try:
        with open(nombre + ".txt", "a") as archivo:
            texto = input("Ingrese el texto que desea agregar: ")
            archivo.write(texto + "\n")
        print("Texto escrito correctamente.")
    except FileNotFoundError:
        print("El archivo no existe. Primero créelo con la opción 1.")

def eliminar():
    nombre = input("Ingrese el nombre del archivo a eliminar (sin .txt): ").strip()
    try:
        os.remove(nombre + ".txt")
        print("Archivo eliminado.")
    except FileNotFoundError:
        print("El archivo no existe.")

def menu():
    while True:
        print("\n= MENÚ ARCHIVOS")
        print("1. Crear archivo")
        print("2. Nuevo (borrar varios archivos)")
        print("3. Escribir en archivo")
        print("4. Eliminar archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            nuevo()
        elif opcion == "3":
            escribir()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()