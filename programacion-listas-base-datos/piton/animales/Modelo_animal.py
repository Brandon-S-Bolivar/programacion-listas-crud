class Animal:
    def __init__(self, nombre_1, edad_1, especie_1, dieta_1):
        self.nombre = nombre_1
        self.edad = edad_1
        self.especie = especie_1
        self.dieta =  dieta_1
        

    def Mostrar_informacion(self):
        return f"el nombre del animal es: {self.nombre} es un {self.especie} de {self.edad} años se alimenta de: {self.dieta}"