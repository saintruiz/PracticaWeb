#Aquí se desarrolla el ejercicio del parcial.
#Pida al usuario ingresar un número N de estudiantes a los cuáles se les hará la promediación de sus notas
#Por cada estudiante se pida: Nombre, edad y calificaciones (Ingresadas como en el siguiente ejemplo: 90 80 70)
#Guarde cada una de esas variables en un diccionario
#Las calificaciones deben ser mayores o iguales a 3, y deben estar en un rango 0-100:
    #Si las calificaciones no se encuentran dentro de ese rango, retorne un mensaje del estilo:
        #Promedio {nombre}: -
        #Resultado {nombre}: LAS CALIFICACIONES SE ENCUENTRAN FUERA DE RANGO
    #Si las calificaciones son menores a tres, retorne un mensaje del siguiente estilo:
        #Promedio {nombre}: -
        #Resultado {nombre}: NO HAY CALIFICACIONES SUFICIENTES
    #Si todo se encuentra en orden, retorne un mensaje del siguiente estilo:
        #Promedio {nombre}: {promedio}
        #Resultado {nombre}: APROBADA/ NO APROBADA (Teniendo en cuenta que una nota mayor o igual a 80 significa que aprobó)
#DEBE TENERSE EN CUENTA QUE LA SALIDA SE DEBE MOSTRAR EN UN SOLO BLOQUE: Se ingresan los datos con una iteración y luego de que internamente se
#ejecutó cada una de las funciones con cada estudiante, se debe retornar en un bloque completo la valoración de cada uno de los estudiantes.
# Si es posible, crear una interfaz gráfica para el ejercicio.
def creador_diccionario(nombre, edad, lista_calificaciones):
  diccionario_estudiante={}
  diccionario_estudiante["nombre"]=nombre
  diccionario_estudiante["edad"]=edad
  diccionario_estudiante["lista calificaciones"]=lista_calificaciones
  return diccionario_estudiante
  
def promedio(diccionario):
  while True:
    for i in diccionario["lista calificaciones"]:
      if int(i) > 100:
        return "CALIFICACIONES FUERA DE RANGO", "-"
        break
  
    if len(diccionario["lista calificaciones"]) < 3:
      return "NO HAY CALIFICACIONES SUFICIENTES", "-"
      break
      
    else:
      sumatoria=0
      for i in diccionario["lista calificaciones"]:
        sumatoria+=int(i)
      promedio=int(sumatoria/len(diccionario["lista calificaciones"]))
      if promedio<80:
        return "NO APROBADA", promedio
        break
      else:
        return "APROBADA", promedio
        break
def calcular_por_evento(N):
    diccionario_resultados_estudiantes={}
    for i in range(N):
        nombre=input("NOMBRE: ")
        edad=int(input("EDAD: "))
        calificaciones=input("CALIFICACIONES: ")
        
        lista_calificaciones=calificaciones.split()
        diccionario=creador_diccionario(nombre, edad, lista_calificaciones)
        resultado, promedio_estudiante = promedio(diccionario)
        diccionario_resultados_estudiantes[i]=[(diccionario["nombre"]), promedio_estudiante, resultado]
    for i in range(N):
        print(f"Promedio {diccionario_resultados_estudiantes[i][0]}: {diccionario_resultados_estudiantes[i][1]} ")
        print(f"Resultado {diccionario_resultados_estudiantes[i][0]}: {diccionario_resultados_estudiantes[i][2]}")


N=int(input("""¿Cuántos estudiantes va a evaluar?
            Ingrese el número: """))
calcular_por_evento(N)