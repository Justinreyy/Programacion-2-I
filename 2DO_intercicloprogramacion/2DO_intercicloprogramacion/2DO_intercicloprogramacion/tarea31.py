with open("mbox.txt", "r") as f_origen:
    contenido = f_origen.read()

with open("mbox_copia.txt", "w") as f_destino:
    f_destino.write(contenido)

print("Contenido de mbox.txt copiado a mbox_copia.txt.")
