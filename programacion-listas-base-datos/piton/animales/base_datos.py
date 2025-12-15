from Modelo_perro import *

datos_perros = []

#__________________________________________________________________

mi_perro = Perro("Rex", 5, "Canino", "Carnívoro", "Labrador")
datos_perros.append(mi_perro)

#________________________modificando______________________________
def modificar():
    datos_perros.clear()
    mi_perro.modificar_datos_perro("Max", 6, "Canino doméstico", "Omnívoro")
    mi_perro.set_raza("Golden Retriever")
    
    datos_perros.append(mi_perro)


