def suma_diagonal_principal(matriz):
    sumatoria=0
    for i in range(0, len(matriz[0])):
        sumatoria+=matriz[i][i]
    return sumatoria
def mult_diagonal_secundaria(matriz):
    multiplicacion=1
    longitud=len(matriz[0])
    contador=(longitud-1)
    for i in range(0, longitud):
        multiplicacion*=matriz[i][contador]
        contador-=1
    return multiplicacion

def suma_elmnts_mitad(matriz):
    longitud=len(matriz[0])
    mitad=int(longitud/2)
    sumatoria=0
    for i in range(0, longitud):
        sumatoria+=matriz[mitad][i]
    return sumatoria
def mult_elmnt_mitad(matriz):
    longitud=len(matriz[0])
    mitad=int(longitud/2)
    multiplicacion=1
    for i in range(0,longitud):
        multiplicacion*=matriz[i][mitad]
    return multiplicacion

def creacion_matriz(string):
    lista=[]
    for i in string:
        lista.append(i)
    if (lista[0] == lista[2]) and ((int(lista[0]))%2!=0):
        matriz=[]
        for _ in range (int(lista[0])):
            fila= [int(input()) for _ in range(int(lista[0]))]
            matriz.append(fila)                
        return matriz, True
    else:
        return "El numero de filas debe ser igual al numero de comlumnas y este valor debe ser impar", False
    
entrada=input()
matriz, validacion=creacion_matriz(entrada)
if validacion==True:
    suma_diagonal_1=suma_diagonal_principal(matriz)
    multiplicacion_diagonal=mult_diagonal_secundaria(matriz)
    suma_elementos_fila_mitad=suma_elmnts_mitad(matriz)
    multiplicacion_elemnts_clmn_mitad=mult_elmnt_mitad(matriz)
    print(f"{suma_diagonal_1}, {multiplicacion_diagonal}, {suma_elementos_fila_mitad}, {multiplicacion_elemnts_clmn_mitad}")
else:
    print(matriz)

