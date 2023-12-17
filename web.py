class apartamento():
    def __init__(self, nombrePropietario:str, idInmueble:str, estadoApto:str):
        self.nombrePropietario=nombrePropietario
        self.idInmueble=idInmueble
        self.estadoApto=estadoApto

    def cambioEstado(self):
        if self.estadoApto=='Nuevo':
            self.estadoApto='Usado'
    
    def caracteristicasApto(self):
        caracteristicas=(f"""
Propietario del apartamento: {self.nombrePropietario}
Identificacion del apartamento: {self.idInmueble}
Estado del apartamento: {self.estadoApto}""")
        return caracteristicas
    

apartamentoEnvigado=apartamento('Caterine Ruiz', 'ed2556', 'Nuevo')
apartamentoEnvigado.cambioEstado()
print(apartamentoEnvigado.caracteristicasApto())