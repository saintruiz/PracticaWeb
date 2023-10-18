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
class apartamento_duplex():
    def __init__(self):
        self.__numero_pisos=2
        self.__numero_cocina=1
        self.__numero_parq=2

    def usado(self,usado):
        self.usado=usado
        if self.usado:
            return "El apartamento es usado"
        else:
            return "El apartamento es nuevo"
        
    def estado(self):
        print(f"El apartamento tiene {self.__numero_pisos} pisos, {self.__numero_cocina} cocinas y  {self.__numero_parq} parqueaderos")

apartamento1=apartamento_duplex()
print(apartamento1.usado(True))
apartamento1.estado()


# print(funcion_principal())
