class apartamento():
    def __init__(self, nombrePropietario:str, idInmueble:str, estadoApto:str):
        self.nombrePropietario=nombrePropietario
        self.idInmueble=idInmueble
        self.estadoApto=estadoApto

    def cambioEstado(self):
        if self.estadoApto=="Nuevo":
            self.estadoApto="Usado"
    
