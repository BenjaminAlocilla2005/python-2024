def reloj():
    for h in range(24): #horas
        for m in range(60): #minutos
            for s in range(60): #segundos
                print(f"{h:02}:{m:02}:{s:02}")
reloj()