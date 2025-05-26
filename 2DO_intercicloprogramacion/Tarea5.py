def saludo (lang) :
    if lang == 'es' :
     return ('Hola')
    elif lang == 'fr':
     return ('Bonjour')
    else:
     return ('Hello')
print(saludo("en"), "glenn")
print(saludo("es"), "Sally")
print(saludo("fr"), "Michael")