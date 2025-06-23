nueva_linea = input("Agrega una nueva línea a mbox.txt: ")
with open("mbox.txt", "a") as f:
    f.write(nueva_linea + "\n")
print("Línea añadida a mbox.txt.")
