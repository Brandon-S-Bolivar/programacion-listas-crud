class Animal:
    def __init__(self, nombre_1, edad_1, especie_1, dieta_1):
        self.nombre = nombre_1
        self.edad = edad_1
        self.especie = especie_1
        self.dieta =  dieta_1
        

    def Mostrar_informacion(self):
        return f"el nombre del animal es: {self.nombre} \n es un {self.especie} \n de años {self.edad} años \n se alimenta de: {self.dieta}"
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def set_edad(self, nueva_edad):
        self.edad = nueva_edad
    def set_especie(self, nueva_especie):
        self.especie = nueva_especie
    def set_dieta(self, nueva_dieta):
        self.dieta = nueva_dieta
    
    
    