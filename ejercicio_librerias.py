from datetime import datetime, time

def separar(string):
    lista=string.split()
    return lista
N=int(input())
red_social=input()
contador_horas=0
contador_veces_redsocial=0
for _ in range(N):
    string=input()
    lista=separar(string)
    if red_social in lista[3]:
        hora_inicio= datetime.strptime(lista[1], '%H:%M:%S')
        hora_final=datetime.strptime(lista[2], '%H:%M:%S')
        horas=((hora_final-hora_inicio).seconds)/3600
        contador_veces_redsocial+=1




