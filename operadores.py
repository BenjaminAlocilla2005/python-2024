

bencina = True
encendido = True
edad = 19

if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

if not bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

edad = 19

if edad >= 18:
    print('eres mayor de edad')
print('este print esta fuera del if')
