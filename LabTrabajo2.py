descripcion = "Una editorial busca que esta aplicacion gestione y manipule contenido"

# verificar si el valor es igual o menor a 60 caracteres
descripcion = descripcion [:60]


# los ultimos 10 caracteres del resumen
descripcion = descripcion [:10]

# insertar valor Booleano
bool(descripcion)

print(f"{descripcion} es igual o menor a 60 caracteres?: ")
print(f"")