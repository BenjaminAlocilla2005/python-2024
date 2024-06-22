def factorial (num):
    if num == 0:
        a = 1
    elif num>=1:
        a = num*factorial(num-1)
    return a
num = int(input("Ingrese un numero: "))
print(f"el numero factorial de {str(num)} es {factorial(num)}")