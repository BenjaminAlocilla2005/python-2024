ciudades = list(["Santiago","Temuco","Osorno","Punta Arenas"])

calidades_de_aire = list([134,99,245,50])

for i in calidades_de_aire:
    print(i)

if calidades_de_aire <= 50:
    print('La calidad es buena')
elif calidades_de_aire <= 100:
    print('La calidad es moderada')
elif calidades_de_aire <= 150:
    print('La calidad es dañina a la salud para grupos sensibles')
elif calidades_de_aire <= 200:
    print('La calidad es dañina a la salud')
elif calidades_de_aire <= 300:
    print('La calidad es peligrosa')
else:
    print('Osorno tiene la calidad de aire más peligrosa')