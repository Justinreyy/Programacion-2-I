palabra=input("ingresa una palabra")
palabra = palabra.lower()
a = e = i = o = u = 0
for letra in palabra:
    if letra in palabra =="a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra =="u":
        u += 1

print("vocales encontradas:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
