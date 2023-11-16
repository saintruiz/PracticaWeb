def creacion_matriz(string):
    lista=[]
    for i in string:
        lista.append(i)
    if (lista[0] == lista[2]) and ((int(lista[0]))%2!=0):
        matriz=[]
        for _ in range (int(lista[0])):
            fila=[]
            for _ in range (int(lista[0])):
                num=int(input())
                fila.append(num)
            matriz.append(fila)                
        return matriz
    else:
        return "El numero de filas debe ser igual al numero de columnas y este valor debe ser impar"
    

entrada=input()
resultado=creacion_matriz(entrada)
print(resultado)
