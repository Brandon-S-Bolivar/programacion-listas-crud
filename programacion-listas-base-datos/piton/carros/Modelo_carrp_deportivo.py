from Modelo_carro import Carro

class CarroDeportivo(Carro):
    def __init__(self, Marca_2, Modelo_2, Año_2, Color_2, Tipo_combustible_2, Velocidad_maxima_1, Aceleracion_0_100_1):
        super().__init__(Marca_2, Modelo_2, Año_2, Color_2, Tipo_combustible_2)
        self.Velocidad_maxima = Velocidad_maxima_1
        self.Aceleracion_0_100 = Aceleracion_0_100_1
        
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        info_adicional = f" Velocidad Máxima: {self.Velocidad_maxima} km/h\n Aceleración 0-100 km/h: {self.Aceleracion_0_100} segundos\n"
        return info_base + info_adicional