from base_datos import *



print("datos botella")

for botellas in list_botella:
    botellas.imprimir_info()
    
print("\n datos botella plastico")

for bo_plasti in list_botella_plas:
    bo_plasti.imprimir_info()

print("\n datos de botella vidrio")

for bo_vidrio in list_botella_vidrio:
    bo_vidrio.imprimir_info()
     
cambiar_botella()
cambiar_botella_plastico()
cambiar_botella_vidrio()

print("\n datos modificados botellas")

for botellas in list_botella:
    botellas.imprimir_info()

print("\n datos modificados botella plastico")

for bo_plasti in list_botella_plas:
    bo_plasti.imprimir_info()

print("\n datos modificados de botella vidrio")

for bo_vidrio in list_botella_vidrio:
    bo_vidrio.imprimir_info()