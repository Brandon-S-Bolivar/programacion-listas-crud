from base_datos import *


for carro in lista_carro:
    print(carro.mostrar_informacion())
    
print("\n datos midificados \n")
modificar_carro(0, "Lamborghini", "Huracan EVO", 2021, "Amarillo", "Gasolina", 325, 2.9)

for carro in lista_carro:
    print(carro.mostrar_informacion())
