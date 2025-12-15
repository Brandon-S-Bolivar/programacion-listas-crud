from Modelo_carro import Carro

class CarroDeportivo(Carro):
    def __init__(self, Marca_2, Modelo_2, Año_2, Color_2, Tipo_combustible_2, Velocidad_maxima_1, Aceleracion_1):
        super().__init__(Marca_2, Modelo_2, Año_2, Color_2, Tipo_combustible_2)
        self.Velocidad_maxima = Velocidad_maxima_1
        self.Aceleracion = Aceleracion_1
        
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        info_adicional = f" Velocidad Máxima: {self.Velocidad_maxima} km/h\n Aceleración 0-100 km/h: {self.Aceleracion} segundos\n"
        return info_base + info_adicional
    
    def modificar(self, nueva_marca, nuevo_modelo, nuevo_año, nuevo_color, nuevo_tipo_combustible, nueva_velocidad_maxima, nueva_aceleracion):
        super().set_marca(nueva_marca)
        super().set_modelo(nuevo_modelo)
        super().set_año(nuevo_año)
        super().set_color(nuevo_color)
        super().set_tipo_combustible(nuevo_tipo_combustible)
        self.Velocidad_maxima = nueva_velocidad_maxima
        self.Aceleracion = nueva_aceleracion