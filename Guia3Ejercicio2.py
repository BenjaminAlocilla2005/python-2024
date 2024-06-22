'''
2. Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800
'''
n1 = 500
n2 = 456
suma = 0
while n1 != 800:
    suma += n1
    suma += n2
    n1 += 10
    n2 -= 2
suma += 800 #benja recuerda separar la suma y print del while
print(suma)



