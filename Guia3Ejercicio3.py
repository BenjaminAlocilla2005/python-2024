td = 12000  
tn = 16000  

ds = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
tdd = td + 2000
tnd = tn + 3000

e = {
    "Primer empleado": {
        "Lunes": "Nocturno",
        "Martes": "Nocturno",
        "Miercoles": "Nocturno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sabado": "descanso",
        "Domingo": "descanso"
    },
    "Segundo empleado": {
        "Lunes": "",
        "Martes": "Nocturno",
        "Miercoles": "Nocturno",
        "Jueves": "Nocturno",
        "Viernes": "descanso",
        "Sabado": "descanso",
        "Domingo": "Diurno"
    },
    "Tercer empleado": {
        "Lunes": "descanso",
        "Martes": "descanso",
        "Miercoles": "Diurno",
        "Jueves": "Diurno",
        "Viernes": "Diurno",
        "Sabado": "Nocturno",
        "Domingo": "Nocturno"
    }
}
for empleado, horario in e.items():
    ps = 0
    for dia, turno in horario.items():
        if turno == "Diurno":
            if dia == "Domingo":
                pd = tdd * 10
            else:
                pd = td * 10
        elif turno == "Nocturno":
            if dia == "Domingo":
                pd = tnd * 10
            else:
                pd = tn * 10
        else:
            pd = 0
        
        if turno != "":
            print(f"{empleado} trabaja {dia} en turno {turno}: Pago diario = {pd} CLP")
            ps += pd
    
    e[empleado]["Pago_Semanal"] = ps
    print(f"Total semanal de {empleado}: {ps} CLP\n")

for empleado, info in e.items():
    print(f"Empleado: {empleado}")
    print(f"  Pago semanal total: {info["Pago_Semanal"]} CLP\n")