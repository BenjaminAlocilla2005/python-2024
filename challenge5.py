n = int(input("Ingrese el número de la serie de Fibonacci para la impresión de la serie"))

#Variantes iniciales de la serie de Fibonacci
a = 0
b = 1

#Se guardan en una lista para almacenar la serie de Fibonacci
fibonacci = [a, b] # Se guardan los valores iniciales 0 y 1

#Serie de Fibonacci hasta el valor n
while True: #Bucle infinito hasta que se encuentre con el break
    c = a + b 
    if c > n:
        break
    fibonacci.append(c)
    a = b
    b = c
    
    a, b = b, c

print(" ".join(map(str, fibonacci)))


