from datetime import datetime, time

def engagement(fecha):
    fecha_formato = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    if fecha_formato.weekday() == 1:  # 1 representa el martes
        if time(0,0) <fecha_formato.time()< time(4,59,59) or time(23,0) <fecha_formato.time()< time(23,59,59):
            return "Martes: Engagement medio bajo"
        elif time(5,0) <fecha_formato.time()< time(6,59,59) or time(16,0) <fecha_formato.time()< time(23,59,59):
            return "Martes: Engagement medio"
        elif time(7,0) <fecha_formato.time()< time(7,59,59) or time(14,0) <fecha_formato.time()< time(15,59,59):
            return "Martes: Engagement medio alto"
        elif time(8,0) <fecha_formato.time()< time(13,59,59):
            return "Martes: Engagement alto"
    else:
        if time(0,0) <fecha_formato.time()< time(4,59,59) or time(23,0) <fecha_formato.time()< time(23,59):
            return "Otro dia: Engagement bajo"
        else:
            return "Otro dia: Sin información"
    


N=int(input())
for _ in range(N):
    fecha=input()
    print(engagement(fecha))



