td = 12000 #tarifa diurna
tn = 16000  #tarifa nocturna
tdd = 14000  #tarifa diurna en domingo
tnd = 19000  #tarifa nocturna en domingo
e = {
    "Primer empleado": {
        "Lunes": "nocturno",
        "Martes": "nocturno",
        "Miercoles": "nocturno",
        "Jueves": "diurno",
        "Viernes": "diurno",
        "Sabado": "descanso",
        "Domingo": "descanso"
    },
    "Segundo empleado": {
        "Lunes": "descanso",
        "Martes": "nocturno",
        "Miercoles": "nocturno",
        "Jueves": "nocturno",
        "Viernes": "descanso",
        "Sabado": "descanso",
        "Domingo": "diurno"
    },
    "Tercer empleado": {
        "Lunes": "descanso",
        "Martes": "descanso",
        "Miercoles": "diurno",
        "Jueves": "diurno",
        "Viernes": "diurno",
        "Sabado": "nocturno",
        "Domingo": "nocturno"
    }
}
def sp(e):   #suma de pagos 
    ps = 0
    for d, t in e.items():
        if t == "diurno":
            if d == "Domingo":
                pd = tdd
            else:
                pd = td
        elif t == "nocturno":
            if d == "Domingo":
                pd = tnd
            else:
                pd = tn
        else:
            pd = 0  

        ps += pd

    return ps
for nombre, horario in e.items():
    c = sp(horario)
    print(f"Empleado: {nombre}") 
    print(f"Pago semanal: {c} CLP")
    print("---")