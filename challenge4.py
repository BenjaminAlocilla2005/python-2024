numeros = 10
while numeros <= 50:
    print(numeros)
    numeros+= 2
else:
    print("los numeros son del rango 10 al 50")

while numeros <= 50:
    numeros+= 2
    if numeros == 50:
        continue
    print(numeros)

