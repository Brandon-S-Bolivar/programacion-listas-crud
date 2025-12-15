from Modelo_animal import Animal

class Perro(Animal):
    def __init__(self, nombre_2, edad_2, especie_2, dieta_2, raza_1):
        super().__init__(nombre_2, edad_2, especie_2, dieta_2)
        self.raza = raza_1

    def Mostrar_informacion_perro(self):
        info_animal = self.Mostrar_informacion()
        return f"{info_animal} y su raza es: {self.raza}"
    
    def set_raza(self, nueva_raza):
        self.raza = nueva_raza
    
    def modificar_datos_perro(self, nuevo_nombre, nueva_edad, nueva_especie, nueva_dieta):
        super().set_nombre(nuevo_nombre)
        super().set_edad(nueva_edad)
        super().set_especie(nueva_especie)
        super().set_dieta(nueva_dieta)

































#te amo mucho mi vida




    