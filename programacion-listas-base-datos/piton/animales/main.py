from base_datos import *

for perro in datos_perros:
    print(perro.Mostrar_informacion_perro())
    

print("\nDatos del perro modificados:\n")
modificar()

for perro in datos_perros:
    print(perro.Mostrar_informacion_perro())


