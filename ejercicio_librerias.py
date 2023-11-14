from datetime import datetime

 #Sismicidad histórica 
def convertir_a_fecha(string):
    fecha=datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return fecha
def diferencia_fechas(fecha1, fecha2):
    diferencia= fecha2-fecha1
    return diferencia
def tiempo_entre_eventos(N):
    lista_fechas=[]
    for _ in range(N):
        fecha=input()
        lista_fechas.append(fecha)
    



N=int(input())
