from Modelo_animal import Animal

class Perro(Animal):
    def __init__(self, nombre_2, edad_2, especie_2, dieta_2, raza_1):
        super().__init__(nombre_2, edad_2, especie_2, dieta_2)
        self.raza = raza_1

    def Mostrar_informacion_perro(self):
        info_animal = self.Mostrar_informacion()
        return f"{info_animal} y su raza es: {self.raza}"