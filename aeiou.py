texto = input("Ingresa una cadena de texto: ").lower()

# Inicializando contadores

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for i in texto:
    if i == 'a':
        contador_a += 1
    elif i == 'e':
        contador_e += 1
    elif i == 'i':
        contador_i += 1
    elif i == 'o':
        contador_o += 1
    elif i == 'u':
        contador_u += 1


print(f"La letra a aparece {contador_a} veces")
print(f"La letra a aparece {contador_e} veces")
print(f"La letra a aparece {contador_i} veces")
print(f"La letra a aparece {contador_o} veces")
print(f"La letra a aparece {contador_u} veces")