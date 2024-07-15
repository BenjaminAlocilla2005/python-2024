
# 1. Frutas
fruta_1 = "manzana"
fruta_1coste = 100
fruta_1cantidad = 150

fruta_2 = "pera"
fruta_2coste = 250
fruta_2cantidad = 80

fruta_3 = "durazno"
fruta_3coste = 300
fruta_3cantidad = 120


# 2.acciones solicitadas

preciodecantidad1 = fruta_1coste * fruta_1cantidad
preciodecantidad2 = fruta_2coste * fruta_2cantidad
preciodecantidad3 = fruta_3coste * fruta_3cantidad

totalquepagar = preciodecantidad1 + preciodecantidad2 + preciodecantidad3

pagodemanzanasyperas = preciodecantidad1 + preciodecantidad2

valormax_de_manzana = preciodecantidad1

valormax_de_pera = preciodecantidad2

valormax_de_durazno = preciodecantidad3

valorminimo1 = (preciodecantidad1/3,3)

valorminimo2 = (preciodecantidad2/3,3)

valorminimo3 = (preciodecantidad3/3,3)

print(f"la suma total a pagar es {totalquepagar}")
print(f"La suma total para pagar la compra de manzanas y peras es {pagodemanzanasyperas}")
print(f"El valor maximo de las manzanas es {valormax_de_manzana}, el de las peras es {valormax_de_pera} y de los duraznos es {valormax_de_durazno}")
print(f"el valor minimo de las manzanas es {valorminimo1}, de las es {valorminimo2} y de los duraznos es {valorminimo3}")
