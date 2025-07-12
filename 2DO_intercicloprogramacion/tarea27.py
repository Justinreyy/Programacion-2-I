#5 ejercicios que utilice archivos
with open("mbox.txt", "r") as f:
    for linea in f:
        print(linea.strip())
