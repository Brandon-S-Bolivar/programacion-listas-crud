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
    
    def set_marca(self, nueva_marca):
        self.Marca = nueva_marca
    def set_modelo(self, nuevo_modelo):
        self.Modelo = nuevo_modelo
    def set_año(self, nuevo_año):
        self.Año = nuevo_año
    def set_color(self, nuevo_color):
        self.Color = nuevo_color
    def set_tipo_combustible(self, nuevo_tipo_combustible):
        self.Tipo_combustible = nuevo_tipo_combustible