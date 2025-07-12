from importlib.resources import contents


correos_raw = contents.split(",")

correos_limpios = [correo.strip().strip('"') for correo in correos_raw]

correos_ucacue = [correo for correo in correos_limpios if correo.endswith("@ucacue.edu.ec")]

print("Correos institucionales UCACUE encontrados:")
for correo in correos_ucacue:
    print(correo)