from Modelo_carrp_deportivo import CarroDeportivo

lista_carro =[]

carro_deportivo = CarroDeportivo("Ferrari", "488 GTB", 2020, "Rojo", "Gasolina", 330, 3.0)
lista_carro.append(carro_deportivo)

def modificar_carro(indice, nueva_marca, nuevo_modelo, nuevo_año, nuevo_color, nuevo_tipo_combustible, nueva_velocidad_maxima, nueva_aceleracion):
    lista_carro.clear()
    carro_deportivo.modificar(nueva_marca, nuevo_modelo, nuevo_año, nuevo_color, nuevo_tipo_combustible, nueva_velocidad_maxima, nueva_aceleracion)
    lista_carro.append(carro_deportivo)
    