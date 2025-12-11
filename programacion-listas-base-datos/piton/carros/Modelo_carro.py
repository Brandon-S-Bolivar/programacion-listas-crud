class Carro:
    def __init__(self,Marca_1,Modelo_1,Año_1,Color_1,Tipo_combustible_1):
        self.Marca=Marca_1
        self.Modelo=Modelo_1
        self.Año=Año_1
        self.Color=Color_1
        self.Tipo_combustible=Tipo_combustible_1
        
    def mostrar_informacion(self):
        info = f"Marca: {self.Marca}\n Modelo: {self.Modelo}\n Año: {self.Año}\n Color: {self.Color}\n Tipo de Combustible: {self.Tipo_combustible}\n"
        return info