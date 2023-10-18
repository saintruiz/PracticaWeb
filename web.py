def funcion_principal():
    opciones=int(input("""BIENVENIDO A ESTE PROYECTO INMOBILIARIO
    Quiere seguir?
    1. Sí
    2. No
    Ingrese opción: """))
    if opciones == 1:
        return "Perfecto, empieza el viaje"
    elif opciones==2:
        return "Regrese cuando esté listo"
print(funcion_principal())
