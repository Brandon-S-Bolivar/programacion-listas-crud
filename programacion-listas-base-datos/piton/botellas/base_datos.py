from Modelo_botella import Botella
from Modelo_botella_plastico import Botella_plastico
from Modelo_botella_vidrio import Botella_vidrio

list_botella = []
list_botella_plas =[]
list_botella_vidrio = []

#______________________________________________________

Botella_datos = Botella("Aluminio")
Botella_datos.Contener_liquido("500 ml")
Botella_datos.forma_botella("cilindrica")
Botella_datos.diseño_botella("moderno")
Botella_datos.Grabados_botella("pepsi")

#_______________________________________________________

Botella_plastico_datos = Botella_plastico("Plastico PET")
Botella_plastico_datos.Definir_datos_plasti("blanco","no","rosca","fria/caliente","1000 ml","cilindrica","deportiva","coca-cola")

#_______________________________________________________

Botella_vidrio_datos = Botella_vidrio("Vidrio reciclado")
Botella_vidrio_datos.Definir_datos_vidrio("manual","bebidas","si","corcho","fria/caliente","750 ml","cilindrica","clasico","vino")

#_______________________________________________________

list_botella.append(Botella_datos)
list_botella_plas.append(Botella_plastico_datos)
list_botella_vidrio.append(Botella_vidrio_datos)







